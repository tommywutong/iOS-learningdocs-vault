---
title: QuickTime File Format Specification
apple_id: TP40000939
resource_type: Guide
platform: macOS
topic: Data Management
technology: QuickTime
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/QTFF/QTFFAppenA/QTFFAppenA.html
archived_at: '2026-07-27T06:57:06.709793Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [QuickTime File Format Specification](Introduction%20to%20QuickTime%20File%20Format%20Specification.md)


[Next](Defining%20Media%20Data%20Layouts.md)[Previous](Some%20Useful%20Examples%20and%20Scenarios.md)

# QuickTime Image File Format

__Note:__ The QuickTime Image File Format is deprecated in the QuickTime file format. The information that follows is intended to document existing content containing QuickTime image file media and should not be used for new development.

This appendix describes QuickTime image files, which provide a useful container for QuickTime-compressed still images.

Most still image file formats define both how images should be stored and compressed. However, the QuickTime image file format is a container format, which describes a storage mechanism independent of compression. The QuickTime image file format uses the same atom-based structure as a QuickTime movie.

## Atom Types in QuickTime Image Files

There are two mandatory atom types: `'idsc'`, which contains an image description, and `'idat'`, which contains the image data. This is illustrated in [Figure A-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqhawtsmzvgy). A QuickTime image file can also contain other atoms.

In QuickTime 4, there is a new optional atom type `'iicc'`, which can store a ColorSync profile.

[Figure A-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqhawtsmzvgy) and [Table A-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqhawtsnztha) show an example QuickTime image file containing a JPEG-compressed image.

__Figure A-1__  An `'idsc'` atom followed by an `'idat'` atom

（原归档配图未能恢复：`gi_l_03.gif`）

__Table A-1__  A QuickTime image file containing JPEG-compressed data

| 0000005E | Atom size, 94 bytes |
| 69647363 | Atom type, `'idsc'` |
| 00000056 | Image description size, 86 bytes |
| 6A706567 | Compressor identifier, `'jpeg'` |
| 00000000 | Reserved, set to 0 |
| 0000 | Reserved, set to 0 |
| 0000 | Reserved, set to 0 |
| 00000000 | Major and minor version of this data, 0 if not applicable |
| 6170706C | Vendor who compressed this data, `'appl'` |
| 00000000 | Temporal quality, 0 (no temporal compression) |
| 00000200 | Spatial quality, `codecNormalQuality` |
| 0140 | Image width, 320 |
| 00F0 | Image height, 240 |
| 00480000 | Horizontal resolution, 72 dpi |
| 00480000 | Vertical resolution, 72 dpi |
| 00003C57 | Data size, 15447 bytes (use 0 if unknown) |
| 0001 | Frame count, 1 |
| 0C 50 68 6F 74 6F 20 2D20  4A 50 45 47 00 00 00  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00 | Compressor name, "Photo - JPEG" (32-byte Pascal string) |
| 0018 | Image bit depth, 24 |
| FFFF | Color lookup table ID, -1 (none) |
| 00003C5F | Atom size, 15455 bytes |
| 69646174 | Atom type, `'idat'` |
| FF D8 FF E0 00 10 4A 46  49 46 00 01 01 01 00 48  ... | JPEG compressed data |

__Important:__
The exact order and size of atoms is not guaranteed to match the example in [Figure A-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqhawtsmzvgy). Applications reading QuickTime image files should always use the atom size to traverse the file and ignore atoms of unrecognized types.

__Note:__ Like QuickTime movie files, QuickTime image files are big-endian. However, image data is typically stored in the same byte order as specified by the particular compression format.

## Recommended File Type and Suffix

On Mac OS systems, QuickTime image files are identified by the file type `'qtif'`. Apple recommends using the filename extension `.QIF` to identify QuickTime image files.

[Next](Defining%20Media%20Data%20Layouts.md)[Previous](Some%20Useful%20Examples%20and%20Scenarios.md)
