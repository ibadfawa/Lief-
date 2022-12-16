
import lief

def test_simple(self):
        sample_path = get_sample('libjiagu_a64.so')
        output      = os.path.join(self.tmp_dir, "ls.section")

        ls = lief.parse(sample_path)
        for i in range(10):
            section = Section(".test.{:d}".format(i), lief.ELF.SECTION_TYPES.PROGBITS)
            section += lief.ELF.SECTION_FLAGS.EXECINSTR
            section += lief.ELF.SECTION_FLAGS.WRITE
            section.content   = STUB.segments[0].content # First LOAD segment which holds payload
            if i % 2 == 0:
                section = ls.add(section, loaded=True)
                ls.header.entrypoint = section.virtual_address + STUB.header.entrypoint
            else:
                section = ls.add(section, loaded=False)

        ls.write(output)

        st = os.stat(output)
        os.chmod(output, st.st_mode | stat.S_IEXEC)

        p = Popen(output, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout, _ = p.communicate()
