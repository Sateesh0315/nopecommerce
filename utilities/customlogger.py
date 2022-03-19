import os
import configparser
import xlwt
import subprocess

ini_file = os.path.abspath(os.path.dirname(".\\..\configurations\."))
config = configparser.RawConfigParser()
config.read(ini_file + "\\config.ini")
updated_repo_path = config.get('common info', 'updated_repo_path')
test_results = xlwt.Workbook()


class TestExecutionAutomation:
    @staticmethod
    def setup():
        print("******************** TEST EXECUTION STARTED ********************")

    @staticmethod
    def teardown(self):
        print("******************** TEST EXECUTION COMPLETED ********************")

    @staticmethod
    def git_command(git_repo_command):
        os.chdir(updated_repo_path)
        repo_path = os.getcwd()
        print(repo_path)
        os.system(command=git_repo_command)

    @staticmethod
    def files_update():
        os.chdir(updated_repo_path)
        folders = os.listdir()
        for folder in folders:
            if folder == "testCases":
                os.chdir(updated_repo_path + "\\testCases")
                files = os.listdir()
                return files

    @staticmethod
    def test_case_execution(file_name):
        os.system(command=file_name)
        print("The file is not available in this directory")

    @staticmethod
    def load_results(file_name):
        os.chdir(updated_repo_path + "\\testCases")
        print(os.getcwd())
        output = subprocess.check_output(file_name, shell=True)
        file_name = file_name[:-3] + "_result"
        file_name_output = test_results.add_sheet(file_name)
        file_name_output.write(output)
        test_results.save('Test_results.xls')


obj = TestExecutionAutomation()
obj.load_results("addition_of_two_numbers.py")

