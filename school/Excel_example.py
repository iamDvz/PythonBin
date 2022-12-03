import csv;

max_gip = 0;
max_summ = 0;
i = 0;
table = open("/Users/iamdvz/Desktop/School/09/9-97.csv");
#print(table.readlines())
for l in table.readlines():
    s = l.split(";");
    s[2] = s[2].replace("\n", "");
    s[0] = s[0].replace("\ufeff", "");
    s[0] = int(s[0]);
    s[1] = int(s[1]);
    s[2] = int(s[2]);
    s = sorted(s);
    print(s);
    if ((int(s[0])**2 + int(s[1])**2) == int(s[2])**2):
        if max_gip < s[2]:
            max_gip = s[2]
        if max_summ < s[1]+ s[0]:
            max_summ = s[0] + s[1]
        i += 1;

print(i);
print(max_gip);
print(max_summ);
    
