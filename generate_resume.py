from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

pdf = canvas.Canvas("Abinesh_Resume.pdf", pagesize=A4)
width, height = A4

pdf.setFont("Helvetica-Bold", 16)
pdf.drawCentredString(width/2, height-50, "ABINESH D")

pdf.setFont("Helvetica", 10)
pdf.drawCentredString(width/2, height-70, "Phone: 9597557201 | Email: rankedabinesh@gmail.com | GitHub: github.com/abyrx-dev")

pdf.setFont("Helvetica-Bold", 12)
pdf.drawString(50, height-100, "OBJECTIVE")
pdf.setFont("Helvetica", 10)
pdf.drawString(50, height-115, "Motivated Python Developer seeking entry-level IT role.")

pdf.setFont("Helvetica-Bold", 12)
pdf.drawString(50, height-145, "TECHNICAL SKILLS")
pdf.setFont("Helvetica", 10)
pdf.drawString(50, height-160, "Python | SQL | SQLite | Flask | Git | GitHub | VS Code | OOP | REST API")

pdf.setFont("Helvetica-Bold", 12)
pdf.drawString(50, height-190, "PROJECTS")
pdf.setFont("Helvetica-Bold", 10)
pdf.drawString(50, height-205, "DLF Prep - Python and Backend Learning Project")
pdf.setFont("Helvetica", 10)
pdf.drawString(50, height-220, "- Built REST API using Flask and SQLite")
pdf.drawString(50, height-235, "- Implemented GET and POST endpoints")
pdf.drawString(50, height-250, "- GitHub: github.com/abyrx-dev/dlf-prep")

pdf.setFont("Helvetica-Bold", 12)
pdf.drawString(50, height-280, "EDUCATION")
pdf.setFont("Helvetica", 10)
pdf.drawString(50, height-295, "B.Com Computer Applications | DP Jan Dhuraipakkam | 2023-2026")

pdf.setFont("Helvetica-Bold", 12)
pdf.drawString(50, height-325, "LANGUAGES")
pdf.setFont("Helvetica", 10)
pdf.drawString(50, height-340, "Tamil, English")

pdf.save()
print("Resume PDF created!")
