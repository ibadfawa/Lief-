import lief
def main():
    logging.basicConfig()
    logger = logging.getLogger(os.path.basename(__file__))

    elffile = lief.parse("libjiagu_a64.so")

   
    

    new_sec = lief.ELF.Section()
    new_sec.name = ".ext_bin"
    
    new_sec.alignment = 4
    new_sec.virtual_address = 100000

    elffile.add(new_sec, True)
    print ('size written : %s' % new_sec.size, 'size expected: %s' )

    elffile.write("out.elf")

    
