##*Arg

def cetak(*mahasiswa):
    print("nama mahasiswa kelas C adalah : " ,mahasiswa)
 
#memanggil fungsi cetak   
cetak("faqih", "ina", "anton")

##*kwarg

def cetak(**mahasiswa):
    print("nama mahasiswa dan NPM kelas C adalah : " ,mahasiswa)
 
#memanggil fungsi cetak   
cetak(nama="andik",tinggal="bogor")
cetak(nama="dika",tinggal="bogor")
cetak(nama="tio",tinggal="bogor")
cetak(nama="acung",tinggal="bogor")

##return

def salam():
    return "hai"

print(salam(),"andik")

##lambda

y=lambda c,d,e,f : c-d/e*f
print(y(4,3,2,1))
