import re
patern = r"school"
text = 'klasdnalskd school sajdnsld'
match = re.findall(patern, text)
print(match)
