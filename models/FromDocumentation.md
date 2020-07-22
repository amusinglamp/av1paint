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