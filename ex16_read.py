from sys import argv

Script, filename = argv

txt = open(filename)

print(f"here's your file {filename}:")
print(txt.read())
print(txt.close())
