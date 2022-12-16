
import lief

elf: lief.ELF.Binary = lief.parse("libjiagu_a64.so")

# Force relocating the .dynamic/.dynstr
elf.add_library("libibad.so")

# For relocating the interpreter
#elf.interpreter = "/a/very/longlonglong/interpreter-1.2.3.bin"

# Force relocating .dynsym / .gnu.hash table
for i in range(10):
    elf.add_exported_function(0xdeadc0de + i, f"new_export_{i}")

# Add a segment
segment         = lief.ELF.Segment()
segment.type    = lief.ELF.SEGMENT_TYPES.LOAD
segment.content = [0xcc] * 0x23

elf.add(segment)

elf.write("jiagu1.so")
