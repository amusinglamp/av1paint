# From Documentation

There are several files referenced in the avif documentation, and some are only available via a paywall.

But in several places the avif documentation references the av1 documentation, and places specific constraints on it.
That means we can at pull out by reference something of a bitstream that will give us some pointers.


```
ISOBMFF -(specialise)->  HEIF
av1     -(specialise)->  +HEIF -> avif
```

avif supports depth maps, alpha channels, layers, sequences, hdr and more. 
We're ignoring all of that right now, just focussing on a single frame of pixels, all the same colour.

AV1 is made of OBUs - but we don't need all the AV1 OBUs for AVIF

```OBUs are made of a 1 or 2 bytes header, identifying in particular the type of OBU, followed by an optional length field and by an optional payload, whose presence and content depend on the OBU type. Depending on its type, an OBU can carry configuration information, metadata, or coded video data```

ISOBMFF is made of boxes. We don't need all the boxes for AVIF, probably.
We need a box called ```av01Image```  hex ```61763031496d616765``` 

it will have a Sequence Header OBU with the features that still_picture and reduced_still_picture_header are set to 1
```
3 ? bit sequence header (value unclear)
2 1 bits for the still_picture and reduced_still_picture_header
5 0 bits for the sequence level index
4 frame width bits minus 1
4 frame height bits minus 1
n max frame width minus 1 + 1
n max frame height minus 1 + 1
1 use_128x128_superblock
1 enable_filter_intra
1 enable_intra_edge_filter
1 enable_superres
1 enable_cdef
1 enable_restoration
n color_config:
  1 high_bitdepth
  1 monochrome (1 if true)
  1 color_description_present_flag
  8 color_primaries
  8 transfer_characteristics
  8 matrix_coefficients
1 film_grain_params_present
```

an AV1 Image Item shall obey the following constraints:
* The AV1 Image Item shall be associated with an AV1 Item Configuration Property.

_I think calling it an item means it is listed in the iloc_

The content of an AV1 Image Item is called the AV1 Image Item Data and shall obey the following constraints:
* The AV1 Image Item Data shall be identical to the content of an AV1 Sample marked as sync, as defined in [AV1-ISOBMFF]. Since such [AV1 Samples] may be composed of multiple frames, e.g. each corresponding to a different spatial layer, [AV1 Image Items] may represent multi-layered images.

**Sync Items**:

```From any sync sample, an AV1 bitstream is formed by first outputting the OBUs contained in the AV1CodecConfigurationBox and then by outputing all OBUs in the samples themselves, in order, starting from the sync sample.```
* The first frame is a Key Frame that has show_frame set to 1
* It has a sequence Header OBU before the first Frame Header OBU


* The AV1 Image Item Data shall have exactly one Sequence Header OBU.
* The AV1 Image Item Data should have its still_picture flag set to 1.
* The AV1 Image Item Data should have its reduced_still_picture_header flag set to 1.

###OBU Header:

* Forbidden bit 1
* Type: [Sequence Header: 1 ¦ Frame Header: 3 ¦ Frame: 6 ¦ Padding  15]
* 3 bits for Extension:[0], size_field:[?], reserved: [0].

####in hex digits:

Sequence header: 0¦0001¦000 = ```08``` or ```10``` with a size field

Frame header: 0¦0011¦000 = ```18``` or ```1a``` with a size field

## YCbCr / YUV

The default colour format for av1 is ITU-R BT.709 - we'll want to target that to get the smallest files.
If we convert from an 8bit per pixel RBG format, then some different RGB values will map to the same YCbCr values


Kry = 0.2126
Kby - 0.0722

Kru = -Kry
Kgu = - Kgy
Kbu = 1-Kby
Krv = 1-Kry
Kgv = -Kgy
Kbv = -Kby

Y = Kry*R + Kgy * G + Kby * B
Cb = Kru*R + Kgu* G + Kbu * B
Cr = Krv*R + Kgv* G + Kbv * B

