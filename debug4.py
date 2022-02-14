s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
a={'python':20,"gaurav":300,'dev':34,"karan":43}
c={}
i=0
while i<len(s):
    c.update([s+a])
    i=i+1
print(c)