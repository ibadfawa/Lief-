import lief

libnative = lief.parse("libjiagu_a64.so")
libnative.add_library("libibad.so")
libnative.write("libjiagu_a64.so")
