import tkinter as tk
from tkinter import ttk, messagebox
import datetime

# ══════════════════════════════════════════════════════════════════════════════
#  COLOUR PALETTE  (VNIT Navy + Gold)
# ══════════════════════════════════════════════════════════════════════════════
C = {
    "navy":      "#0D1B3E", "navy2":     "#162444", "navy3":     "#1E3160",
    "gold":      "#C8921A", "gold_lt":   "#E5A820", "gold_dim":  "#8A6410",
    "white":     "#FFFFFF", "off_white": "#F5F7FA", "light_bg":  "#EEF1F7",
    "card":      "#FFFFFF", "border":    "#D0D8E8", "border2":   "#B8C4D8",
    "text_dark": "#0D1B3E", "text_mid":  "#3A4B6E", "text_muted":"#6B7A99",
    "text_light":"#9BA8C0",
    "green":     "#1A7A45", "green_bg":  "#E6F4ED",
    "red":       "#B82020", "red_bg":    "#FAEAEA",
    "blue":      "#1A55A0", "blue_bg":   "#E6EEF8",
    "orange":    "#C45C0A", "orange_bg": "#FDF0E6",
    "purple":    "#5B2D8E", "purple_bg": "#F0EAF9",
    "hover":     "#1E3160",
}

# ══════════════════════════════════════════════════════════════════════════════
#  DATABASE  — real VNIT CSE faculty + curriculum
# ══════════════════════════════════════════════════════════════════════════════
DB = {

    # ── FACULTY (from VNIT CSE curriculum PDF) ────────────────────────────────
    "faculty": {
        "FAC001": {"name":"Prof. S.R. Sathe",          "short":"S.R. Sathe",
                   "designation":"Professor",           "qual":"Ph.D.",
                   "area":"Theoretical Foundation of CS, Cryptography, Discrete Maths",
                   "dept":"CSE", "password":"sathe123"},
        "FAC002": {"name":"Prof. O.G. Kakde",           "short":"O.G. Kakde",
                   "designation":"Professor",           "qual":"Ph.D.",
                   "area":"Language Processor, Computer Programming Languages, Compiler",
                   "dept":"CSE", "password":"kakde123"},
        "FAC003": {"name":"Prof. P.S. Deshpande",       "short":"P.S. Deshpande",
                   "designation":"Professor",           "qual":"Ph.D.",
                   "area":"Database Management Systems, Data Warehousing & Mining",
                   "dept":"CSE", "password":"deshpande123"},
        "FAC004": {"name":"Prof. U.A. Deshpande",       "short":"U.A. Deshpande",
                   "designation":"Professor & Head",    "qual":"Ph.D.",
                   "area":"Multi-agent Systems, Distributed Systems, Soft Computing",
                   "dept":"CSE", "password":"uadeshpande123"},
        "FAC005": {"name":"Prof. R.B. Keskar",          "short":"R.B. Keskar",
                   "designation":"Associate Professor", "qual":"Ph.D.",
                   "area":"Telecommunication Software, Distributed Systems, Compiler Optimization",
                   "dept":"CSE", "password":"keskar123"},
        "FAC006": {"name":"Prof. M.P. Kurhekar",        "short":"M.P. Kurhekar",
                   "designation":"Associate Professor", "qual":"Ph.D.",
                   "area":"Theoretical Computer Science, Bioinformatics",
                   "dept":"CSE", "password":"kurhekar123"},
        "FAC007": {"name":"Prof. A.S. Mokhade",         "short":"A.S. Mokhade",
                   "designation":"Assistant Professor", "qual":"Ph.D.",
                   "area":"Software Engineering, Software Architecture, Data Analytics",
                   "dept":"CSE", "password":"mokhade123"},
        "FAC008": {"name":"Prof. M.M. Dhabu",           "short":"M.M. Dhabu",
                   "designation":"Assistant Professor", "qual":"Ph.D.",
                   "area":"Soft Computing, Network Security",
                   "dept":"CSE", "password":"dhabu123"},
        "FAC009": {"name":"Prof. Ashish Tiwari",        "short":"A. Tiwari",
                   "designation":"Assistant Professor", "qual":"Ph.D.",
                   "area":"Mobile Communication, Information Security, Operating Systems",
                   "dept":"CSE", "password":"tiwari123"},
        "FAC010": {"name":"Prof. S.A. Raut",            "short":"S.A. Raut",
                   "designation":"Assistant Professor", "qual":"Ph.D.",
                   "area":"Data Mining & Warehousing, MC Data Science, Bioinformatics",
                   "dept":"CSE", "password":"raut123"},
        "FAC011": {"name":"Prof. Deepti Shrimankar",    "short":"D. Shrimankar",
                   "designation":"Assistant Professor", "qual":"Ph.D.",
                   "area":"Parallel & Distributed Systems, Embedded Systems, Computer Networks",
                   "dept":"CSE", "password":"shrimankar123"},
        "FAC012": {"name":"Prof. M.A. Radke",           "short":"M.A. Radke",
                   "designation":"Assistant Professor", "qual":"Ph.D.",
                   "area":"Information Retrieval, Natural Language Processing, Semantic Web",
                   "dept":"CSE", "password":"radke123"},
        "FAC013": {"name":"Prof. P.A. Sharma",          "short":"P.A. Sharma",
                   "designation":"Assistant Professor", "qual":"Ph.D.",
                   "area":"Image Processing, Biometrics, Neural Networks",
                   "dept":"CSE", "password":"pasharma123"},
        "FAC014": {"name":"Prof. Praveen Kumar",        "short":"P. Kumar",
                   "designation":"Assistant Professor", "qual":"Ph.D.",
                   "area":"Image Processing, Computer Vision",
                   "dept":"CSE", "password":"praveen123"},
        "FAC015": {"name":"Prof. Syed Taqi Ali",        "short":"S.T. Ali",
                   "designation":"Assistant Professor", "qual":"Ph.D.",
                   "area":"Information Security, Cryptography",
                   "dept":"CSE", "password":"taqi123"},
        "FAC016": {"name":"Prof. Anshul Agarwal",       "short":"A. Agarwal",
                   "designation":"Assistant Professor", "qual":"Ph.D.",
                   "area":"Cyber Physical System, IoT, Applied ML, Game Theory",
                   "dept":"CSE", "password":"agarwal123"},
        "FAC017": {"name":"Prof. Swati Jaiswal",        "short":"S. Jaiswal",
                   "designation":"Assistant Professor", "qual":"Ph.D.",
                   "area":"Compilers, Program Analysis",
                   "dept":"CSE", "password":"jaiswal123"},
    },

    # ── COURSES  (real VNIT CSE curriculum) ───────────────────────────────────
    "courses": {
        # Semester III
        "MAL208":{"name":"Probability Theory & Statistical Methods","sem":3,"credits":4,"ltp":"3-1-0","type":"DC","faculty":"FAC006"},
        "CSL202":{"name":"Discrete Mathematics and Graph Theory",   "sem":3,"credits":4,"ltp":"3-1-0","type":"DC","faculty":"FAC001"},
        "CSL226":{"name":"Digital Circuits and Microprocessor",     "sem":3,"credits":5,"ltp":"3-1-2","type":"DC","faculty":"FAC005"},
        "CSL213":{"name":"Data Structures and Program Design - I",  "sem":3,"credits":5,"ltp":"3-1-2","type":"DC","faculty":"FAC006"},
        "CSP201":{"name":"Software Lab – I",                        "sem":3,"credits":2,"ltp":"0-1-2","type":"DC","faculty":"FAC007"},
        "HUL201":{"name":"Technical Communication",                 "sem":3,"credits":3,"ltp":"3-0-0","type":"DE","faculty":"FAC007"},
        # Semester IV
        "CSL204":{"name":"Concepts in Programming Languages",       "sem":4,"credits":4,"ltp":"3-0-2","type":"DC","faculty":"FAC002"},
        "CSL214":{"name":"Data Structures and Program Design - II", "sem":4,"credits":5,"ltp":"3-1-2","type":"DC","faculty":"FAC006"},
        "CSL222":{"name":"Computer Organization",                   "sem":4,"credits":4,"ltp":"4-0-0","type":"DC","faculty":"FAC005"},
        "MAL206":{"name":"Linear Algebra & Applications",           "sem":4,"credits":4,"ltp":"3-1-0","type":"DC","faculty":"FAC001"},
        "CSP202":{"name":"Software Lab – II",                       "sem":4,"credits":2,"ltp":"0-1-2","type":"DC","faculty":"FAC007"},
        "CSL233":{"name":"Introduction to Object Oriented Methodology","sem":4,"credits":4,"ltp":"3-0-2","type":"DE","faculty":"FAC008"},
        # Semester V
        "CSL307":{"name":"Theory of Computation",                   "sem":5,"credits":4,"ltp":"3-1-0","type":"DC","faculty":"FAC001"},
        "CSL321":{"name":"Design and Analysis of Algorithms",       "sem":5,"credits":4,"ltp":"3-1-0","type":"DC","faculty":"FAC006"},
        "CSL309":{"name":"Operating Systems",                       "sem":5,"credits":4,"ltp":"3-0-2","type":"DC","faculty":"FAC009"},
        "CSP300":{"name":"Software Lab – III",                      "sem":5,"credits":2,"ltp":"0-1-2","type":"DC","faculty":"FAC007"},
        "CSL304":{"name":"Neuro Fuzzy Techniques",                  "sem":5,"credits":4,"ltp":"3-0-2","type":"DE","faculty":"FAC008"},
        "CSL305":{"name":"Computer Graphics",                       "sem":5,"credits":4,"ltp":"3-0-2","type":"DE","faculty":"FAC014"},
        "CSL318":{"name":"Business Information Systems",            "sem":5,"credits":4,"ltp":"3-0-2","type":"DE","faculty":"FAC010"},
        "CSL327":{"name":"Introduction to Web Programming",        "sem":5,"credits":4,"ltp":"3-0-2","type":"DE","faculty":"FAC016"},
        # Semester VI  ← main semester for test students
        "CSL308":{"name":"Software Engineering",                    "sem":6,"credits":3,"ltp":"3-0-0","type":"DC","faculty":"FAC007"},
        "CSL315":{"name":"Database Management Systems",             "sem":6,"credits":4,"ltp":"3-0-2","type":"DC","faculty":"FAC003"},
        "CSL316":{"name":"Language Processors",                     "sem":6,"credits":4,"ltp":"3-0-2","type":"DC","faculty":"FAC002"},
        "CSL317":{"name":"Computer Networks",                       "sem":6,"credits":4,"ltp":"3-0-2","type":"DC","faculty":"FAC011"},
        "CSP302":{"name":"Software Lab – IV",                       "sem":6,"credits":2,"ltp":"0-1-2","type":"DC","faculty":"FAC007"},
        "CSL326":{"name":"Steganography and Digital Watermarking",  "sem":6,"credits":3,"ltp":"3-0-0","type":"DE","faculty":"FAC015"},
        "MAL304":{"name":"Financial Mathematics",                   "sem":6,"credits":3,"ltp":"3-0-0","type":"DE","faculty":"FAC001"},
        "CSL328":{"name":"Advance Web Programming",                 "sem":6,"credits":3,"ltp":"2-0-2","type":"DE","faculty":"FAC016"},
        "CSL442":{"name":"Image and Video Processing",              "sem":6,"credits":4,"ltp":"3-0-2","type":"DE","faculty":"FAC013"},
        # Semester VII
        "CSL443":{"name":"System and Network Security",             "sem":7,"credits":4,"ltp":"3-0-2","type":"DC","faculty":"FAC015"},
        "CSD401":{"name":"Project Phase I",                         "sem":7,"credits":2,"ltp":"0-0-4","type":"DC","faculty":"FAC003"},
        "CSL451":{"name":"Introduction to Embedded Systems",        "sem":7,"credits":4,"ltp":"3-0-2","type":"DE","faculty":"FAC011"},
        "CSL412":{"name":"Artificial Intelligence",                 "sem":7,"credits":4,"ltp":"3-0-2","type":"DE","faculty":"FAC008"},
        "CSL436":{"name":"Information Retrieval",                   "sem":7,"credits":4,"ltp":"3-0-2","type":"DE","faculty":"FAC012"},
        "CSL450":{"name":"Introduction to Machine Learning",        "sem":7,"credits":3,"ltp":"3-0-0","type":"DE","faculty":"FAC010"},
        "CSL407":{"name":"Data Mining & Data Warehousing",          "sem":7,"credits":4,"ltp":"3-0-2","type":"DE","faculty":"FAC010"},
        # Semester VIII
        "CSD402":{"name":"Project Phase II",                        "sem":8,"credits":4,"ltp":"0-0-4","type":"DC","faculty":"FAC003"},
        "CSL409":{"name":"Introduction to Distributed Systems",     "sem":8,"credits":4,"ltp":"3-0-2","type":"DE","faculty":"FAC004"},
        "CSL411":{"name":"Software Project Management",             "sem":8,"credits":3,"ltp":"3-0-0","type":"DE","faculty":"FAC007"},
        "CSL431":{"name":"Introduction to Cloud Computing",         "sem":8,"credits":3,"ltp":"3-0-0","type":"DE","faculty":"FAC004"},
        "CSL537":{"name":"Natural Language Processing",             "sem":8,"credits":4,"ltp":"3-0-2","type":"DE","faculty":"FAC012"},
    },

    # ── STUDENTS ──────────────────────────────────────────────────────────────
    "students": {
        "BT23CS001":{"name":"Sangle Sarvambh Keshav", "roll":"BT23CS001","branch":"CSE","batch":"B.Tech","section":"Sec A","sem":6,"year":3,"password":"sarvambh123","dob":"15-Aug-2004","phone":"9876543210","email":"bt23cse001@vnit.ac.in"},
        "BT23CS002":{"name":"Sharma Rohan Kumar",     "roll":"BT23CS002","branch":"CSE","batch":"B.Tech","section":"Sec A","sem":6,"year":3,"password":"rohan123",   "dob":"22-Jan-2004","phone":"9876543211","email":"bt23cse002@vnit.ac.in"},
        "BT23CS003":{"name":"Patil Kiran Suresh",     "roll":"BT23CS003","branch":"CSE","batch":"B.Tech","section":"Sec A","sem":6,"year":3,"password":"kiran123",   "dob":"10-Mar-2004","phone":"9876543212","email":"bt23cse003@vnit.ac.in"},
        "BT23CS004":{"name":"Deshpande Aman Vijay",   "roll":"BT23CS004","branch":"CSE","batch":"B.Tech","section":"Sec B","sem":6,"year":3,"password":"aman123",    "dob":"05-Nov-2003","phone":"9876543213","email":"bt23cse004@vnit.ac.in"},
        "BT23CS005":{"name":"Kulkarni Sneha Pramod",  "roll":"BT23CS005","branch":"CSE","batch":"B.Tech","section":"Sec B","sem":6,"year":3,"password":"sneha123",   "dob":"18-Jul-2004","phone":"9876543214","email":"bt23cse005@vnit.ac.in"},
        "MT24CS001":{"name":"Joshi Priya Nilesh",     "roll":"MT24CS001","branch":"CSE","batch":"M.Tech","section":"Sec A","sem":2,"year":1,"password":"priya123",   "dob":"12-Feb-2001","phone":"9876543220","email":"mt24cse001@vnit.ac.in"},
    },

    # ── REGISTRATIONS ─────────────────────────────────────────────────────────
    "registrations": [
        {"enrollment":"BT23CS001","course":"CSL315","section":"Sec A","batch":"B.Tech"},
        {"enrollment":"BT23CS001","course":"CSL308","section":"Sec A","batch":"B.Tech"},
        {"enrollment":"BT23CS001","course":"CSL317","section":"Sec A","batch":"B.Tech"},
        {"enrollment":"BT23CS002","course":"CSL315","section":"Sec A","batch":"B.Tech"},
        {"enrollment":"BT23CS002","course":"CSL316","section":"Sec A","batch":"B.Tech"},
        {"enrollment":"BT23CS003","course":"CSL315","section":"Sec A","batch":"B.Tech"},
        {"enrollment":"BT23CS004","course":"CSL315","section":"Sec B","batch":"B.Tech"},
        {"enrollment":"BT23CS005","course":"CSL315","section":"Sec B","batch":"B.Tech"},
        {"enrollment":"MT24CS001","course":"CSD401","section":"Sec A","batch":"M.Tech"},
    ],

    # ── ATTENDANCE ────────────────────────────────────────────────────────────
    "attendance": [
        {"date":"27-MAR-2026","enrollment":"BT23CS001","course":"CSL315","status":"Present","time":"11 AM","session":"Morning","duration":"1 Hour"},
        {"date":"24-MAR-2026","enrollment":"BT23CS001","course":"CSL315","status":"Present","time":"11 AM","session":"Morning","duration":"1 Hour"},
        {"date":"20-MAR-2026","enrollment":"BT23CS001","course":"CSL315","status":"Absent", "time":"11 AM","session":"Morning","duration":"1 Hour"},
        {"date":"17-MAR-2026","enrollment":"BT23CS001","course":"CSL315","status":"Present","time":"11 AM","session":"Morning","duration":"1 Hour"},
        {"date":"27-MAR-2026","enrollment":"BT23CS001","course":"CSL317","status":"Present","time":"2 PM", "session":"Afternoon","duration":"1 Hour"},
        {"date":"27-MAR-2026","enrollment":"BT23CS002","course":"CSL315","status":"Absent", "time":"11 AM","session":"Morning","duration":"1 Hour"},
        {"date":"24-MAR-2026","enrollment":"BT23CS002","course":"CSL315","status":"Present","time":"11 AM","session":"Morning","duration":"1 Hour"},
        {"date":"27-MAR-2026","enrollment":"BT23CS003","course":"CSL315","status":"Present","time":"11 AM","session":"Morning","duration":"1 Hour"},
        {"date":"27-MAR-2026","enrollment":"BT23CS004","course":"CSL315","status":"Present","time":"11 AM","session":"Morning","duration":"1 Hour"},
        {"date":"27-MAR-2026","enrollment":"BT23CS005","course":"CSL315","status":"Absent", "time":"11 AM","session":"Morning","duration":"1 Hour"},
    ],

    # ── GRADES (Sem V sample) ─────────────────────────────────────────────────
    "grades": {
        "BT23CS001": [
            {"sem":5,"code":"CSL307","name":"Theory of Computation",           "grade":"AB","points":9,"credits":4},
            {"sem":5,"code":"CSL321","name":"Design and Analysis of Algorithms","grade":"AA","points":10,"credits":4},
            {"sem":5,"code":"CSL309","name":"Operating Systems",               "grade":"BB","points":8,"credits":4},
            {"sem":5,"code":"CSP300","name":"Software Lab – III",              "grade":"AA","points":10,"credits":2},
            {"sem":5,"code":"CSL327","name":"Introduction to Web Programming", "grade":"AB","points":9,"credits":4},
        ],
    },
}

# Grade system
GRADES = {"AA":10,"AB":9,"BB":8,"BC":7,"CC":6,"CD":5,"DD":4,"FF":0}

# ══════════════════════════════════════════════════════════════════════════════
#  HELPERS
# ══════════════════════════════════════════════════════════════════════════════
def _sep(parent, color=C["border"], padx=0, pady=4):
    tk.Frame(parent, bg=color, height=1).pack(fill="x", padx=padx, pady=pady)

def _next_enrollment(batch="B.Tech"):
    prefix = "BT" if batch == "B.Tech" else "MT"
    year   = str(datetime.date.today().year)[-2:]
    existing = [k for k in DB["students"] if k.startswith(prefix + year + "CS")]
    num = len(existing) + 1
    return f"{prefix}{year}CS{num:03d}"

# ══════════════════════════════════════════════════════════════════════════════
#  MAIN APPLICATION
# ══════════════════════════════════════════════════════════════════════════════
class VNITApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("VNIT Nagpur — Academic Information Management System")
        self.geometry("1280x800")
        self.minsize(1100, 700)
        self.configure(bg=C["off_white"])
        self._setup_styles()
        self.current_user = None
        self.user_type    = None
        self._show_login()

    # ── STYLES ────────────────────────────────────────────────────────────────
    def _setup_styles(self):
        s = ttk.Style(self); s.theme_use("clam")
        for name, bg, fg, abg in [
            ("Gold",   C["gold"],   C["navy"],  C["gold_lt"]),
            ("Navy",   C["navy"],   C["white"], C["navy3"]),
            ("Green",  C["green"],  C["white"], "#238A50"),
            ("Red",    C["red"],    C["white"], "#CC3030"),
            ("Ghost",  C["card"],   C["text_mid"], C["light_bg"]),
            ("Purple", C["purple"], C["white"], "#6E3AA0"),
        ]:
            s.configure(f"{name}.TButton", background=bg, foreground=fg,
                        font=("Segoe UI Semibold", 10), relief="flat",
                        borderwidth=0, padding=(14, 8))
            s.map(f"{name}.TButton", background=[("active", abg), ("pressed", abg)])
        s.configure("Treeview", background=C["card"], foreground=C["text_dark"],
                    rowheight=30, fieldbackground=C["card"], font=("Segoe UI", 10))
        s.configure("Treeview.Heading", background=C["navy"], foreground=C["white"],
                    font=("Segoe UI Semibold", 10), relief="flat")
        s.map("Treeview", background=[("selected", C["blue_bg"])],
              foreground=[("selected", C["blue"])])
        s.configure("TCombobox", font=("Segoe UI", 10), padding=5)

    def _clear(self):
        for w in self.winfo_children(): w.destroy()

    # ══════════════════════════════════════════════════════════════════════════
    #  LOGIN
    # ══════════════════════════════════════════════════════════════════════════
    def _show_login(self):
        self._clear(); self.geometry("1100x700")
        self.current_user = None; self.user_type = None

        # LEFT branding panel
        left = tk.Frame(self, bg=C["navy"], width=430)
        left.pack(side="left", fill="y"); left.pack_propagate(False)
        tk.Frame(left, bg=C["gold"], height=5).pack(fill="x")

        logo = tk.Frame(left, bg=C["navy"]); logo.pack(expand=True, pady=(0, 40))
        # Canvas emblem
        e = tk.Canvas(logo, width=110, height=110, bg=C["navy"], highlightthickness=0)
        e.pack(pady=(50, 16))
        e.create_oval(4,4,106,106, outline=C["gold"],    width=3)
        e.create_oval(14,14,96,96, outline=C["gold_lt"], width=1)
        e.create_text(55,42, text="VNIT",  fill=C["gold"],    font=("Segoe UI Black",18))
        e.create_text(55,62, text="NAGPUR",fill=C["gold_lt"], font=("Segoe UI",10,"bold"))

        tk.Label(logo, text="Visvesvaraya National",   font=("Segoe UI Light",16), fg=C["white"],    bg=C["navy"]).pack()
        tk.Label(logo, text="Institute of Technology", font=("Segoe UI Light",16), fg=C["white"],    bg=C["navy"]).pack()
        tk.Label(logo, text="Nagpur",                  font=("Segoe UI Black",20), fg=C["gold"],     bg=C["navy"]).pack(pady=(3,20))
        _sep(logo, color="#2A3F6A", padx=40, pady=6)
        tk.Label(logo, text="Academic Information Management System",
                 font=("Segoe UI",10), fg=C["text_light"], bg=C["navy"],
                 wraplength=300, justify="center").pack(pady=(6,0))
        tk.Label(logo, text="Department of Computer Science & Engineering",
                 font=("Segoe UI",9), fg=C["gold_dim"], bg=C["navy"],
                 wraplength=300, justify="center").pack(pady=(4,0))

        # bottom strip
        bot = tk.Frame(left, bg=C["navy2"]); bot.pack(fill="x")
        for t in ["Session 2025–26","Location: Nagpur","Autonomous Institute"]:
            tk.Label(bot, text=t, font=("Segoe UI",8), fg=C["text_light"],
                     bg=C["navy2"], padx=10, pady=7).pack(side="left")

        # RIGHT form panel
        right = tk.Frame(self, bg=C["off_white"]); right.pack(side="left", fill="both", expand=True)
        tk.Frame(right, bg=C["gold"], height=5).pack(fill="x")

        top_bar = tk.Frame(right, bg=C["light_bg"])
        top_bar.pack(fill="x")
        tk.Label(top_bar, text="  aims.vnit.ac.in",
                 font=("Segoe UI",9), fg=C["text_muted"], bg=C["light_bg"]).pack(side="left", padx=12, pady=8)
        tk.Label(top_bar, text=datetime.datetime.now().strftime("%a %d %b %Y  |  %I:%M %p  "),
                 font=("Segoe UI",9), fg=C["text_muted"], bg=C["light_bg"]).pack(side="right", pady=8)

        # tab row: Student | Faculty | New Registration
        wrap = tk.Frame(right, bg=C["off_white"]); wrap.pack(expand=True)
        card = tk.Frame(wrap, bg=C["card"], highlightbackground=C["border"], highlightthickness=1)
        card.pack(padx=60, pady=30, ipadx=36, ipady=28)

        tk.Label(card, text="Sign In to AIMS", font=("Segoe UI Black",22), fg=C["navy"], bg=C["card"]).pack(anchor="w", pady=(0,3))
        tk.Label(card, text="Enter your credentials to continue", font=("Segoe UI",10), fg=C["text_muted"], bg=C["card"]).pack(anchor="w", pady=(0,16))

        # Role tabs
        self.role_var = tk.StringVar(value="student")
        tab_frame = tk.Frame(card, bg=C["light_bg"]); tab_frame.pack(fill="x", pady=(0,18))
        self._tabs = {}
        for role, label in [("student","  Student  "),("faculty","  Faculty  "),("register","  New Registration  ")]:
            lbl = tk.Label(tab_frame, text=label, font=("Segoe UI",10), cursor="hand2", pady=8, padx=4)
            lbl.pack(side="left")
            self._tabs[role] = lbl
            lbl.bind("<Button-1>", lambda e, r=role: self._set_role(r))

        # fields
        tk.Label(card, text="Enrollment / Faculty ID", font=("Segoe UI Semibold",9),
                 fg=C["text_mid"], bg=C["card"]).pack(anchor="w")
        self.login_id = tk.Entry(card, font=("Segoe UI",11), bg=C["light_bg"], fg=C["text_dark"],
                                  relief="flat", highlightbackground=C["border"], highlightthickness=1,
                                  insertbackground=C["navy"], width=34)
        self.login_id.pack(fill="x", ipady=9, pady=(3,12))

        tk.Label(card, text="Password", font=("Segoe UI Semibold",9), fg=C["text_mid"], bg=C["card"]).pack(anchor="w")
        self.login_pw = tk.Entry(card, font=("Segoe UI",11), bg=C["light_bg"], fg=C["text_dark"],
                                  relief="flat", show="●",
                                  highlightbackground=C["border"], highlightthickness=1,
                                  insertbackground=C["navy"], width=34)
        self.login_pw.pack(fill="x", ipady=9, pady=(3,6))

        self._hint = tk.Label(card, text="Student: BT23CS001 / sarvambh123   |   Faculty: FAC003 / deshpande123",
                               font=("Segoe UI",8), fg=C["text_light"], bg=C["card"])
        self._hint.pack(anchor="w", pady=(0,16))

        # Set default tab AFTER _hint is created (avoids AttributeError)
        self._set_role("student")

        ttk.Button(card, text="Sign In →", style="Gold.TButton", command=self._do_login).pack(anchor="w", ipadx=10)
        self.login_id.bind("<Return>", lambda e: self._do_login())
        self.login_pw.bind("<Return>", lambda e: self._do_login())

        tk.Label(right, text="© 2026 VNIT Nagpur. All rights reserved.  |  Powered by Oracle Database 21c XE",
                 font=("Segoe UI",8), fg=C["text_light"], bg=C["off_white"]).pack(side="bottom", pady=10)

    def _set_role(self, role):
        self.role_var.set(role)
        for r, lbl in self._tabs.items():
            if r == role:
                lbl.config(fg=C["white"], bg=C["navy"], font=("Segoe UI Semibold",10))
            else:
                lbl.config(fg=C["text_muted"], bg=C["light_bg"], font=("Segoe UI",10))
        if not hasattr(self, "_hint"):
            return
        if role == "register":
            self._hint.config(text="Fill details below after clicking Sign In to open the Registration form")
        else:
            self._hint.config(text="Student: BT23CS001 / sarvambh123   |   Faculty: FAC003 / deshpande123")

    def _do_login(self):
        uid = self.login_id.get().strip()
        pw  = self.login_pw.get().strip()
        role = self.role_var.get()
        if role == "register":
            self._show_new_student_registration(); return
        if role == "student":
            s = DB["students"].get(uid)
            if s and s["password"] == pw:
                self.current_user = uid; self.user_type = "student"
                self._build_student_shell(); return
            messagebox.showerror("Login Failed", "Invalid Enrollment Number or Password.")
        else:
            f = DB["faculty"].get(uid)
            if f and f["password"] == pw:
                self.current_user = uid; self.user_type = "faculty"
                self._build_faculty_shell(); return
            messagebox.showerror("Login Failed", "Invalid Faculty ID or Password.")

    # ══════════════════════════════════════════════════════════════════════════
    #  NEW STUDENT REGISTRATION (Admin / self-registration form)
    # ══════════════════════════════════════════════════════════════════════════
    def _show_new_student_registration(self):
        win = tk.Toplevel(self)
        win.title("VNIT AIMS — New Student Registration")
        win.geometry("700x680")
        win.configure(bg=C["off_white"])
        win.grab_set()

        tk.Frame(win, bg=C["gold"], height=5).pack(fill="x")
        hdr = tk.Frame(win, bg=C["navy"]); hdr.pack(fill="x")
        tk.Label(hdr, text="  New Student Registration", font=("Segoe UI Black",14),
                 fg=C["white"], bg=C["navy"]).pack(side="left", pady=12, padx=12)
        tk.Label(hdr, text="VNIT AIMS Portal  |  CSE Department",
                 font=("Segoe UI",9), fg=C["gold_lt"], bg=C["navy"]).pack(side="right", padx=14)

        body = tk.Frame(win, bg=C["off_white"]); body.pack(fill="both", expand=True, padx=30, pady=20)

        def row(parent, label, widget_fn):
            f = tk.Frame(parent, bg=C["off_white"]); f.pack(fill="x", pady=5)
            tk.Label(f, text=label, font=("Segoe UI Semibold",9), fg=C["text_mid"],
                     bg=C["off_white"], width=22, anchor="w").pack(side="left")
            w = widget_fn(f); w.pack(side="left", fill="x", expand=True, ipady=6, padx=(0,8)); return w

        def entry(p): return tk.Entry(p, font=("Segoe UI",11), bg=C["light_bg"], fg=C["text_dark"],
                                       relief="flat", highlightbackground=C["border"], highlightthickness=1,
                                       insertbackground=C["navy"])
        def combo(p, vals, defval=None):
            v = tk.StringVar(value=defval or vals[0])
            c = ttk.Combobox(p, textvariable=v, state="readonly", values=vals, font=("Segoe UI",11))
            c._var = v; return c

        tk.Label(body, text="Personal Information", font=("Segoe UI Black",13),
                 fg=C["navy"], bg=C["off_white"]).pack(anchor="w", pady=(0,8))

        e_name  = row(body, "Full Name *",             entry)
        e_dob   = row(body, "Date of Birth (DD-Mon-YY)*", entry)
        e_phone = row(body, "Mobile Number *",         entry)
        e_email = row(body, "Institute Email",         entry)

        _sep(body, pady=8)
        tk.Label(body, text="Academic Information", font=("Segoe UI Black",13),
                 fg=C["navy"], bg=C["off_white"]).pack(anchor="w", pady=(0,8))

        cb_batch = row(body, "Programme *",  lambda p: combo(p, ["B.Tech","M.Tech"]))
        cb_sem   = row(body, "Semester *",   lambda p: combo(p, [str(i) for i in range(1,9)], "1"))
        cb_sec   = row(body, "Section *",    lambda p: combo(p, ["Sec A","Sec B","Sec C"]))

        def suggest_roll(*_):
            batch = cb_batch._var.get()
            suggested = _next_enrollment(batch)
            if not e_roll.get().strip():
                e_roll.delete(0, "end")
                e_roll.insert(0, suggested)
                e_roll.config(fg=C["text_muted"])
        cb_batch._var.trace_add("write", suggest_roll)

        roll_f = tk.Frame(body, bg=C["off_white"]); roll_f.pack(fill="x", pady=5)
        tk.Label(roll_f, text="Enrollment No. *", font=("Segoe UI Semibold",9),
                 fg=C["text_mid"], bg=C["off_white"], width=22, anchor="w").pack(side="left")
        e_roll = tk.Entry(roll_f, font=("Segoe UI",11), bg=C["light_bg"], fg=C["text_dark"],
                          relief="flat", highlightbackground=C["border"], highlightthickness=1,
                          insertbackground=C["navy"])
        e_roll.pack(side="left", fill="x", expand=True, ipady=6)

        hint_f = tk.Frame(body, bg=C["off_white"]); hint_f.pack(fill="x")
        tk.Label(hint_f, text=" " * 23 + "Format: BT26CS001 for B.Tech  |  MT26CS001 for M.Tech",
                 font=("Segoe UI",8), fg=C["text_light"], bg=C["off_white"]).pack(anchor="w")

        def on_roll_focus_in(e):
            if e_roll.get() == _next_enrollment(cb_batch._var.get()):
                e_roll.config(fg=C["text_dark"])
        def on_roll_focus_out(e):
            if not e_roll.get().strip():
                suggest_roll()

        e_roll.bind("<FocusIn>",  on_roll_focus_in)
        e_roll.bind("<FocusOut>", on_roll_focus_out)
        suggest_roll()

        _sep(body, pady=8)
        pw_f = tk.Frame(body, bg=C["off_white"]); pw_f.pack(fill="x", pady=5)
        tk.Label(pw_f, text="Set Password *", font=("Segoe UI Semibold",9),
                 fg=C["text_mid"], bg=C["off_white"], width=22, anchor="w").pack(side="left")
        e_pw = tk.Entry(pw_f, font=("Segoe UI",11), bg=C["light_bg"], fg=C["text_dark"],
                        show="●", relief="flat", highlightbackground=C["border"], highlightthickness=1)
        e_pw.pack(side="left", fill="x", expand=True, ipady=6)

        # action bar
        bar = tk.Frame(win, bg=C["navy"]); bar.pack(fill="x", side="bottom")
        tk.Frame(bar, bg=C["navy"]).pack(side="left", expand=True)

        def register():
            name  = e_name.get().strip()
            dob   = e_dob.get().strip()
            phone = e_phone.get().strip()
            email = e_email.get().strip()
            batch = cb_batch._var.get()
            sem   = int(cb_sem._var.get())
            sec   = cb_sec._var.get()
            pw    = e_pw.get().strip()
            enr   = e_roll.get().strip()

            import re
            enr = enr.upper()
            if not name or not dob or not phone or not pw or not enr:
                messagebox.showerror("Missing Fields", "Please fill all required (*) fields including Enrollment No.", parent=win); return
            if not re.match(r'^(BT|MT)\d{2}CS\d{3}$', enr):
                messagebox.showerror("Invalid Enrollment Format",
                    "Enrollment No. format is invalid.\n\nValid examples:\n  B.Tech  →  BT26CS001\n  M.Tech  →  MT26CS001", parent=win); return
            if enr in DB["students"]:
                messagebox.showerror("Duplicate Enrollment",
                    f"Enrollment No. '{enr}' already exists in the system.\nPlease enter a different number.", parent=win); return
            if not email:
                email = f"{enr.lower()}@vnit.ac.in"
            year  = 1 if sem <= 2 else (2 if sem <= 4 else (3 if sem <= 6 else 4))
            DB["students"][enr] = {
                "name":name,"roll":enr,"branch":"CSE",
                "batch":batch,"section":sec,"sem":sem,"year":year,
                "password":pw,"dob":dob,"phone":phone,"email":email
            }
            messagebox.showinfo("Registered Successfully",
                f"Student registered!\n\nEnrollment No: {enr}\nName: {name}\n\nUse these credentials to login.",
                parent=win)
            win.destroy()

        ttk.Button(bar, text="✔  Register Student", style="Green.TButton", command=register).pack(side="right", padx=12, pady=10)
        ttk.Button(bar, text="Cancel", style="Ghost.TButton", command=win.destroy).pack(side="right", padx=4, pady=10)

    # ══════════════════════════════════════════════════════════════════════════
    #  SHARED CHROME  (topbar + sidebar)
    # ══════════════════════════════════════════════════════════════════════════
    def _build_chrome(self, sidebar_items, active_item=None):
        self._clear(); self.geometry("1300x820")

        # ── Topbar
        top = tk.Frame(self, bg=C["navy"], height=52); top.pack(fill="x"); top.pack_propagate(False)
        tk.Frame(top, bg=C["gold"], width=5).pack(side="left", fill="y")
        e2 = tk.Canvas(top, width=38, height=38, bg=C["navy"], highlightthickness=0)
        e2.pack(side="left", padx=(8,6), pady=7)
        e2.create_oval(2,2,36,36, outline=C["gold"], width=2)
        e2.create_text(19,19, text="VNIT", fill=C["gold"], font=("Segoe UI Black",8))
        tk.Label(top, text="Visvesvaraya National Institute of Technology",
                 font=("Segoe UI Semibold",12), fg=C["white"], bg=C["navy"]).pack(side="left", padx=4)
        tk.Label(top, text="· AIMS", font=("Segoe UI",11), fg=C["gold_lt"], bg=C["navy"]).pack(side="left")

        if self.user_type == "student":
            u    = DB["students"][self.current_user]
            name = u["name"].upper()
            sub  = f"{self.current_user}  ·  Sem {u['sem']}  ·  {u['branch']}  ·  {u['batch']}"
        else:
            u    = DB["faculty"][self.current_user]
            name = u["name"].upper()
            sub  = f"{u['designation']}  ·  {u['dept']}"

        rf = tk.Frame(top, bg=C["navy"]); rf.pack(side="right", padx=14)
        tk.Label(rf, text=name, font=("Segoe UI Semibold",10), fg=C["white"], bg=C["navy"]).pack(anchor="e")
        tk.Label(rf, text=sub,  font=("Segoe UI",8),           fg=C["gold_lt"],bg=C["navy"]).pack(anchor="e")

        out = tk.Label(top, text="  ⏻ Logout  ", font=("Segoe UI",9),
                       fg=C["text_light"], bg=C["navy"], cursor="hand2", pady=16)
        out.pack(side="right", padx=4)
        out.bind("<Button-1>", lambda e: self._show_login())
        out.bind("<Enter>", lambda e: out.config(fg=C["white"]))
        out.bind("<Leave>", lambda e: out.config(fg=C["text_light"]))

        tk.Frame(self, bg=C["gold"], height=3).pack(fill="x")

        # ── Body
        body = tk.Frame(self, bg=C["off_white"]); body.pack(fill="both", expand=True)

        # Sidebar
        sb = tk.Frame(body, bg=C["navy"], width=235); sb.pack(side="left", fill="y"); sb.pack_propagate(False)

        for item in sidebar_items:
            if item == "---":
                tk.Frame(sb, bg="#1E3160", height=1).pack(fill="x", padx=16, pady=5); continue
            text, icon, cmd = item
            active = (text == active_item)
            rbg = C["gold"] if active else C["navy"]
            rfg = C["navy"] if active else C["white"]
            row = tk.Frame(sb, bg=rbg, cursor="hand2"); row.pack(fill="x", pady=1)
            il  = tk.Label(row, text=icon, font=("Segoe UI",12), fg=C["navy"] if active else C["gold_lt"],
                           bg=rbg, width=3); il.pack(side="left", padx=(12,4), pady=9)
            tl  = tk.Label(row, text=text, font=("Segoe UI Semibold" if active else "Segoe UI",10),
                           fg=rfg, bg=rbg, anchor="w"); tl.pack(side="left", pady=9, fill="x", expand=True)

            def _in(e, r=row, i=il, t=tl, act=active):
                if not act: [w.config(bg=C["hover"]) for w in (r,i,t)]
            def _out(e, r=row, i=il, t=tl, act=active, ob=rbg):
                if not act: [w.config(bg=ob) for w in (r,i,t)]

            for w in (row, il, tl):
                w.bind("<Button-1>", lambda e, c=cmd: c())
                w.bind("<Enter>", _in); w.bind("<Leave>", _out)

        tk.Frame(sb, bg=C["navy2"]).pack(fill="both", expand=True)
        bot_sb = tk.Frame(sb, bg=C["navy2"]); bot_sb.pack(fill="x")
        tk.Label(bot_sb, text="Oracle DB 21c XE  ·  2025–26",
                 font=("Segoe UI",8), fg=C["text_light"], bg=C["navy2"]).pack(pady=8)

        # Content
        content = tk.Frame(body, bg=C["off_white"]); content.pack(side="left", fill="both", expand=True)
        return sb, content

    # ── Page header
    def _hdr(self, parent, title, sub="", breadcrumb=""):
        h = tk.Frame(parent, bg=C["off_white"]); h.pack(fill="x", padx=24, pady=(16,8))
        if breadcrumb:
            tk.Label(h, text=breadcrumb, font=("Segoe UI",9), fg=C["text_light"], bg=C["off_white"]).pack(anchor="w")
        tk.Label(h, text=title, font=("Segoe UI Black",20), fg=C["navy"], bg=C["off_white"]).pack(anchor="w")
        if sub: tk.Label(h, text=sub, font=("Segoe UI",10), fg=C["text_muted"], bg=C["off_white"]).pack(anchor="w", pady=(2,0))
        tk.Frame(parent, bg=C["border"], height=1).pack(fill="x", padx=24, pady=(0,10))

    # ── Stat card
    def _stat(self, parent, label, val, icon, col, bg):
        c = tk.Frame(parent, bg=bg, highlightbackground=C["border"], highlightthickness=1)
        c.pack(side="left", padx=5, pady=4, ipadx=14, ipady=10, fill="x", expand=True)
        tk.Label(c, text=icon, font=("Segoe UI",16), fg=col, bg=bg).pack(anchor="w")
        tk.Label(c, text=str(val), font=("Segoe UI Black",22), fg=col, bg=bg).pack(anchor="w")
        tk.Label(c, text=label, font=("Segoe UI",9), fg=C["text_muted"], bg=bg).pack(anchor="w")

    # ── Section card with navy header
    def _card(self, parent, title, fill_fn, hdr_color=None):
        hc = hdr_color or C["navy"]
        c  = tk.Frame(parent, bg=C["card"], highlightbackground=C["border"], highlightthickness=1)
        c.pack(fill="x", pady=6)
        hf = tk.Frame(c, bg=hc, height=36); hf.pack(fill="x"); hf.pack_propagate(False)
        tk.Frame(hf, bg=C["gold"], width=4).pack(side="left", fill="y")
        tk.Label(hf, text=f"  {title}", font=("Segoe UI Semibold",11), fg=C["white"], bg=hc).pack(side="left", pady=7)
        b = tk.Frame(c, bg=C["card"]); b.pack(fill="x", padx=14, pady=10)
        fill_fn(b)
        return c

    # ── Scrollable canvas wrapper
    def _scrollable(self, parent, width=960):
        cvs = tk.Canvas(parent, bg=C["off_white"], highlightthickness=0)
        sb  = ttk.Scrollbar(parent, orient="vertical", command=cvs.yview)
        cvs.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y"); cvs.pack(side="left", fill="both", expand=True)
        inner = tk.Frame(cvs, bg=C["off_white"])
        win   = cvs.create_window((0,0), window=inner, anchor="nw")
        inner.bind("<Configure>", lambda e: cvs.configure(scrollregion=cvs.bbox("all")))
        cvs.bind("<Configure>", lambda e: cvs.itemconfig(win, width=e.width))
        def _on_mousewheel(e):
            try: cvs.yview_scroll(int(-1*(e.delta/120)), "units")
            except: pass
        cvs.bind_all("<MouseWheel>", _on_mousewheel)
        return inner

    # ── Treeview factory
    def _tv(self, parent, cols, widths, height=10, anchors=None):
        frame = tk.Frame(parent, bg=C["card"]); frame.pack(fill="both", expand=True)
        tv = ttk.Treeview(frame, columns=cols, show="headings", height=height)
        vsb = ttk.Scrollbar(frame, orient="vertical", command=tv.yview); tv.configure(yscrollcommand=vsb.set)
        for col, w, anc in zip(cols, widths, anchors or ["center"]*len(cols)):
            tv.heading(col, text=col); tv.column(col, width=w, anchor=anc)
        tv.tag_configure("present", foreground=C["green"])
        tv.tag_configure("absent",  foreground=C["red"])
        tv.tag_configure("alt",     background=C["off_white"])
        tv.pack(side="left", fill="both", expand=True)
        vsb.pack(side="right", fill="y")
        return tv

    # ══════════════════════════════════════════════════════════════════════════
    #  STUDENT SHELL
    # ══════════════════════════════════════════════════════════════════════════
    def _build_student_shell(self):
        self._sitems = [
            ("Dashboard",    "⌂", self._s_dashboard),  "---",
            ("My Courses",   "📚", self._s_registration),
            ("Attendance",   "✔", self._s_attendance),  "---",
            ("Examination",  "📋", self._s_exam),
            ("Fee Payment",  "₹",  self._s_fee),
            ("Grade Card",   "★",  self._s_grades),     "---",
            ("My Profile",   "◉",  self._s_profile),
        ]
        self._s_dashboard()

    # ── Student: Dashboard
    def _s_dashboard(self):
        _, c = self._build_chrome(self._sitems, "Dashboard")
        u = DB["students"][self.current_user]
        self._hdr(c, f"Welcome, {u['name'].split()[0]}!",
                  f"Semester {u['sem']}  ·  {u['batch']}  ·  {u['branch']}  ·  {u['section']}",
                  "Home › Dashboard")
        inner = self._scrollable(c)
        inner.config(padx=22)

        enrolled = [r for r in DB["registrations"] if r["enrollment"]==self.current_user]
        att      = [a for a in DB["attendance"]    if a["enrollment"]==self.current_user]
        present  = sum(1 for a in att if a["status"]=="Present")
        pct      = int(present/len(att)*100) if att else 0

        # stat row
        sr = tk.Frame(inner, bg=C["off_white"]); sr.pack(fill="x", pady=(4,14))
        self._stat(sr, "Courses Enrolled", len(enrolled), "📚", C["blue"],   C["blue_bg"])
        self._stat(sr, "Attendance %",     f"{pct}%",     "✔",  C["green"] if pct>=75 else C["orange"], C["green_bg"] if pct>=75 else C["orange_bg"])
        self._stat(sr, "Semester",         u["sem"],      "🎓", C["navy"],   C["light_bg"])
        self._stat(sr, "CGPA",             "8.42",        "★",  C["gold"],   C["orange_bg"])
        self._stat(sr, "Year",             u["year"],     "📅", C["purple"], C["purple_bg"])

        # enrolled courses table
        def fill_courses(p):
            cols = ("Code","Course Name","Faculty","Credits","Type","Section")
            tv = self._tv(p, cols, [80,260,170,70,60,80], anchors=["center","w","w","center","center","center"])
            for r in enrolled:
                crs = DB["courses"].get(r["course"],{})
                fid = crs.get("faculty","")
                fn  = DB["faculty"].get(fid,{}).get("short","—")
                tv.insert("","end", values=(r["course"], crs.get("name","—"), fn,
                                            crs.get("credits","—"), crs.get("type","—"), r["section"]))
        self._card(inner, "Registered Courses — Semester "+str(u["sem"]), fill_courses)

        # attendance summary
        def fill_att(p):
            by = {}
            for a in att:
                by.setdefault(a["course"],{"total":0,"present":0})
                by[a["course"]]["total"]+=1
                if a["status"]=="Present": by[a["course"]]["present"]+=1
            if not by:
                tk.Label(p, text="No attendance records yet.", fg=C["text_muted"], bg=C["card"], font=("Segoe UI",10)).pack(); return
            for code, d in by.items():
                p2 = int(d["present"]/d["total"]*100)
                col = C["green"] if p2>=75 else C["orange"] if p2>=60 else C["red"]
                bg  = C["green_bg"] if p2>=75 else C["orange_bg"] if p2>=60 else C["red_bg"]
                row = tk.Frame(p, bg=C["card"]); row.pack(fill="x", pady=3)
                cn  = DB["courses"].get(code,{}).get("name", code)
                tk.Label(row, text=f"{code} – {cn}", font=("Segoe UI",10), fg=C["text_dark"],
                         bg=C["card"], width=38, anchor="w").pack(side="left")
                tk.Label(row, text=f"{d['present']}/{d['total']}", font=("Segoe UI",10),
                         fg=C["text_muted"], bg=C["card"], width=8).pack(side="left")
                tk.Label(row, text=f"  {p2}%  ", font=("Segoe UI Semibold",10), fg=col, bg=bg,
                         padx=6, pady=2).pack(side="left", padx=6)
                if p2<75:
                    tk.Label(row, text="⚠ Below 75% — W grade risk", font=("Segoe UI",9),
                             fg=C["red"], bg=C["card"]).pack(side="left")
        self._card(inner, "Attendance Summary", fill_att)

        # quick actions
        def fill_qa(p):
            row = tk.Frame(p, bg=C["card"]); row.pack(anchor="w", pady=4)
            ttk.Button(row, text="Register / Drop Courses →", style="Gold.TButton",  command=self._s_registration).pack(side="left",padx=4)
            ttk.Button(row, text="View Full Attendance",       style="Navy.TButton",  command=self._s_attendance).pack(side="left",padx=4)
            ttk.Button(row, text="Download Grade Card",        style="Ghost.TButton").pack(side="left",padx=4)
        self._card(inner, "Quick Actions", fill_qa)

    # ── Student: Course Registration
    def _s_registration(self):
        _, c = self._build_chrome(self._sitems, "My Courses")
        u = DB["students"][self.current_user]
        self._hdr(c, "Course Registration",
                  f"{u['batch']}  ·  {u['section']}  ·  {u['branch']}  —  Select semester to browse & register",
                  "Home › My Courses › Registration")

        # ── Semester selector bar
        sel_bar = tk.Frame(c, bg=C["light_bg"])
        sel_bar.pack(fill="x", padx=22, pady=(0,6))
        tk.Label(sel_bar, text="  Browse Semester:", font=("Segoe UI Semibold",10),
                 fg=C["text_mid"], bg=C["light_bg"]).pack(side="left", pady=8)

        sem_var = tk.IntVar(value=u["sem"])
        max_sem = 8 if u["batch"]=="B.Tech" else 4
        sem_btns = {}
        for s in range(1, max_sem+1):
            btn = tk.Label(sel_bar, text=f"  {s}  ", font=("Segoe UI Semibold",10),
                           cursor="hand2", padx=4, pady=6)
            btn.pack(side="left", padx=2, pady=6)
            sem_btns[s] = btn

        # Section / Batch selectors
        tk.Label(sel_bar, text="  |  Section:", font=("Segoe UI",10),
                 fg=C["text_muted"], bg=C["light_bg"]).pack(side="left", padx=(10,2), pady=8)
        sec_var = tk.StringVar(value=u["section"])
        sec_cb = ttk.Combobox(sel_bar, textvariable=sec_var, state="readonly",
                               values=["Sec A","Sec B","Sec C"], width=7)
        sec_cb.pack(side="left", pady=6)

        tk.Label(sel_bar, text="  Batch:", font=("Segoe UI",10),
                 fg=C["text_muted"], bg=C["light_bg"]).pack(side="left", padx=(8,2), pady=8)
        bat_var = tk.StringVar(value=u["batch"])
        bat_cb = ttk.Combobox(sel_bar, textvariable=bat_var, state="readonly",
                               values=["B.Tech","M.Tech"], width=7)
        bat_cb.pack(side="left", pady=6)

        outer = tk.Frame(c, bg=C["off_white"]); outer.pack(fill="both", expand=True, padx=22, pady=4)

        # Available panel
        lf = tk.Frame(outer, bg=C["card"], highlightbackground=C["border"], highlightthickness=1)
        lf.pack(side="left", fill="both", expand=True, padx=(0,6))
        lhdr = tk.Frame(lf, bg=C["navy"], height=36); lhdr.pack(fill="x"); lhdr.pack_propagate(False)
        tk.Frame(lhdr, bg=C["gold"], width=4).pack(side="left", fill="y")
        avail_lbl = tk.Label(lhdr, text=f"  Available Courses — Semester {u['sem']}",
                             font=("Segoe UI Semibold",11), fg=C["white"], bg=C["navy"])
        avail_lbl.pack(side="left", pady=7)

        cols = ("Code","Course Name","Sem","Cr","Type","Faculty")
        tv_a = self._tv(lf, cols, [75,210,45,40,50,130], height=14,
                        anchors=["center","w","center","center","center","w"])

        # Mid buttons
        mid = tk.Frame(outer, bg=C["off_white"], width=82)
        mid.pack(side="left", fill="y", padx=4); mid.pack_propagate(False)
        tk.Frame(mid, bg=C["off_white"]).pack(expand=True)

        # Enrolled panel
        rf = tk.Frame(outer, bg=C["card"], highlightbackground=C["border"], highlightthickness=1)
        rf.pack(side="left", fill="both", expand=True, padx=(6,0))
        rhdr = tk.Frame(rf, bg=C["green"], height=36); rhdr.pack(fill="x"); rhdr.pack_propagate(False)
        tk.Frame(rhdr, bg=C["gold"], width=4).pack(side="left", fill="y")
        tk.Label(rhdr, text="  My Registered Courses (All Semesters)",
                 font=("Segoe UI Semibold",11), fg=C["white"], bg=C["green"]).pack(side="left", pady=7)

        tv_e = self._tv(rf, cols, [75,210,45,40,50,130], height=14,
                        anchors=["center","w","center","center","center","w"])

        # Populate enrolled
        def refresh_enrolled():
            tv_e.delete(*tv_e.get_children())
            for r in DB["registrations"]:
                if r["enrollment"] == self.current_user:
                    code = r["course"]; crs = DB["courses"].get(code,{})
                    fn = DB["faculty"].get(crs.get("faculty",""),{}).get("short","—")
                    tv_e.insert("","end", iid=code,
                                values=(code, crs.get("name","—"), crs.get("sem","—"),
                                        crs.get("credits","—"), crs.get("type","—"), fn))

        # Populate available for a given semester
        def refresh_available(sem):
            tv_a.delete(*tv_a.get_children())
            avail_lbl.config(text=f"  Available Courses — Semester {sem}")
            enrolled_codes = {r["course"] for r in DB["registrations"] if r["enrollment"]==self.current_user}
            for code, crs in DB["courses"].items():
                if crs["sem"] == sem and code not in enrolled_codes:
                    fn = DB["faculty"].get(crs["faculty"],{}).get("short","—")
                    tv_a.insert("","end", iid=code,
                                values=(code, crs["name"], crs["sem"],
                                        crs["credits"], crs["type"], fn))

        # Semester button styling
        def set_sem(s):
            sem_var.set(s)
            for n, b in sem_btns.items():
                if n == s:
                    b.config(bg=C["navy"], fg=C["gold"])
                else:
                    b.config(bg=C["light_bg"], fg=C["text_mid"])
            refresh_available(s)

        for s, btn in sem_btns.items():
            btn.bind("<Button-1>", lambda e, n=s: set_sem(n))

        def add_course():
            sel = tv_a.selection()
            if not sel: messagebox.showwarning("Select","Please select a course to add."); return
            code = sel[0]
            sec  = sec_var.get(); bat = bat_var.get()
            DB["registrations"].append({"enrollment":self.current_user,"course":code,
                                        "section":sec,"batch":bat})
            crs = DB["courses"][code]
            fac_name = DB["faculty"].get(crs["faculty"],{}).get("name","—")
            refresh_available(sem_var.get())
            refresh_enrolled()
            messagebox.showinfo("Registered",
                f"Registered for:\n{crs['name']}  (Sem {crs['sem']})\n\nSection: {sec}  ·  Batch: {bat}\nFaculty: {fac_name}")

        def drop_course():
            sel = tv_e.selection()
            if not sel: messagebox.showwarning("Select","Please select a course to drop."); return
            code = sel[0]
            crs  = DB["courses"].get(code,{})
            if not messagebox.askyesno("Confirm Drop",
                f"Drop course:\n{crs.get('name',code)}  (Sem {crs.get('sem','?')})\n\nThis removes you from attendance records."): return
            DB["registrations"] = [r for r in DB["registrations"]
                                   if not (r["enrollment"]==self.current_user and r["course"]==code)]
            refresh_available(sem_var.get())
            refresh_enrolled()

        ttk.Button(mid, text="Add →",  style="Green.TButton", command=add_course).pack(pady=6)
        ttk.Button(mid, text="← Drop", style="Red.TButton",   command=drop_course).pack(pady=6)
        tk.Frame(mid, bg=C["off_white"]).pack(expand=True)

        # Initial load
        refresh_enrolled()
        set_sem(u["sem"])

    # ── Student: Attendance
    def _s_attendance(self):
        _, c = self._build_chrome(self._sitems, "Attendance")
        self._hdr(c, "My Attendance", "Complete attendance record across all courses", "Home › Attendance")
        att = [a for a in DB["attendance"] if a["enrollment"]==self.current_user]
        inner = self._scrollable(c); inner.config(padx=22)

        total   = len(att); present = sum(1 for a in att if a["status"]=="Present"); absent = total-present
        pct     = int(present/total*100) if total else 0
        col     = C["green"] if pct>=75 else C["orange"] if pct>=60 else C["red"]
        sr = tk.Frame(inner, bg=C["off_white"]); sr.pack(fill="x", pady=(4,12))
        self._stat(sr,"Total Classes",total,"📅",C["navy"],C["blue_bg"])
        self._stat(sr,"Present",present,"✔",C["green"],C["green_bg"])
        self._stat(sr,"Absent",absent,"✗",C["red"],C["red_bg"])
        self._stat(sr,"Overall %",f"{pct}%","◎",col,C["green_bg"] if pct>=75 else C["orange_bg"] if pct>=60 else C["red_bg"])

        def fill(p):
            cols    = ("Date","Course","Course Name","Time","Session","Duration","Status")
            widths  = [100,80,240,70,80,80,80]
            anchors = ["center","center","w","center","center","center","center"]
            tv = self._tv(p, cols, widths, height=16, anchors=anchors)
            for a in sorted(att, key=lambda x:x["date"], reverse=True):
                cn  = DB["courses"].get(a["course"],{}).get("name","—")
                tag = "present" if a["status"]=="Present" else "absent"
                tv.insert("","end", values=(a["date"],a["course"],cn,a["time"],a["session"],a["duration"],a["status"]), tags=(tag,))
        self._card(inner,"Detailed Attendance Log",fill)

    # ── Student: Examination
    def _s_exam(self):
        _, c = self._build_chrome(self._sitems,"Examination")
        self._hdr(c,"Examination","End-semester exam schedule & hall ticket","Home › Examination")
        u = DB["students"][self.current_user]
        inner = self._scrollable(c); inner.config(padx=22)
        # Notice card
        notice = tk.Frame(inner, bg=C["orange_bg"], highlightbackground=C["orange"], highlightthickness=1)
        notice.pack(fill="x", pady=8, ipadx=12, ipady=10)
        tk.Label(notice, text="📢  End Semester Examination — April / May 2026",
                 font=("Segoe UI Semibold",12), fg=C["orange"], bg=C["orange_bg"]).pack(anchor="w", padx=12)
        tk.Label(notice, text="Time Table will be published by the Examination Section. Hall tickets will be available 7 days before exams.",
                 font=("Segoe UI",10), fg=C["text_mid"], bg=C["orange_bg"], wraplength=800).pack(anchor="w", padx=12, pady=(4,0))

        enrolled = [r["course"] for r in DB["registrations"] if r["enrollment"]==self.current_user]
        def fill_exam(p):
            cols    = ("Sr.","Code","Course Name","Credits","Type","Exam Date","Time","Venue")
            widths  = [40,80,260,65,60,120,80,100]
            anchors = ["center","center","w","center","center","center","center","center"]
            tv = self._tv(p, cols, widths, height=8, anchors=anchors)
            for i,code in enumerate(enrolled,1):
                crs = DB["courses"].get(code,{})
                tv.insert("","end", values=(i,code,crs.get("name","—"),crs.get("credits","—"),
                                            crs.get("type","—"),"To be announced","—","—"))
        self._card(inner, f"Enrolled Courses — Exam Schedule (Semester {u['sem']})", fill_exam)

    # ── Student: Fee
    def _s_fee(self):
        _, c = self._build_chrome(self._sitems,"Fee Payment")
        self._hdr(c,"Fee Payment","Academic year 2025–26  ·  Semester 6","Home › Fee Payment")
        inner = self._scrollable(c); inner.config(padx=22)
        u = DB["students"][self.current_user]
        fee_data = [
            ("Tuition Fee",          "₹1,20,000", "Paid",    "01-Jul-2025"),
            ("Hostel / Mess Fee",    "₹60,000",   "Paid",    "01-Jul-2025"),
            ("Library Fee",          "₹2,000",    "Paid",    "01-Jul-2025"),
            ("Examination Fee",      "₹2,500",    "Pending", "—"),
            ("Sports & Gymkhana",    "₹1,500",    "Paid",    "01-Jul-2025"),
        ]
        total_paid = sum(int(f[1].replace("₹","").replace(",","")) for f in fee_data if f[2]=="Paid")
        total_pending = sum(int(f[1].replace("₹","").replace(",","")) for f in fee_data if f[2]=="Pending")

        sr = tk.Frame(inner, bg=C["off_white"]); sr.pack(fill="x", pady=(4,12))
        self._stat(sr,"Total Paid",  f"₹{total_paid:,}",   "✔",C["green"],C["green_bg"])
        self._stat(sr,"Pending",     f"₹{total_pending:,}","⚠",C["red"],  C["red_bg"])
        self._stat(sr,"Academic Year","2025–26",            "📅",C["navy"], C["blue_bg"])

        def fill_fee(p):
            cols    = ("Description","Amount","Status","Date Paid")
            widths  = [260,130,100,130]
            anchors = ["w","center","center","center"]
            tv = self._tv(p, cols, widths, height=7, anchors=anchors)
            for row in fee_data:
                tag = "present" if row[2]=="Paid" else "absent"
                tv.insert("","end", values=row, tags=(tag,))
        self._card(inner,"Fee Details",fill_fee)

        def fill_pay(p):
            row = tk.Frame(p, bg=C["card"]); row.pack(anchor="w", pady=4)
            ttk.Button(row, text="Pay Examination Fee →", style="Gold.TButton").pack(side="left",padx=4)
            ttk.Button(row, text="Download Receipt",      style="Ghost.TButton").pack(side="left",padx=4)
        self._card(inner,"Payment Actions",fill_pay)

    # ── Student: Grades
    def _s_grades(self):
        _, c = self._build_chrome(self._sitems,"Grade Card")
        u = DB["students"][self.current_user]
        self._hdr(c,"Grade Card",f"Academic Transcript  ·  {u['batch']}  ·  {u['branch']}","Home › Grade Card")
        inner = self._scrollable(c); inner.config(padx=22)

        g = DB["grades"].get(self.current_user,[])
        if g:
            egp = sum(x["points"]*x["credits"] for x in g)
            ec  = sum(x["credits"] for x in g)
            sgpa= round(egp/ec,2) if ec else 0.0
        else:
            sgpa = 0.0

        sr = tk.Frame(inner, bg=C["off_white"]); sr.pack(fill="x", pady=(4,12))
        self._stat(sr,"SGPA (Sem V)", sgpa,    "★",C["gold"],  C["orange_bg"])
        self._stat(sr,"CGPA",         "8.42",  "◎",C["navy"],  C["blue_bg"])
        self._stat(sr,"Earned Credits","18",   "✔",C["green"], C["green_bg"])
        self._stat(sr,"Backlog",       "0",    "✗",C["text_muted"],C["light_bg"])

        def fill_sem(p, records, sem_label):
            cols    = ("Code","Course Name","L-T-P","Credits","Grade","Grade Points","Weighted")
            widths  = [85,260,80,70,70,110,80]
            anchors = ["center","w","center","center","center","center","center"]
            tv = self._tv(p, cols, widths, height=max(len(records),3), anchors=anchors)
            for r in records:
                crs = DB["courses"].get(r["code"],{})
                tv.insert("","end", values=(r["code"], r["name"], crs.get("ltp","—"),
                                            r["credits"], r["grade"], r["points"],
                                            r["points"]*r["credits"]))
            total_w = sum(r["points"]*r["credits"] for r in records)
            total_c = sum(r["credits"] for r in records)
            sgpa_row = round(total_w/total_c,2) if total_c else "—"
            tk.Label(p, text=f"  Semester SGPA: {sgpa_row}   |   Total Credits: {total_c}",
                     font=("Segoe UI Semibold",11), fg=C["navy"], bg=C["card"]).pack(anchor="w", pady=(6,0))

        if g: self._card(inner, "Semester V — Grade Report", lambda p: fill_sem(p, g, "Sem V"))

        tk.Label(inner, text="Grades for Semester VI will be published after End Semester Examination.",
                 font=("Segoe UI",10), fg=C["text_muted"], bg=C["off_white"]).pack(anchor="w", pady=6)

    # ── Student: Profile
    def _s_profile(self):
        _, c = self._build_chrome(self._sitems,"My Profile")
        u = DB["students"][self.current_user]
        self._hdr(c,"My Profile","Personal & Academic Information","Home › My Profile")
        inner = self._scrollable(c); inner.config(padx=22)

        def fill_profile(p):
            fields = [
                ("Full Name",         u["name"]),
                ("Enrollment No.",    self.current_user),
                ("Roll Number",       u["roll"]),
                ("Programme",         u["batch"]),
                ("Branch",            "Computer Science & Engineering"),
                ("Section",           u["section"]),
                ("Current Semester",  str(u["sem"])),
                ("Academic Year",     "3rd Year" if u["year"]==3 else f"{u['year']}{'st' if u['year']==1 else 'nd' if u['year']==2 else 'th'} Year"),
                ("Date of Birth",     u.get("dob","—")),
                ("Mobile",            u.get("phone","—")),
                ("Email",             u.get("email","—")),
                ("Institute",         "VNIT Nagpur"),
            ]
            for label, val in fields:
                row = tk.Frame(p, bg=C["card"]); row.pack(fill="x", pady=5)
                tk.Label(row, text=label+":", font=("Segoe UI Semibold",10), fg=C["text_muted"],
                         bg=C["card"], width=22, anchor="w").pack(side="left")
                tk.Label(row, text=val, font=("Segoe UI",11), fg=C["navy"], bg=C["card"]).pack(side="left")
        self._card(inner,"Student Profile",fill_profile)

    # ══════════════════════════════════════════════════════════════════════════
    #  FACULTY SHELL
    # ══════════════════════════════════════════════════════════════════════════
    def _build_faculty_shell(self):
        self._fitems = [
            ("Dashboard",          "⌂", self._f_dashboard),  "---",
            ("Mark Attendance",    "✔", self._f_attendance),
            ("Attendance Reports", "📊", self._f_reports),    "---",
            ("My Courses",         "📚", self._f_courses),
            ("Student Register",   "👥", self._f_students),
            ("Class Logistics",    "⚙", self._f_logistics),  "---",
            ("Faculty Directory",  "🏛", self._f_directory),
            ("My Profile",         "◉", self._f_profile),
        ]
        self._f_dashboard()

    # ── Faculty: Dashboard
    def _f_dashboard(self):
        _, c = self._build_chrome(self._fitems,"Dashboard")
        u = DB["faculty"][self.current_user]
        self._hdr(c, u["name"], f"{u['designation']}  ·  Dept. of {u['dept']}  ·  {u['qual']}", "Home › Dashboard")
        inner = self._scrollable(c); inner.config(padx=22)

        my_courses  = [v for v in DB["courses"].values() if v["faculty"]==self.current_user]
        my_codes    = {c2["code"] if "code" in c2 else k for k,c2 in DB["courses"].items() if c2["faculty"]==self.current_user}
        # rebuild properly
        my_codes2   = {k for k,v in DB["courses"].items() if v["faculty"]==self.current_user}
        total_stu   = sum(1 for r in DB["registrations"] if r["course"] in my_codes2)
        total_att   = len([a for a in DB["attendance"] if a["course"] in my_codes2])

        sr = tk.Frame(inner, bg=C["off_white"]); sr.pack(fill="x", pady=(4,14))
        self._stat(sr,"Assigned Courses", len(my_courses), "📚",C["blue"],   C["blue_bg"])
        self._stat(sr,"Total Students",   total_stu,        "👥",C["navy"],   C["light_bg"])
        self._stat(sr,"Classes Logged",   total_att,        "📅",C["green"],  C["green_bg"])
        # Shorten research area to fit the stat card (first keyword phrase only)
        area_short = u["area"].split(",")[0].strip()
        if len(area_short) > 18: area_short = area_short[:16] + "…"
        self._stat(sr,"Research Area",    area_short,        "🔬",C["purple"],C["purple_bg"])

        def fill_courses(p):
            cols    = ("Code","Course Name","Sem","Credits","L-T-P","Type","Enrolled")
            widths  = [80,260,55,70,80,60,80]
            anchors = ["center","w","center","center","center","center","center"]
            tv = self._tv(p, cols, widths, height=min(len(my_courses)+1,8), anchors=anchors)
            for k,crs in DB["courses"].items():
                if crs["faculty"]==self.current_user:
                    enrolled = sum(1 for r in DB["registrations"] if r["course"]==k)
                    tv.insert("","end", values=(k, crs["name"], crs["sem"], crs["credits"],
                                                crs["ltp"], crs["type"], enrolled))
        self._card(inner,"My Assigned Courses",fill_courses)

        def fill_recent(p):
            recent = sorted(DB["attendance"], key=lambda a:a["date"], reverse=True)[:8]
            my_recent = [a for a in recent if a["course"] in my_codes2]
            if not my_recent:
                tk.Label(p,text="No recent attendance.",fg=C["text_muted"],bg=C["card"],font=("Segoe UI",10)).pack(); return
            cols    = ("Date","Enrollment","Student Name","Course","Status")
            widths  = [110,110,220,100,80]
            anchors = ["center","center","w","center","center"]
            tv = self._tv(p, cols, widths, height=6, anchors=anchors)
            for a in my_recent:
                sn  = DB["students"].get(a["enrollment"],{}).get("name","—")
                tag = "present" if a["status"]=="Present" else "absent"
                tv.insert("","end", values=(a["date"],a["enrollment"],sn,a["course"],a["status"]),tags=(tag,))
        self._card(inner,"Recent Attendance Activity",fill_recent)

        def fill_qa(p):
            row = tk.Frame(p,bg=C["card"]); row.pack(anchor="w",pady=4)
            ttk.Button(row,text="Mark Attendance →",     style="Gold.TButton", command=self._f_attendance).pack(side="left",padx=4)
            ttk.Button(row,text="View Reports",          style="Navy.TButton", command=self._f_reports).pack(side="left",padx=4)
            ttk.Button(row,text="Student Register",      style="Ghost.TButton",command=self._f_students).pack(side="left",padx=4)
            ttk.Button(row,text="Faculty Directory",     style="Ghost.TButton",command=self._f_directory).pack(side="left",padx=4)
        self._card(inner,"Quick Actions",fill_qa)

    # ── Faculty: Mark Attendance
    def _f_attendance(self):
        _, c = self._build_chrome(self._fitems,"Mark Attendance")
        self._hdr(c,"Mark Daily Attendance","Select course → Load students → Mark attendance","Home › Mark Attendance")
        outer = tk.Frame(c,bg=C["off_white"]); outer.pack(fill="both",expand=True,padx=22,pady=4)

        # Config card
        cfg = tk.Frame(outer,bg=C["card"],highlightbackground=C["border"],highlightthickness=1)
        cfg.pack(fill="x",pady=(0,8))
        ch = tk.Frame(cfg,bg=C["navy"],height=36); ch.pack(fill="x"); ch.pack_propagate(False)
        tk.Frame(ch,bg=C["gold"],width=4).pack(side="left",fill="y")
        tk.Label(ch,text="  1.  Class Details & Course Selection",
                 font=("Segoe UI Semibold",11),fg=C["white"],bg=C["navy"]).pack(side="left",pady=7)
        cb = tk.Frame(cfg,bg=C["card"]); cb.pack(fill="x",padx=14,pady=10)

        def lbl(p,text,w=8): return tk.Label(p,text=text,font=("Segoe UI",10),fg=C["text_mid"],bg=C["card"],width=w,anchor="w")
        def ent(p,val,w=12,state="normal"):
            v=tk.StringVar(value=val)
            e=tk.Entry(p,textvariable=v,font=("Segoe UI",10),bg=C["light_bg"],fg=C["text_dark"],
                       relief="flat",highlightbackground=C["border"],highlightthickness=1,width=w,state=state)
            e._var=v; return e
        def cmb(p,vals,val=None,w=10):
            v=tk.StringVar(value=val or vals[0])
            cb2=ttk.Combobox(p,textvariable=v,state="readonly",values=vals,width=w)
            cb2._var=v; return cb2

        r1=tk.Frame(cb,bg=C["card"]); r1.pack(fill="x",pady=4)
        lbl(r1,"Date:").pack(side="left")
        date_e=ent(r1,datetime.date.today().strftime("%d/%m/%Y"),12); date_e.pack(side="left",ipady=6,padx=(0,18))
        lbl(r1,"Time:",6).pack(side="left")
        time_cb=cmb(r1,["8 AM","9 AM","10 AM","11 AM","12 PM","2 PM","3 PM","4 PM"],"11 AM",9); time_cb.pack(side="left",padx=(0,18))
        lbl(r1,"Session:",8).pack(side="left")
        sess_cb=cmb(r1,["Morning","Afternoon","Evening"],"Morning",10); sess_cb.pack(side="left",padx=(0,18))
        lbl(r1,"Duration:",9).pack(side="left")
        dur_cb=cmb(r1,["1 Hour","2 Hours","3 Hours"],"1 Hour",9); dur_cb.pack(side="left")

        r2=tk.Frame(cb,bg=C["card"]); r2.pack(fill="x",pady=(8,4))
        lbl(r2,"Course:",8).pack(side="left")
        my_crs = {k:v for k,v in DB["courses"].items() if v["faculty"]==self.current_user}
        crs_opts = [f"{k} – {v['name']}" for k,v in my_crs.items()]
        crs_cb=cmb(r2, crs_opts, crs_opts[0] if crs_opts else "", 36); crs_cb.pack(side="left",padx=(0,18))
        lbl(r2,"Section:",8).pack(side="left")
        sec_cb=cmb(r2,["Sec A","Sec B","Sec C"],"Sec A",8); sec_cb.pack(side="left",padx=(0,18))
        lbl(r2,"Batch:",6).pack(side="left")
        bat_cb=cmb(r2,["B.Tech","M.Tech"],"B.Tech",8); bat_cb.pack(side="left")

        # Attendance card
        ac = tk.Frame(outer,bg=C["card"],highlightbackground=C["border"],highlightthickness=1)
        ac.pack(fill="both",expand=True)
        ah = tk.Frame(ac,bg=C["orange"],height=36); ah.pack(fill="x"); ah.pack_propagate(False)
        tk.Frame(ah,bg=C["gold"],width=4).pack(side="left",fill="y")
        tk.Label(ah,text="  2.  Mark Attendance",font=("Segoe UI Semibold",11),fg=C["white"],bg=C["orange"]).pack(side="left",pady=7)

        toolbar=tk.Frame(ac,bg=C["light_bg"]); toolbar.pack(fill="x")
        self._att_vars={}
        srf=tk.Frame(ac,bg=C["card"]); srf.pack(fill="both",expand=True)

        def load_students():
            for w in srf.winfo_children(): w.destroy()
            self._att_vars.clear()
            code = crs_cb._var.get().split(" –")[0].strip()
            sec  = sec_cb._var.get(); bat=bat_cb._var.get()
            enrolled=[r["enrollment"] for r in DB["registrations"]
                      if r["course"]==code and r["section"]==sec and r["batch"]==bat]
            if not enrolled:
                tk.Label(srf,text="No students enrolled for this course / section / batch.",
                         font=("Segoe UI",11),fg=C["text_muted"],bg=C["card"]).pack(pady=24); return
            # header
            hrow=tk.Frame(srf,bg=C["navy"]); hrow.pack(fill="x")
            for t,pw in [("#",40),("Enrollment",130),("Student Name",280),("Roll",60),("Present",100),("Absent",100)]:
                tk.Label(hrow,text=t,font=("Segoe UI Semibold",10),fg=C["white"],bg=C["navy"],width=pw//7,pady=8).pack(side="left",padx=2)
            # student rows
            for i,enr in enumerate(enrolled):
                s=DB["students"].get(enr,{}); var=tk.StringVar(value="Present")
                self._att_vars[enr]=var
                rbg=C["card"] if i%2==0 else C["off_white"]
                sr2=tk.Frame(srf,bg=rbg); sr2.pack(fill="x")
                tk.Label(sr2,text=str(i+1),font=("Segoe UI",10),fg=C["text_muted"],bg=rbg,width=4,pady=10).pack(side="left",padx=2)
                tk.Label(sr2,text=enr,font=("Segoe UI",10),fg=C["text_mid"],bg=rbg,width=14).pack(side="left",padx=2)
                tk.Label(sr2,text=s.get("name","—"),font=("Segoe UI",11),fg=C["text_dark"],bg=rbg,width=28,anchor="w").pack(side="left",padx=2)
                tk.Label(sr2,text=s.get("roll","—"),font=("Segoe UI",10),fg=C["text_muted"],bg=rbg,width=6).pack(side="left",padx=2)
                tk.Radiobutton(sr2,text="Present",variable=var,value="Present",font=("Segoe UI",10),
                               fg=C["green"],bg=rbg,selectcolor=C["green_bg"],activebackground=rbg).pack(side="left",padx=12)
                tk.Radiobutton(sr2,text="Absent",variable=var,value="Absent",font=("Segoe UI",10),
                               fg=C["red"],bg=rbg,selectcolor=C["red_bg"],activebackground=rbg).pack(side="left",padx=12)

        ttk.Button(toolbar,text="  ⟳ Load Student List",style="Gold.TButton",command=load_students).pack(side="left",padx=8,pady=6)
        ttk.Button(toolbar,text="✔ Mark All Present",style="Green.TButton",
                   command=lambda:[v.set("Present") for v in self._att_vars.values()]).pack(side="left",padx=4,pady=6)
        ttk.Button(toolbar,text="✗ Mark All Absent",style="Red.TButton",
                   command=lambda:[v.set("Absent") for v in self._att_vars.values()]).pack(side="left",padx=4,pady=6)

        # Submit bar
        subbar=tk.Frame(ac,bg=C["navy"],height=48); subbar.pack(fill="x",side="bottom"); subbar.pack_propagate(False)
        tk.Frame(subbar,bg=C["navy"]).pack(side="left",expand=True)
        def submit():
            if not self._att_vars: messagebox.showwarning("No Students","Please load students first."); return
            code=crs_cb._var.get().split(" –")[0].strip()
            dt=datetime.date.today().strftime("%d-%b-%Y").upper()
            for enr,var in self._att_vars.items():
                DB["attendance"].append({"date":dt,"enrollment":enr,"course":code,"status":var.get(),
                                         "time":time_cb._var.get(),"session":sess_cb._var.get(),"duration":dur_cb._var.get()})
            p_count=sum(1 for v in self._att_vars.values() if v.get()=="Present")
            messagebox.showinfo("Submitted",f"Attendance submitted!\nDate: {dt}\nPresent: {p_count}/{len(self._att_vars)}")
        ttk.Button(subbar,text="  Submit Attendance  →",style="Gold.TButton",command=submit).pack(side="right",padx=14,pady=8)

    # ── Faculty: Attendance Reports
    def _f_reports(self):
        _, c = self._build_chrome(self._fitems,"Attendance Reports")
        self._hdr(c,"Attendance Reports","Complete logs for your courses","Home › Attendance Reports")
        outer=tk.Frame(c,bg=C["off_white"]); outer.pack(fill="both",expand=True,padx=22,pady=4)

        my_codes={k for k,v in DB["courses"].items() if v["faculty"]==self.current_user}
        opts=["All Courses"]+[f"{k} – {v['name']}" for k,v in DB["courses"].items() if v["faculty"]==self.current_user]

        flt=tk.Frame(outer,bg=C["card"],highlightbackground=C["border"],highlightthickness=1); flt.pack(fill="x",pady=(0,8))
        fb=tk.Frame(flt,bg=C["card"]); fb.pack(fill="x",padx=14,pady=10)
        tk.Label(fb,text="Course:",font=("Segoe UI",10),fg=C["text_mid"],bg=C["card"]).pack(side="left",padx=(0,6))
        fv=tk.StringVar(value="All Courses")
        ttk.Combobox(fb,textvariable=fv,state="readonly",values=opts,width=36).pack(side="left",padx=(0,14))
        tk.Label(fb,text="Status:",font=("Segoe UI",10),fg=C["text_mid"],bg=C["card"]).pack(side="left",padx=(0,6))
        sv=tk.StringVar(value="All")
        ttk.Combobox(fb,textvariable=sv,state="readonly",values=["All","Present","Absent"],width=10).pack(side="left")

        card2=tk.Frame(outer,bg=C["card"],highlightbackground=C["border"],highlightthickness=1); card2.pack(fill="both",expand=True)
        ch2=tk.Frame(card2,bg=C["navy"],height=36); ch2.pack(fill="x"); ch2.pack_propagate(False)
        tk.Frame(ch2,bg=C["gold"],width=4).pack(side="left",fill="y")
        tk.Label(ch2,text="  Complete Attendance Log",font=("Segoe UI Semibold",11),fg=C["white"],bg=C["navy"]).pack(side="left",pady=7)

        cols=("Date","Enrollment","Student Name","Course","Time","Session","Status")
        widths=[100,110,220,90,70,80,80]; anchors=["center","center","w","center","center","center","center"]
        tv=self._tv(card2,cols,widths,height=18,anchors=anchors)

        def refresh():
            tv.delete(*tv.get_children())
            sel_code=fv.get().split(" –")[0].strip() if fv.get()!="All Courses" else None
            sel_stat=sv.get()
            for a in sorted(DB["attendance"],key=lambda x:x["date"],reverse=True):
                if a["course"] not in my_codes: continue
                if sel_code and a["course"]!=sel_code: continue
                if sel_stat!="All" and a["status"]!=sel_stat: continue
                sn=DB["students"].get(a["enrollment"],{}).get("name","—")
                tag="present" if a["status"]=="Present" else "absent"
                tv.insert("","end",values=(a["date"],a["enrollment"],sn,a["course"],a["time"],a["session"],a["status"]),tags=(tag,))

        ttk.Button(fb,text="Apply",style="Navy.TButton",command=refresh).pack(side="left",padx=10)
        ttk.Button(fb,text="Reset",style="Ghost.TButton",command=lambda:[fv.set("All Courses"),sv.set("All"),refresh()]).pack(side="left",padx=4)
        refresh()

    # ── Faculty: My Courses
    def _f_courses(self):
        _, c = self._build_chrome(self._fitems,"My Courses")
        self._hdr(c,"My Courses","All courses assigned to you","Home › My Courses")
        inner=self._scrollable(c); inner.config(padx=22)
        my_c={(k,v["sem"]):v for k,v in DB["courses"].items() if v["faculty"]==self.current_user}
        for (code,sem),crs in sorted(my_c.items(),key=lambda x:x[0][1]):
            enrolled=sum(1 for r in DB["registrations"] if r["course"]==code)
            card=tk.Frame(inner,bg=C["card"],highlightbackground=C["border"],highlightthickness=1)
            card.pack(fill="x",pady=5,ipadx=16,ipady=12)
            top=tk.Frame(card,bg=C["card"]); top.pack(fill="x")
            tk.Label(top,text=f"{code} — {crs['name']}",font=("Segoe UI Black",13),fg=C["navy"],bg=C["card"]).pack(side="left")
            for txt,col,bg in [(crs["type"], C["blue"], C["blue_bg"]),(f"{enrolled} Students",C["green"],C["green_bg"])]:
                tk.Label(top,text=f"  {txt}  ",font=("Segoe UI Semibold",9),fg=col,bg=bg,padx=6,pady=2).pack(side="right",padx=4)
            tk.Label(card,text=f"Semester {sem}  ·  {crs['credits']} Credits  ·  L-T-P: {crs['ltp']}",
                     font=("Segoe UI",9),fg=C["text_muted"],bg=C["card"]).pack(anchor="w")

    # ── Faculty: Student Register (view & add students for own courses)
    def _f_students(self):
        _, c = self._build_chrome(self._fitems,"Student Register")
        self._hdr(c,"Student Register","View all students enrolled in your courses  ·  Add new students",
                  "Home › Student Register")
        outer=tk.Frame(c,bg=C["off_white"]); outer.pack(fill="both",expand=True,padx=22,pady=4)

        my_codes={k for k,v in DB["courses"].items() if v["faculty"]==self.current_user}
        opts=[f"{k} – {DB['courses'][k]['name']}" for k in sorted(my_codes)]

        top_row=tk.Frame(outer,bg=C["off_white"]); top_row.pack(fill="x",pady=(0,8))
        tk.Label(top_row,text="Filter by Course:",font=("Segoe UI",10),fg=C["text_mid"],bg=C["off_white"]).pack(side="left",padx=(0,6))
        fv=tk.StringVar(value=opts[0] if opts else "")
        ttk.Combobox(top_row,textvariable=fv,state="readonly",values=opts,width=38).pack(side="left",padx=(0,12))
        ttk.Button(top_row,text="Load Students",style="Gold.TButton").pack(side="left",padx=4)

        # ADD student popup
        def open_add():
            win=tk.Toplevel(self); win.title("Add Student to Course"); win.geometry("560px"); win.configure(bg=C["off_white"]); win.grab_set()
            win.geometry("560x480")
            tk.Frame(win,bg=C["gold"],height=4).pack(fill="x")
            tk.Frame(win,bg=C["navy"],height=40).pack(fill="x")
            tk.Label(win,text="  Add Student Enrollment",font=("Segoe UI Semibold",12),fg=C["white"],bg=C["navy"]).place(x=12,y=44)

            body=tk.Frame(win,bg=C["off_white"]); body.pack(fill="both",expand=True,padx=28,pady=24)
            tk.Label(body,text="This will register the student for the selected course,\nmaking them appear in your attendance list.",
                     font=("Segoe UI",10),fg=C["text_mid"],bg=C["off_white"],justify="left").pack(anchor="w",pady=(0,14))

            def frow(lbl,widget_fn):
                f=tk.Frame(body,bg=C["off_white"]); f.pack(fill="x",pady=6)
                tk.Label(f,text=lbl,font=("Segoe UI Semibold",9),fg=C["text_mid"],bg=C["off_white"],width=20,anchor="w").pack(side="left")
                w=widget_fn(f); w.pack(side="left",fill="x",expand=True,ipady=6); return w

            e_enr = frow("Enrollment No. *", lambda p: tk.Entry(p,font=("Segoe UI",11),bg=C["light_bg"],fg=C["text_dark"],
                         relief="flat",highlightbackground=C["border"],highlightthickness=1))
            sel_course_var=tk.StringVar(value=opts[0] if opts else "")
            cb_crs=frow("Course *", lambda p: ttk.Combobox(p,textvariable=sel_course_var,state="readonly",values=opts,font=("Segoe UI",11)))
            cb_crs._var=sel_course_var
            cb_sec=frow("Section *", lambda p: ttk.Combobox(p,state="readonly",values=["Sec A","Sec B","Sec C"],font=("Segoe UI",11)))
            cb_bat=frow("Batch *",   lambda p: ttk.Combobox(p,state="readonly",values=["B.Tech","M.Tech"],font=("Segoe UI",11)))
            cb_sec.set("Sec A"); cb_bat.set("B.Tech")

            def do_add():
                enr  = e_enr.get().strip().upper()
                code = sel_course_var.get().split(" –")[0].strip()
                sec  = cb_sec.get(); bat=cb_bat.get()
                if enr not in DB["students"]:
                    messagebox.showerror("Not Found",f"Enrollment {enr} not found in student database.\nPlease register the student first.",parent=win); return
                already=[r for r in DB["registrations"] if r["enrollment"]==enr and r["course"]==code]
                if already:
                    messagebox.showwarning("Already Enrolled",f"{DB['students'][enr]['name']} is already enrolled in {code}.",parent=win); return
                DB["registrations"].append({"enrollment":enr,"course":code,"section":sec,"batch":bat})
                messagebox.showinfo("Added",f"✔  {DB['students'][enr]['name']} added to {code}!\nThey will now appear in your attendance list.",parent=win)
                win.destroy(); self._f_students()

            bar=tk.Frame(win,bg=C["navy"]); bar.pack(fill="x",side="bottom")
            ttk.Button(bar,text="✔  Add to Course",style="Green.TButton",command=do_add).pack(side="right",padx=12,pady=10)
            ttk.Button(bar,text="Cancel",style="Ghost.TButton",command=win.destroy).pack(side="right",padx=4,pady=10)

        ttk.Button(top_row,text="+ Add Student to Course",style="Green.TButton",command=open_add).pack(side="left",padx=8)
        ttk.Button(top_row,text="+ Register New Student",style="Purple.TButton",command=self._show_new_student_registration).pack(side="left",padx=4)

        # student table
        card=tk.Frame(outer,bg=C["card"],highlightbackground=C["border"],highlightthickness=1); card.pack(fill="both",expand=True)
        ch=tk.Frame(card,bg=C["navy"],height=36); ch.pack(fill="x"); ch.pack_propagate(False)
        tk.Frame(ch,bg=C["gold"],width=4).pack(side="left",fill="y")
        tk.Label(ch,text="  Enrolled Students — All My Courses",font=("Segoe UI Semibold",11),fg=C["white"],bg=C["navy"]).pack(side="left",pady=7)

        cols=("Enrollment","Student Name","Course Code","Course Name","Sem","Section","Batch")
        widths=[110,220,100,220,55,80,80]; anchors=["center","w","center","w","center","center","center"]
        tv=self._tv(card,cols,widths,height=18,anchors=anchors)

        for r in DB["registrations"]:
            if r["course"] in my_codes:
                s=DB["students"].get(r["enrollment"],{})
                crs=DB["courses"].get(r["course"],{})
                tv.insert("","end",values=(r["enrollment"],s.get("name","—"),r["course"],
                                           crs.get("name","—"),crs.get("sem","—"),r["section"],r["batch"]))

    # ── Faculty: Class Logistics
    def _f_logistics(self):
        _, c = self._build_chrome(self._fitems,"Class Logistics")
        self._hdr(c,"Class Logistics","Update class settings for your courses","Home › Class Logistics")
        inner=self._scrollable(c); inner.config(padx=22)

        my_c=[f"{k} – {v['name']}" for k,v in DB["courses"].items() if v["faculty"]==self.current_user]
        def fill(p):
            for label,vals,default in [
                ("Course",  my_c,                               my_c[0] if my_c else ""),
                ("Time",    ["8 AM","9 AM","10 AM","11 AM","12 PM","2 PM","3 PM","4 PM"],"11 AM"),
                ("Session", ["Morning","Afternoon","Evening"],  "Morning"),
                ("Duration",["1 Hour","2 Hours","3 Hours"],     "1 Hour"),
                ("Section", ["Sec A","Sec B","Sec C"],          "Sec A"),
                ("Batch",   ["B.Tech","M.Tech"],                "B.Tech"),
            ]:
                row=tk.Frame(p,bg=C["card"]); row.pack(fill="x",pady=7)
                tk.Label(row,text=label+":",font=("Segoe UI Semibold",10),fg=C["text_mid"],bg=C["card"],width=14,anchor="w").pack(side="left")
                v=tk.StringVar(value=default)
                ttk.Combobox(row,textvariable=v,state="readonly",values=vals,width=36).pack(side="left")
            _sep(p,pady=10)
            ttk.Button(p,text="Save Class Settings",style="Gold.TButton",
                       command=lambda:messagebox.showinfo("Saved","Class logistics updated successfully!")).pack(anchor="w")
        self._card(inner,"Change Class Settings",fill)

    # ── Faculty: Faculty Directory
    def _f_directory(self):
        _, c = self._build_chrome(self._fitems,"Faculty Directory")
        self._hdr(c,"Faculty Directory","Department of Computer Science & Engineering, VNIT Nagpur","Home › Faculty Directory")
        inner=self._scrollable(c); inner.config(padx=22)
        def fill(p):
            cols=("ID","Name","Designation","Qualification","Research Area")
            widths=[65,180,160,90,340]; anchors=["center","w","w","center","w"]
            tv=self._tv(p,cols,widths,height=18,anchors=anchors)
            for fid,f in DB["faculty"].items():
                tv.insert("","end",values=(fid,f["name"],f["designation"],f["qual"],f["area"]))
        self._card(inner,f"Faculty Members — CSE Department  ({len(DB['faculty'])} faculty)",fill)

    # ── Faculty: Profile
    def _f_profile(self):
        _, c = self._build_chrome(self._fitems,"My Profile")
        u = DB["faculty"][self.current_user]
        self._hdr(c,"My Profile","Faculty Information","Home › My Profile")
        inner=self._scrollable(c); inner.config(padx=22)
        def fill(p):
            for label,val in [
                ("Faculty ID",       self.current_user),
                ("Full Name",        u["name"]),
                ("Designation",      u["designation"]),
                ("Qualification",    u["qual"]),
                ("Department",       u["dept"]),
                ("Research Area",    u["area"]),
                ("Institute",        "VNIT Nagpur"),
                ("Session",          "2025–26"),
            ]:
                row=tk.Frame(p,bg=C["card"]); row.pack(fill="x",pady=6)
                tk.Label(row,text=label+":",font=("Segoe UI Semibold",10),fg=C["text_muted"],
                         bg=C["card"],width=20,anchor="w").pack(side="left")
                tk.Label(row,text=val,font=("Segoe UI",11),fg=C["navy"],bg=C["card"],wraplength=600,anchor="w",justify="left").pack(side="left")
        self._card(inner,"Faculty Profile",fill)


if __name__=="__main__":
    app=VNITApp()
    app.mainloop()
