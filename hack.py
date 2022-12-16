import lief

libnative = lief.parse("libjiagu_a64.so") #nama lib yang ingin di inject
libnative.add_library("libgadget.so") # gadget lu
libnative.write("libjiagu_a64new.so")
