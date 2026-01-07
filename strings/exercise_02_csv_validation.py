filename = "REPORT.CSV "

#I should verify with endswith if the extension is csv
def is_csv_file(myFile):
    return print(myFile.strip().lower().endswith("csv"))

is_csv_file(filename)