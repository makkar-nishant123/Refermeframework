from Util import Configparser
class write_results(object):

    RESULT_FILE=Configparser.parser("General","result_file")
    @classmethod
    def write_data(self,result_data):
        with open(self.RESULT_FILE,"a") as result_file:
            for data in result_data.split("|"):
                result_file.write(data+"\n")
