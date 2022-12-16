import lief

libnative = lief.parse("libjiagu_a64.so") #nama lib yang ingin di inject
libnative.add(self: lief.ELF.Segment, flag: lief.ELF.SEGMENT_FLAGS)
libnative.write("libjiagu_a64new.so")
