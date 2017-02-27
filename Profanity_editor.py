
import urllib

def read_txt():
    text = open("/Users/TigranTT/Desktop/UDACITY/ipnd-starter-code-master/stage_3/lesson_3.3_classes/c_profanity_editor/movie_quotes.txt")
    content = text.read()
    text.close()
    #print content
    check_profanity(content)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    #print output
    connection.close()
    if "true" in output:
        print "Profanity Alert!!!"
    elif "false" in output:
        print "This document has no curse words!"
    else:
        print "Could not scan the document properly."

read_txt()
