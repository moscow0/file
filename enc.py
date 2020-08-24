import PyPDF2 as p_
import sys
import string
import random

output = p_.PdfFileWriter()


def generate_pass():
    """
    generate random pass
    :return:
    """
    length = random.randint(5, 20)
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def main(doc):
    docx = str(doc).split(".")

    if docx[1] != "pdf":
        print("ONLY pdf docs !!")
        exit(0)

    # read from Input
    input_stream = p_.PdfFileReader(open(doc, "rb"))

    for i in range(0, input_stream.getNumPages()):
        output.addPage(input_stream.getPage(i))

    # write to output
    outputstream = open("{0}.encrypted.pdf".format(docx[0]), "wb")

    # generate pass

    passw = generate_pass()

    # encrypt
    output.encrypt(passw, use_128bit=True)
    output.write(outputstream)

    # close stream
    outputstream.close()

    print("Document {0} encrypted with password {1} to {2}.encrypted.pdf".format(doc, passw, docx[0]))


# driver code
if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            # pdf file to encrypt
            file = sys.argv[1]
            main(file)
        except Exception as e_:
            print(str(e_))
    else:
        print("Doc to encrypt !!")
