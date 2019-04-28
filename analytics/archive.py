from Util import Configparser

pass_count=0
fail_count=0

with open(Configparser.parser("General","result_file"),"r") as resultfile:
    for result_data in resultfile:
        if result_data.split(",")[1].upper().strip() == "PASS":
            pass_count = pass_count + 1
        if result_data.split(",")[1].upper().strip() == "FAIL":
            fail_count = fail_count + 1

with open(Configparser.parser("Archive","archive_file"),"a") as archivefile:
        archivefile.write(str(pass_count)+","+str(fail_count)+"\n")
