import requests
import subprocess 
import sys
import os
from comment_parser import comment_parser
domain=sys.argv[1]
urllinks=open("urllinks.txt", "a")
textfile=open ("urllinks.txt", "r")
text2=open("js4.txt", "a")
text3=open("js5.txt", "a")
text4=open("js6.txt", "a")
text5=open("final-links.txt", "a")
links=subprocess.run(["curl", "https://web.archive.org/cdx/search/cdx?url=*." + domain + "&output=raw&fl=original&collapse=urlkey"], universal_newlines=True, stdout=subprocess.PIPE)
linkstr = links.stdout
urllinks.write(str(linkstr))
for text in textfile:
	s=text.split("?")
	print (str(s[0]))
	text2.write(str(s[0]) + "\n")
greps=subprocess.run(["grep", "\.js", "js4.txt"], universal_newlines=True, stdout=subprocess.PIPE)
output = greps.stdout
text3.write(str(output))
greps2=subprocess.run(["grep", "-v", "\.json", "js5.txt"], universal_newlines=True, stdout=subprocess.PIPE)
output2 = greps2.stdout
text4.write(str(output2))
greps3=subprocess.run(["sort", "-u", "js6.txt"], universal_newlines=True, stdout=subprocess.PIPE)
output3 = greps3.stdout
text5.write(str(output3))
os.remove("js4.txt")
os.remove("js5.txt")
os.remove("js6.txt")
jsfiles=open("final-links.txt", "r")
comment_file=open("js-comment.txt", "a")
for jsfile in jsfiles:
	try:
		req=requests.get(jsfile, timeout=2)
		print("downloading " + jsfile)
		jscontent=open("jscontent.txt", "a")
		jscontent.write(req.text)
		comment=comment_parser.extract_comments("jscontent.txt", mime="text/x-javascript")
		comment_file.write(jsfile + "-" * len(jsfile) + "\n" + str(comment) + "\n" + "=" * 100 + "\n")
		print (comment)
		os.remove("jscontent.txt")
	except:
		pass
jsfiles.close()
comment_file.close()
