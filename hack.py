import lief

 elf = lief.parse("libjiagu_a64.so")
  for entry in elf.dynamic_entries:
    if entry.tag == lief.ELF.DYNAMIC_TAGS.INIT:
      entry.value = 0x88888888
 Elf.write("test_modified")
