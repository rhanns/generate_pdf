from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():

    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=25)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=25, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 30, 200, 30)

    pdf.ln(250)

    #set the footer
    pdf.set_font(family="Times", style="I", size=12)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)



    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # set the footer
        pdf.ln(270)
        pdf.set_font(family="Times", style="I", size=12)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R", ln=1)
pdf.output("output.pdf")
