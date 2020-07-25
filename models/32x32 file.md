# Current model of a 32 x 32 avif

Taking a solid color image as the current model, what do I currently understand the structure of the avif to be?

| Bytes | Purpose | Code |
| --- | --- | --- |
| 0 - 125  | unclear   | 0000001c667479706d696631000000006d696631617669666d696166000000f26d657461000000000000002b68646c72000000000000000070696374000000000000000000000000676f2d61766966207630000000000e7069746d0000000000010000001e696c6f63000000000440000100010000000001160001000000
| _101-104_| iloc box preamble |
| 123 | uint32 possibly item 1 length field for iloc box |
| 127-194 | unclear     | 0000002869696e660000000000010000001a696e6665020000000001000061763031496d616765000000006769707270000000486970636f0000001469737065000000000000
| _157-165_| av01Image (ISOBMFF box) | 61763031496d616765
| _187-194_ | ispe (HEIF dimensions) preamble | 697370650000000000
| 195-198 | canvas width | uint32
| 199-202 | canvas height | uint32
| 203-272 | unclear     | 000000107061737000000001000000010000000c6176314381000c00000000107069786900000000030808080000001769706d61000000000000000100010401028384000000
| 273     | unclear but variable |
| 274-277 | media data box header     | 6d646174
| 278-280 | unclear     | 12000a
| 281-282 | size class  | 0x0518 - 1x1 to 8x8 ¦ 0x0618 - 9x9 to 64x64 ¦ 0x0718 - 512x512 ¦ 0x081c - 4192x4192 |
| 283-288 | varies somehow with size | 0cffdb008032 |
| 289     | count of bytes to EOF | |
| 290-299    | unclear, same for all solid colour | 0x0cffdb008032 |
| 300 - EOF | colour and other variable information | | 

the 'size class' field I've identified here, looks like it might be the 'frame_with_bits_minus_1' +1 value from the sequence header OBU syntax definition.
To get sensible values out, I'd need to split into 2 hex digits.
worth looking at the binary here, and comparing with the size information from the isobmff box that matches it


