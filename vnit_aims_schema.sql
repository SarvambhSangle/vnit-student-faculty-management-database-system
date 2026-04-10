SET DEFINE OFF;
SET VERIFY OFF;
SET FEEDBACK OFF;









DROP TABLE ATTENDANCE       CASCADE CONSTRAINTS PURGE;
DROP TABLE GRADE            CASCADE CONSTRAINTS PURGE;
DROP TABLE FEE              CASCADE CONSTRAINTS PURGE;
DROP TABLE REGISTRATION     CASCADE CONSTRAINTS PURGE;
DROP TABLE CLASS_LOGISTICS  CASCADE CONSTRAINTS PURGE;
DROP TABLE COURSE           CASCADE CONSTRAINTS PURGE;
DROP TABLE STUDENT          CASCADE CONSTRAINTS PURGE;
DROP TABLE FACULTY          CASCADE CONSTRAINTS PURGE;

DROP SEQUENCE att_seq;
DROP SEQUENCE reg_seq;
DROP SEQUENCE grade_seq;
DROP SEQUENCE fee_seq;
DROP SEQUENCE log_seq;





CREATE TABLE FACULTY (
    faculty_id      VARCHAR2(10)   NOT NULL,
    full_name       VARCHAR2(100)  NOT NULL,
    designation     VARCHAR2(60)   NOT NULL,
    qualification   VARCHAR2(20)   DEFAULT 'Ph.D.' NOT NULL,
    research_area   VARCHAR2(300),
    dept            VARCHAR2(10)   DEFAULT 'CSE' NOT NULL,
    password_hash   VARCHAR2(100)  NOT NULL,
    created_at      DATE           DEFAULT SYSDATE,
    CONSTRAINT pk_faculty      PRIMARY KEY (faculty_id),
    CONSTRAINT ck_fac_dept     CHECK (dept IN ('CSE','ECE','ME','CE','EE')),
    CONSTRAINT ck_fac_desig    CHECK (designation IN (
        'Professor','Professor & Head','Associate Professor','Assistant Professor'
    ))
)
STORAGE (INITIAL 64K NEXT 64K);




CREATE TABLE STUDENT (
    enrollment_no   VARCHAR2(12)  NOT NULL,
    full_name       VARCHAR2(100) NOT NULL,
    roll_no         VARCHAR2(10)  NOT NULL,
    branch          VARCHAR2(10)  DEFAULT 'CSE' NOT NULL,
    batch           VARCHAR2(10)  NOT NULL,
    section         VARCHAR2(6)   NOT NULL,
    current_sem     NUMBER(1)     NOT NULL,
    year            NUMBER(1)     NOT NULL,
    dob             DATE,
    phone           VARCHAR2(15),
    email           VARCHAR2(80),
    password_hash   VARCHAR2(100) NOT NULL,
    created_at      DATE          DEFAULT SYSDATE,
    CONSTRAINT pk_student      PRIMARY KEY (enrollment_no),
    CONSTRAINT ck_stu_batch    CHECK (batch IN ('B.Tech','M.Tech')),
    CONSTRAINT ck_stu_section  CHECK (section IN ('Sec A','Sec B','Sec C')),
    CONSTRAINT ck_stu_sem      CHECK (current_sem BETWEEN 1 AND 8),
    CONSTRAINT ck_stu_year     CHECK (year BETWEEN 1 AND 4),
    CONSTRAINT uq_stu_roll     UNIQUE (roll_no)
)
STORAGE (INITIAL 128K NEXT 128K);





CREATE TABLE COURSE (
    course_code     VARCHAR2(10)  NOT NULL,
    course_name     VARCHAR2(120) NOT NULL,
    semester        NUMBER(1)     NOT NULL,
    credits         NUMBER(2)     NOT NULL,
    ltp             VARCHAR2(10)  NOT NULL, 
    course_type     VARCHAR2(5)   NOT NULL, 
    faculty_id      VARCHAR2(10),
    CONSTRAINT pk_course        PRIMARY KEY (course_code),
    CONSTRAINT fk_course_fac    FOREIGN KEY (faculty_id)
                                REFERENCES FACULTY(faculty_id)
                                ON DELETE SET NULL,
    CONSTRAINT ck_course_sem    CHECK (semester BETWEEN 1 AND 8),
    CONSTRAINT ck_course_type   CHECK (course_type IN ('DC','DE','BS','ES','HM','AU'))
)
STORAGE (INITIAL 64K NEXT 64K);





CREATE SEQUENCE log_seq START WITH 1 INCREMENT BY 1 NOCACHE;

CREATE TABLE CLASS_LOGISTICS (
    log_id          NUMBER         DEFAULT log_seq.NEXTVAL NOT NULL,
    course_code     VARCHAR2(10)   NOT NULL,
    section         VARCHAR2(6)    NOT NULL,
    batch           VARCHAR2(10)   NOT NULL,
    default_time    VARCHAR2(10)   DEFAULT '11 AM',
    default_session VARCHAR2(15)   DEFAULT 'Morning',
    duration        VARCHAR2(10)   DEFAULT '1 Hour',
    CONSTRAINT pk_logistics     PRIMARY KEY (log_id),
    CONSTRAINT fk_log_course    FOREIGN KEY (course_code)
                                REFERENCES COURSE(course_code)
                                ON DELETE CASCADE,
    CONSTRAINT uq_log_course_sec UNIQUE (course_code, section, batch),
    CONSTRAINT ck_log_session   CHECK (default_session IN ('Morning','Afternoon','Evening')),
    CONSTRAINT ck_log_duration  CHECK (duration IN ('1 Hour','2 Hours','3 Hours'))
)
STORAGE (INITIAL 32K NEXT 32K);







CREATE SEQUENCE reg_seq START WITH 1 INCREMENT BY 1 NOCACHE;

CREATE TABLE REGISTRATION (
    reg_id          NUMBER         DEFAULT reg_seq.NEXTVAL NOT NULL,
    enrollment_no   VARCHAR2(12)   NOT NULL,
    course_code     VARCHAR2(10)   NOT NULL,
    section         VARCHAR2(6)    NOT NULL,
    batch           VARCHAR2(10)   NOT NULL,
    reg_date        DATE           DEFAULT SYSDATE,
    CONSTRAINT pk_registration  PRIMARY KEY (reg_id),
    CONSTRAINT fk_reg_student   FOREIGN KEY (enrollment_no)
                                REFERENCES STUDENT(enrollment_no)
                                ON DELETE CASCADE,
    CONSTRAINT fk_reg_course    FOREIGN KEY (course_code)
                                REFERENCES COURSE(course_code)
                                ON DELETE CASCADE,
    CONSTRAINT uq_reg_stu_crs   UNIQUE (enrollment_no, course_code)
)
STORAGE (INITIAL 128K NEXT 128K);







CREATE SEQUENCE att_seq START WITH 1 INCREMENT BY 1 NOCACHE;

CREATE TABLE ATTENDANCE (
    att_id          NUMBER         DEFAULT att_seq.NEXTVAL NOT NULL,
    enrollment_no   VARCHAR2(12)   NOT NULL,
    course_code     VARCHAR2(10)   NOT NULL,
    att_date        DATE           NOT NULL,
    status          VARCHAR2(10)   NOT NULL,
    time_slot       VARCHAR2(10),
    session         VARCHAR2(15),
    duration        VARCHAR2(10),
    marked_by       VARCHAR2(10), 
    marked_at       DATE           DEFAULT SYSDATE,
    CONSTRAINT pk_attendance    PRIMARY KEY (att_id),
    CONSTRAINT fk_att_student   FOREIGN KEY (enrollment_no)
                                REFERENCES STUDENT(enrollment_no)
                                ON DELETE CASCADE,
    CONSTRAINT fk_att_course    FOREIGN KEY (course_code)
                                REFERENCES COURSE(course_code)
                                ON DELETE CASCADE,
    CONSTRAINT ck_att_status    CHECK (status IN ('Present','Absent','Late')),
    CONSTRAINT ck_att_session   CHECK (session IN ('Morning','Afternoon','Evening'))
)
STORAGE (INITIAL 256K NEXT 256K);


CREATE INDEX idx_att_enr_crs ON ATTENDANCE(enrollment_no, course_code);
CREATE INDEX idx_att_date    ON ATTENDANCE(att_date);






CREATE SEQUENCE grade_seq START WITH 1 INCREMENT BY 1 NOCACHE;

CREATE TABLE GRADE (
    grade_id        NUMBER         DEFAULT grade_seq.NEXTVAL NOT NULL,
    enrollment_no   VARCHAR2(12)   NOT NULL,
    course_code     VARCHAR2(10)   NOT NULL,
    semester        NUMBER(1)      NOT NULL,
    grade           VARCHAR2(5)    NOT NULL,
    grade_points    NUMBER(2),
    credits_earned  NUMBER(2),
    CONSTRAINT pk_grade         PRIMARY KEY (grade_id),
    CONSTRAINT fk_grade_stu     FOREIGN KEY (enrollment_no)
                                REFERENCES STUDENT(enrollment_no)
                                ON DELETE CASCADE,
    CONSTRAINT fk_grade_crs     FOREIGN KEY (course_code)
                                REFERENCES COURSE(course_code)
                                ON DELETE CASCADE,
    CONSTRAINT uq_grade_stu_crs UNIQUE (enrollment_no, course_code, semester),
    CONSTRAINT ck_grade_val     CHECK (grade IN
        ('AA','AB','BB','BC','CC','CD','DD','FF','W','NP','NF','SS','ZZ'))
)
STORAGE (INITIAL 64K NEXT 64K);




CREATE SEQUENCE fee_seq START WITH 1 INCREMENT BY 1 NOCACHE;

CREATE TABLE FEE (
    fee_id          NUMBER         DEFAULT fee_seq.NEXTVAL NOT NULL,
    enrollment_no   VARCHAR2(12)   NOT NULL,
    description     VARCHAR2(100)  NOT NULL,
    amount          NUMBER(10,2)   NOT NULL,
    status          VARCHAR2(10)   DEFAULT 'Pending' NOT NULL,
    due_date        DATE,
    paid_date       DATE,
    CONSTRAINT pk_fee           PRIMARY KEY (fee_id),
    CONSTRAINT fk_fee_student   FOREIGN KEY (enrollment_no)
                                REFERENCES STUDENT(enrollment_no)
                                ON DELETE CASCADE,
    CONSTRAINT ck_fee_status    CHECK (status IN ('Paid','Pending','Waived'))
)
STORAGE (INITIAL 64K NEXT 64K);




CREATE OR REPLACE PROCEDURE sp_register_course (
    p_enrollment  IN VARCHAR2,
    p_course      IN VARCHAR2,
    p_section     IN VARCHAR2,
    p_batch       IN VARCHAR2,
    p_status      OUT VARCHAR2
) AS
    v_count NUMBER;
BEGIN
  
    SELECT COUNT(*) INTO v_count FROM STUDENT WHERE enrollment_no = p_enrollment;
    IF v_count = 0 THEN
        p_status := 'ERROR: Student not found';
        RETURN;
    END IF;
  
    SELECT COUNT(*) INTO v_count FROM COURSE WHERE course_code = p_course;
    IF v_count = 0 THEN
        p_status := 'ERROR: Course not found';
        RETURN;
    END IF;
  
    SELECT COUNT(*) INTO v_count FROM REGISTRATION
    WHERE enrollment_no = p_enrollment AND course_code = p_course;
    IF v_count > 0 THEN
        p_status := 'ERROR: Already registered';
        RETURN;
    END IF;
    INSERT INTO REGISTRATION (enrollment_no, course_code, section, batch)
    VALUES (p_enrollment, p_course, p_section, p_batch);
    COMMIT;
    p_status := 'SUCCESS';
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        p_status := 'ERROR: ' || SQLERRM;
END sp_register_course;
/




CREATE OR REPLACE PROCEDURE sp_mark_attendance (
    p_enrollment  IN VARCHAR2,
    p_course      IN VARCHAR2,
    p_date        IN DATE,
    p_status      IN VARCHAR2,
    p_time        IN VARCHAR2,
    p_session     IN VARCHAR2,
    p_duration    IN VARCHAR2,
    p_faculty     IN VARCHAR2,
    p_result      OUT VARCHAR2
) AS
BEGIN
    INSERT INTO ATTENDANCE
        (enrollment_no, course_code, att_date, status, time_slot, session, duration, marked_by)
    VALUES
        (p_enrollment, p_course, p_date, p_status, p_time, p_session, p_duration, p_faculty);
    COMMIT;
    p_result := 'SUCCESS';
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        p_result := 'ERROR: ' || SQLERRM;
END sp_mark_attendance;
/




CREATE OR REPLACE PACKAGE pkg_attendance AS
    FUNCTION get_attendance_pct(
        p_enrollment VARCHAR2,
        p_course     VARCHAR2
    ) RETURN NUMBER;

    PROCEDURE get_at_risk_students(
        p_course    IN  VARCHAR2,
        p_cursor    OUT SYS_REFCURSOR
    );
END pkg_attendance;
/

CREATE OR REPLACE PACKAGE BODY pkg_attendance AS

    FUNCTION get_attendance_pct(
        p_enrollment VARCHAR2,
        p_course     VARCHAR2
    ) RETURN NUMBER AS
        v_total   NUMBER := 0;
        v_present NUMBER := 0;
    BEGIN
        SELECT COUNT(*) INTO v_total
        FROM ATTENDANCE
        WHERE enrollment_no = p_enrollment AND course_code = p_course;

        SELECT COUNT(*) INTO v_present
        FROM ATTENDANCE
        WHERE enrollment_no = p_enrollment
          AND course_code   = p_course
          AND status        = 'Present';

        IF v_total = 0 THEN RETURN 0; END IF;
        RETURN ROUND((v_present / v_total) * 100, 2);
    END get_attendance_pct;

    PROCEDURE get_at_risk_students(
        p_course IN  VARCHAR2,
        p_cursor OUT SYS_REFCURSOR
    ) AS
    BEGIN
        OPEN p_cursor FOR
            SELECT s.enrollment_no,
                   s.full_name,
                   s.section,
                   pkg_attendance.get_attendance_pct(s.enrollment_no, p_course) AS pct
            FROM STUDENT s
            JOIN REGISTRATION r ON s.enrollment_no = r.enrollment_no
            WHERE r.course_code = p_course
              AND pkg_attendance.get_attendance_pct(s.enrollment_no, p_course) < 75
            ORDER BY pct ASC;
    END get_at_risk_students;

END pkg_attendance;
/




INSERT INTO FACULTY VALUES ('FAC001','Prof. S.R. Sathe',       'Professor',           'Ph.D.','Theoretical Foundation of CS, Cryptography, Discrete Maths','CSE','sathe123',   SYSDATE);
INSERT INTO FACULTY VALUES ('FAC002','Prof. O.G. Kakde',        'Professor',           'Ph.D.','Language Processor, Computer Programming Languages, Compiler','CSE','kakde123',   SYSDATE);
INSERT INTO FACULTY VALUES ('FAC003','Prof. P.S. Deshpande',    'Professor',           'Ph.D.','Database Management Systems, Data Warehousing and Mining',  'CSE','deshpande123',SYSDATE);
INSERT INTO FACULTY VALUES ('FAC004','Prof. U.A. Deshpande',    'Professor & Head',    'Ph.D.','Multi-agent Systems, Distributed Systems, Soft Computing',   'CSE','uadeshpande123',SYSDATE);
INSERT INTO FACULTY VALUES ('FAC005','Prof. R.B. Keskar',       'Associate Professor', 'Ph.D.','Telecommunication Software, Distributed Systems',             'CSE','keskar123',  SYSDATE);
INSERT INTO FACULTY VALUES ('FAC006','Prof. M.P. Kurhekar',     'Associate Professor', 'Ph.D.','Theoretical Computer Science, Bioinformatics',               'CSE','kurhekar123', SYSDATE);
INSERT INTO FACULTY VALUES ('FAC007','Prof. A.S. Mokhade',      'Assistant Professor', 'Ph.D.','Software Engineering, Software Architecture, Data Analytics', 'CSE','mokhade123', SYSDATE);
INSERT INTO FACULTY VALUES ('FAC008','Prof. M.M. Dhabu',        'Assistant Professor', 'Ph.D.','Soft Computing, Network Security',                           'CSE','dhabu123',    SYSDATE);
INSERT INTO FACULTY VALUES ('FAC009','Prof. Ashish Tiwari',     'Assistant Professor', 'Ph.D.','Mobile Communication, Information Security, OS',             'CSE','tiwari123',   SYSDATE);
INSERT INTO FACULTY VALUES ('FAC010','Prof. S.A. Raut',         'Assistant Professor', 'Ph.D.','Data Mining and Warehousing, Bioinformatics',                'CSE','raut123',     SYSDATE);
INSERT INTO FACULTY VALUES ('FAC011','Prof. Deepti Shrimankar', 'Assistant Professor', 'Ph.D.','Parallel and Distributed Systems, Computer Networks',        'CSE','shrimankar123',SYSDATE);
INSERT INTO FACULTY VALUES ('FAC012','Prof. M.A. Radke',        'Assistant Professor', 'Ph.D.','Information Retrieval, NLP, Semantic Web',                  'CSE','radke123',    SYSDATE);
INSERT INTO FACULTY VALUES ('FAC013','Prof. P.A. Sharma',       'Assistant Professor', 'Ph.D.','Image Processing, Biometrics, Neural Networks',              'CSE','pasharma123', SYSDATE);
INSERT INTO FACULTY VALUES ('FAC014','Prof. Praveen Kumar',     'Assistant Professor', 'Ph.D.','Image Processing, Computer Vision',                          'CSE','praveen123',  SYSDATE);
INSERT INTO FACULTY VALUES ('FAC015','Prof. Syed Taqi Ali',     'Assistant Professor', 'Ph.D.','Information Security, Cryptography',                         'CSE','taqi123',     SYSDATE);
INSERT INTO FACULTY VALUES ('FAC016','Prof. Anshul Agarwal',    'Assistant Professor', 'Ph.D.','Cyber Physical System, IoT, Applied ML, Game Theory',        'CSE','agarwal123',  SYSDATE);
INSERT INTO FACULTY VALUES ('FAC017','Prof. Swati Jaiswal',     'Assistant Professor', 'Ph.D.','Compilers, Program Analysis',                                'CSE','jaiswal123',  SYSDATE);


INSERT INTO COURSE VALUES ('CSL308','Software Engineering',               6,3,'3-0-0','DC','FAC007');
INSERT INTO COURSE VALUES ('CSL315','Database Management Systems',        6,4,'3-0-2','DC','FAC003');
INSERT INTO COURSE VALUES ('CSL316','Language Processors',                6,4,'3-0-2','DC','FAC002');
INSERT INTO COURSE VALUES ('CSL317','Computer Networks',                  6,4,'3-0-2','DC','FAC011');
INSERT INTO COURSE VALUES ('CSP302','Software Lab IV',                    6,2,'0-1-2','DC','FAC007');
INSERT INTO COURSE VALUES ('CSL326','Steganography and Digital Watermarking',6,3,'3-0-0','DE','FAC015');
INSERT INTO COURSE VALUES ('CSL328','Advance Web Programming',            6,3,'2-0-2','DE','FAC016');
INSERT INTO COURSE VALUES ('CSL442','Image and Video Processing',         6,4,'3-0-2','DE','FAC013');


INSERT INTO STUDENT VALUES ('BT23CS001','Sangle Sarvambh Keshav','101','CSE','B.Tech','Sec A',6,3,TO_DATE('15-08-2004','DD-MM-YYYY'),'9876543210','bt23cse001@vnit.ac.in','sarvambh123',SYSDATE);
INSERT INTO STUDENT VALUES ('BT23CS002','Sharma Rohan Kumar',    '102','CSE','B.Tech','Sec A',6,3,TO_DATE('22-01-2004','DD-MM-YYYY'),'9876543211','bt23cse002@vnit.ac.in','rohan123',   SYSDATE);
INSERT INTO STUDENT VALUES ('BT23CS003','Patil Kiran Suresh',    '103','CSE','B.Tech','Sec A',6,3,TO_DATE('10-03-2004','DD-MM-YYYY'),'9876543212','bt23cse003@vnit.ac.in','kiran123',   SYSDATE);


INSERT INTO REGISTRATION (enrollment_no,course_code,section,batch) VALUES ('BT23CS001','CSL315','Sec A','B.Tech');
INSERT INTO REGISTRATION (enrollment_no,course_code,section,batch) VALUES ('BT23CS001','CSL317','Sec A','B.Tech');
INSERT INTO REGISTRATION (enrollment_no,course_code,section,batch) VALUES ('BT23CS002','CSL315','Sec A','B.Tech');
INSERT INTO REGISTRATION (enrollment_no,course_code,section,batch) VALUES ('BT23CS003','CSL315','Sec A','B.Tech');


INSERT INTO ATTENDANCE (enrollment_no,course_code,att_date,status,time_slot,session,duration,marked_by)
VALUES ('BT23CS001','CSL315',TO_DATE('27-03-2026','DD-MM-YYYY'),'Present','11 AM','Morning','1 Hour','FAC003');
INSERT INTO ATTENDANCE (enrollment_no,course_code,att_date,status,time_slot,session,duration,marked_by)
VALUES ('BT23CS001','CSL315',TO_DATE('24-03-2026','DD-MM-YYYY'),'Present','11 AM','Morning','1 Hour','FAC003');
INSERT INTO ATTENDANCE (enrollment_no,course_code,att_date,status,time_slot,session,duration,marked_by)
VALUES ('BT23CS002','CSL315',TO_DATE('27-03-2026','DD-MM-YYYY'),'Absent', '11 AM','Morning','1 Hour','FAC003');


INSERT INTO CLASS_LOGISTICS (course_code,section,batch,default_time,default_session,duration)
VALUES ('CSL315','Sec A','B.Tech','11 AM','Morning','1 Hour');
INSERT INTO CLASS_LOGISTICS (course_code,section,batch,default_time,default_session,duration)
VALUES ('CSL317','Sec A','B.Tech','2 PM','Afternoon','1 Hour');

COMMIT;

























PROMPT Schema created successfully!
PROMPT Tables: FACULTY, STUDENT, COURSE, CLASS_LOGISTICS, REGISTRATION, ATTENDANCE, GRADE, FEE
PROMPT Packages: pkg_attendance
PROMPT Procedures: sp_register_course, sp_mark_attendance