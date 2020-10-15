from os import path
from os.path import isfile
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import pickle
import os.path

inp_course = open(os.getcwd()+'\\timetables\\'+'saturday'+'.pkl',"rb")
courses = pickle.load(inp_course)
inp_course.close()

print(courses)