from pdf2image import convert_from_path

old_pdf = convert_from_path("Question Bank for DCN.pdf",
                            poppler_path=r"C:\Users\91960\PycharmProjects\PythonProject7\poppler-24.08.0\Library\bin")


for i in range(len(old_pdf)):
    old_pdf[i].save("new"+str(i)+".jpg","JPEG")