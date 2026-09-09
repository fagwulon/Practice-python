from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    ListFlowable, ListItem
)

out = "/mnt/data/CareerReady_Job_Seeker_Starter_Kit.pdf"

# Brand palette
PURPLE = colors.HexColor("#5B21B6")
INDIGO = colors.HexColor("#4338CA")
LIGHT = colors.HexColor("#F5F3FF")
GRAY = colors.HexColor("#E5E7EB")
DARK = colors.HexColor("#111827")
MID = colors.HexColor("#4B5563")
WHITE = colors.white

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="CoverTitle", parent=styles["Title"], fontName="Helvetica-Bold",
    fontSize=30, leading=34, textColor=WHITE, alignment=TA_CENTER, spaceAfter=12
))
styles.add(ParagraphStyle(
    name="CoverSub", parent=styles["Normal"], fontName="Helvetica",
    fontSize=13, leading=18, textColor=WHITE, alignment=TA_CENTER
))
styles.add(ParagraphStyle(
    name="H1CR", parent=styles["Heading1"], fontName="Helvetica-Bold",
    fontSize=22, leading=27, textColor=PURPLE, spaceBefore=6, spaceAfter=12
))
styles.add(ParagraphStyle(
    name="H2CR", parent=styles["Heading2"], fontName="Helvetica-Bold",
    fontSize=14, leading=18, textColor=INDIGO, spaceBefore=10, spaceAfter=6
))
styles.add(ParagraphStyle(
    name="BodyCR", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=10.5, leading=16, textColor=DARK, spaceAfter=7
))
styles.add(ParagraphStyle(
    name="SmallCR", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=8.5, leading=12, textColor=MID, spaceAfter=5
))
styles.add(ParagraphStyle(
    name="QuoteCR", parent=styles["BodyText"], fontName="Helvetica-BoldOblique",
    fontSize=13, leading=19, textColor=INDIGO, leftIndent=12, rightIndent=12,
    spaceBefore=10, spaceAfter=10
))
styles.add(ParagraphStyle(
    name="BoxCR", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=9.5, leading=14, textColor=DARK, spaceAfter=0
))
styles.add(ParagraphStyle(
    name="TOC", parent=styles["BodyText"], fontName="Helvetica",
    fontSize=10.5, leading=18, textColor=DARK
))

def bullet(items):
    return ListFlowable(
        [ListItem(Paragraph(x, styles["BodyCR"]), leftIndent=10) for x in items],
        bulletType="bullet", start="circle", leftIndent=18, bulletFontSize=6
    )

def table(data, widths=None, header=True):
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0, hAlign="LEFT")
    cmds = [
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("FONTNAME", (0,0), (-1,-1), "Helvetica"),
        ("FONTSIZE", (0,0), (-1,-1), 9),
        ("LEADING", (0,0), (-1,-1), 13),
        ("TEXTCOLOR", (0,0), (-1,-1), DARK),
        ("GRID", (0,0), (-1,-1), 0.4, GRAY),
        ("LEFTPADDING", (0,0), (-1,-1), 7),
        ("RIGHTPADDING", (0,0), (-1,-1), 7),
        ("TOPPADDING", (0,0), (-1,-1), 7),
        ("BOTTOMPADDING", (0,0), (-1,-1), 7),
    ]
    if header:
        cmds += [
            ("BACKGROUND", (0,0), (-1,0), PURPLE),
            ("TEXTCOLOR", (0,0), (-1,0), WHITE),
            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ]
        if len(data) > 1:
            cmds.append(("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, LIGHT]))
    t.setStyle(TableStyle(cmds))
    return t

def footer(canvas, doc):
    canvas.saveState()
    w, h = A4
    canvas.setStrokeColor(GRAY)
    canvas.line(18*mm, 14*mm, w-18*mm, 14*mm)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(MID)
    canvas.drawString(18*mm, 9*mm, "CareerReady — Job Seeker Starter Kit")
    canvas.drawRightString(w-18*mm, 9*mm, f"{doc.page}")
    canvas.restoreState()

def cover(canvas, doc):
    canvas.saveState()
    w, h = A4
    canvas.setFillColor(PURPLE)
    canvas.rect(0, 0, w, h, fill=1, stroke=0)
    canvas.setFillColor(INDIGO)
    canvas.circle(w*0.82, h*0.82, 95*mm, fill=1, stroke=0)
    canvas.setFillColor(colors.HexColor("#6D28D9"))
    canvas.circle(w*0.12, h*0.18, 55*mm, fill=1, stroke=0)
    # Simple document/checkmark icon
    x, y = w/2, h*0.63
    canvas.setFillColor(WHITE)
    canvas.roundRect(x-25*mm, y-32*mm, 50*mm, 64*mm, 4*mm, fill=1, stroke=0)
    canvas.setFillColor(PURPLE)
    canvas.setFont("Helvetica-Bold", 22)
    canvas.drawCentredString(x, y+14*mm, "CV")
    canvas.setStrokeColor(INDIGO)
    canvas.setLineWidth(4)
    canvas.line(x-13*mm, y-4*mm, x-3*mm, y-14*mm)
    canvas.line(x-3*mm, y-14*mm, x+17*mm, y+7*mm)
    canvas.setFont("Helvetica-Bold", 30)
    canvas.setFillColor(WHITE)
    canvas.drawCentredString(x, h*0.43, "CAREERREADY")
    canvas.setFont("Helvetica", 13)
    canvas.drawCentredString(x, h*0.385, "JOB SEEKER STARTER KIT")
    canvas.setFont("Helvetica", 10)
    canvas.drawCentredString(x, h*0.33, "CV  •  APPLICATIONS  •  INTERVIEW PREPARATION")
    canvas.setFont("Helvetica", 9)
    canvas.drawCentredString(x, 18*mm, "Build your CV. Apply with confidence. Prepare to succeed.")
    canvas.restoreState()

doc = SimpleDocTemplate(
    out, pagesize=A4, rightMargin=18*mm, leftMargin=18*mm,
    topMargin=18*mm, bottomMargin=20*mm,
    title="CareerReady — Job Seeker Starter Kit",
    author="CareerReady"
)

story = [Spacer(1, 245 * mm), PageBreak()]

# Cover

# Welcome
story += [
    Paragraph("Welcome to CareerReady", styles["H1CR"]),
    Paragraph(
        "Your job search becomes easier when you stop treating it as a series of random applications "
        "and start treating it as a system. This starter kit gives you the tools to build a stronger CV, "
        "tailor applications, prepare for interviews, track your progress, and keep improving.", styles["BodyCR"]),
    Paragraph(
        "CareerReady is built for students, graduates, early-career professionals, and career changers "
        "who want practical resources rather than vague career advice.", styles["BodyCR"]),
    Paragraph("How to use this kit", styles["H2CR"]),
    bullet([
        "Work through the sections in order the first time.",
        "Use the checklists every time you prepare an application.",
        "Customize every template instead of sending generic copies.",
        "Track applications so you know what you have sent and what needs follow-up.",
        "Repeat the process until it becomes a habit."
    ]),
    Spacer(1, 8),
    Paragraph("The CareerReady principle", styles["QuoteCR"]),
    Paragraph(
        "Being qualified matters. Knowing how to present yourself and being ready when opportunity comes matters too.",
        styles["QuoteCR"]),
    PageBreak()
]

# Contents
contents = [
    ("01", "Career Readiness Foundations"),
    ("02", "Build a Professional CV"),
    ("03", "Write Strong Job Applications"),
    ("04", "Tailor Your Application"),
    ("05", "LinkedIn & Professional Presence"),
    ("06", "Interview Preparation"),
    ("07", "Answer Frameworks & Sample Questions"),
    ("08", "Job Application Tracker"),
    ("09", "30-Day Job Search Plan"),
    ("10", "Final Checklists & Action Pages"),
]
story.append(Paragraph("Contents", styles["H1CR"]))
for n, title in contents:
    story.append(Paragraph(f"<b>{n}</b> &nbsp;&nbsp; {title}", styles["TOC"]))
story.append(PageBreak())

# Section 1
story += [
    Paragraph("01 — Career Readiness Foundations", styles["H1CR"]),
    Paragraph("A job search is a process, not a lottery.", styles["QuoteCR"]),
    Paragraph(
        "Your goal is not to apply to everything. Your goal is to identify relevant opportunities, "
        "present evidence that you can contribute, and make it easy for an employer to understand your value.",
        styles["BodyCR"]),
    Paragraph("The 5-part CareerReady system", styles["H2CR"]),
    table([
        ["Stage", "What you do", "Output"],
        ["1. Target", "Choose roles and employers that fit your direction.", "Target role list"],
        ["2. Position", "Translate your education, skills, experience and projects into evidence.", "Professional profile"],
        ["3. Apply", "Tailor your CV and application to each opportunity.", "Submitted application"],
        ["4. Prepare", "Research the employer and practise likely interview questions.", "Interview plan"],
        ["5. Improve", "Track results and learn from responses or rejections.", "Better next application"],
    ], [28*mm, 75*mm, 55*mm]),
    Paragraph("Before you apply: your career inventory", styles["H2CR"]),
    Paragraph("Write down evidence for each category:", styles["BodyCR"]),
    bullet([
        "<b>Education:</b> degrees, diplomas, certifications, relevant coursework.",
        "<b>Skills:</b> technical, communication, leadership, analytical, organizational and creative skills.",
        "<b>Experience:</b> internships, volunteering, school responsibilities, freelance work, projects and part-time roles.",
        "<b>Achievements:</b> awards, measurable results, competitions, leadership wins and improvements you contributed to.",
        "<b>Projects:</b> personal, academic or portfolio projects that demonstrate ability."
    ]),
    Paragraph("Your value statement", styles["H2CR"]),
    Paragraph(
        "Complete this sentence: “I am a [student/graduate/professional] with strengths in [2–3 relevant strengths]. "
        "I have demonstrated these strengths through [experience/project/achievement], and I am interested in "
        "[target role/field] because [specific reason].”", styles["BodyCR"]),
    PageBreak()
]

# Section 2 CV
story += [
    Paragraph("02 — Build a Professional CV", styles["H1CR"]),
    Paragraph(
        "A strong CV is not a biography. It is a focused document that shows why you are relevant to a specific role.",
        styles["BodyCR"]),
    Paragraph("Recommended CV structure", styles["H2CR"]),
    table([
        ["Section", "What to include"],
        ["Header", "Name, phone, professional email, location, LinkedIn/portfolio where relevant."],
        ["Professional Summary", "2–4 lines connecting your strengths to the target role."],
        ["Skills", "Relevant technical and transferable skills; prioritize those requested in the job description."],
        ["Experience", "Role, organization, dates and achievement-focused bullet points."],
        ["Education", "Institution, qualification, dates; include relevant coursework only when useful."],
        ["Projects", "Project name, what you built/did, tools used and result."],
        ["Certifications", "Relevant certifications, courses or credentials."],
    ], [40*mm, 118*mm]),
    Paragraph("Turn duties into achievements", styles["H2CR"]),
    Paragraph(
        "Weak CV bullets often describe what the person was supposed to do. Stronger bullets show what the person did and what changed because of it.",
        styles["BodyCR"]),
    table([
        ["Instead of", "Try"],
        ["“Responsible for social media.”", "“Created and scheduled weekly social content, improving consistency across the brand's channels.”"],
        ["“Worked with customers.”", "“Handled customer enquiries and resolved routine issues while maintaining clear, professional communication.”"],
        ["“Built a website.”", "“Built a responsive portfolio website using HTML, CSS and JavaScript and deployed it for public access.”"],
    ], [72*mm, 86*mm]),
    Paragraph("The achievement formula", styles["H2CR"]),
    Paragraph("<b>Action + Task + Method/Skill + Result</b>", styles["QuoteCR"]),
    Paragraph(
        "Example: “Automated weekly spreadsheet cleanup using Python, reducing repetitive manual work and making the reporting process faster.”",
        styles["BodyCR"]),
    Paragraph("CV checklist", styles["H2CR"]),
    bullet([
        "Is the CV tailored to the role?",
        "Is the most relevant information easy to find?",
        "Are bullet points concise and specific?",
        "Did you quantify results where possible?",
        "Is the email address professional?",
        "Are spelling, dates, formatting and punctuation consistent?",
        "Is the file name professional, e.g. Firstname_Lastname_CV.pdf?",
        "Have you removed unnecessary personal details and irrelevant information?"
    ]),
    PageBreak()
]

# CV template page
story += [
    Paragraph("03 — CV Blueprint", styles["H1CR"]),
    Paragraph("Use this blueprint to draft your CV before formatting it.", styles["BodyCR"]),
    table([
        ["YOUR NAME", "Phone | Email | City | LinkedIn/Portfolio"],
        ["PROFESSIONAL SUMMARY", "2–4 lines: who you are + strongest relevant skills + target direction."],
        ["CORE SKILLS", "Skill 1 • Skill 2 • Skill 3 • Skill 4 • Skill 5 • Skill 6"],
        ["EXPERIENCE", "Role — Organization — Dates\n• Achievement/action bullet\n• Achievement/action bullet\n• Achievement/action bullet"],
        ["EDUCATION", "Qualification — Institution — Dates\nRelevant achievement/coursework if useful."],
        ["PROJECTS", "Project — Tools/skills — Result\nWhat you built, solved, improved or learned."],
        ["CERTIFICATIONS", "Certification — Provider — Year"],
    ], [47*mm, 111*mm]),
    Paragraph("Important", styles["H2CR"]),
    Paragraph(
        "Do not copy a template word-for-word. Replace every placeholder with truthful information from your own experience. "
        "If you do not have formal work experience, use projects, volunteering, school leadership, community work, internships and other genuine evidence.",
        styles["BodyCR"]),
    PageBreak()
]

# Applications
story += [
    Paragraph("04 — Write Strong Job Applications", styles["H1CR"]),
    Paragraph(
        "Your application should answer three questions quickly: Why this role? Why you? Why this organization?",
        styles["BodyCR"]),
    Paragraph("Simple application structure", styles["H2CR"]),
    table([
        ["Part", "Purpose"],
        ["Opening", "Name the role and establish genuine interest."],
        ["Fit", "Show 2–3 relevant strengths backed by evidence."],
        ["Employer connection", "Explain why the organization/role interests you specifically."],
        ["Close", "Invite the next step and thank the reader."],
    ], [40*mm, 118*mm]),
    Paragraph("Cover-letter template", styles["H2CR"]),
    Paragraph(
        "<b>Dear Hiring Manager,</b><br/><br/>"
        "I am writing to apply for the <b>[Role]</b> position at <b>[Organization]</b>. "
        "I am particularly interested in this opportunity because <b>[specific reason connected to the role/company]</b>.<br/><br/>"
        "My background in <b>[field/education]</b> has helped me develop strengths in <b>[skill 1]</b>, <b>[skill 2]</b>, "
        "and <b>[skill 3]</b>. For example, <b>[brief evidence or achievement]</b>. "
        "This experience has prepared me to contribute to <b>[relevant responsibility]</b>.<br/><br/>"
        "I would welcome the opportunity to discuss how my skills and motivation could contribute to your team. "
        "Thank you for considering my application.<br/><br/>"
        "Kind regards,<br/><b>[Your Name]</b>", styles["BoxCR"]),
    Paragraph("Application message template", styles["H2CR"]),
    Paragraph(
        "Hello [Name/Recruiter], I’m [Name], a [student/graduate/professional] with experience in [relevant area]. "
        "I’m interested in the [Role] opportunity because [specific reason]. I’ve attached my CV and would appreciate "
        "the opportunity to be considered. Thank you for your time.", styles["BoxCR"]),
    PageBreak()
]

# Tailoring
story += [
    Paragraph("05 — Tailor Your Application", styles["H1CR"]),
    Paragraph(
        "One of the simplest ways to improve an application is to stop treating every job description the same.",
        styles["BodyCR"]),
    Paragraph("The 10-minute tailoring method", styles["H2CR"]),
    table([
        ["Minute", "Action"],
        ["1–2", "Read the job title, responsibilities and required qualifications."],
        ["3–4", "Highlight repeated keywords and skills."],
        ["5–6", "Match each important requirement with evidence from your background."],
        ["7–8", "Reorder your CV so the strongest relevant evidence appears early."],
        ["9", "Adjust your summary and application message."],
        ["10", "Proofread and confirm every claim is truthful."],
    ], [28*mm, 130*mm]),
    Paragraph("Requirement-to-evidence worksheet", styles["H2CR"]),
    table([
        ["Job requirement", "My evidence", "Where I will show it"],
        ["Example: Python", "Built a data-cleaning script.", "Skills + Projects"],
        ["", "", ""],
        ["", "", ""],
        ["", "", ""],
        ["", "", ""],
    ], [58*mm, 65*mm, 35*mm]),
    Paragraph("Never keyword-stuff", styles["H2CR"]),
    Paragraph(
        "Use relevant keywords naturally and only when they accurately describe your skills. The objective is not to trick a screening system; "
        "it is to make your genuine qualifications easier to recognize.", styles["BodyCR"]),
    PageBreak()
]

# LinkedIn
story += [
    Paragraph("06 — LinkedIn & Professional Presence", styles["H1CR"]),
    Paragraph(
        "Your online presence should tell the same professional story as your CV. Keep the message consistent: who you are, what you can do, and what direction you are pursuing.",
        styles["BodyCR"]),
    Paragraph("Profile checklist", styles["H2CR"]),
    bullet([
        "Use a clear, professional profile photo.",
        "Write a headline that communicates your role, skills or direction—not only “student” or “job seeker.”",
        "Use the About section to explain your strengths, experience, interests and goals.",
        "Add projects, certifications, education and relevant experience.",
        "Use keywords naturally in your headline, About section and experience.",
        "Keep dates and job titles consistent with your CV.",
        "Add a portfolio or project link where relevant.",
        "Engage professionally: comment thoughtfully, share useful work and celebrate others."
    ]),
    Paragraph("Headline formula", styles["H2CR"]),
    Paragraph("<b>[Role/Direction] | [2–3 relevant skills] | [Value/Area of interest]</b>", styles["QuoteCR"]),
    Paragraph(
        "Example: “Aspiring Software Engineer | Python • Web Development | Building practical digital solutions”",
        styles["BodyCR"]),
    Paragraph("About-section starter", styles["H2CR"]),
    Paragraph(
        "“I’m a [student/graduate/professional] interested in [field]. I’m developing strengths in [skills] through [projects/coursework/experience]. "
        "I enjoy [relevant interest] and I’m currently looking for opportunities where I can [contribution/learning goal].”", styles["BoxCR"]),
    PageBreak()
]

# Interview
story += [
    Paragraph("07 — Interview Preparation", styles["H1CR"]),
    Paragraph(
        "Interview preparation is not memorizing perfect sentences. It is preparing enough evidence and structure that you can answer clearly under pressure.",
        styles["BodyCR"]),
    Paragraph("The 4 things to research", styles["H2CR"]),
    bullet([
        "<b>The organization:</b> mission, products/services, customers and recent developments.",
        "<b>The role:</b> responsibilities, skills and expected outcomes.",
        "<b>The industry:</b> major trends, challenges and competitors.",
        "<b>Your fit:</b> 3–5 examples showing why your background matches the role."
    ]),
    Paragraph("The STAR framework", styles["H2CR"]),
    table([
        ["S — Situation", "Set the context briefly."],
        ["T — Task", "Explain what needed to be done."],
        ["A — Action", "Focus on what YOU did."],
        ["R — Result", "Explain what happened; quantify when possible."],
    ], [42*mm, 116*mm]),
    Paragraph("Before the interview", styles["H2CR"]),
    bullet([
        "Review the job description.",
        "Prepare a 60-second introduction.",
        "Prepare 5–7 STAR stories from your experience.",
        "Research the organization.",
        "Prepare 3 thoughtful questions.",
        "Test your internet, microphone and camera for virtual interviews.",
        "Choose appropriate clothing and a distraction-free environment.",
        "Have your CV and notes available."
    ]),
    PageBreak()
]

# Questions
story += [
    Paragraph("08 — Common Interview Questions & Answer Frameworks", styles["H1CR"]),
    Paragraph("1. Tell me about yourself.", styles["H2CR"]),
    Paragraph(
        "<b>Framework:</b> Present → Evidence → Direction. Start with what you are doing now, mention 1–2 relevant experiences or strengths, "
        "then explain why you are interested in this opportunity.", styles["BodyCR"]),
    Paragraph("2. Why do you want this role?", styles["H2CR"]),
    Paragraph(
        "Connect the role to your skills, interests and a specific part of the organization or responsibilities. Avoid making the entire answer about salary or convenience.",
        styles["BodyCR"]),
    Paragraph("3. What is your greatest strength?", styles["H2CR"]),
    Paragraph(
        "Name one strength, then prove it with a short example. “One of my strengths is [skill]. I demonstrated this when [situation/action/result].”",
        styles["BodyCR"]),
    Paragraph("4. Tell me about a challenge you faced.", styles["H2CR"]),
    Paragraph("Use STAR. Choose an example that shows judgment, resilience, learning, teamwork or problem-solving.", styles["BodyCR"]),
    Paragraph("5. Why should we hire you?", styles["H2CR"]),
    Paragraph(
        "Bring together the role's needs and your evidence: “From what I understand, this role needs [need]. My experience with [evidence] "
        "has helped me develop [relevant capability], and I’m confident I can contribute by [specific contribution].”", styles["BodyCR"]),
    Paragraph("6. What is a weakness you are working on?", styles["H2CR"]),
    Paragraph(
        "Choose a genuine but manageable weakness. Explain the action you are taking and what has improved. Avoid disguised strengths such as “I work too hard.”",
        styles["BodyCR"]),
    Paragraph("7. Do you have any questions for us?", styles["H2CR"]),
    Paragraph(
        "Good questions explore expectations, success, team culture, learning and the role's priorities. Examples: “What would success look like in the first 90 days?” "
        "“What are the biggest priorities for this role right now?”", styles["BodyCR"]),
    PageBreak()
]

# Practice page
story += [
    Paragraph("09 — Interview Practice Sheet", styles["H1CR"]),
    Paragraph("Prepare your own evidence before interview day.", styles["BodyCR"]),
    table([
        ["Question", "My key points / evidence"],
        ["Tell me about yourself.", ""],
        ["Why this role?", ""],
        ["Why this organization?", ""],
        ["Greatest strength?", ""],
        ["A challenge you solved?", ""],
        ["A teamwork example?", ""],
        ["A failure or mistake and what you learned?", ""],
        ["Why should we hire you?", ""],
        ["Questions I will ask them", ""],
    ], [70*mm, 88*mm]),
    Paragraph("My 60-second introduction", styles["H2CR"]),
    table([["Draft:", "\n\n\n\n"]], [158*mm]),
    PageBreak()
]

# Tracker
story += [
    Paragraph("10 — Job Application Tracker", styles["H1CR"]),
    Paragraph(
        "A tracker prevents missed follow-ups, repeated applications and uncertainty about where each opportunity stands.",
        styles["BodyCR"]),
    table([
        ["Date", "Company", "Role", "Status", "Next action"],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
        ["", "", "", "", ""],
    ], [20*mm, 34*mm, 35*mm, 30*mm, 39*mm]),
    Paragraph("Suggested status labels", styles["H2CR"]),
    Paragraph("Saved → Preparing → Applied → Screening → Interview → Offer → Rejected → Follow-up", styles["QuoteCR"]),
    Paragraph("Follow-up rule", styles["H2CR"]),
    Paragraph(
        "If an employer provides a specific follow-up timeline, respect it. If they do not, use a reasonable professional follow-up rather than sending repeated messages.",
        styles["BodyCR"]),
    PageBreak()
]

# Strategy
story += [
    Paragraph("11 — Job Search Strategy", styles["H1CR"]),
    Paragraph("Quality + consistency beats random volume.", styles["H1CR"]),
    Paragraph(
        "Set a weekly target that you can sustain. For example, identify 10 relevant opportunities, submit 5 carefully tailored applications, "
        "make 5 meaningful professional connections, and spend time improving one skill or portfolio project.", styles["BodyCR"]),
    Paragraph("Weekly scorecard", styles["H2CR"]),
    table([
        ["Activity", "Target", "Actual"],
        ["Relevant opportunities found", "10", ""],
        ["Tailored applications", "5", ""],
        ["Professional connections", "5", ""],
        ["Follow-ups", "3", ""],
        ["Portfolio/CV improvements", "1", ""],
        ["Interview practice sessions", "2", ""],
    ], [72*mm, 35*mm, 51*mm]),
    Paragraph("Where to look", styles["H2CR"]),
    bullet([
        "Company career pages",
        "Professional networks such as LinkedIn",
        "Job boards relevant to your country or industry",
        "University or training-facility career resources",
        "Professional communities and associations",
        "Referrals and genuine networking relationships"
    ]),
    Paragraph("Avoid these traps", styles["H2CR"]),
    bullet([
        "Applying to every job without checking fit.",
        "Sending the same CV to every employer.",
        "Paying suspicious “recruiters” for a job offer.",
        "Lying about qualifications or experience.",
        "Ignoring your portfolio or professional presence.",
        "Giving up after a small number of rejections."
    ]),
    PageBreak()
]

# 30 day plan
story += [
    Paragraph("12 — Your 30-Day Job Search Action Plan", styles["H1CR"]),
    table([
        ["Days", "Focus", "Actions"],
        ["1–3", "Foundation", "Choose target roles; inventory skills; define your value statement."],
        ["4–7", "CV", "Draft, edit and proofread your CV; create a master version."],
        ["8–10", "Profile", "Improve LinkedIn and portfolio; align your professional story."],
        ["11–15", "Applications", "Find relevant roles and tailor your first applications."],
        ["16–20", "Networking", "Reach out professionally; join relevant communities; learn from practitioners."],
        ["21–24", "Interview", "Prepare STAR stories and practise common questions."],
        ["25–27", "Improve", "Review applications; identify weak points; improve CV or portfolio."],
        ["28–30", "System", "Review tracker, follow up where appropriate and plan the next 30 days."],
    ], [25*mm, 35*mm, 98*mm]),
    Paragraph("Daily 30-minute minimum", styles["H2CR"]),
    bullet([
        "10 minutes: find or research one relevant opportunity.",
        "10 minutes: improve an application, CV, profile or portfolio.",
        "10 minutes: practise a skill, interview answer or professional networking action."
    ]),
    Paragraph("Consistency checklist", styles["H2CR"]),
    bullet([
        "I know the roles I am targeting.",
        "My CV reflects those roles.",
        "My online profile tells the same story.",
        "I track every application.",
        "I practise before interviews.",
        "I review results and adjust my approach."
    ]),
    PageBreak()
]

# Final checklist + worksheets
story += [
    Paragraph("13 — Final CareerReady Checklists", styles["H1CR"]),
    Paragraph("Application-ready checklist", styles["H2CR"]),
    bullet([
        "I meet the essential requirements or can honestly explain relevant transferable skills.",
        "My CV is tailored.",
        "My summary reflects the role.",
        "My strongest evidence is easy to find.",
        "My application message is specific.",
        "All information is truthful.",
        "The files are named professionally.",
        "I saved a copy of what I submitted."
    ]),
    Paragraph("Interview-ready checklist", styles["H2CR"]),
    bullet([
        "I can explain my background in 60 seconds.",
        "I have prepared STAR examples.",
        "I researched the organization.",
        "I understand the role.",
        "I have questions prepared.",
        "I know the interview format and logistics.",
        "I have practised aloud."
    ]),
    Paragraph("My next three actions", styles["H2CR"]),
    table([
        ["Priority", "Action", "Deadline", "Done"],
        ["1", "", "", "□"],
        ["2", "", "", "□"],
        ["3", "", "", "□"],
    ], [18*mm, 90*mm, 35*mm, 15*mm]),
    Paragraph("CareerReady commitment", styles["H2CR"]),
    Paragraph(
        "I will not wait until I feel completely ready before I take action. I will build evidence, improve continuously, "
        "apply strategically, learn from rejection, and keep moving toward the opportunities I want.",
        styles["QuoteCR"]),
    Spacer(1, 10),
    Paragraph("CAREERREADY", styles["H1CR"]),
    Paragraph("Build your CV. Apply with confidence. Prepare to succeed.", styles["QuoteCR"]),
    Paragraph(
        "This starter kit is an educational resource. Templates should be adapted to the specific role, organization, "
        "industry and circumstances of the user.", styles["SmallCR"])
]

doc.build(story, onFirstPage=cover, onLaterPages=footer)

print(f"Created: {out}")
