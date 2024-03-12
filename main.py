from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=25)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=25, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 30, 200, 30)


pdf.output("output.pdf")
