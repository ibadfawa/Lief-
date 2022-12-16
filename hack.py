
import lief

def main():
    logging.basicConfig()
    logger = logging.getLogger(os.path.basename(__file__))

    elffile = lief.parse("libjiagu_a64.so")

    if elffile.format != lief.EXE_FORMATS.ELF:
        raise Exception('"%s" invalid executable format %s, expected %s'
                        % (args.inf, elffile.format, lief.EXE_FORMATS.ELF))
        return

    with open("binary.bin", 'rb') as f:
        bin_img = f.read()

    new_sec = lief.ELF.Section()
    new_sec.name = ".ext_bin"
    new_sec.content = bytearray(bin_img)
    new_sec.size = len(bin_img)
    new_sec.alignment = 4
    new_sec.virtual_address = 100000

    elffile.add(new_sec, True)
    print ('size written : %s' % new_sec.size, 'size expected: %s' % len(bin_img))

    elffile.write("out.elf")

    read_sec = elffile.get_section(".ext_bin")
    print ('size read : %s' % read_sec.size, 'size expected: %s' % new_sec.size)
    read_sec.size = len(bin_img)

    elffile.write("out.elf")
