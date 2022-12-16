import lief

libnative = lief.parse("libjiagu_a64.so") #nama lib yang ingin di inject
libnative.add(lief.ELF.Segment, lief.None)
libnative.write("out.so")
