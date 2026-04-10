# VNIT AIMS — Academic Information Management System

> **Visvesvaraya National Institute of Technology, Nagpur**
> Department of Computer Science & Engineering
> DBMS Project — Academic Year 2025–26

---

## What is this project?

A fully functional replica of the VNIT AIMS portal built using **Python (tkinter)** for the UI and **Oracle Database 21c XE** as the backend. The system handles student course registration, faculty attendance marking, grade tracking, and fee management — mirroring the real `aims.vnit.ac.in` portal.

---

## Architecture — Vertical Slice Design

This project is structured as **Vertical Slices**, not horizontal layers.

> A vertical slice is a complete, end-to-end piece of functionality that cuts across all layers — UI, logic, and database — at once.

### Why Vertical Slices?

| Horizontal Thinking  | Vertical Slice Thinking  |
|---|---|
| Build all UI first, then all DB | Build one complete feature at a time |
| No working system for weeks | Each slice delivers a working feature |
| Integration failures at the end | Integration is built-in from day one |
| Poor architectural understanding | Clear ownership per feature |

---

## Project Structure

```
DBMS Project/
├── vnit_aims_v2.py          ← UI layer (all screens, tkinter)
├── db_connect.py            ← Data access layer (Oracle queries)
├── vnit_aims_schema.sql     ← Database layer (tables, procedures, packages)
└── README.md                ← This file
```

---

## Vertical Slices — Feature Breakdown

Each slice below is a **complete working feature** spanning UI → Logic → Database.

---

### Slice 1 — Student Login

**What it does:** A student enters their enrollment number and password and gets access to their personalized dashboard.

| Layer | Implementation |
|---|---|
| UI | Login screen with Student / Faculty / New Registration tabs |
| Logic | Password verification against DB, session management |
| Database | `STUDENT` table — `enrollment_no (PK)`, `password_hash` |

```sql
SELECT enrollment_no, full_name, batch, current_sem
FROM STUDENT
WHERE enrollment_no = :1 AND password_hash = :2;
```

---

### Slice 2 — Faculty Login

**What it does:** A faculty member logs in and sees only their assigned courses and students.

| Layer | Implementation |
|---|---|
| UI | Faculty tab on login, personalized dashboard with research area |
| Logic | Faculty ID lookup, course filtering by `faculty_id` |
| Database | `FACULTY` table — `faculty_id (PK)`, `designation`, `research_area` |

```sql
SELECT faculty_id, full_name, designation, research_area
FROM FACULTY
WHERE faculty_id = :1 AND password_hash = :2;
```

---

### Slice 3 — New Student Registration

**What it does:** Register a brand new student with personal and academic details. Auto-generates enrollment number, validates format, checks for duplicates.

| Layer | Implementation |
|---|---|
| UI | Registration popup — name, DOB, phone, programme, semester, section |
| Logic | Enrollment format validation (`BT26CS001`), duplicate check |
| Database | `INSERT INTO STUDENT` via `sp_register_course` stored procedure |

```sql
INSERT INTO STUDENT
  (enrollment_no, full_name, roll_no, branch, batch,
   section, current_sem, year, dob, phone, email, password_hash)
VALUES (:1,:2,:3,:4,:5,:6,:7,:8, TO_DATE(:9,'DD-Mon-YYYY'),:10,:11,:12);
```

**Validation Rules:**
- Format must match `BT` or `MT` + 2-digit year + `CS` + 3-digit serial
- Enrollment number must be unique across all students
- Name, DOB, phone, password are mandatory fields

---

### Slice 4 — Course Registration

**What it does:** Student browses courses by semester (1–8), selects section and batch, registers for courses. Registered student immediately appears in the faculty's attendance list.

| Layer | Implementation |
|---|---|
| UI | Semester selector buttons (1–8), Available ↔ Registered dual-panel |
| Logic | Semester filter, duplicate enrollment check, batch/section assignment |
| Database | `REGISTRATION` table — `reg_id (PK)`, `enrollment_no (FK)`, `course_code (FK)` |

```sql
EXEC sp_register_course(:enrollment_no, :course_code, :section, :batch, :status_out);
```

**Business Rules:**
- One student cannot register for the same course twice
- Student appears in faculty's attendance list immediately after registration
- Student can drop a course (removes from attendance records)

---

### Slice 5 — Mark Attendance (Faculty)

**What it does:** Faculty selects a course, loads enrolled students, marks each as Present or Absent, and submits. Supports Mark All Present, Mark All Absent.

| Layer | Implementation |
|---|---|
| UI | Class config (date, time, session, duration, course, section, batch) → student radio buttons |
| Logic | Filter students by course + section + batch, batch submit |
| Database | `ATTENDANCE` table — `att_id (PK)`, `enrollment_no (FK)`, `course_code (FK)`, `status` |

```sql
EXEC sp_mark_attendance(
  :enrollment_no, :course_code, :att_date,
  :status, :time_slot, :att_session, :duration,
  :faculty_id, :result_out
);
```

**Business Rules (VNIT Attendance Ordinance):**
- Minimum 75% attendance required per course
- Student with < 75% attendance receives **W grade**
- W grade = not eligible for end semester examination

---

### Slice 6 — Attendance Reports (Faculty)

**What it does:** Faculty views complete attendance logs for all their courses. Filterable by course and status (Present / Absent).

| Layer | Implementation |
|---|---|
| UI | Filter bar (course dropdown, status dropdown), sortable table |
| Logic | Dynamic SQL filtering, course ownership check |
| Database | JOIN across `ATTENDANCE`, `STUDENT`, `COURSE` |

```sql
SELECT TO_CHAR(a.att_date,'DD-Mon-YYYY'), s.full_name,
       a.course_code, a.att_session, a.status
FROM ATTENDANCE a
JOIN STUDENT s ON a.enrollment_no = s.enrollment_no
JOIN COURSE c  ON a.course_code   = c.course_code
WHERE c.faculty_id = :1
ORDER BY a.att_date DESC;
```

---

### Slice 7 — Student Attendance View

**What it does:** Student sees their own attendance per course with percentage, Present/Absent count, and W grade warning if below 75%.

| Layer | Implementation |
|---|---|
| UI | Stat cards (Total, Present, Absent, %), color-coded log table |
| Logic | Attendance % calculation, W grade risk flag |
| Database | `pkg_attendance.get_attendance_pct()` Oracle package function |

```sql
SELECT pkg_attendance.get_attendance_pct(:enrollment_no, :course_code)
FROM DUAL;
```

---

### Slice 8 — Grade Card

**What it does:** Student views semester-wise grade report with SGPA and CGPA calculation.

| Layer | Implementation |
|---|---|
| UI | Grade table per semester, SGPA / CGPA summary |
| Logic | SGPA = Σ(grade_points × credits) / Σ(credits) |
| Database | `GRADE` table — `grade`, `grade_points`, `credits_earned` |

**VNIT Grading System:**

| Grade | Points | Description |
|---|---|---|
| AA | 10 | Outstanding |
| AB | 9 | Excellent |
| BB | 8 | Very Good |
| BC | 7 | Good |
| CC | 6 | Average |
| CD | 5 | Below Average |
| DD | 4 | Marginal (Pass) |
| FF | 0 | Fail |
| W | — | Insufficient Attendance |

---

### Slice 9 — Fee Payment

**What it does:** Student views fee breakdown (Tuition, Hostel, Library, Exam, Sports) with Paid/Pending status.

| Layer | Implementation |
|---|---|
| UI | Stat cards (Total Paid, Pending), fee table with color-coded status |
| Logic | Sum calculation for paid and pending amounts |
| Database | `FEE` table — `fee_id (PK)`, `enrollment_no (FK)`, `amount`, `status` |

---

### Slice 10 — Class Logistics (Faculty)

**What it does:** Faculty updates default class settings — time slot, session (Morning/Afternoon/Evening), duration — per course per section.

| Layer | Implementation |
|---|---|
| UI | Dropdowns for course, time, session, duration, section, batch |
| Logic | Updates default settings used when marking attendance |
| Database | `CLASS_LOGISTICS` table — `log_id (PK)`, `course_code (FK)`, `default_time`, `default_session` |

---

### Slice 11 — Faculty Directory

**What it does:** Any logged-in faculty can view all 17 CSE faculty members with designation, qualification and research area.

| Layer | Implementation |
|---|---|
| UI | Searchable table with all faculty details |
| Logic | Simple full-table read |
| Database | `FACULTY` table — all 17 real VNIT CSE faculty |

---

## Database Schema Summary

### Tables (8)

| Table | Purpose | Key Constraints |
|---|---|---|
| `FACULTY` | 17 CSE faculty members | PK: `faculty_id` |
| `STUDENT` | Enrolled students | PK: `enrollment_no`, UQ: `roll_no` |
| `COURSE` | VNIT CSE curriculum (Sem 3–8) | PK: `course_code`, FK: `faculty_id` |
| `REGISTRATION` | Student–Course enrollment | PK: `reg_id`, UQ: `(enrollment_no, course_code)` |
| `ATTENDANCE` | Per-class attendance records | PK: `att_id`, CHECK: status IN ('Present','Absent','Late') |
| `GRADE` | Semester grades | PK: `grade_id`, CHECK: grade IN ('AA','AB','BB',...,'W') |
| `FEE` | Fee payment tracking | PK: `fee_id`, CHECK: status IN ('Paid','Pending','Waived') |
| `CLASS_LOGISTICS` | Default class settings | PK: `log_id`, UQ: `(course_code, section, batch)` |

### Stored Procedures & Packages (Assignment Deliverable vi)

| Object | Type | Purpose |
|---|---|---|
| `sp_register_course` | Stored Procedure | Validates and inserts student course registration |
| `sp_mark_attendance` | Stored Procedure | Inserts attendance record with validation |
| `pkg_attendance` | Package | `get_attendance_pct()` function + `get_at_risk_students()` procedure |

### Storage Clauses (Assignment Deliverable v)

All tables created with explicit `STORAGE (INITIAL 64K NEXT 64K)` clauses as required.

---

## Setup Instructions

### Prerequisites
- Python 3.10+
- Oracle Database 21c XE
- `oracledb` Python package

### Installation

```bash
# 1. Install Oracle driver
pip install oracledb

# 2. Start Oracle services (PowerShell as Admin)
net start OracleServiceXE
net start OracleXETNSListener

# 3. Create database user
sqlplus / as sysdba
ALTER SESSION SET CONTAINER = XEPDB1;
CREATE USER student_admin IDENTIFIED BY password123;
GRANT ALL PRIVILEGES TO student_admin;
EXIT;

# 4. Run schema
sqlplus student_admin/password123@localhost:1521/XEPDB1
@vnit_aims_schema.sql
EXIT;

# 5. Test database connection
python db_connect.py

# 6. Launch the application
python vnit_aims_v2.py
```

---

## Test Credentials

### Students
| Enrollment No. | Name | Password |
|---|---|---|
| BT23CS001 | Sangle Sarvambh Keshav | sarvambh123 |
| BT23CS002 | Sharma Rohan Kumar | rohan123 |
| BT23CS003 | Patil Kiran Suresh | kiran123 |

### Faculty (sample)
| Faculty ID | Name | Password |
|---|---|---|
| FAC003 | Prof. P.S. Deshpande | deshpande123 |
| FAC011 | Prof. Deepti Shrimankar | shrimankar123 |
| FAC001 | Prof. S.R. Sathe | sathe123 |

---

## Assignment Deliverables Checklist

| # | Deliverable | Status |
|---|---|---|
| i | ER Diagram |  EER diagram with 8 entities, normalized to 3NF |
| ii | Tables with PK, FK, domain constraints |  8 tables in `vnit_aims_schema.sql` |
| iii | Approx rows per table per session |  Seed data for all tables included |
| iv | UI for Registration & Attendance |  Full Python tkinter app (11 vertical slices) |
| v | Storage clause INITIAL, NEXT |  All CREATE TABLE statements include STORAGE clause |
| vi | Stored procedures & packages called from UI |  `sp_register_course`, `sp_mark_attendance`, `pkg_attendance` |

---

## Technology Stack

| Layer | Technology |
|---|---|
| UI | Python 3.13, tkinter, ttk |
| Database Driver | oracledb 3.4.2 |
| Database | Oracle 21c Express Edition (XE) |
| SQL Objects | Tables, Sequences, Indexes, Stored Procedures, Packages |
| OS | Windows 11 |
| IDE | VS Code |

---

## Author

**Sangle Sarvambh Keshav**
B.Tech Computer Science & Engineering — Semester 6
Enrollment No: BT23CSE094
Visvesvaraya National Institute of Technology, Nagpur
Academic Year 2025–26
