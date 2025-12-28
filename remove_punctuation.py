punctuation = '''[,[]/?.><\|{!}'''

string = input("Enter something: ")

No_Punct = ""
for chr in string:
    if chr not in punctuation:
        No_Punct += chr

print(No_Punct)