from scripts.main import mainrunner
import traceback


if __name__ == "__main__":
    with open('log.txt','w') as log:
        try:
            mainrunner()
        except:
            traceback.print_exc(file=log)
            print('Errors have been written to a log file')
