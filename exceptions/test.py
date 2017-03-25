#exception test
try:
    fh=open("test.txt","w")
    fh.write("this is test text")
except:
    print("write error")
else:
    print("wrote successfully")
