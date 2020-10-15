from prompt_toolkit.completion import WordCompleter
from prompt_toolkit import prompt
bye = WordCompleter(['8:45','945'])
time = prompt('Enter the time',completer=bye)