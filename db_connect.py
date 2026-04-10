import oracledb

# ══════════════════════════════════════════════════════════════════════════════
#  ORACLE CONNECTION CONFIG
#  oracledb runs in "thin" mode — no Oracle Client install needed!
# ══════════════════════════════════════════════════════════════════════════════
DB_CONFIG = {
    "user":     "student_admin",
    "password": "password123",
    "dsn":      "localhost:1521/XEPDB1",   # XE default pluggable DB
}

# ── Get a connection ──────────────────────────────────────────────────────────
def get_connection():
    try:
        conn = oracledb.connect(**DB_CONFIG)
        return conn
    except oracledb.DatabaseError as e:
        print(f"[DB ERROR] Could not connect: {e}")
        return None

# ══════════════════════════════════════════════════════════════════════════════
#  READ FUNCTIONS  (SELECT)
# ══════════════════════════════════════════════════════════════════════════════

def get_all_students():
    conn = get_connection()
    if not conn: return []
    cur = conn.cursor()
    cur.execute("""
        SELECT enrollment_no, full_name, roll_no, branch,
               batch, section, current_sem, year,
               TO_CHAR(dob,'DD-Mon-YYYY'), phone, email
        FROM STUDENT ORDER BY enrollment_no
    """)
    rows = cur.fetchall()
    conn.close()
    return rows

def get_student_by_id(enrollment_no):
    conn = get_connection()
    if not conn: return None
    cur = conn.cursor()
    cur.execute("""
        SELECT enrollment_no, full_name, roll_no, branch,
               batch, section, current_sem, year,
               TO_CHAR(dob,'DD-Mon-YYYY'), phone, email, password_hash
        FROM STUDENT WHERE enrollment_no = :1
    """, [enrollment_no])
    row = cur.fetchone()
    conn.close()
    return row

def get_all_faculty():
    conn = get_connection()
    if not conn: return []
    cur = conn.cursor()
    cur.execute("""
        SELECT faculty_id, full_name, designation,
               qualification, research_area, dept
        FROM FACULTY ORDER BY faculty_id
    """)
    rows = cur.fetchall()
    conn.close()
    return rows

def get_all_courses():
    conn = get_connection()
    if not conn: return []
    cur = conn.cursor()
    cur.execute("""
        SELECT c.course_code, c.course_name, c.semester,
               c.credits, c.ltp, c.course_type,
               f.full_name as faculty_name
        FROM COURSE c
        LEFT JOIN FACULTY f ON c.faculty_id = f.faculty_id
        ORDER BY c.semester, c.course_code
    """)
    rows = cur.fetchall()
    conn.close()
    return rows

def get_registrations_for_student(enrollment_no):
    conn = get_connection()
    if not conn: return []
    cur = conn.cursor()
    cur.execute("""
        SELECT r.course_code, c.course_name, c.semester,
               c.credits, r.section, r.batch,
               TO_CHAR(r.reg_date,'DD-Mon-YYYY')
        FROM REGISTRATION r
        JOIN COURSE c ON r.course_code = c.course_code
        WHERE r.enrollment_no = :1
        ORDER BY c.semester, r.course_code
    """, [enrollment_no])
    rows = cur.fetchall()
    conn.close()
    return rows

def get_attendance_for_student(enrollment_no):
    conn = get_connection()
    if not conn: return []
    cur = conn.cursor()
    cur.execute("""
        SELECT TO_CHAR(a.att_date,'DD-Mon-YYYY'), a.course_code,
               c.course_name, a.time_slot, a.att_session,
               a.duration, a.status
        FROM ATTENDANCE a
        JOIN COURSE c ON a.course_code = c.course_code
        WHERE a.enrollment_no = :1
        ORDER BY a.att_date DESC
    """, [enrollment_no])
    rows = cur.fetchall()
    conn.close()
    return rows

def get_attendance_for_faculty_course(faculty_id, course_code=None):
    conn = get_connection()
    if not conn: return []
    cur = conn.cursor()
    if course_code:
        cur.execute("""
            SELECT TO_CHAR(a.att_date,'DD-Mon-YYYY'), a.enrollment_no,
                   s.full_name, a.course_code, a.time_slot,
                   a.att_session, a.status
            FROM ATTENDANCE a
            JOIN STUDENT s ON a.enrollment_no = s.enrollment_no
            JOIN COURSE c  ON a.course_code   = c.course_code
            WHERE c.faculty_id = :1 AND a.course_code = :2
            ORDER BY a.att_date DESC
        """, [faculty_id, course_code])
    else:
        cur.execute("""
            SELECT TO_CHAR(a.att_date,'DD-Mon-YYYY'), a.enrollment_no,
                   s.full_name, a.course_code, a.time_slot,
                   a.att_session, a.status
            FROM ATTENDANCE a
            JOIN STUDENT s ON a.enrollment_no = s.enrollment_no
            JOIN COURSE c  ON a.course_code   = c.course_code
            WHERE c.faculty_id = :1
            ORDER BY a.att_date DESC
        """, [faculty_id])
    rows = cur.fetchall()
    conn.close()
    return rows

def get_attendance_percentage(enrollment_no, course_code):
    conn = get_connection()
    if not conn: return 0
    cur = conn.cursor()
    cur.execute("""
        SELECT pkg_attendance.get_attendance_pct(:1, :2) FROM DUAL
    """, [enrollment_no, course_code])
    row = cur.fetchone()
    conn.close()
    return row[0] if row else 0

# ══════════════════════════════════════════════════════════════════════════════
#  WRITE FUNCTIONS  (INSERT / UPDATE via Stored Procedures)
# ══════════════════════════════════════════════════════════════════════════════

def register_student_to_db(enrollment_no, full_name, roll_no, branch,
                            batch, section, sem, year, dob, phone, email, password):
    conn = get_connection()
    if not conn: return False, "No DB connection"
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO STUDENT
              (enrollment_no, full_name, roll_no, branch, batch,
               section, current_sem, year, dob, phone, email, password_hash)
            VALUES (:1,:2,:3,:4,:5,:6,:7,:8,
                    TO_DATE(:9,'DD-Mon-YYYY'),:10,:11,:12)
        """, [enrollment_no, full_name, roll_no, branch, batch,
              section, sem, year, dob, phone, email, password])
        conn.commit()
        conn.close()
        return True, "Student registered in Oracle DB"
    except oracledb.DatabaseError as e:
        conn.rollback(); conn.close()
        return False, str(e)

def register_course_to_db(enrollment_no, course_code, section, batch):
    conn = get_connection()
    if not conn: return False, "No DB connection"
    cur = conn.cursor()
    status_var = cur.var(str)
    try:
        cur.callproc("sp_register_course",
                     [enrollment_no, course_code, section, batch, status_var])
        conn.commit()
        conn.close()
        return True, status_var.getvalue()
    except oracledb.DatabaseError as e:
        conn.rollback(); conn.close()
        return False, str(e)

def mark_attendance_to_db(enrollment_no, course_code, att_date,
                           status, time_slot, session, duration, faculty_id):
    conn = get_connection()
    if not conn: return False, "No DB connection"
    cur = conn.cursor()
    result_var = cur.var(str)
    try:
        import datetime
        if isinstance(att_date, str):
            att_date = datetime.datetime.strptime(att_date, "%d-%b-%Y")
        cur.callproc("sp_mark_attendance",
                     [enrollment_no, course_code, att_date,
                      status, time_slot, session, duration,
                      faculty_id, result_var])
        conn.commit()
        conn.close()
        return True, result_var.getvalue()
    except oracledb.DatabaseError as e:
        conn.rollback(); conn.close()
        return False, str(e)

# ══════════════════════════════════════════════════════════════════════════════
#  TEST — run this file directly to verify connection
# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("Testing Oracle DB connection...")
    conn = get_connection()
    if conn:
        print("Connected successfully!")
        cur = conn.cursor()

        print("\n── FACULTY ──────────────────────────────────")
        for row in get_all_faculty():
            print(f"  {row[0]}  {row[1]:<35}  {row[2]}")

        print("\n── STUDENTS ─────────────────────────────────")
        for row in get_all_students():
            print(f"  {row[0]}  {row[1]:<30}  Sem {row[6]}  {row[4]}")

        print("\n── COURSES (Sem 6) ──────────────────────────")
        for row in get_all_courses():
            if row[2] == 6:
                print(f"  {row[0]}  {row[1]:<45}  {row[3]} cr")

        print("\n── REGISTRATIONS for BT23CS001 ──────────────")
        for row in get_registrations_for_student("BT23CS001"):
            print(f"  {row[0]}  {row[1]}")

        print("\n── ATTENDANCE for BT23CS001 ─────────────────")
        for row in get_attendance_for_student("BT23CS001"):
            print(f"  {row[0]}  {row[1]}  {row[6]}")

        print("\n── ATTENDANCE % for BT23CS001 / CSL315 ──────")
        pct = get_attendance_percentage("BT23CS001", "CSL315")
        print(f"  Attendance: {pct}%")

        conn.close()
        print("\nAll tests passed!")
    else:
        print("Connection FAILED. Check Oracle service is running.")
        print("Run in PowerShell (Admin): net start OracleServiceXE")