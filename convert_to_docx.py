from pdf2docx import Converter

if __name__=="__main__":
    input_pdf = "Personal Page - Zhang Xu.pdf"
    output_doc = "Resume - Zhang Xu.docx"

    cv = Converter(input_pdf)
    cv.convert(output_doc, start=0, end=None)
    cv.close()
