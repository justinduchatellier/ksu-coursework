import requests
import sys

the_url = str(sys.argv[1])
f_name = str(sys.argv[2])
r = requests.get(the_url)

with open(f_name, 'w', encoding="utf-8") as f:
    f.write("The status of the HTTP request is: " + "\n" + str(r.status_code) + "\n\n")
    f.write("This is what is contained in the body: " + "\n" + str(r.content))
