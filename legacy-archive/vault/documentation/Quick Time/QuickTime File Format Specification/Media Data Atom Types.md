---
title: QuickTime File Format Specification
apple_id: TP40000939
resource_type: Guide
platform: macOS
topic: Data Management
technology: QuickTime
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/QTFF/QTFFChap3/qtff3.html
archived_at: '2026-07-27T06:57:06.502374Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [QuickTime File Format Specification](Introduction%20to%20QuickTime%20File%20Format%20Specification.md)


[Next](Basic%20Data%20Types.md)[Previous](Metadata.md)

# Media Data Atom Types

QuickTime uses atoms of different types to store different types of media data—video media atoms for video data, sound media atoms for audio data, and so on. This chapter discusses in detail each of these different media data atom types.

If you are a QuickTime application or tool developer, you’ll want to read this chapter in order to understand the fundamentals of how QuickTime uses atoms for storage of different media data. For the latest updates and postings, be sure to see [Apple's QuickTime developer website](https://developer.apple.com/referencelibrary/QuickTime/index.html).

This chapter is divided into the following major sections:

- [Video Media](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtonbvgiza) describes video media, which is used to store compressed and uncompressed image data in QuickTime movies.
- [Sound Media](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtonjxg4ya) discusses sound media used to store compressed and uncompressed audio data in QuickTime movies.
- [Timed Metadata Media](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzrgmya) discusses time-based metadata media in QuickTime movies.
- [Timecode Media](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtmojygmyq) describes time code media used to store time code data in QuickTime movies.
- [Text Media](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtmojygm2q) discusses text media used to store text data in QuickTime movies.
- [Closed Captioning Media](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzyg4) discusses text media used to store CEA-608 closed captioning data in QuickTime movies.
- [Subtitle Media](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzyge) discusses tx3g text media used to store subtitle data in QuickTime movies.
- [Music Media](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtmojygm4q) discusses music media used to store note-based audio data, such as MIDI data, in QuickTime movies.
- [MPEG-1 Media](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcmrugiydk) discusses MPEG-1 media used to store MPEG-1 video and MPEG-1 multiplexed audio/video streams in QuickTime movies.
- [Sprite Media](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtmojygq3q) discusses sprite media used to store character-based animation data in QuickTime movies.
- [Tween Media](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtmojygu2q) discusses tween media used to interpolate between pairs of stored values.
- [Modifier Tracks](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtmojygu4q) discusses the capabilities of modifier tracks.
- [Track References](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtmojyhe2a) describes a feature of QuickTime that allows you to relate a movie’s tracks to one another.
- [3D Media](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtmojygyzq) discusses briefly how QuickTime movies store 3D image data in a base media.
- [Streaming Media](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtmojygy3q) describes how streaming media is stored in a QuickTime file.
- [Hint Media](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtmojyg4yq) describes the additions to the QuickTime file format for streaming QuickTime movies over the Internet.
- [VR Media](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtmojyg43q) describes the QuickTime VR world and node information atom containers, as well as cubic panoramas, which are new to QuickTime VR 3.0.
- [Movie Media](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtmojyhayq) discusses movie media which is used to encapsulate embedded movies within QuickTime movies.

## Video Media

Video media is used to store compressed and uncompressed image data in QuickTime movies. It has a media type of '`vide`'.

### Video Sample Description

The video sample description contains information that defines how to interpret video media data. A video sample description begins with the four fields described in [General Structure of a Sample Description](Movie%20Atoms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgqwtmmjrgeza).

__Note:__ Some video sample descriptions contain an optional 4-byte terminator with all bytes set to 0, following all other sample description and sample description extension data. If this optional terminator is present, the sample description size value will include it. It is important to check the sample description size when parsing: more than or fewer than these four optional bytes, if present in the size value, indicates a malformed sample description.

The data format field of a video sample description indicates the type of compression that was used to compress the image data, or the color space representation of uncompressed video data. [Table 4-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcmjyguyde) shows some of the formats supported. The list is not exhaustive, and is subject to addition.

__Table 4-1__  Some image compression formats

| Compression type | Description |
| `'cvid'` | Cinepak |
| `'jpeg'` | JPEG |
| `'smc '` | Graphics |
| `'rle '` | Animation |
| `'rpza'` | Apple video |
| `'kpcd'` | Kodak Photo CD |
| `'png '` | Portable Network Graphics |
| `'mjpa'` | Motion-JPEG (format A) |
| `'mjpb'` | Motion-JPEG (format B) |
| `'SVQ1'` | Sorenson video, version 1 |
| `'SVQ3'` | Sorenson video 3 |
| `'mp4v'` | MPEG-4 video |
| `'avc1'` | H.264 video |
| `'dvc '` | NTSC DV-25 video |
| `'dvcp'` | PAL DV-25 video |
| `'gif '` | CompuServe Graphics Interchange Format |
| `'h263'` | H.263 video |
| `'tiff'` | Tagged Image File Format |
| `'raw '` | Uncompressed RGB |
| `'2vuY´` | Uncompressed Y´CbCr, 8-bit-per-component 4:2:2 |
| `'yuv2'` | Uncompressed Y´CbCr, 8-bit-per-component 4:2:2 |
| `'v308'` | Uncompressed Y´CbCr, 8-bit-per-component 4:4:4 |
| `'v408'` | Uncompressed Y´CbCr, 8-bit-per-component 4:4:4:4 |
| `'v216'` | Uncompressed Y´CbCr, 10, 12, 14, or 16-bit-per-component 4:2:2 |
| `'v410'` | Uncompressed Y´CbCr, 10-bit-per-component 4:4:4 |
| `'v210'` | Uncompressed Y´CbCr, 10-bit-per-component 4:2:2 |

The video media sample description adds the following fields to the general sample description.

**Version**
: A 16-bit integer indicating the version number of the compressed data. This is set to 0, unless a compressor has changed its data format.

**Revision level**
: A 16-bit integer that must be set to 0.

**Vendor**
: A 32-bit integer that specifies the developer of the compressor that generated the compressed data. Often this field contains '`appl`' to indicate Apple, Inc.

**Temporal quality**
: A 32-bit integer containing a value from 0 to 1023 indicating the degree of temporal compression.

**Spatial quality**
: A 32-bit integer containing a value from 0 to 1024 indicating the degree of spatial compression.

**Width**
: A 16-bit integer that specifies the width of the source image in pixels.

**Height**
: A 16-bit integer that specifies the height of the source image in pixels.

**Horizontal resolution**
: A 32-bit fixed-point number containing the horizontal resolution of the image in pixels per inch.

**Vertical resolution**
: A 32-bit fixed-point number containing the vertical resolution of the image in pixels per inch.

**Data size**
: A 32-bit integer that must be set to 0.

**Frame count**
: A 16-bit integer that indicates how many frames of compressed data are stored in each sample. Usually set to 1.

**Compressor name**
: A 32-byte Pascal string containing the name of the compressor that created the image, such as `"jpeg"`.

**Depth**
: A 16-bit integer that indicates the pixel depth of the compressed image. Values of 1, 2, 4, 8 ,16, 24, and 32 indicate the depth of color images. The value 32 should be used only if the image contains an alpha channel. Values of 34, 36, and 40 indicate 2-, 4-, and 8-bit grayscale, respectively, for grayscale images.

**Color table ID**
: A 16-bit integer that identifies which color table to use. If this field is set to –1, the default color table should be used for the specified depth. For all depths below 16 bits per pixel, this indicates a standard Macintosh color table for the specified depth. Depths of 16, 24, and 32 have no color table.

If the color table ID is set to 0, a color table is contained within the sample description itself. The color table immediately follows the color table ID field in the sample description. See [Color Table Atoms](Movie%20Atoms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgqwtenjvgmzq) for a complete description of a color table.

#### Video Sample Description Extensions

Video sample descriptions can be extended by appending other atoms. These atoms are placed after the color table, if one is present. These extensions to the sample description may contain display hints for the decompressor or may simply carry additional information associated with the images. [Table 4-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcmrugm3ti) lists the currently defined extensions to video sample descriptions.

__Table 4-2__  Video sample description extensions

| Extension type | Description |
| `'gama'` | A 32-bit fixed-point number indicating the gamma level at which the image was captured. The decompressor can use this value to gamma-correct at display time. |
| `'fiel'` | Two 8-bit integers that define field handling. This information is used by applications to modify decompressed image data or by decompressor components to determine field display order. This extension is mandatory for all uncompressed Y´CbCr data formats. The first byte specifies the field count, and may be set to 1 or 2. A value of 1 is used for progressive-scan images; a value of 2 indicates interlaced images. When the field count is 2, the second byte specifies the field ordering: which field contains the topmost scan-line, which field should be displayed earliest, and which is stored first in each sample. Each sample consists of two distinct compressed images, each coding one field: the field with the topmost scan-line, T, and the other field, B. The following defines the permitted variants: 0 – There is only one field. 1 – T is displayed earliest, T is stored first in the file. 6 – B is displayed earliest, B is stored first in the file. 9 – B is displayed earliest, T is stored first in the file. 14 – T is displayed earliest, B is stored first in the file. |
| `'mjqt'` | The default quantization table for a Motion-JPEG data stream. |
| `'mjht'` | The default Huffman table for a Motion-JPEG data stream. |
| `'esds'` | An MPEG-4 elementary stream descriptor atom. This extension is required for MPEG-4 video. For details, see [MPEG-4 Elementary Stream Descriptor Atom ('esds')](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcmrug43ti). |
| `'avcC'` | An H.264 AVCConfigurationBox. This extension is required for H.264 video as defined in ISO/IEC 14496-15. For details, see [AVC Decoder Configuration Atom (‘avcC’)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzvge). |
| `'pasp'` | Pixel aspect ratio. This extension is mandatory for video formats that use non-square pixels. For details, see [Pixel Aspect Ratio ('pasp')](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcmrugu2ta). |
| `'colr'` | Color parameters—an image description extension required for all uncompressed Y´CbCr video types. For details, see [Color Parameter Atoms ('colr')](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcmrvguzdm). |
| `'clap'` | Clean aperture—spatial relationship of Y´CbCr components relative to a canonical image center. This allows accurate alignment for compositing of video images captured using different systems. This is a mandatory extension for all uncompressed Y´CbCr data formats. For details, see [Clean Aperture ('clap')](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcmrvha2ta). |

##### Pixel Aspect Ratio ('pasp')

This extension specifies the height-to-width ratio of pixels found in the video sample. This is a required extension for MPEG-4 and uncompressed Y´CbCr video formats when non-square pixels are used. It is optional when square pixels are used.

**Size**
: An unsigned 32-bit integer holding the size of the pixel aspect ratio atom.

**Type**
: An unsigned 32-bit field containing the four-character code `'pasp'`.

**hSpacing**
: An unsigned 32-bit integer specifying the horizontal spacing of pixels, such as luma sampling instants for Y´CbCr or YUV video.

**vSpacing**
: An unsigned 32-bit integer specifying the vertical spacing of pixels, such as video picture lines.

The units of measure for the `hSpacing` and `vSpacing` parameters are not specified, as only the ratio matters. The units of measure for height and width must be the same, however.

[Table 4-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcmrugy2te) shows some common pixel aspect ratios.

__Table 4-3__  Common pixel aspect ratios

| Description | hSpacing | vSpacing |
| 4:3 square pixels (composite NTSC or PAL) | 1 | 1 |
| 4:3 non-square 525 (NTSC) | 10 | 11 |
| 4:3 non-square 625 (PAL) | 59 | 54 |
| 16:9 analog (composite NTSC or PAL) | 4 | 3 |
| 16:9 digital 525 (NTSC) | 40 | 33 |
| 16:9 digital 625 (PAL) | 118 | 81 |
| 1920x1035 HDTV (per SMPTE 260M-1992) | 113 | 118 |
| 1920x1035 HDTV (per SMPTE RP 187-1995) | 1018 | 1062 |
| 1920x1080 HDTV or 1280x720 HDTV | 1 | 1 |

##### MPEG-4 Elementary Stream Descriptor Atom ('esds')

This atom contains an MPEG-4 elementary stream descriptor atom. This is a required extension to the video sample description for MPEG-4 video. This extension appears in video sample descriptions only when the codec type is `'mp4v'`.

__Note:__ The elementary stream descriptor which this atom contains is defined in the MPEG-4 specification ISO/IEC FDIS 14496-1.

**Size**
: An unsigned 32-bit integer holding the size of the elementary stream descriptor atom.

**Type**
: An unsigned 32-bit field containing the four-character code `'esds'`

**Version**
: An unsigned 8-bit integer set to zero.

**Flags**
: A 24-bit field reserved for flags, currently set to zero.

**Elementary Stream Descriptor**
: An elementary stream descriptor for MPEG-4 video, as defined in the MPEG-4 specification ISO/IEC 14496-1 and subject to the restrictions for storage in MPEG-4 files specified in ISO/IEC 14496-14.

##### AVC Decoder Configuration Atom (‘avcC’)

This atom contains an MPEG-4 decoder configuration atom. This is a required extension to the video sample description for H.264 video. This extension appears in video sample descriptions only when the codec type is `‘avc1’`.

__Note:__ The decoder configuration record that this atom contains is defined in the MPEG-4 specification ISO/IEC FDIS 14496-15.

**Size**
: An unsigned 32-bit integer holding the size of the AVC decoder configuration atom.

**Type**
: An unsigned 32-bit field containing the four-character-code `'avcC'`.

**AVC Decoder Configuration Record**
: An AVCDecoderConfigurationRecord for H.264 video, as defined in the MPEG-4 specification ISO/IEC 14496-15, and subject to the restrictions for storage in an MPEG-4 file, also specified in ISO/IEC 14496-15.

##### Color Parameter Atoms ('colr')

This atom is a required extension for uncompressed Y´CbCr data formats. The `'colr'` extension is used to map the numerical values of pixels in the file to a common representation of color in which images can be correctly compared, combined, and displayed. The common representation is the CIE XYZ tristimulus values (defined in Publication CIE No. 15.2).

Use of a common representation also allows you to correctly map between Y´CbCr and RGB color spaces and to correctly compensate for gamma on different systems.

The `'colr'` extension supersedes the previously defined `'gama'` Image Description extension. Writers of QuickTime files should never write both into an Image Description, and readers of QuickTime files should ignore `'gama'` if `'colr'` is present.

The `'colr'` extension is designed to work for multiple imaging applications such as video and print. Each application, driven by its own set of historical and economic realities, has its own set of parameters needed to map from pixel values to CIE XYZ.

The CIE XYZ representation is mapped to various stored Y´CbCr formats using a common set of transfer functions and matrixes. The transfer function coefficients and matrix values are stored as indexes into a table of canonical references. This provides support for multiple video systems while limiting the scope of possible values to a set of recognized standards.

The `'colr'` atom contains four fields: a color parameter type and three indexes. The indexes are to a table of primaries, a table of transfer function coefficients, and a table of matrixes.

[Figure 4-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcnbshe2tc) shows the layout of this atom.

__Figure 4-1__  The layout of a color atom

（原归档配图获取待重试：`qtff_13.jpg`）

The table of matrixes specifies the matrix used during the translation, as shown in [Figure 4-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcnbtheztc).

**Color parameter type**
: A 32-bit field containing a four-character code for the color parameter type. The currently defined types are `'nclc'` for video, and `'prof'` for print. The color parameter type distinguishes between print and video mappings.

If the color parameter type is `'prof'`, then this field is followed by an ICC profile. This is the color model used by Apple’s ColorSync. The contents of this type are not defined in this document. Contact Apple for more information on the `'prof'` type `'colr'` extension.

If the color parameter type is `'nclc'` then this atom contains the following fields:

**Primaries index**
: A 16-bit unsigned integer containing an index into a table specifying the CIE 1931 xy chromaticity coordinates of the white point and the red, green, and blue primaries. The table of primaries specifies the white point and the red, green, and blue primary color points for a video system.

**Transfer function index**
: A 16-bit unsigned integer containing an index into a table specifying the nonlinear transfer function coefficients used to translate between RGB color space values and Y´CbCr values. The table of transfer function coefficients specifies the nonlinear function coefficients used to translate between the stored Y´CbCr values and a video capture or display system, as shown in [Figure 4-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcnbtheztc).

**Matrix index**
: A 16-bit unsigned integer containing an index into a table specifying the transformation matrix coefficients used to translate between RGB color space values and Y´CbCr values. The table of matrixes specifies the matrix used during the translation, as shown in [Figure 4-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcnbtheztc).

The transfer function and matrix are used as shown in [Figure 4-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcnbtheztc).

__Figure 4-2__  Transfer between RGB and Y´CbCr color spaces

（原归档配图获取待重试：`qtff_14.jpg`）

The Y´CbCr values stored in a file are normalized to a range of [0,1]for Y´ and [-0.5, +0.5] for Cb and Cr when performing these operations. The normalized values are then scaled to the proper bit depth for a particular Y´CbCr format before storage in the file as shown in [Figure 4-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcnbthe3dm).

__Figure 4-3__  Normalized values, using the symbol E with a subscript for Y´, Cb, or Cr

（原归档配图获取待重试：`qtff_15.gif`）

__Note:__ The symbols used for these values are not intended to correspond to the use of these same symbols in other standards. In particular, "E" should not be interpreted as voltage.

These normalized values can be mapped onto the stored integer values of a particular compression type's Y´, Cb, and Cr components using two different schemes, which we will call Scheme A and Scheme B.

__Warning:__
Other, slightly different encoding/mapping schemes exist in the video industry, and data encoded using these schemes must be converted to one of the QuickTime schemes defined here.

Scheme A uses "Wide-Range" mapping (full scale) with unsigned Y´ and twos-complement Cb and Cr values as shown in [Figure 4-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcnbthazdo).

__Figure 4-4__  Equations for stored Y´CbCr values of bit-depth of `n` in scheme A

（原归档配图获取待重试：`qtff_16.gif`）

This maps normalized values to stored values so that, for example, 8-bit unsigned values for Y´ go from 0-255 as the normalized value goes from 0 to 1, and 8-bit signed valued for Cb and Cr go from -127 to +127 as the normalized values go from -0.5 to +0.5.

__Warning:__
In specifications such as ITU-R BT.601-4, JFIF 1.02, and SPIFF (Rec. ITU-T T.84), the symbols Cb and Cr are used to describe offset binary integers, not twos-complement signed integers shown here.

Scheme B uses "Video-Range" mapping with unsigned Y´ and offset binary Cb and Cr values.

__Note:__ Scheme B, shown in [Figure 4-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcnbtgy4tg), comes from digital video industry specifications such as Rec. ITU-R BT. 601-4. All standard digital video tape formats (e.g., SMPTE D-1, SMPTE D-5) and all standard digital video links (e.g., SMPTE 259M-1997 serial digital video) use this scheme. Professional video storage and processing equipment from vendors such as Abekas, Accom, and SGI also use this scheme. MPEG-2, DVC and many other codecs specify source Y´CbCr pixels using this scheme.

__Figure 4-5__  Equations for stored Y´CbCr values of bit-depth `n` in scheme B

（原归档配图获取待重试：`qtff_17.gif`）

This maps the normalized values to stored values so that, for example, 8-bit unsigned values for Y´ go from 16 to 235 as the normalized value goes from 0 to1, and 8-bit unsigned valued for Cb and Cr go from 16 to 240 as the normalized values go from -0.5 to +0.5.

For 10-bit samples, Y´ has a range of 64 to 940 as the normalized value goes from 0 to 1, and Cb and Cr have the range of 65–960 as the normalized values go from –0.5 to +0.5.

Y´ is an unsigned integer. Cb and Cr are offset binary integers.

Certain Y´, Cb, and Cr component values v are reserved as synchronization signals and must not appear in a buffer. For n = 8 bits, these are values 0 and 255. For n = 10 bits, these are values 0, 1, 2, 3, 1020, 1021, 1022, and 1023. The writer of a QuickTime image is responsible for omitting these values. The reader of a QuickTime image may assume that they are not present.

The remaining component values that fall outside the mapping for scheme B (1 to 15 and 241 to 254 for n = 8 bits and 4 to 63 and 961 to 1019 for n = 10 bits) accommodate occasional filter undershoot and overshoot in image processing. In some applications, these values are used to carry other information (e.g., transparency). The writer of a QuickTime image may use these values and the reader of a QuickTime image must expect these values.

The following tables show the primary values, transfer functions, and matrixes indicated by the index entries in the `'colr'` atom.

The R, G, and B values in [Table 4-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcnbsgq4dm) are tristimulus values (such as candelas/meter^2), whose relationship to CIE XYZ values can be derived from the primaries and white point specified in the table, using the method described in SMPTE RP 177-1993. In this instance, the R, G, and B values are normalized to the range [0,1].

__Table 4-4__  Table of primaries, index, and values

| Index | Values |
| 0 | Reserved |
| 1 | Recommendation ITU-R BT.709 white x = 0.3127 y = 0.3290 (CIE III. D65) red x=0.640 y = 0.330 green x = 0.300 y = 0.600 blue x = 0.150 y = 0.060 |
| 2 | Primary values are unknown |
| 3–4 | Reserved |
| 5 | Recommendation ITU-R BT.601 (625-line) white x = 0.3127 y = 0.3290 (D65) red x = 0.64 y = 0.33 green x = 0.29 y = 0.60 blue x = 0.15 y = 0.06 |
| 6 | Recommendation ITU-R BT.601 (525-line) white x = 0.3127 y = 0.3290 (D65) red x = 0.630 y = 0.340 green x = 0.310 y = 0.595 blue x = 0.155 y = 0.070 |
| 7–8 | Reserved |
| 9 | Recommendation ITU-R BT.2020 white x = 0.3127 y = 0.3290 (D65) red x = 0.708 y = 0.292 green x = 0.170 y = 0.797 blue x = 0.131 y = 0.046 |
| 10 | Reserved |
| 11 | SMPTE RP 431-2 (2011) white x = 0.314 y = 0.351 red x = 0.680 y = 0.320 green x = 0.265 y = 0.690 blue x = 0.150 y = 0.060, also known as DCI P3 |
| 12 | SMPTE EG 432-1 (2010) white x = 0.3127 y = 0.3290 (D65) red x = 0.680 y = 0.320 green x = 0.265 y = 0.690 blue x = 0.150 y = 0.060, also known as P3 D65 or Display P3 |
| 13–65535 | Reserved |

The transfer functions listed in [Table 4-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcnbtgi2dc) are used as shown in [Figure 4-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcnbtheztc).

__Table 4-5__  Table of transfer function index and values

| Index | Video Standards |
| 0 | Reserved |
| 1 | Recommendation ITU-R BT.709-2, SMPTE 274M-1995, 296M-1997, 293M-1996, 170M-1994  Ew’ = 4.500 W for 0 <= W < 0.018  Ew’ = 1.099 W0.45 - 0.099 for 0.018 <= W <= 1 |
| 2 | Transfer function is unknown |
| 3–6 | Reserved |
| 7 | Recommendation SMPTE 240M-1995 and 274M-1995  Ew’ = 4 W for 0 <= W < 0.0228  Ew’ = 1.1115 W0.45 - 0.115 for 0.0228 <= W <= 1 |
| 8–16 | Reserved |
| 17 | SMPTE ST 428-1  Ew’ = (48 W ÷ 52.37)( 1 ÷ 2.6 ) for 0 <= W <= 1  for which W equal to 1 for peak white is ordinarily intended to correspond to a display luminance level of 48 candelas per square meter. |
| 18–65535 | Reserved |

The MPEG-2 sequence display extension `transfer_characteristics` defines a code 6 whose transfer function is identical to that in code 1. QuickTime writers should map 6 to 1 when converting from `transfer_characteristics` to `transferFunction`.

Recommendation ITU-R BT.470-4 specified an "assumed gamma value of the receiver for which the primary signals are pre-corrected" as 2.2 for NTSC and 2.8 for PAL systems. This information is both incomplete and obsolete. Modern 525- and 625-line digital and NTSC/PAL systems use the transfer function with code 1.

The matrix values are shown in [Table 4-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcnbtguytm) and in Matrix values for index code 1. These figures show a formula for obtaining the normalized value of Y´ in the range [0,1]. You can derive the formula for normalized values of Cb and Cr as follows:

If the equation for normalized Y´ has the form:

EY’ = KG’EG’ + KB’EB’+KR’ER’

Then the formulas for normalized Cb and Cr are:

ECb = (0.5/(1-KB’))(EB’-EY’)

ECr = (0.5/(1-KR’))(ER’-EY’)

__Table 4-6__  Table of matrix index and values

| Index | Video Standard |
| 0 | Reserved |
| 1 | Recommendation ITU-R BT.709-2 (1125/60/2:1 only), SMPTE 274M-1995, 296M-1997    EY’ = 0.7152 EG’ + 0.0722 EB’+ 0.2126 ER’ |
| 2 | Coefficient values are unknown |
| 3–5 | Reserved |
| 6 | Recommendation ITU-R BT.601-4 and BT.470-4 System B and G, SMPTE 170M-1994, 293M-1996    EY’ = 0.587 EG’ + 0.114 EB’+ 0.299 ER’ |
| 7 | SMPTE 240M-1995, 274M-1995    EY’ = 0.701 EG’ + 0.087 EB’+ 0.212 ER’ |
| 8 | Reserved |
| 9 | Recommendation ITU-R BT.2020 (non-constant luminance)    EY’ = 0.6780 EG’ + 0.0593 EB’+ 0.2627 ER’ |
| 10–65535 | Reserved |

##### Clean Aperture ('clap')

The clean aperture extension defines the relationship between the pixels in a stored image and a canonical rectangular region of a video system from which it was captured or to which it will be displayed. This can be used to correlate pixel locations in two or more images—possibly recorded using different systems—for accurate compositing. This is necessary because different video digitizer devices can digitize different regions of the incoming video signal, causing pixel misalignment between images. In particular, a stored image may contain “edge” data outside the canonical display area for a given system.

The clean aperture is either coincident with the stored image or a subset of the stored image; if it is a subset, it may be centered on the stored image, or it may be offset positively or negatively from the stored image center.

The clean aperture extension contains a width in pixels, a height in picture lines, and a horizontal and vertical offset between the stored image center and a canonical image center for the given video system. The width is typically the width of the canonical clean aperture for a video system divided by the pixel aspect ratio of the stored data. The offsets also take into account any “overscan” in the stored image. The height and width must be positive values, but the offsets may be positive, negative, or zero.

These values are given as ratios of two 32-bit numbers, so that applications can calculate precise values with minimum roundoff error. For whole values, the value should be stored in the numerator field while the denominator field is set to 1.

**Size**
: A 32-bit unsigned integer containing the size of the `'clap'` atom.

**Type**
: A 32-bit unsigned integer containing the four-character code `'clap'`.

**apertureWidth_N (numerator)**
: A 32-bit signed integer containing either the width of the clean aperture in pixels or the numerator portion of a fractional width.

**apertureWidth_D (denominator)**
: A 32-bit signed integer containing either the denominator portion of a fractional width or the number 1.

**apertureHeight_N (numerator)**
: A 32-bit signed integer containing either the height of the clean aperture in picture lines or the numerator portion of a fractional height.

**apertureHeight_D (denominator)**
: A 32-bit signed integer containing either the denominator portion of a fractional height or the number 1.

**horizOff_N (numerator)**
: A 32-bit signed integer containing either the horizontal offset of the clean aperture center minus (width–1)/2 or the numerator portion of a fractional offset. This value is typically zero.

**horizOff_D (denominator)**
: A 32-bit signed integer containing either the denominator portion of the horizontal offset or the number 1.

**vertOff_N (numerator)**
: A 32-bit signed integer containing either the vertical offset of the clean aperture center minus (height–1)/2 or the numerator portion of a fractional offset. This value is typically zero.

**vertOff_D (denominator)**
: A 32-bit signed integer containing either the denominator portion of the vertical offset or the number 1.

### Video Sample Data

The format of the data stored in video samples is completely dependent on the type of the compression used, as indicated in the video sample description. The following sections discuss some of the video encoding schemes supported by QuickTime.

#### Uncompressed RGB

Uncompressed RGB data is stored in a variety of different formats. The format used depends on the depth field of the video sample description. For all depths, the image data is padded on each scan line to ensure that each scan line begins on an even byte boundary.

- For depths of 1, 2, 4, and 8, the values stored are indexes into the color table specified in the color table ID field.
- For a depth of 16, the pixels are stored as 5-5-5 RGB values with the high bit of each 16-bit integer set to 0.
- For a depth of 24, the pixels are stored packed together in RGB order.
- For a depth of 32, the pixels are stored with an 8-bit alpha channel, followed by 8-bit RGB components.

RGB data can be stored in composite or planar format. Composite format stores the RGB data for each pixel contiguously, while planar format stores the R, G, and B data separately, so the RGB information for a given pixel is found using the same offset into multiple tables. For example, the data for two pixels could be represented in composite format as RGB-RGB or in planar format as RR-GG-BB.

#### Uncompressed Y´CbCr (including yuv2)

The Y´CbCr color space is widely used for digital video. In this data format, luminance is stored as a single value (Y), and chrominance information is stored as two color-difference components (Cb and Cr). Cb is the difference between the blue component and a reference value; Cr is the difference between the red component and a reference value.

This is commonly referred to as “YUV” format, with “U” standing-in for Cb and “V” standing-in for Cr. This usage is not strictly correct, as YUV, YIC, and Y´CbCr are distinct color models for PAL, NTSC, and digital video, but most Y´CbCr data formats and codecs are described or even named as some variant of “YUV.”

The values of Y, Cb, and Cr can be represented using a variety of bit depths, trading off accuracy for file size. Similarly, the chrominance values can be subsampled, recording only one pixel’s color value out of two, for example, or averaging the color value of adjacent pixels. This subsampling is a form of compression, but if no additional lossy compression is performed on the sampled video, it is still referred to as “uncompressed” Y´CbCr video. In addition, a fourth component can be added to Y´CbCr video to record an alpha channel.

The number of components (Y´CbCr with or without alpha) and any subsampling are denoted using ratios of three or four numbers, such as 4:2:2 to indicate 4 bits of Y to 2 bits each of Cb and Cr (chroma subsampling), or 4:4:4 for equal storage of Y, Cb, and Cr (no subsampling), or 4:4:4:4 for Y´CbCr plus alpha with no subsampling. The ratios do not typically denote actual bit depths.

Uncompressed Y´CbCr video data is typically stored as follows:

- Y´, Cb, and Cr components of each line are stored spatially left to right and temporally from earliest to latest.
- The lines of a field or frame are stored spatially top to bottom and temporally earliest to latest.
- Y´ is an unsigned integer. Cb and Cr are twos-complement signed integers.

The yuv2 stream, for example, is encoded in a series of 4-byte packets. Each packet represents two adjacent pixels on the same scan line. The bytes within each packet are ordered as follows:

```
    y0 u y1 v
```

`y0` is the luminance value for the left pixel; `y1` the luminance for the right pixel. `u` and `v` are chromatic values that are shared by both pixels.

Accurate conversion between RGB and Y´CbCr color spaces requires a computation for each component of each pixel. An example conversion from yuv2 into RGB is represented by the following equations:

r = 1.402 \* v + y + .5

g = y - .7143 \* v - .3437 \* u + .5

b = 1.77 \* u + y + .5

The r, g, and b values range from 0 to 255.

The coefficients in these equations are derived from matrix operations and depend on the reference values used for the primary colors and for white. QuickTime uses canonical values for these reference coefficients based on published standards. The sample description extension for Y´CbCr formats includes a `'colr'` atom, which contains indexes into a table of canonical references. This provides support for multiple video standards without opening the door to data entry errors for stored coefficient values. Refer to the published standards for the formulas and methods used to derive conversion coefficients from the table entries.

#### JPEG

QuickTime stores JPEG images according to the rules described in the ISO JPEG specification, document number DIS 10918-1.

#### MPEG-4 Video

MPEG-4 video uses the `'mp4v'` data format. The sample description requires the elementary stream descriptor (`'esds'`) extension to the standard video sample description. If non-square pixels are used, the pixel aspect ratio (`'pasp'`) extension is also required. For details on these extensions, see [Pixel Aspect Ratio ('pasp')](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcmrugu2ta) and [MPEG-4 Elementary Stream Descriptor Atom ('esds')](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcmrug43ti).

MPEG-4 video conforms to ISO/IEC documents 14496-1/2000(E) and 14496-2:1999/Amd.1:2000(E).

#### Motion-JPEG

Motion-JPEG (M-JPEG) is a variant of the ISO JPEG specification for use with digital video streams. Instead of compressing an entire image into a single bitstream, Motion-JPEG compresses each video field separately, returning the resulting JPEG bitstreams consecutively in a single frame.

There are two flavors of Motion-JPEG currently in use. These two formats differ based on their use of markers. Motion-JPEG format A supports markers; Motion-JPEG format B does not. The following paragraphs describe how QuickTime stores Motion-JPEG sample data. [Figure 4-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtonjxgm4q) shows an example of Motion-JPEG A dual-field sample data. [Figure 4-7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtonjxgu2a) shows an example of Motion- JPEG B dual-field sample data.

__Figure 4-6__  Motion-JPEG A dual-field sample data

（原归档配图获取待重试：`qt_l_216.jpg`）

Each field of Motion-JPEG format A fully complies with the ISO JPEG specification, and therefore supports application markers. QuickTime uses the APP1 marker to store control information, as follows (all of the fields are 32-bit integers):

**Reserved**
: Unpredictable; should be set to 0.

**Tag**
: Identifies the data type; this field must be set to `'mjpg'`.

**Field size**
: The actual size of the image data for this field, in bytes.

**Padded field size**
: Contains the size of the image data, including pad bytes. Some video hardware may append pad bytes to the image data; this field, along with the field size field, allows you to compute how many pad bytes were added.

**Offset to next field**
: The offset, in bytes, from the start of the field data to the start of the next field in the bitstream. This field should be set to 0 in the last field’s marker data.

**Quantization table offset**
: The offset, in bytes, from the start of the field data to the quantization table marker. If this field is set to 0, check the image description for a default quantization table.

**Huffman table offset**
: The offset, in bytes, from the start of the field data to the Huffman table marker. If this field is set to 0, check the image description for a default Huffman table.

**Start of frame offset**
: The offset from the start of the field data to the start of image marker. This field should never be set to 0.

**Start of scan offset**
: The offset, in bytes, from the start of the field data to the start of the scan marker. This field should never be set to 0.

**Start of data offset**
: The offset, in bytes, from the start of the field data to the start of the data stream. Typically, this immediately follows the start of scan data.

__Note:__ The last two fields have been added since the original Motion-JPEG specification, and so they may be missing from some Motion-JPEG A files. You should check the length of the APP1 marker before using the start of scan offset and start of data offset fields.

Motion-JPEG format B does not support markers. In place of the marker, therefore, QuickTime inserts a header at the beginning of the bitstream. Again, all of the fields are 32-bit integers.

__Figure 4-7__  Motion-JPEG B dual-field sample data

（原归档配图获取待重试：`qt_l_215.jpg`）

**Reserved**
: Unpredictable; should be set to 0.

**Tag**
: The data type; this field must be set to `'mjpg'`.

**Field size**
: The actual size of the image data for this field, in bytes.

**Padded field size**
: The size of the image data, including pad bytes. Some video hardware may append pad bytes to the image data; this field, along with the field size field, allows you to compute how many pad bytes were added.

**Offset to next field**
: The offset, in bytes, from the start of the field data to the start of the next field in the bitstream. This field should be set to 0 in the second field’s header data.

**Quantization table offset**
: The offset, in bytes, from the start of the field data to the quantization table. If this field is set to 0, check the image description for a default quantization table.

**Huffman table offset**
: The offset, in bytes, from the start of the field data to the Huffman table. If this field is set to 0, check the image description for a default Huffman table.

**Start of frame offset**
: The offset from the start of the field data to the field’s image data. This field should never be set to 0.

**Start of scan offset**
: The offset, in bytes, from the start of the field data to the start of scan data.

**Start of data offset**
: The offset, in bytes, from the start of the field data to the start of the data stream. Typically, this immediately follows the start of scan data.

__Note:__ The last two fields were “reserved, must be set to zero” in the original Motion-JPEG specification.

The Motion-JPEG format B header must be a multiple of 16 in size. When you add pad bytes to the header, set them to 0.

Because Motion-JPEG format B does not support markers, the JPEG bitstream does not have NULL bytes (0x00) inserted after data bytes that are set to 0xFF.

## Sound Media

Sound media is used to store compressed and uncompressed audio data in QuickTime movies. It has a media type of '`soun`'. This section describes the sound sample description and the storage format of sound files using various data formats.

### Sound Sample Descriptions

The sound sample description contains information that defines how to interpret sound media data. This sample description is based on the standard sample description, as described in [Sample Description Atoms](Movie%20Atoms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgqwtenjwheyq).

The data format field contains the format of the audio data. This may specify a compression format or one of several uncompressed audio formats. [Table 4-7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcmzrgm4tk) shows a list of some supported sound formats.

__Table 4-7__  Partial list of supported QuickTime audio formats.

| Format | 4-Character code | Description |
| Not specified | 0x00000000 | This format descriptor should not be used, but may be found in some files. Samples are assumed to be stored in either `'raw '` or `'twos'` format, depending on the sample size field in the sound description. |
| `kSoundNotCompressed` | `'NONE'` | This format descriptor should not be used, but may be found in some files. Samples are assumed to be stored in either `'raw '` or `'twos'` format, depending on the sample size field in the sound description. |
| `k8BitOffsetBinaryFormat` | `'raw '` | Samples are stored uncompressed, in offset-binary format (values range from 0 to 255; 128 is silence). These are stored as 8-bit offset binaries. |
| `k16BitBigEndianFormat` | `'twos'` | Samples are stored uncompressed, in two’s-complement format (sample values range from -128 to 127 for 8-bit audio, and -32768 to 32767 for 1- bit audio; 0 is always silence). These samples are stored in 16-bit big-endian format. |
| `k16BitLittleEndianFormat` | `'sowt'` | 16-bit little-endian, twos-complement |
| `kMACE3Compression` | '`MAC3` ' | Samples have been compressed using MACE 3:1. (Obsolete.) |
| `kMACE6Compression` | '`MAC6` ' | Samples have been compressed using MACE 6:1. (Obsolete.) |
| `kIMACompression` | `'ima4'` | Samples have been compressed using IMA 4:1. |
| `kFloat32Format` | `'fl32'` | 32-bit floating point |
| `kFloat64Format` | `'fl64'` | 64-bit floating point |
| `k24BitFormat` | `'in24'` | 24-bit integer |
| `k32BitFormat` | `'in32'` | 32-bit integer |
| `kULawCompression` | `'ulaw'` | uLaw 2:1 |
| `kALawCompression` | `'alaw'` | uLaw 2:1 |
| `kMicrosoftADPCMFormat` | `0x6D730002` | Microsoft ADPCM-ACM code 2 |
| `kDVIIntelIMAFormat` | `0x6D730011` | DVI/Intel IMAADPCM-ACM code 17 |
| `kDVAudioFormat` | `'dvca'` | DV Audio |
| `kQDesignCompression` | `'QDMC'` | QDesign music |
| `kQDesign2Compression` | `'QDM2'` | QDesign music version 2 |
| `kQUALCOMMCompression` | `'Qclp'` | QUALCOMM PureVoice |
| `kMPEGLayer3Format` | `0x6D730055` | MPEG-1 layer 3, CBR only (pre-QT4.1) |
| `kFullMPEGLay3Format` | `'.mp3'` | MPEG-1 layer 3, CBR & VBR (QT4.1 and later) |
| `kMPEG4AudioFormat` | `'mp4a'` | MPEG-4, Advanced Audio Coding (AAC) |
| `kAC3AudioFormat` | `'ac-3'` | Digital Audio Compression Standard (AC-3, Enhanced AC-3) |

#### Sound Sample Description (Version 0)

There are currently three versions of the sound sample description, versions 0, 1 and 2. Version 0 supports only uncompressed audio in raw (`'raw '`) or twos-complement (`'twos'`) format, although these are sometimes incorrectly specified as either `'NONE'` or 0x00000000.

**Version**
: A 16-bit integer that holds the sample description version (currently 0 or 1).

**Revision level**
: A 16-bit integer that must be set to 0.

**Vendor**
: A 32-bit integer that must be set to 0.

**Number of channels**
: A 16-bit integer that indicates the number of sound channels used by the sound sample. Set to 1 for monaural sounds, 2 for stereo sounds. Higher numbers of channels are not supported.

**Sample size (bits)**
: A 16-bit integer that specifies the number of bits in each uncompressed sound sample. Allowable values are 8 or 16. Formats using more than 16 bits per sample set this field to 16 and use sound description version 1.

**Compression ID**
: A 16-bit integer that must be set to 0 for version 0 sound descriptions. This may be set to –2 for some version 1 sound descriptions; see [Redefined Sample Tables](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcmztge3tq).

**Packet size**
: A 16-bit integer that must be set to 0.

**Sample rate**
: A 32-bit unsigned fixed-point number (16.16) that indicates the rate at which the sound samples were obtained. The integer portion of this number should match the media’s time scale. Many older version 0 files have values of 22254.5454 or 11127.2727, but most files have integer values, such as 44100. Sample rates greater than 2^16 are not supported.

Version 0 of the sound description format assumes uncompressed audio in `'raw '` or `'twos'` format, 1 or 2 channels, 8 or 16 bits per sample, and a compression ID of 0.

#### Sound Sample Description (Version 1)

The version field in the sample description is set to 1 for this version of the sound description structure. In version 1 of the sound description, introduced in QuickTime 3, the sound description record is extended by 4 fields, each 4 bytes long, and includes the ability to add atoms to the sound description.

These added fields are used to support out-of-band configuration settings for decompression and to allow some parsing of compressed QuickTime sound tracks without requiring the services of a decompressor.

These fields introduce the idea of a _packet_. For uncompressed audio, a packet is a sample from a single channel. For compressed audio, this field has no real meaning; by convention, it is treated as 1/number-of-channels.

These fields also introduce the idea of a _frame_. For uncompressed audio, a frame is one sample from each channel. For compressed audio, a frame is a compressed group of samples whose format is dependent on the compressor.

__Important:__ The value of all these fields has different meaning for compressed and uncompressed audio. The meaning may not be easily deducible from the field name.

The four new fields are:

**Samples per packet**
: The number of uncompressed frames generated by a compressed frame (an uncompressed frame is one sample from each channel). This is also the frame duration, expressed in the media’s timescale, where the timescale is equal to the sample rate. For uncompressed formats, this field is always 1.

**Bytes per packet**
: For uncompressed audio, the number of bytes in a sample for a single channel. This replaces the older _sampleSize_ field, which is set to 16.This value is calculated by dividing the frame size by the number of channels. The same calculation is performed to calculate the value of this field for compressed audio, but the result of the calculation is not generally meaningful for compressed audio.

**Bytes per frame**
: The number of bytes in a frame: for uncompressed audio, an uncompressed frame; for compressed audio, a compressed frame. This can be calculated by multiplying the bytes per packet field by the number of channels.

**Bytes per sample**
: The size of an uncompressed sample in bytes. This is set to 1 for 8-bit audio, 2 for all other cases, even if the sample size is greater than 2 bytes.

When capturing or compressing audio using the QuickTime API, the value of these fields can be obtained by calling the Apple Sound Manager’s `GetCompression` function. Historically, the value returned for the bytes per frame field was not always reliable, however, so this field was set by multiplying bytes per packet by the number of channels.

To facilitate playback on devices that support only one or two channels of audio in `'raw '` or `'twos'` format (such as most early Macintosh and Windows computers), all other uncompressed audio formats are treated as compressed formats, allowing a simple “decompressor” component to perform the necessary format conversion during playback. The audio samples are treated as opaque compressed frames for these data types, and the fields for sample size and bytes per sample are not meaningful.

The new fields correspond to the `CompressionInfo` structure used by the Macintosh Sound Manager (which uses 16-bit values) to describe the compression ratio of fixed ratio audio compression algorithms. If these fields are not used, they are set to 0. File readers only need to check to see if `samplesPerPacket` is 0.

##### Redefined Sample Tables

If the compression ID in the sample description is set to –2, the sound track uses redefined sample tables optimized for compressed audio.

Unlike video media, the data structures for QuickTime sound media were originally designed for uncompressed samples. The extended version 1 sound description structure provides a great deal of support for compressed audio, but it does not deal directly with the sample table atoms that point to the media data.

The ordinary sample tables do not point to compressed frames, which are the fundamental units of compressed audio data. Instead, they appear to point to individual uncompressed audio samples, each one byte in size, within the compressed frames. When used with the QuickTime API, QuickTime compensates for this fiction in a largely transparent manner, but attempting to parse the sound samples using the original sample tables alone can be quite complicated.

With the introduction of support for the playback of variable bit-rate (VBR) audio in QuickTime 4.1, the contents of a number of these fields were redefined, so that a frame of compressed audio is treated as a single media sample. The sample-to-chunk and chunk offset atoms point to compressed frames, and the sample size table documents the size of the frames. The size is constant for CBR audio, but can vary for VBR.

The time-to-sample table documents the duration of the frames. If the time scale is set to the sampling rate, which is typical, the duration equals the number of uncompressed samples in each frame, which is usually constant even for VBR (it is common to use a fixed frame duration). If a different media timescale is used, it is necessary to convert from timescale units to sampling rate units to calculate the number of samples.

This change in the meaning of the sample tables allows you to use the tables accurately to find compressed frames.

To indicate that this new meaning is used, a version 1 sound description is used and the compression ID field is set to –2. The `samplesPerPacket` field and the `bytesPerSample` field are not necessarily meaningful for variable bit rate audio, but these fields should be set correctly in cases where the values are constant; the other two new fields ( `bytesPerPacket` and `bytesPerFrame`) are reserved and should be set to 0.

If the compression ID field is set to zero, the sample tables describe uncompressed audio samples and cannot be used directly to find and manipulate compressed audio frames. QuickTime has built-in support that allows programmers to act as if these sample tables pointed to uncompressed 1-byte audio samples.

#### Sound Sample Description (Version 2)

QuickTime 7 introduced a new version of the sound sample description, version 2, which extends QuickTime capabilities to include high resolution audio with another expansion of the sound sample description structure. In QuickTime 7, the sound and audio facilities are based on the Core Audio framework facilities and the Sound Manager has been deprecated. In this version of the sound sample description, the format field is set to `‘lpcm’` for uncompressed data. For compressed data formats, the format field is set to the compression type code (normally `‘mp4a’`) and the compression specifics and other features of QuickTime 7 are supplied by extensions.

The version field is set to 2 for this version of the sound sample description structure.

The sound sample description v2 structure adds the following new fields, appending to the v1 structure and renaming the four fields added in v1 to help ensure backwards compatibility with older applications. The version 2 fields are:

__Important:__ The values contained in these fields have different meanings for compressed and uncompressed audio. The meaning may not be easily deducible from the field name and require reference to the appropriate sound sample description extensions to understand fully.

**Version**
: A 16-bit integer that holds the sample description version (set to 2).

**Revision level**
: A 16-bit integer that must be set to 0.

**Vendor**
: A 32-bit integer that must be set to 0.

**always3**
: A 16-bit integer field that must be set to 3.

**always16**
: A 16-bit integer field that must be set to 16 (0x0010).

**alwaysMinus2**
: A 16-bit integer field that must be set to -2 (0xFFFE).

**always0**
: A 16-bit integer field that must be set to 0.

**always65536**
: A 32-bit integer field that must be set to 65536.

**sizeOfStructOnly**
: A 32-bit integer field providing the offset to sound sample description structure’s extensions.

**audioSampleRate**
: A 64-bit floating point number representing the number of audio frames per second, for example: 44,100.0.

**numAudioChannels**
: A 32-bit integer field set to the number of audio channels; any channel assignment will be expressed in an extension.

**always7F000000**
: A 32-bit integer field that must be set to 0x7F000000.

**constBitsPerChannel**
: A 32-bit integer field which is set only if constant and only for uncompressed audio. For all other cases set to 0.

**formatSpecificFlags**
: A 32-bit integer field which carries LPCM flag values defined in [LPCM flag values](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzvga) below.

**constBytesPerAudioPacket**
: A 32-bit unsigned integer set to the number of bytes per packet only if this value is constant. For other cases set to 0.

**constLPCMFramesPerAudioPacket**
: A 32-bit unsigned integer set to the number of PCM frames per packet only if this value is constant. For other cases set to 0.

Some definitions for sound sample description version 2:

- LPCM Frame: one uncompressed sample in each of the channels (for instance, 44100Hz audio has 44100 _LPCM_ frames per second, whether it is mono, stereo, 5.1, or other possible values). In other words, LPCM Frames divided by the `audioSampleRate` value is duration in seconds.
- Audio Packet: For compressed audio, an audio packet is the natural compressed access unit of that format. For uncompressed audio, an audio packet is simply one LPCM frame.
- Fields prefixed by “const”: Note the three sound sample description v2 fields whose names start with "const". These fields are only nonzero if the value is a constant. A zero in each field implies that the value is variable. For example: AAC audio would have a zero in `constBytesPerAudioPacket` because AAC has variable sized audio packets. Codecs with variable duration audio packets set a zero in `constLPCMFramesPerAudioPacket`.

##### LPCM flag values

The `formatSpecificFlags` field carries flags significant to the layout and formatting of audio streams defined in the Core Audio underpinnings for sound sample description v2. These are enumerated in the Apple QuickTime/CoreAudioFormat.h interface file and are subject to a fuller interpretation in the context of the `AudioStreamBasicDescription` data type. See the CoreAudio, “Core Audio Framework Reference” in the [OS X Developer Library](https://developer.apple.com/library/mac/navigation/index.html).

```
enum {     kAudioFormatFlagIsFloat                  = (1 << 0),  // 0x1     kAudioFormatFlagIsBigEndian              = (1 << 1),  // 0x2     kAudioFormatFlagIsSignedInteger          = (1 << 2),  // 0x4     kAudioFormatFlagIsPacked                 = (1 << 3),  // 0x8     kAudioFormatFlagIsAlignedHigh            = (1 << 4),  // 0x10     kAudioFormatFlagIsNonInterleaved         = (1 << 5),  // 0x20     kAudioFormatFlagIsNonMixable             = (1 << 6),  // 0x40     kAudioFormatFlagsAreAllClear             = (1 << 31),          kLinearPCMFormatFlagIsFloat              = kAudioFormatFlagIsFloat,     kLinearPCMFormatFlagIsBigEndian          = kAudioFormatFlagIsBigEndian,     kLinearPCMFormatFlagIsSignedInteger      = kAudioFormatFlagIsSignedInteger,     kLinearPCMFormatFlagIsPacked             = kAudioFormatFlagIsPacked,     kLinearPCMFormatFlagIsAlignedHigh        = kAudioFormatFlagIsAlignedHigh,     kLinearPCMFormatFlagIsNonInterleaved     = kAudioFormatFlagIsNonInterleaved,     kLinearPCMFormatFlagIsNonMixable         = kAudioFormatFlagIsNonMixable,     kLinearPCMFormatFlagsSampleFractionShift = 7,     kLinearPCMFormatFlagsSampleFractionMask  = (0x3F << kLinearPCMFormatFlagsSampleFractionShift),     kLinearPCMFormatFlagsAreAllClear         = kAudioFormatFlagsAreAllClear,          kAppleLosslessFormatFlag_16BitSourceData = 1,     kAppleLosslessFormatFlag_20BitSourceData = 2,     kAppleLosslessFormatFlag_24BitSourceData = 3,     kAppleLosslessFormatFlag_32BitSourceData = 4 };
```

#### Sound Sample Description Extensions

All extensions to the `SoundDescription` record are made using atoms. That means one or more atoms can be appended to the end of the `SoundDescription` record using the standard [size, type] mechanism used throughout the QuickTime movie architecture. Extensions were first added with sound sample description v1.

To illustrate this, for sound sample description v1, the extensions are added by following the last field of the struct with QuickTime atoms. The struct implementation looks like this:

```swift
struct SoundDescriptionV1 {
    // original fields
    SoundDescription    desc;
    // fixed compression ratio information
    unsigned long   samplesPerPacket;
    unsigned long   bytesPerPacket;
    unsigned long   bytesPerFrame;
    unsigned long   bytesPerSample;
    // optional, additional atom-based fields --
    // ([long size, long type, some data], repeat)
};
```

Version 2 of the sound sample description maintains the same mechanism for the addition of extensions. In the sound sample description v2 structure, the `sizeOfStructOnly` field value provides the offset to the extensions.

##### siSlopeAndIntercept Atom

__Note:__ The siSlopeAndIntercept atom is deprecated in the QuickTime file format. The information that follows is intended to document existing content containing this atom and should not be used for new development.

The siSlopeAndIntercept atom contains `slope`, `intercept`, `minClip`, and `maxClip` parameters relevant to a decompressor component.

At runtime, the contents of the type `siSlopeAndIntercept` and `siDecompressorSettings` atoms are provided to the decompressor component through the standard `SetInfo` mechanism of the Sound Manager.

```swift
struct SoundSlopeAndInterceptRecord {
    Float64                 slope;
    Float64                 intercept;
    Float64                 minClip;
    Float64                 maxClip;
};
typedef struct SoundSlopeAndInterceptRecord SoundSlopeAndInterceptRecord;
```

##### siDecompressionParam Atom ('wave')

The `siDecompressionParam` atom provides the ability to store data specific to a given audio decompressor in the `SoundDescription` record. As example, some audio decompression algorithms, such as Microsoft’s ADPCM, require a set of out-of-band values to configure the decompressor. These are stored in an atom of this type.

This atom contains other atoms with audio decompressor settings and is a required extension to the sound sample description for MPEG-4 audio. A `'wave'` chunk for `'mp4a'` typically contains (in order) at least a `'frma'` atom, an `'mp4a'` atom, an `'esds'` atom, and a Terminator Atom (0x00000000) atom.

The contents of other `siDecompressionParam` atoms are dependent on the audio decompressor.

**Size**
: An unsigned 32-bit integer holding the size of the decompression parameters atom.

**Type**
: An unsigned 32-bit field containing the four-character code `'wave'`.

**Extension atoms**
: Atoms containing the necessary out-of-band decompression parameters for the sound decompressor. For MPEG-4 audio (`'mp4a'`), this includes elementary stream descriptor (`'esds'`), format (`'frma'`), and terminator atoms.

##### Format Atom ('frma')

This atom shows the data format of the stored sound media.

**Size**
: An unsigned 32-bit integer holding the size of the format atom.

**Type**
: An unsigned 32-bit field containing the four-character code `'frma'`.

**Data format**
: The value of this field is copied from the data-format field of the sound sample description.

##### Terminator Atom (0x00000000)

This atom is present to indicate the end of the sound description. It contains no data, and has a type field of zero (0x00000000) instead of a four-character code.

**Size**
: An unsigned 32-bit integer holding the size of the decompression parameters atom (always set to 8).

**Type**
: An unsigned 32-bit integer set to zero (0x00000000). This is a rare instance in which the type field is _not_ a four-character ASCII code.

##### MPEG-4 Elementary Stream Descriptor Atom ('esds')

This atom is a required extension to the sound sample description for MPEG-4 audio. This atom contains an elementary stream descriptor, which is defined in ISO/IEC FDIS 14496.

**Size**
: An unsigned 32-bit integer holding the size of the elementary stream descriptor atom.

**Type**
: An unsigned 32-bit field containing the four-character code `'esds'`.

**Version**
: An unsigned 32-bit field set to zero.

**Elementary Stream Descriptor**
: An elementary stream descriptor for MPEG-4 audio, as defined in the MPEG-4 specification ISO/IEC 14496.

##### Audio Channel Layout Atom (‘chan’)

This atom is an optional extension to the sound sample description specifying audio channel layouts for sound media contained in QuickTime movies. It is a full atom followed by a big-endian audio channel layout structure as defined by Apple’s Core Audio framework. Audio channel layouts can be applied to both compressed and uncompressed sound formats.

__Note:__ Audio channel layouts with more than two channels per track require implementation with a version 2 sound sample description.

**Size**
: An unsigned 32-bit integer holding the size of the audio channel layout atom.

**Type**
: An unsigned 32-bit field containing the four-character code `'chan'`

**Version**
: A 1-byte specification of the version of the audio channel layout atom.

**Flags**
: A 3-byte space for audio channel layout flags.

**Audio channel layout**
: A big-endian `AudioChannelLayout` structure as defined in CoreAudioTypes.h. See the [OS X Developer Library](https://developer.apple.com/library/mac/navigation/index.html) for CoreAudio framework details.

##### Subtitle Follows Track Reference Atom

Sound tracks can have a track reference of type `'folw'` (for “follows”) to a single subtitle track from among the subtitle tracks in the same alternate group; this subtitle track should be considered the default to select if the sound track is selected. Use this only if compatibility between language tags is not possible for some reason making it impossible to otherwise select a default track. See [Preparing Sound and Subtitle Alternate Groups for Use with Apple Devices](Some%20Useful%20Examples%20and%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wvgvzu) for related information.

### Sound Sample Data

The format of data stored in sound samples is completely dependent on the type of the compressed data stored in the sound sample description. The following sections discuss some of the formats supported by QuickTime.

#### Uncompressed 8-Bit Sound

Eight-bit audio is stored in offset-binary encodings. If the data is in stereo, the left and right channels are interleaved.

#### Uncompressed 16-Bit Sound

Sixteen-bit audio may be stored in two’s-complement encodings. If the data is in stereo, the left and right channels are interleaved.

#### IMA, uLaw, and aLaw

- IMA 4:1

  The IMA encoding scheme is based on a standard developed by the International Multimedia Association for pulse code modulation (PCM) audio compression. QuickTime uses a slight variation of the format to allow for random access. IMA is a 16-bit audio format which supports 4:1 compression. It is defined as follows:

  ```
  kIMACompression = FOUR_CHAR_CODE('ima4'), /*IMA 4:1*/
  ```

- uLaw 2:1 and aLaw 2:1

  The uLaw (mu-law) encoding scheme is used on North American and Japanese phone systems, and is coming into use for voice data interchange, and in PBXs, voice-mail systems, and Internet talk radio (via MIME). In uLaw encoding, 14 bits of linear sample data are reduced to 8 bits of logarithmic data.

  The aLaw encoding scheme is used in Europe and the rest of the world.

  The kULawCompression and the kALawCompression formats are typically found in `.au` formats.

#### Floating-Point Formats

Both `kFloat32Format` and `kFloat64Format` are floating-point uncompressed formats. Depending upon codec-specific data associated with the sample description, the floating-point values may be in big-endian (network) or little-endian (Intel) byte order. This differs from the 16-bit formats, where there is a single format for each endian layout.

#### 24- and 32-Bit Integer Formats

Both `k24BitFormat` and `k32BitFormat` are integer uncompressed formats. Depending upon codec-specific data associated with the sample description, the floating-point values may be in big-endian (network) or little-endian (Intel) byte order.

#### kMicrosoftADPCMFormat and kDVIIntelIMAFormat Sound Codecs

The `kMicrosoftADPCMFormat` and the `kDVIIntelIMAFormat` codec provide QuickTime interoperability with AVI and WAV files. The four-character codes used by Microsoft for their formats are numeric. To construct a QuickTime-supported codec format of this type, the Microsoft numeric ID is taken to generate a four-character code of the form `'msxx'` where _xx_ takes on the numeric ID.

#### kDVAudioFormat Sound Codec

The DV audio sound codec, `kDVAudioFormat`, decodes audio found in a DV stream. Since a DV frame contains both video and audio, this codec knows how to skip video portions of the frame and only retrieve the audio portions. Likewise, the video codec skips the audio portions and renders only the image.

#### kQDesignCompression Sound Codec

The `kQDesignCompression` sound codec is the QDesign 1 (pre-QuickTime 4) format. Note that there is also a QDesign 2 format whose four-character code is `'QDM2'`.

#### MPEG-1 Layer 3 (MP3) Codecs

The QuickTime MPEG layer 3 (MP3) codecs come in two particular flavors, as shown in [Table 4-7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcmzrgm4tk). The first (`kMPEGLayer3Format`) is used exclusively in the constant bit rate (CBR) case (pre-QuickTime 4). The other (`kFullMPEGLay3Format`) is used in both the CBR and variable bit rate (VBR) cases. Note that they are the same codec underneath.

#### MPEG-4 Audio

MPEG-4 audio is stored as a sound track with data format `'mp4a'` and certain additions to the sound sample description and sound track atom. Specifically:

- The compression ID is set to -2 and redefined sample tables are used (see [Redefined Sample Tables](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcmztge3tq)).
- The sound sample description includes an `siDecompressionParam` atom (see [siDecompressionParam Atom ('wave')](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcmzugiyde)). The `siDecompressionParam` atom includes:

  - An MPEG-4 elementary stream descriptor extension atom (see [MPEG-4 Elementary Stream Descriptor Atom ('esds')](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcmzugq3dg)).
  - The inclusion of a format atom is strongly recommended. See [Format Atom ('frma')](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcmzugmzto).
  - The last atom in the `siDecompressionParam` atom must be a terminator atom. See [Terminator Atom (0x00000000)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcmzugqytg).
- Other atoms may be present as well; unknown atoms should be ignored.

The audio data is stored as an elementary MPEG-4 audio stream, as defined in ISO/IEC specification 14496-1.

#### Formats Not Currently in Use: MACE 3:1 and 6:1

These compression formats are obsolete: MACE 3:1 and 6:1.

These are 8-bit sound codec formats, defined as follows:

```
kMACE3Compression = FOUR_CHAR_CODE('MAC3'), /*MACE 3:1*/
kMACE6Compression = FOUR_CHAR_CODE('MAC6'), /*MACE 6:1*/
```

## Timed Metadata Media

A track structure is used to store timed metadata in QuickTime movies. This section provides an overview of the timed metadata track structure, and describes the timed metadata sample descriptions and the storage format of timed metadata media samples. The timed metadata track structure has a media type of `‘meta’`.

### Overview of Timed Metadata

A timed metadata track synchronizes metadata references to media tracks for particular media time periods through the track reference, edit, and edit list structures. It is a specialization of the track structure which uses the base media information atom of type `‘minf’`, and a track handler type value set to `‘meta’`. The base media information atom contains the generic media header atom of type `‘gmhd’`.

Because a metadata track is neither visual nor aural, the following track properties should have these values:

- Track width and track height each set to 0.
- The track volume set to 0.
- The track matrix set to the identity matrix.

A QuickTime movie can contain none, one, or several timed metadata tracks. Timed metadata tracks can refer to multiple tracks. Metadata tracks are linked to the tracks they describe using a track-reference of type `‘cdsc’`. The metadata track holds the `‘cdsc’` track reference. If a metadata track describes characteristics of the entire movie, there should be no track reference of type `'cdsc'` between it and another track. These metadata tracks can be considered to hold global metadata for the movie.

Using a timed metadata track, any form of descriptive metadata that changes over time can be linked to a range of media times for which it is valid. Examples of timed metadata can include:

- Faces detected in the scene
- Location-based information (such as GPS)
- Camera aperture and other changing camera-related information
- Copyright and other information for individual clips edited together
- Information such as scene changes and actor names added to the movie in production

As with other tracks, each metadata sample is associated with a single timed metadata sample description. This sample description signals information needed to interpret the data in the metadata sample in a way that is analogous to how a video track’s video sample atom indicates that video samples contain H.264 compressed sample data of particular dimensions.

Zero, one, or many metadata values can be associated with a range of media time in the track. The accommodation for no metadata values for a time allows runs of time with metadata interspersed with runs of time with no metadata. Because the timed metadata is organized as a track, it is also possible to use track edits to indicate the absence of metadata. For some situations, however, it would be better to include metadata samples that themselves carry no metadata values.

### Timed Metadata Sample Description

The timed metadata sample description contains information that defines how to interpret timed metadata media samples. This sample description is based on the standard sample description header, as described in [Sample Description Atoms](Movie%20Atoms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgqwtenjwheyq).

The metadata sample description is a derived sample description format which describes metadata values represented in atoms. It may also include other atoms not holding metadata values.

Zero, one, or more values may be carried in a metadata sample description for a particular time.

The data format field contains the format of the timed metadata media, which is set to `'mebx'`.

__Note:__ Other forms of timed metadata media are not described here. They would be indicated by an alternative type code in the place of `‘mebx’`.

The metadata sample description must contain a metadata key table atom and optionally contains a bit rate atom following the standard sample description atom header, defined below. Other atoms may be introduced in the future.

**Metadata key table**
: An atom containing a table of keys and mappings to payload data in the corresponding timed metadata media samples

**Bit rate atom**
: An optional atom that contains data that signals the bit rate of a media stream

#### Metadata Key Table Atom

The metadata key table atom contains a table of keys and mappings to payload data in the corresponding timed metadata media samples. The type of the metadata key table atom is set to `‘keys’`.

The metadata key table atom contains one or more instances of metadata key atoms, one for each configuration of a key that may occur in the sample units of the track. For example, if there are two keys, there will be two metadata key atoms in the metadata key table atom—one for each key.

If the metadata key table atom does not contain a key for which a client is searching, no timed metadata media samples associated with this sample description contain values with that key.

If the metadata key table atom does contain a particular key, this does not guarantee that timed metadata media samples containing a value for the key were written. So, clients finding a key in the metadata key table atom may still need to look through the track’s timed metadata media samples for values to determine if the track has the particular metadata.

__Note:__ Having the ability for the metadata key table atom to contain keys that are not associated with any instances of timed metadata media samples allows a metadata sample description to be populated with keys that might be discovered (say during a capture process) and then samples to be written with a binding only for the keys found. If a key is never used, there’s no requirement that the timed metadata sample description be rewritten to exclude the key that isn’t needed.

If it is possible to remove unused entries and rewrite the metadata sample description efficiently, this is preferred.

If a timed metadata track includes a key in the metadata sample description but has values using the key in associated media samples, the metadata sample description can still be rewritten to eliminate the key from the metadata key table atom. While the metadata values remain in associated media samples, the data is no longer reachable because the key is now gone. Care should be exercised if the values should themselves be removed from the movie file. Although not a requirement, the remaining but now unreachable data can be removed by copying only referenced metadata values when copying media samples to a new track.

__Figure 4-8__  The layout of a metadata key table atom:

（原归档配图获取待重试：`qtff-keys_atom.jpg`）

**Size**
: A 32-bit unsigned integer that indicates the size in bytes of the atom structure

**Type**
: A 32-bit unsigned integer value set to `'keys’`

**Metadata key table**
: An array of metadata key atoms

#### Bit Rate Atom

The optional bit rate atom may be present at the end of any timed metadata sample description to signal the bit rate information of a stream. The bit rate information can be used for buffer configuration.

__Figure 4-9__  The layout of a bit rate atom:

（原归档配图获取待重试：`qtff-btrt_atom.jpg`）

**Size**
: A 32-bit unsigned integer that indicates the size in bytes of the atom structure

**Type**
: A 32-bit unsigned integer value set to `'btrt’`

**Buffer size**
: A 32-bit unsigned integer that indicates the suggested size of the associated data buffer

**Max bit rate**
: A 32-bit unsigned integer that indicates the maximum bit rate in bits/second of the associated media stream

**Average bit rate**
: A 32-bit unsigned integer that indicates the average bit rate in bits/second of the associated media stream

#### Metadata Key Atom

A metadata key atom is identified by a `local_key_id` corresponding to a 32-bit integer (or FourCC) type code local to the timed metadata track containing it. This `local_key_id` will correspond to atom types within the metadata sample data.

For example, if the metadata key atom has the atom type of `'stuf'`, any atoms of type `'stuf'` in timed metadata samples sharing this sample description hold the value for this key. Any value fitting in a 32-bit big endian integer can be used (such as `'stuf'` or the integer 72). If a FourCC is used, it is recommended that the value be mnemonic if possible. For example, a metadata key atom type of `‘actr’` might contain information about actors in a movie. See [Metadata Sample Data Format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzug4) below.

There are two reserved atom types for metadata key atoms: 0 and 0xFFFFFFFF.

A `local_key_id` of 0 indicates the metadata key atom is unused and should not be interpreted. This indication allows the key to be marked as unused in the timed metadata sample description without requiring the sample description and parent atoms to be rewritten or resized.

A `local_key_id` of 0xFFFFFFFF must not occur in a metadata key atom. It is reserved for future use and can occur as an atom type in timed metadata samples.

All other type codes are available for use as a `local_key_id`.

__Note:__ Because the atoms within the metadata key table atom can take on any atom type, there should be no special interpretation of the type for contained atoms other than for the special value 0. Therefore, including a `'free'` atom does not have the conventional meaning in the metadata key atom. It is recommended that writers avoid the use of overly confusing existing atom type codes.

Each metadata key atom contains a variable number of atoms that define the key structure, optionally the data type for values, and optionally locale information for values. Atoms may be introduced in the future.

A metadata key atom must contain a metadata declaration atom.

__Figure 4-10__  The layout of a metadata key atom:

（原归档配图获取待重试：`qtff-local_key_id_atom.jpg`）

**Size**
: A 32-bit unsigned integer that indicates the size in bytes of the atom structure

**Type**
: A 32-bit unsigned integer value set to `local_key_id`

**Variable array of atoms**
: An array of atoms carrying the definitions for key structure and other optional information

#### Metadata Key Declaration Atom

The metadata key declaration atom holds the key namespace and key value of that namespace for the given values. The type of the metadata key declaration atom is `‘keyd’`.

__Figure 4-11__  The layout of a metadata key declaration atom:

（原归档配图获取待重试：`qtff-keyd_atom.jpg`）

**Size**
: A 32-bit unsigned integer that indicates the size in bytes of the atom structure

**Type**
: A 32-bit unsigned integer value set to `'keyd’`

**Key_namespace**
: A 32-bit identifier describing the domain and the structure of the `key_value`

For example, this could indicate that `key_value` is a reverse-address style string (such as "com.apple.quicktime.ISO6709"), a binary four-character code (such as a `'cprt'` user data key), a Uniform Resource Identifier (URI), or other structures (such as native formats from other metadata standards). New key namespaces must be registered but because a reverse-address style string can often be used, using the reverse-address key namespace may be sufficient for most uses.

**Key_value array**
: An array of unsigned 8-bit bytes holding the key’s value

The interpretation of this array is defined by the associated `key_namespace` field. See the [QuickTime Metadata Keys](Metadata.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmjnknltgny) table for examples.

#### Metadata Datatype Definition Atom

A metadata datatype definition atom can be used to specify the data type of the metadata key atom’s value. The type of the metadata datatype definition atom is `‘dtyp’`.

__Figure 4-12__  The layout of a metadata datatype definition atom:

（原归档配图获取待重试：`qtff-dtyp_atom.jpg`）

**Size**
: A 32-bit unsigned integer that indicates the size in bytes of the atom structure

**Type**
: A 32-bit unsigned integer value set to `'dtyp’`

**Datatype namespace**
: A 32-bit identifier describing how to interpret the data type for the value

New namespace types should be registered with Apple.

**Datatype array**
: An array of unsigned 8-bit bytes holding the data type designation for values in timed metadata media samples having this key. The interpretation of this array is defined by the associated `datatype namespace`.

The combination of `datatype namespace` and `datatype array` indicate the data type (or structure) of a metadata item value. The `datatype namespace` type indicates the interpretation of the `datatype array` value. This specification defines two `datatype namespace` types:

- If `datatype namespace` is 0, `datatype array` contains a big-endian 32-bit unsigned integer corresponding to a well-known type specified in [Table 3-5](Metadata.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmjnknltgni). For example, a well-known type of 1 indicates UTF-8 text and 23 indicates a big-endian 32-bit floating-point number.
- If `datatype namespace` is 1, `datatype array` contains a reverse-address style UTF-8 string indicating an extended data type. This data type namespace type can be used if the data type does not have a corresponding well-known data type. `Datatype array` consists of the bytes of a case-sensitive UTF-8 string without a nul (‘\0’) terminator. For example, a hypothetical `datatype array` “com.company.my-custom-datatype” could register a custom data type belonging to the owner of the DNS registration “mycompany.com”.

A `datatype namespace` other than 0 or 1 may occur in a timed metadata track, perhaps written according to a later version of this specification. Metadata item values with unrecognized data types should be ignored. Even so, some processing is still possible on the metadata item with unrecognized data type, such as copying it between tracks.

__Note:__ New datatype namespaces must be registered with Apple.

__Note:__ Many uses for proprietary or custom metadata data types can be satisfied by using the extended data type namespace type code 1. This allows the new data type to be specified without registration. The reason to add a custom `datatype namespace` type is to allow an existing numbering or naming scheme from a foreign metadata standard to be used with metadata items.

#### Metadata Locale Atom

A metadata value may optionally be tagged with its locale so that it may be chosen based upon the user's language, country, and so on. This tagging makes it possible to include several keys of the same key type (e.g., copyright or scene description) but with differing locales for users with different languages or locations. The type of the metadata locale atom is `‘loca’`.

If the metadata locale atom is absent, metadata values should be considered appropriate for all locales.

__Figure 4-13__  The layout of a metadata locale atom:

（原归档配图获取待重试：`qtff-loca_atom.jpg`）

**Size**
: A 32-bit unsigned integer that indicates the size in bytes of the atom structure

**Type**
: A 32-bit unsigned integer value set to `'loca’`

**Locale string**
: A NULL-terminated string of UTF-8 characters holding a language tag complying with RFC 4646 (BCP 47). Examples include 'en-US', 'fr-FR', or 'zh-CN'.

### Timed Metadata Sample Data Format

A timed metadata media sample is structured as a concatenation of one or more atoms. Typically each atom will contain a metadata value corresponding to a key signaled in the timed metadata sample description.

If no value for a particular key is present in the timed metadata media sample at a given time, the interpretation should be that there is no metadata of that type at the specified time. Timed metadata values for that key for other times (such as from a previous timed metadata media sample) should not be interpreted as applying to the given time.

__Note:__ All metadata samples are marked as sync samples.

If no values for any key are present for a time range, one approach is to include a “NULL” or unreferenced metadata media sample (see [Unreferenced or NULL timed metadata sample data](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzrgqzq)) for the time range. A zero-byte timed metadata media sample cannot be used because all sample sizes must be one or more bytes. Alternatively, “empty edit” track edit list entries could be used to indicate there is no metadata for a range of movie time.

In general, however, it is preferable to include a NULL metadata media sample data instead of using a track edit with an empty edit list to indicate the absence of metadata. Some readers may be unprepared for complex edits (more than one edit list entry and/or a non-contiguous presentation media time).

#### Timed Metadata Media Sample Structure

The timed metadata media sample data consists of some number of concatenated atoms. A `local_key_id` value defines the atom type for each of the atoms. The `local_key_id` value corresponds to a `local_key_id` defined for a metadata key atom in the metadata key table atom for the timed metadata sample. No special interpretation is made regarding the 32-bit value of `local_key_id`. Its interpretation is based solely on what is defined in the corresponding metadata key of the associated metadata sample description.

The `local_key_id` value 0 is reserved and can be used as a placeholder atom in the meda sample. Such an atom has no prescribed contents. (See [Metadata Key Atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzuha).)

The `local_key_id` value 0xFFFFFFFF is also reserved. In the future, this may be documented to hold a particular payload. This `local_key_id` should not be used or interpreted otherwise. If a reader finds an atom with `local_key_id` of 0xFFFFFFFF and does not understand its format, the atom should be ignored.

A timed metadata media sample may contain atoms with types other than those defined in the metadata key table atom and other than the two reserved values 0 and 0xFFFFFFFF. Although this practice is discouraged, any instances of such atoms may be interpreted according to their conventional meaning (such as `‘free’`) or in a private way so long as they are not advertised as keys.

Example:

Consider the metadata format for a geographic point location using coordinates as defined in ISO-6709. The timed metadata media sample created for this data might have a `local_key_id` value of `‘wher’` and the resulting metadata sample would contain the information (such as “+27.5916+086.5640+8850/”) in a corresponding `‘wher’` atom. There is no interpretation of this atom type or a requirement that it be `‘wher’`.

### Constant-size Timed Metadata Sample Data

Some clients using timed metadata tracks may prefer to create metadata tracks with samples that have the same size. Two approaches are described here.

In one approach, the metadata written might contain a fixed number of fixed-sized metadata values (for example, integers or statically sized structures). If one or more values are not used, atoms corresponding to unused values can have their `local_key_id` value set to an unreferenced value (such as 0).

In the second approach, the size of individual metadata values may vary. It is possible to create constant-sized metadata samples by determining a maximum timed metadata media sample size and using unreferenced atoms to add up to this size. The approach is:

1. Determine the constant metadata media atom size desired.
2. Fill in the atoms holding metadata values (see the [Timed Metadata Media Sample Structure](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzrgmzq) example above).
3. If necessary, add one or more unreferenced atoms to reach the constant metadata media atom size.

__Note:__ Because an atom has a minimum size of 8 bytes, the sum of the sizes of contained timed metadata media samples either

- must equal the target constant metadata media atom size, or
- must be 8 or more bytes smaller than the target constant atom size to allow for one or more padding atoms.

#### Unreferenced or NULL timed metadata sample data

A timed metadata sample is identified by its derived atom type supplied by the `local_key_id` value in the metadata sample description’s key tables. An unreferenced metadata atom, meaning one which is not identified in the key tables and not having the reserved value 0xFFFFFFFF, can be considered a “NULL” metadata media sample since its type is unknown in the local namespace and its data will not be interpreted. There is no prescribed atom type indicating a NULL metadata sample although a type of 0 is recommended, as mentioned in the [Metadata Key Atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzrgmyq) description above. Using unreferenced atoms presents a useful way to supply padding when structuring a track for constant-sized metadata sample data or when there are runs of no-metadata interspersed with runs of metadata in a given track, instead of using multiple track edits.

### Combining Multiple Streams of Metadata into the Same Track

Because two “streams” or tracks of metadata values might occur where the time ranges for one stream does not coincide with those of the other stream, a convention is recommended if both streams of metadata values are combined into a single new metadata track (typically because of some production process). At any point in the timeline where a metadata value comes into scope or goes out of scope, new metadata samples should be introduced with the union of all metadata values present for the time range, replacing the existing overlapped samples for that portion of the media time range.

For example, this figure shows the results of combining the metadata from two metadata tracks:

__Figure 4-14__  Combining metadata streams

（原归档配图获取待重试：`timed-metadata_combining-g.jpg`）

__Note:__ The combined timed metadata media samples from time t1 to t2 contain both the A and B metadata values. This is done so that for any time t, it is possible to determine all applicable metadata values without needing to scan through all timed metadata media tracks in backward or forward directions.

In the new combined track, a single timed metadata sample description containing the keys A and B may be used. Creating sample descriptions for each combination (A, B, {A,B}) is possible but discouraged as this makes the determination of whether a key is in the tracks more complex.

### Movie-Level Relationships Among Tracks

A “presentation” track (for example, video or audio) may have more than one metadata track associated with it via `'cdsc'` type track references. The union of all metadata across those tracks should be considered the metadata for the presentation track—just as if there was a single metadata track with all the corresponding metadata.

There is a potential conflict if more than one metadata value of the same type is in the metadata tracks. In this case, the layer of the metadata tracks should be used to establish which should be used. Tracks with lesser layer values (that is, -1 is less than 0) take priority and their metadata values should be used. If two tracks have the same layer value, the last track in movie track order (the order of `'trak'` atoms in the `'moov'` atom) shall override metadata values from tracks earlier in order.

If a metadata track does not have a relationship to another track defined by a track reference of `‘cdsc’`, it should be considered a global metadata track—its metadata applying to the entire movie. If part of a track would apply to a presentation track and part would apply globally, the metadata should be carried in two tracks, the first referencing the presentation track and the other not referencing any track.

## Timecode Media

Timecode media is used to store time code data in QuickTime movies. It has a media type of `'tmcd'`.

### Timecode Sample Description

The timecode sample description contains information that defines how to interpret time code media data. This sample description is based on the standard sample description header, as described in [Sample Description Atoms](Movie%20Atoms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgqwtenjwheyq).

The data format field in the sample description is always set to `'tmcd'`.

The timecode media handler also adds some of its own fields to the sample description.

**Reserved**
: A 32-bit integer that is reserved for future use. Set this field to 0.

**Flags**
: A 32-bit integer containing flags that identify some timecode characteristics. The following flags are defined.

**Drop frame**
: Indicates whether the timecode is drop frame. Set it to 1 if the timecode is drop frame. This flag’s value is 0x0001.

**24 hour max**
: Indicates whether the timecode wraps after 24 hours. Set it to 1 if the timecode wraps. This flag’s value is 0x0002.

**Negative times OK**
: Indicates whether negative time values are allowed. Set it to 1 if the timecode supports negative values. This flag’s value is 0x0004.

**Counter**
: Indicates whether the time value corresponds to a tape counter value. Set it to 1 if the timecode values are tape counter values. This flag’s value is 0x0008.

**Time scale**
: A 32-bit integer that specifies the time scale for interpreting the frame duration field.

**Frame duration**
: A 32-bit integer that indicates how long each frame lasts in real time.

**Number of frames**
: An 8-bit integer that contains the number of frames per second for the timecode format. If the time is a counter, this is the number of frames for each counter tick.

**Reserved**
: An 8-bit quantity that must be set to 0.

**Source reference**
: A user data atom containing information about the source tape. The only currently used user data list entry is the `'name'` type. This entry contains a text item specifying the name of the source tape.

### Timecode Media Information Atom

The timecode media also requires a media information atom. This atom contains information governing how the timecode text is displayed. This media information atom is stored in a base media information atom (see [Base Media Information Atoms](Movie%20Atoms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgqwtenjwgu4a) for more information). The type of the timecode media information atom is `'tcmi'`.

The timecode media information atom contains the following fields:

**Size**
: A 32-bit integer that specifies the number of bytes in this time code media information atom.

**Type**
: A 32-bit integer that identifies the atom type; this field must be set to `'tcmi'`.

**Version**
: A 1-byte specification of the version of this timecode media information atom.

**Flags**
: A 3-byte space for timecode media information flags. Set this field to 0.

**Text font**
: A 16-bit integer that indicates the font to use. Set this field to 0 to use the system font. If the font name field contains a valid name, ignore this field.

**Text face**
: A 16-bit integer that indicates the font’s style. Set this field to 0 for normal text. You can enable other style options by using one or more of the bit masks listed in [Table 4-8](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzygu).

__Table 4-8__  Text face values

| Value | Meaning |
| 0x0001 | Bold |
| 0x0002 | Italic |
| 0x0004 | Underline |
| 0x0008 | Outline |
| 0x0010 | Shadow |
| 0x0020 | Condense |
| 0x0040 | Extend |

**Text size**
: A 16-bit integer that specifies the point size of the time code text.

**Reserved**
: A 16-bit integer that is reserved for use by Apple. Set this field to 0.

**Text color**
: A 48-bit RGB color value for the timecode text.

**Background color**
: A 48-bit RGB background color for the timecode text.

**Font name**
: A Pascal string specifying the name of the timecode text’s font.

#### Timecode Sample Data

A timecode media sample is recorded as a 32-bit integer, interpreted based on the value of the Counter flag in the timecode sample description.

If the Counter flag is set to 1 in the timecode sample description, the sample data is an unsigned 32-bit integer. The timecode counter value is determined by dividing this unsigned 32-bit integer by the number of frames field in the timecode sample description.

If the Counter flag is set to 0 in the timecode sample description, the sample data format is a signed 32-bit integer and is used to calculate a timecode record, defined as follows.

**Hours**
: An 8-bit unsigned integer that indicates the starting number of hours.

**Negative**
: A 1-bit value indicating the time’s sign. If bit is set to 1, the timecode record value is negative.

**Minutes**
: A 7-bit integer that contains the starting number of minutes.

**Seconds**
: An 8-bit unsigned integer indicating the starting number of seconds.

**Frames**
: An 8-bit unsigned integer that specifies the starting number of frames. This field’s value cannot exceed the value of the number of frames field in the timecode sample description.

## Text Media

Text media is used to store text data in QuickTime movies. It has a media type of `'text'`.

### Text Sample Description

The text sample description contains information that defines how to interpret text media data. This sample description is based on the standard sample description header, as described in [Sample Description Atoms](Movie%20Atoms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgqwtenjwheyq).

The data format field in the sample description is always set to `'text'`.

The text media handler also adds some of its own fields to the sample description.

**Display flags**
: A 32-bit integer containing flags that describe how the text should be drawn. The following flags are defined.

**Don’t auto scale**
: Controls text scaling. If this flag is set to 1, the text media handler reflows the text instead of scaling when the track is scaled. This flag’s value is 0x0002.

**Use movie background color**
: Controls background color. If this flag is set to 1, the text media handler ignores the background color field in the text sample description and uses the movie’s background color instead. This flag’s value is 0x0008.

**Scroll in**
: Controls text scrolling. If this flag is set to 1, the text media handler scrolls the text until the last of the text is in view. This flag’s value is 0x0020.

**Scroll out**
: Controls text scrolling. If this flag is set to 1, the text media handler scrolls the text until the last of the text is gone. This flag’s value is 0x0040.

**Horizontal scroll**
: Controls text scrolling. If this flag is set to 1, the text media handler scrolls the text horizontally; otherwise, it scrolls the text vertically. This flag’s value is 0x0080.

**Reverse scroll**
: Controls text scrolling. If this flag is set to 1, the text media handler scrolls down (if scrolling vertically) or backward (if scrolling horizontally; note that horizontal scrolling also depends upon text justification). This flag’s value is 0x0100.

**Continuous scroll**
: Controls text scrolling. If this flag is set to 1, the text media handler displays new samples by scrolling out the old ones. This flag’s value is 0x0200.

**Drop shadow**
: Controls drop shadow. If this flag is set to 1, the text media handler displays the text with a drop shadow. This flag’s value is 0x1000.

**Anti-alias**
: Controls anti-aliasing. If this flag is set to 1, the text media handler uses anti-aliasing when drawing text. This flag’s value is 0x2000.

**Key text**
: Controls background color. If this flag is set to 1, the text media handler does not display the background color, so that the text overlay background tracks. This flag’s value is 0x4000.

**Text justification**
: A 32-bit integer that indicates how the text should be aligned. Set this field to 0 for left-justified text, to 1 for centered text, and to –1 for right-justified text.

**Background color**
: A 48-bit RGB color that specifies the text’s background color.

**Default text box**
: A 64-bit rectangle that specifies an area to receive text (top, left, bottom, right). Typically this field is set to all zeros.

**Reserved**
: A 64-bit value that must be set to 0.

**Font number**
: A 16-bit value that must be set to 0.

**Font face**
: A 16-bit integer that indicates the font’s style. Set this field to 0 for normal text. You can enable other style options by using one or more of the bit masks listed in [Table 4-9](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzrgaya).

__Table 4-9__  Font face values

| Value | Meaning |
| 0x0001 | Bold |
| 0x0002 | Italic |
| 0x0004 | Underline |
| 0x0008 | Outline |
| 0x0010 | Shadow |
| 0x0020 | Condense |
| 0x0040 | Extend |

**Reserved**
: An 8-bit value that must be set to 0.

**Reserved**
: A 16-bit value that must be set to 0.

**Foreground color**
: A 48-bit RGB color that specifies the text’s foreground color.

**Text name**
: A Pascal string specifying the name of the font to use to display the text.

### Text Media Information Atom

The text media also requires a text media information atom. This media information atom is stored in a base media information atom (`'minf'`) in the base media information header atom (`'gmhd'`) (see [Base Media Information Atoms](Movie%20Atoms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgqwtenjwgu4a)). The type of the text media information atom is `'text'`.

The timecode media information atom contains the following fields:

**Size**
: A 32-bit integer that specifies the number of bytes in this text media information atom.

**Type**
: A 32-bit integer that identifies the atom type; this field must be set to `'text'`.

**Matrix structure**
: A matrix structure associated with this text media. This should be the identity matrix. A matrix shows how to map points from one coordinate space into another. See [Matrices](Basic%20Data%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgywtcobxgm3q) for a discussion of how display matrices are used in QuickTime and see [Figure 2-3](Movie%20Atoms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgqwtgmrzgq3q) for an illustration of a matrix structure within an atom.

### Text Sample Data

The format of the text data is a 16-bit length word followed by the actual text. The length word specifies the number of bytes of text, not including the length word itself. Following the text, there may be one or more atoms containing additional information for drawing and searching the text.

[Table 4-10](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwviucykjcummjqgm) lists the currently defined text sample extensions.

__Table 4-10__  Text sample extensions

| Text sample extension | Description |
| `'styl'` | Style information for the text. Allows you to override the default style in the sample description or to define more than one style for a sample. The data is a TextEdit style scrap. |
| `'ftab'` | Table of font names. Each table entry contains a font number (stored in a 16-bit integer) and a font name (stored in a Pascal string).This atom is required if the `'styl'` atom is present. |
| `'hlit'` | Highlight information. The atom data consists of two 32-bit integers. The first contains the starting offset for the highlighted text, and the second has the ending offset. A highlight sample can be in a key frame or in a differenced frame. When it’s used in a differenced frame, the sample should contain a zero-length piece of text. |
| `'hclr'` | Highlight color. This atom specifies the 48-bit RGB color to use for highlighting. |
| `'drpo'` | Drop shadow offset. When the display flags indicate drop shadow style, this atom can be used to override the default drop shadow placement. The data consists of two 16-bit integers. The first indicates the horizontal displacement of the drop shadow, in pixels; the second, the vertical displacement. |
| `'drpt'` | Drop shadow transparency. The data is a 16-bit integer between 0 and 256 indicating the degree of transparency of the drop shadow. A value of 256 makes the drop shadow completely opaque. |
| `'imag'` | Image font data. This atom contains two more atoms. An `'idat'` atom contains compressed image data to be used to draw the text when the required fonts are not available. An `'idsc'` atom contains a video sample description describing the format of the compressed image data. |
| `'metr'` | Image font highlighting. This atom contains metric information that governs highlighting when an `'imag'` atom is used for drawing. |

### Hypertext and Wired Text

Hypertext is used as an action that takes you to a Web URL; like a Web URL, it appears blue and underlined. Hypertext is stored in a text track sample atom stream as type `'htxt'`. The same mechanism is used to store wired actions linked to text strings. A text string can be wired to act as a hypertext link when clicked or to perform any defined QuickTime wired action when clicked. For details on wired actions, see [Wired Action Grammar](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtknzxhaza).

The data stored is a `QTAtomContainer`. The root atom of hypertext in this container is a wired-text atom of type `'wtxt'`. This is the parent for all individual hypertext objects.

For each hypertext item, the parent atom is of type `'htxt'`. This is the atom container atom type. Two children of this atom that define the offset of the hypertext in the text stream are:

```
kRangeStart         strt // unsigned long
kRangeEnd           end  // unsigned long
```

Child atoms of the parent atom are the events of type `kQTEventType` and the ID of the event type. The children of these event atoms follow the same format as other wired events.

```

kQTEventType, (kQTEventMouseClick, kQTEventMouseClickEnd,
                    kQTEventMouseClickEndTriggerButton,
                    kQTEventMouseEnter, kQTEventMouseExit)
...
kTextWiredObjectsAtomType, 1
    kHyperTextItemAtomType, 1..n
         kRangeStart, 1
            long
        kRangeEnd, 1
            long

    kAction     // The known range of track movie sprite actions
```

## Closed Captioning Media

A closed caption media track contains text data used for closed captioning in QuickTime movies. It has a media type of `'clcp'`. Closed captions are used to display the audio portions of a movie as text. They transcribe dialog and indicate other sounds.

Other tracks can identify this track as being a related closed captioning track by using the `'clcp'` track reference to refer to this track.

Like other media data tracks, a closed caption track should include a language code and an extended language tag atom.

### Closed Captioning Sample Description

The closed captioning sample description contains information that defines how to interpret closed captioning media data. This sample description is based on the standard sample description header, as described in [Sample Description Atoms](Movie%20Atoms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgqwtenjwheyq), and adds no additional fields.

The data format field in the sample description must be set to `'c608'` or `'c708'`. A closed caption track must use only one data format.

__Note:__ Closed caption tracks with data formats other than `'c608'` or `'c708'` are not defined by this specification. Unrecognized data formats should be ignored.

### Closed Captioning Sample Data

The format of the closed captioning sample data is a sequence of one or more atoms, one of which must be a 'cdat' atom. Unrecognized atoms should be ignored.

**Size**
: A 32-bit integer that specifies the number of bytes in this closed captioning media data atom.

**Type**
: A 32-bit integer that identifies the atom type; this field must be set to `'cdat'`.

__Note:__ Apple reserves all atom types with lowercase letters and numbers.

**Sample data**
: For a CEA-608 track, the data is an array of one or more byte pairs for data channel 1/field 1 (“CC1”) of a CEA-608 data stream, each byte pair corresponding to a video frame. For details about the content, refer to the specification _CEA-608-E, Line 21 Data Services, April, 2008_.

The durations of closed caption media samples can vary but should not be shorter than the number of byte pairs in the byte pair array. A closed caption media sample duration that is longer than the array length in video frames should treat additional durations as though null (0) byte pair bytes are received.

__Note:__ The carriage of byte pairs for other elements of the source CEA-608-E frame data are not described here. If supported, other atom types and their content will be documented.

For a CEA-708 track, the should be formatted according to the ANSI CEA-708-E specification, August, 2013.

### Including Multiple Closed-Caption Tracks

If a single closed caption track is included, it is recommended that the track be separate from any subtitle tracks in the movie. However, you can also include multiple closed-caption tracks in a movie. If you do, the following rules apply:

- The closed caption tracks must be part of the same alternate group. If the movie also includes subtitle tracks or non-chapter text tracks, those tracks should also be part of this group.
- The closed caption tracks should be tagged with the appropriate language.

## Subtitle Media

Subtitle media is used to store text data used for subtitles in QuickTime movies. It has a media type of `'sbtl'`. Subtitles provide written versions of audio or visual content, such as to offer alternate language translations or to supplement the content. Subtitles differ from closed captions in that subtitles are usually a translation of the sound track into a different language rather than a transcription of the sound track in the same language.

### Subtitle Sample Description

The subtitle sample description contains information that defines how to interpret subtitle media data. This sample description is based on the standard sample description header, as described in [Sample Description Atoms](Movie%20Atoms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgqwtenjwheyq).

__Note:__ Only one sample description is permitted in a `'sbtl'` track.

The data format field in the sample description is currently always set to `'tx3g'`. Unrecognized data formats should be ignored. The text media described here is based on the text box defined in the 3GPP Timed Text specification but provides a different track type and media handler designed specifically for subtitles.

The subtitle media handler adds some of its own fields to the sample description.

**Display flags**
: A 32-bit integer containing flags that describe how the subtitle text should be drawn. The following flags are defined.

**Vertical placement**
: Controls vertical placement of the subtitle text. If this flag is set, the subtitle media handler uses the top coordinate of the display bounds of the override `'tbox'` text box to determine the subtitle’s vertical placement as described in [Subtitle Track Header Size and Placement](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzygq). Otherwise, the subtitle displays at the bottom of the video. This flag’s value is 0x20000000.

**Some samples are forced**
: Indicates whether any subtitle samples contain forced atoms. If this flag is set, at least one sample contains a forced (`'frcd'`) atom as described in [Subtitle Sample Data](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzygi). This flag’s value is 0x40000000.

**All samples are forced**
: If this flag is set, the subtitle media handler treats all samples as forced subtitles, regardless of the presence or absence of a `'frcd'` atom. This flag’s value is 0x80000000. If this flag is set, the Some Samples Are Forced flag must also be set (making 0xC0000000).

**Reserved**
: An 8-bit integer that must be set to 1.

**Reserved**
: An 8-bit integer that must be set to -1 (negative one).

**Reserved**
: A 32-bit integer that must be set to 0.

**Default text box**
: A 64-bit rectangle that specifies an area to receive text (each 16 bits indicate top, left, bottom, and right, respectively) within the subtitle track. This rectangle must fill the track header dimensions exactly; that is, top is 0, left is 0, bottom is the height of the subtitle track header, and right is the width of the subtitle track header. See [Subtitle Track Header Size and Placement](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzygq).

**Reserved**
: A 32-bit value that must be set to 0.

**Font identifier**
: A 16-bit value that must be set to the same font identifier as in the font table (`'ftab'` extension).

**Font face**
: An 8-bit integer that indicates the font’s style. Set this field to 0 for normal text. You can enable other style options by using one or more of the bit masks listed in [Table 4-11](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzzgq).

__Table 4-11__  Font face values

| Value | Meaning |
| 0x0001 | Bold |
| 0x0002 | Italic |
| 0x0004 | Underline |

**Font size**
: An 8-bit value that should always be 0.05 multiplied by the video track header height. For example, if the video track header is 720 points in height, this should be 36 (points). This size should be used in the default style record and in any per-sample style records. If a subtitle does not fit in the text box, the subtitle media handler may choose to shrink the font size so that the subtitle fits.

**Foreground color**
: A 32-bit RGBA color that specifies the text’s color, 8 bits each for red, green, blue, and alpha (transparency). For example, this would be (0,0,0,255) for opaque black or (255,255,255,255) for opaque white. Dark colors are not recommended, as the text could be placed onto a dark background.

**Font table**
: An atom of type `'ftab'` that identifies the font to use to display the text. See [Font Table Atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzygy).

### Font Table Atom

This atom specifies the font used to display the subtitle.

**Size**
: An unsigned 32-bit integer holding the size of the font table atom.

**Type**
: An unsigned 32-bit field containing the four-character code `'ftab'`.

**Count**
: An unsigned 16-bit integer specifying how many fonts are described in this table. This must be 1.

**Font identifier**
: An unsigned 16-bit integer that identifies the font. This can be any number to uniquely identify this font in this table, but it must match the font number specified in the subtitle sample description and in any per-sample style records (`'styl'`).

**Font name length**
: An unsigned 8-bit integer specifying the length of the font name in bytes.

**Font name**
: Must be either “Serif” or “Sans-Serif”.

### Subtitle Sample Data

Subtitle sample data consists of a 16-bit word that specifies the length (number of bytes) of the subtitle text, followed by the subtitle text and then by optional sample extensions. The subtitle text is Unicode text, encoded either as UTF-8 text or UTF-16 text beginning with a UTF-16 BYTE ORDER MARK ('\uFEFF') in big or little endian order. There is no null termination for the text.

Following the subtitle text, there may be one or more atoms containing additional information for selecting and drawing the subtitle.

[Table 4-12](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzygm) lists the currently defined subtitle sample extensions.

__Table 4-12__  Subtitle sample extensions

| Subtitle sample extension | Description |
| `'frcd'` | The presence of this atom indicates that the sample contains a forced subtitle. This extension has no data.  Forced subtitles are shown automatically when appropriate without any interaction from the user. If any sample contains a forced subtitle, the Some Samples Are Forced (0x40000000) flag must also be set in the display flags.  Consider an example where the primary language of the content is English, but the user has chosen to listen to a French dub of the audio. If a scene in the video displays something in English that is important to the plot or the content (such as a newspaper headline), a forced subtitle displays the content translated into French. In this case, the subtitle is linked (“forced”) to the French language sound track.  If this atom is not present, the subtitle is typically simply a translation of the audio content, which a user can choose to display or hide. |
| `'styl'` | Style information for the subtitle. This atom allows you to override the default style in the sample description or to define more than one style within a sample. See [Subtitle Style Atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzzgm). |
| `'tbox'` | Override of the default text box for this sample. Used only if the 0x20000000 display flag is set in the sample description and, in that case, only the top is considered. Even so, all fields should be set as though they are considered. See [Text Box atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzzgu). |
| `'twrp'` | Text wrap. Set the one-byte payload to 0x00 for no wrapping or 0x01 for automatic soft wrapping. |

### Subtitle Style Atom

This extension specifies changes to the appearance of a subtitle. The style information in the subtitle sample description provides the default style for the subtitle text. This extension allows you to override the default style for different parts, or all, of the subtitle text.

**Size**
: An unsigned 32-bit integer holding the size of the subtitle style atom.

**Type**
: An unsigned 32-bit field containing the four-character code `'styl'`.

**Entry count**
: An unsigned 16-bit integer specifying how many subtitle text style records follow this entry count.

**Subtitle text style record**
: One or more records that provide details about the subtitle’s style. One record consists of the following fields.

**Start character**
: A 16-bit value that is the offset of the first character that is to use the style specified in this record. Zero (0) is the first character in the subtitle.

**End character**
: A 16-bit value that is the offset of the character that follows the last character to use this style.

**Font identifier**
: A 16-bit value that must be set to the same font identifier as in the font table (`'ftab'` extension).

**Font face**
: An 8-bit integer that indicates the font’s style. Set this field to 0 for normal text. You can enable other style options by using one or more of the bit masks listed in Text.

**Font size**
: An 8-bit value that specifies the font’s size. See [Subtitle Sample Description](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzyga) for more information.

**Foreground color**
: A 32-bit RGBA color that specifies the text’s color. See [Subtitle Sample Description](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzyga) for more information.

### Text Box atom

This optional extension defines a text box for a subtitle sample, to be used as described in [Table 4-12](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzygm). If present, this overrides the default text box in the associated sample description. If the subtitle sample description’s Display flags do not include the Vertical Placement flag (0x20000000), the Text Box atom should not be included in any sample of the subtitle track.

**Size**
: An unsigned 32-bit integer holding the size of the subtitle style atom.

**Type**
: An unsigned 32-bit field containing the four-character code `'tbox'`.

**Text box**
: A 64-bit rectangle that specifies an area to receive text (each 16 bits indicate top, left, bottom, and right, respectively) within the subtitle track. This rectangle must fill the track width dimensions exactly. The top and bottom coordinates can vary because they are used to place and size the subtitle text vertically. The top is used to place the text; the height is determined by the bottom minus the top. Neither the top nor the bottom should be outside the subtitle track dimensions. See [Subtitle Track Header Size and Placement](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzygq).

### Subtitle Track Header Size and Placement

Individual subtitles can be placed only within the subtitle track’s dimensions, adjusted by the subtitle track’s matrix. This is expressed relative to the main video track, allowing subtitles to overlay the video. Typically, all subtitles are placed at the bottom of the video. Alternatively, subtitles can be placed at a different vertical location, which allows individual subtitles at the bottom or the top of the associated video. This section describes how this is controlled and how track and subtitle geometry is established.

The value of the track dimensions and track matrix differ depending upon the absence or presence of the Vertical Placement (0x20000000) flag in the subtitle sample description’s display flags. When Vertical Placement is not set, subtitles are always placed at the bottom of the video. When Vertical Placement is set, the vertical position of subtitles can vary based upon the Text Box atom (`'tbox'`) in each sample.

In both cases, the subtitle track width must be the same as that of its associated main video (`'vide'`) track.

If the the Vertical Placement flag (0x20000000) display flag of the sample description is not set, the following should be true:

- The subtitle track’s height should be 0.15 \* the `'vide'` track header height. This allows room for two lines of subtitle text. For example, if the `'vide'` track header height is 720 pixels, then the `'sbtl`' track header height should be 108 (pixels).
- The subtitle track’s vertical placement is determined by the track matrix, which should be a simple vertical translation matrix that shifts the subtitle down by 0.85 \* the `'vide'` track header height. For a subtitle media handler that obeys the tx3g rules, this positions the subtitles atop the bottom 15 percent of the video. Media handlers may choose to shift the subtitles further down in some modes; for example, in a playback mode that displays black bars above and below content, the video could be shifted up and the subtitles moved down into the black area.
- Subtitle samples must not contain a text box sample data extension (`'tbox'`) because no control over vertical placement is allowed.

Alternatively, if the the Vertical Placement flag (0x20000000) display flag of the sample description is set, the following should be true:

- The height of the subtitle track should be the height of the video track header instead of 0.15 \* the video track height. Because the subtitle track dimensions match the video track dimensions, subtitle text can be positioned at the bottom or top of the video, unlike when the Vertical Placement flag is not set.
- The track matrix should be the identity matrix.
- A subtitle’s placement is determined by the top coordinate of one of two rectangles. If the override text box sample data extension ('tbox') is present, it is used. Otherwise, the default text box in the sample description is used. Some players will use the top coordinate to determine whether the subtitle is in the top half of the track dimensions and place the subtitle at the top of the video, otherwise placing it at the bottom of the video. Other players might use the top coordinate precisely, placing the subtitle at the specified vertical coordinate. As both playback environments are possible for a piece of content, it is recommend that a top coordinate of 0 be used for placing at the top and a top coordinate equal to the track height minus the subtitle height be used. In this way, if the content is played in either kind of player, its placement is predictable.

### Referencing a Related Forced Subtitle Track

A subtitle track can contain a track reference of type `'forc'` to a paired subtitle track that contains only forced subtitles.

Pairing two subtitle tracks might be necessary if the timing of forced subtitle samples (see `'frcd'`) differs from the regular subtitle text, such as when a forced subtitle display would overlap in time with the display of the regular subtitle. If timings are the same, a single subtitle track should be used.

To pair two tracks, one subtitle track can contain any combination of forced and non-forced (regular) subtitle samples and the other track must contain only forced subtitles. The tracks must be in the same alternate group and be tagged with the same extended language tag and language code. The first, regular track then uses a track reference of type 'forc' to reference the second, forced-only track. (Mixing extended language tags or codes for the same language in the same alternate group is undefined.)

__Note:__ The regular track in a pair provides a complete transcription of the audio as subtitle text. This allows a user to listen in one language but to read subtitled dialogue in another language.

See [Alternate Subtitle Tracks](Some%20Useful%20Examples%20and%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wvgvzx) and [Track Reference Atoms](Movie%20Atoms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgqwtenjwga2a) for more information.

## Music Media

Music media is used to store note-based audio data, such as MIDI data, in QuickTime movies. It has a media type of `'musi'`.

### Music Sample Description

The music sample description uses the standard sample description header, as described in the section [Sample Description Atoms](Movie%20Atoms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgqwtenjwheyq).

The data format field in the sample description is always set to `'musi'`. The music media handler adds an additional 32-bit integer field to the sample description containing flags. Currently no flags are defined, and this field should be set to 0.

Following the flags field, there may be appended data in the QuickTime music format. This data consists of part-to-instrument mappings in the form of General events containing note requests. One note request event should be present for each part that will be used in the sample data.

### Music Sample Data

The sample data for music samples consists entirely of data in the QuickTime music format. Typically, up to 30 seconds of notes are grouped into a single sample.

## MPEG-1 Media

MPEG-1 media is used to store MPEG-1 video streams, MPEG-1, layer 2 audio streams, and multiplexed MPEG-1 audio and video streams in QuickTime movies. It has a media type of `'MPEG'`.

### MPEG-1 Sample Description

The MPEG-1 sample description uses the standard sample description header, as described in [Sample Description Atoms](Movie%20Atoms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgqwtenjwheyq).

The data format field in the sample description is always set to `'MPEG'`. The MPEG-1 media handler adds no additional fields to the sample description.

__Note:__ This data format is not used for MPEG-1, layer 3 audio, however (see [MPEG-1 Layer 3 (MP3) Codecs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtcmryg4zdk)).

### MPEG-1 Sample Data

Each sample in an MPEG-1 media is an entire MPEG-1 stream. This means that a single MPEG-1 sample may be several hundred megabytes in size. The MPEG-1 encoding used by QuickTime corresponds to the ISO standard, as described in ISO document CD 11172.

## Sprite Media

__Note:__ Sprite media is deprecated in the QuickTime file format. The information that follows is intended to document existing content containing sprite media and should not be used for new development.

Sprite media is used to store character-based animation data in QuickTime movies. It has a media type of `'sprt'`.

### Sprite Sample Description

The sprite sample description uses the standard sample description header, as described in [Sample Description Atoms](Movie%20Atoms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgqwtenjwheyq).

The data format field in the sample description is always set to `'sprt'`. The sprite media handler adds no additional fields to the sample description.

### Sprite Sample Data

All sprite samples are stored in QT atom structures. The sprite media uses both key frames and differenced frames. The key frames contain all of the sprite’s image data, and the initial settings for each of the sprite’s properties.

A key frame always contains a shared data atom of type `'dflt'`. This atom contains data to be shared between the sprites, consisting mainly of image data and sample descriptions. The shared data atom contains a single sprite image container atom, with an atom type value of `'imct'` and an ID value of 1.

The sprite image container atom stores one or more sprite image atoms of type `'imag'`. Each sprite image atom contains an image sample description immediately followed by the sprite’s compressed image data. The sprite image atoms should have ID numbers starting at 1 and counting consecutively upward.

The key frame also must contain definitions for each sprite in atoms of type `'sprt'`. Sprite atoms should have ID numbers start at 1 and count consecutively upward. Each sprite atom contains a list of properties. [Table 4-13](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtqmrzgeyq) shows all currently defined sprite properties.

__Table 4-13__  Sprite properties

| Property name | Value | Description |
| `kSpritePropertyMatrix` | 1 | Describes the sprite’s location and scaling within its sprite world or sprite track. By modifying a sprite’s matrix, you can modify the sprite’s location so that it appears to move in a smooth path on the screen or so that it jumps from one place to another. You can modify a sprite’s size, so that it shrinks, grows, or stretches. Depending on which image compressor is used to create the sprite images, other transformations, such as rotation, may be supported as well. Translation-only matrices provide the best performance. |
| `kSpritePropertyVisible` | 4 | Specifies whether or not the sprite is visible. To make a sprite visible, you set the sprite’s visible property to `true`. |
| `kSpritePropertyLayer` | 5 | Contains a 16-bit integer value specifying the layer into which the sprite is to be drawn. Sprites with lower layer numbers appear in front of sprites with higher layer numbers. To designate a sprite as a background sprite, you should assign it the special layer number `kBackgroundSpriteLayerNum`. |
| `kSpritePropertyGraphicsMode` | 6 | Specifies a graphics mode and blend color that indicates how to blend a sprite with any sprites behind it and with the background. To set a sprite’s graphics mode, you call `SetSpriteProperty`, passing a pointer to a `ModifierTrackGraphicsModeRecord` structure. |
| `kSpritePropertyActionHandlingSpriteID` | 8 | Specifies another sprite by ID that delegates QT events. |
| `kSpritePropertyImageIndex` | 100 | Contains the atom ID of the sprite’s image atom. |

The override sample differs from the key frame sample in two ways. First, the override sample does not contain a shared data atom. All shared data must appear in the key frame. Second, only those sprite properties that change need to be specified. If none of a sprite’s properties change in a given frame, then the sprite does not need an atom in the differenced frame.

The override sample can be used in one of two ways: combined, as with video key frames, to construct the current frame; or the current frame can be derived by combining only the key frame and the current override sample.

Refer to the section [Sprite Track Media Format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtknzuheza) for information on how override samples are indicated in the file, using `kSpriteTrackPropertySampleFormat` and the default behavior of the `kKeyFrameAndSingleOverride` format.

## Sprite Track Properties

__Note:__ Sprite media is deprecated in the QuickTime file format. The information that follows is intended to document existing content containing sprite media and should not be used for new development.

In addition to defining properties for individual sprites, you can also define properties that apply to an entire sprite track. These properties may override default behavior or provide hints to the sprite media handler. The following sprite track properties are supported:

**`kSpriteTrackPropertyBackgroundColor`**
: Specifies a background color for the sprite track. The background color is used for any area that is not covered by regular sprites or background sprites. If you do not specify a background color, the sprite track uses black as the default background color.

**`kSpriteTrackPropertyOffscreenBitDepth`**
: Specifies a preferred bit depth for the sprite track’s offscreen buffer. The allowable values are 8 and 16. To save memory, you should set the value of this property to the minimum depth needed. If you do not specify a bit depth, the sprite track allocates an offscreen buffer with the depth of the deepest intersecting monitor.

**`kSpriteTrackPropertySampleFormat`**
: Specifies the sample format for the sprite track. If you do not specify a sample format, the sprite track uses the default format, `kKeyFrameAndSingleOverride`.

To specify sprite track properties, you create a single QT atom container and add a leaf atom for each property you want to specify. To add the properties to a sprite track, you call the media handler function `SetMediaPropertyAtom`. To retrieve a sprite track’s properties, you call the media handler function `GetMediaPropertyAtom`.

The sprite track properties and their corresponding data types are listed in [Table 4-14](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtqmrzhezq).

__Table 4-14__  Sprite track properties

| Atom type | Atom ID | Leaf data type |
| `kSpriteTrackPropertyBackgroundColor` | 1 | `RGBColor` |
| `kSpriteTrackPropertyOffscreenBitDepth` | 1 | `unsigned short` |
| `kSpriteTrackPropertySampleFormat` | 1 | `long` |
| `kSpriteTrackPropertyHasActions` | 1 | `Boolean` |
| `kSpriteTrackPropertyQTIdleEventsFrequency` | 1 | `UInt32` |
| `kSpriteTrackPropertyVisible` | 1 | `Boolean` |
| `kSpriteTrackPropertyScaleSpritesToScaleWorld` | 1 | `Boolean` |

__Note:__ When pasting portions of two different tracks together, the Movie Toolbox checks to see that all sprite track properties match. If, in fact, they do match, the paste results in a single sprite track instead of two.

## Sprite Track Media Format

__Note:__ Sprite media is deprecated in the QuickTime file format. The information that follows is intended to document existing content containing sprite media and should not be used for new development.

The sprite track media format is hierarchical and based on QT atoms and atom containers. A sprite track is defined by one or more key frame samples, each followed by any number of override samples. A key frame sample and its subsequent override samples define a scene in the sprite track. A key frame sample is a QT atom container that contains atoms defining the sprites in the scene and their initial properties. The override samples are other QT atom containers that contain atoms that modify sprite properties, thereby animating the sprites in the scene. In addition to defining properties for individual sprites, you can also define properties that apply to an entire sprite track.

[Figure 4-15](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtmojtgqyq) shows the high-level structure of a sprite track key frame sample. Each atom in the atom container is represented by its atom type, atom ID, and, if it is a leaf atom, the type of its data.

__Figure 4-15__  A key frame sample atom container

（原归档配图获取待重试：`qtml_03.gif`）

The QT atom container contains one child atom for each sprite in the key frame sample. Each sprite atom has a type of `kSpriteAtomType`. The sprite IDs are numbered from 1 to the number of sprites defined by the key frame sample (`numSprites`).

Each sprite atom contains leaf atoms that define the properties of the sprite, as shown in [Figure 4-16](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtmojtgq2q). For example, the `kSpritePropertyLayer` property defines a sprite’s layer. Each sprite property atom has an atom type that corresponds to the property and an ID of 1.

__Figure 4-16__  Atoms that describe a sprite and its properties

（原归档配图获取待重试：`qtml_11.gif`）

In addition to the sprite atoms, the QT atom container contains one atom of type `kSpriteSharedDataAtomType` with an ID of 1. The atoms contained by the shared data atom describe data that is shared by all sprites. The shared data atom contains one atom of type `kSpriteImagesContainerAtomType` with an ID of 1 ([Figure 4-17](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtmojtgq4q)).

The image container atom contains one atom of type `kImageAtomType` for each image in the key frame sample. The image atom IDs are numbered from 1 to the number of images (`numImages`). Each image atom contains a leaf atom that holds the image data (type `kSpriteImageDataAtomType`) and an optional leaf atom (type `kSpriteNameAtomType`) that holds the name of the image.

__Figure 4-17__  Atoms that describe sprite images

（原归档配图获取待重试：`qtml_17.gif`）

### Sprite Media Format Atoms

The sprite track’s sample format enables you to store the atoms necessary to describe action lists that are executed in response to QuickTime events. [QT Atom Container Description Key](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtknzxgy2q) defines a grammar for constructing valid action sprite samples, which may include complex expressions.

Both key frame samples and override samples support the sprite action atoms. Override samples override actions at the QuickTime event level. In effect, what you do by overriding is to completely replace one event handler and all its actions with another. The sprite track’s `kSpriteTrackPropertySampleFormat` property has no effect on how actions are performed. The behavior is similar to the default `kKeyFrameAndSingleOverride` format where, if in a given override sample there is no handler for the event, the key frame’s handler is used, if there is one.

### Sprite Media Format Extensions

This section describes some of the atom types and IDs used to extend the sprite track’s media format, thus enabling action sprite capabilities.

A complete description of the grammar for sprite media handler samples, including action sprite extensions, is included in the section [Sprite Media Handler Track Properties QT Atom Container Format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtknzxg4ya).

__Important:__
Some sprite track property atoms were added in QuickTime 4. In particular, you must set the `kSpriteTrackPropertyHasActions` track property in order for your sprite actions to be executed.

### Sprite Track Property Atoms

The following constants represent atom types for sprite track properties. These atoms are applied to the whole track, not just to a single sample.

##### Constant Descriptions

**`kSpriteTrackPropertyHasActions`**
: You must add an atom of this type with its leaf data set to `true` if you want the movie controller to execute the actions in your sprite track’s media. The atom’s leaf data is of type `Boolean`. The default value is `false`, so it is very important to add an atom of this type if you want interactivity to take place.

**`kSpriteTrackPropertyQTIdleEventsFrequency`**
: You must add an atom of this type if you want the sprites in your sprite track to receive `kQTEventIdle` QuickTime events. The atom’s leaf data is of type `UInt32`. The value is the minimum number of ticks that must pass before the next `QTIdle` event is sent. Each tick is 1/60th of one second. To specify “Idle as fast as possible,” set the value to 0. The default value is `kNoQTIdleEvents`, which means don’t send any idle events.

It is possible that for small idle event frequencies, the movie will not be able to keep up, in which case idle events will be sent as fast as possible.

Since sending idle events takes up some time, it is best to specify the largest frequency that produces the results that you desire, or `kNoQTIdleEvents` if you do not need them.

**`kSpriteTrackPropertyVisible`**
: You can cause the entire sprite track to be invisible by setting the value of this `Boolean` property to `false`. This is useful for using a sprite track as a hidden button track—for example, placing an invisible sprite track over a video track would allow the characters in the video to be clickable. The default value is visible (`true`).

**`kSpriteTrackPropertyScaleSpritesToScaleWorld`**
: You can cause each sprite to be rescaled when the sprite track is resized by setting the value of this `Boolean` property to `true`. Setting this property can improve the drawing performance and quality of a scaled sprite track. This is particularly useful for sprite images compressed with codecs that are resolution-independent, such as the Curve codec. The default value for this property is `false`.

## Sprite Media Atom and Data Types

The following constants represent atom types for sprite media:

```
enum {
    kSpriteAtomType                     = 'sprt',
    kSpriteImagesContainerAtomType      = 'imct',
    kSpriteImageAtomType                = 'imag',
    kSpriteImageDataAtomType            = 'imda',
    kSpriteImageDataRefAtomType         = 'imre',
    kSpriteImageDataRefTypeAtomType     = 'imrt',
    kSpriteImageGroupIDAtomType         = 'imgr',
    kSpriteImageRegistrationAtomType    = 'imrg',
    kSpriteImageDefaultImageIndexAtomType ='defi',
    kSpriteSharedDataAtomType           = 'dflt',
    kSpriteNameAtomType                 = 'name',
    kSpriteImageNameAtomType            = 'name',
    kSpriteUsesImageIDsAtomType         = 'uses',
    kSpriteBehaviorsAtomType            = 'beha',
    kSpriteImageBehaviorAtomType        = 'imag',
    kSpriteCursorBehaviorAtomType       = 'crsr',
    kSpriteStatusStringsBehaviorAtomType = 'sstr',
    kSpriteVariablesContainerAtomType    = 'vars',
    kSpriteStringVariableAtomType        = 'strv',
    kSpriteFloatingPointVariableAtomType = 'flov'
    kSpriteSharedDataAtomType           = 'dflt',
    kSpriteURLLinkAtomType              = 'url '
    kSpritePropertyMatrix               = 1
    kSpritePropertyVisible              = 4
    kSpritePropertyLayer                = 5
    kSpritePropertyGraphicsMode         = 6
    kSpritePropertyImageIndex           = 100
    kSpritePropertyBackgroundColor      = 101
    kSpritePropertyOffscreenBitDepth    = 102
    kSpritePropertySampleFormat         = 103
};
```

##### Constant Descriptions

**`kSpriteAtomType`**
: The atom is a parent atom that describes a sprite. It contains atoms that describe properties of the sprite. Optionally, it may also include an atom of type `kSpriteNameAtomType` that defines the name of the sprite.

**`kSpriteImagesContainerAtomType`**
: The atom is a parent atom that contains atoms of type `kSpriteImageAtomType`.

**`kSpriteImageAtomType`**
: The atom is a parent atom that contains an atom of type `kSpriteImageDataAtomType`. Optionally, it may also include an atom of type `kSpriteNameAtomType` that defines the name of the image.

**`kSpriteImageDataAtomType`**
: The atom is a leaf atom that contains image data.

**`kSpriteSharedDataAtomType`**
: The atom is a parent atom that contains shared sprite data, such as an atom container of type `kSpriteImagesContainerAtomType`.

**`kSpriteNameAtomType`**
: The atom is a leaf atom that contains the name of a sprite or an image. The leaf data is composed of one or more ASCII characters.

**`kSpritePropertyImageIndex`**
: A leaf atom containing the image index property which is of type `short`. This atom is a child atom of `kSpriteAtom`.

**`kSpritePropertyLayer`**
: A leaf atom containing the layer property which is of type `short`. This atom is a child atom of `kSpriteAtom`.

**`kSpritePropertyMatrix`**
: A leaf atom containing the matrix property which is of type `MatrixRecord`. This atom is a child atom of `kSpriteAtom`.

**`kSpritePropertyVisible`**
: A leaf atom containing the visible property which is of type `short`. This atom is a child atom of `kSpriteAtom`.

**`kSpritePropertyGraphicsMode`**
: A leaf atom containing the graphics mode property which is of type `ModifyerTrackGraphicsModeRecord`. This atom is a child atom of `kSpriteAtom`.

**`kSpritePropertyBackgroundColor`**
: A leaf atom containing the background color property which is of type `RGBColor`. This atom is used in a sprite track’s `MediaPropertyAtom` atom container.

**`kSpritePropertyOffscreenBitDepth`**
: A leaf atom containing the preferred offscreen bit depth which is of type `short`. This atom is used in a sprite track’s `MediaPropertyAtom` atom container.

**`kSpritePropertySampleFormat`**
: A leaf atom containing the sample format property, which is of type `short`. This atom is used in a sprite track’s `MediaPropertyAtom` atom container.

**`kSpriteImageRegistrationAtomType`**
: Sprite images have a default registration point of 0, 0. To specify a different point, add an atom of type `kSpriteImageRegistrationAtomType` as a child atom of the `kSpriteImageAtomType` and set its leaf data to a `FixedPoint` value with the desired registration point.

**`kSpriteImageGroupIDAtomType`**
: You must assign group IDs to sets of equivalent images in your key frame sample. For example, if the sample contains ten images where the first two images are equivalent, and the last eight images are equivalent, then you could assign a group ID of 1000 to the first two images, and a group ID of 1001 to the last eight images. This divides the images in the sample into two sets. The actual ID does not matter, it just needs to be a unique positive integer.

Each image in a sprite media key frame sample is assigned to a group. Add an atom of type `kSpriteImageGroupIDAtomType` as a child of the `kSpriteImageAtomType` atom and set its leaf data to a long containing the group ID.

__Important:__
You must assign group IDs to your sprite sample if you want a sprite to display images with non-equivalent image descriptions (i.e., images with different dimensions).

For each of the following atom types (added to QuickTime 4)—except `kSpriteBehaviorsAtomType`—you fill in the structure `QTSpriteButtonBehaviorStruct`, which contains a value for each of the four states.

**`kSpriteBehaviorsAtomType`**
: This is the parent atom of `kSpriteImageBehaviorAtomType`, `kSpriteCursorBehaviorAtomType`, and `kSpriteStatusStringsBehaviorAtomType`.

**`kSpriteImageBehaviorAtomType`**
: Specifies the `imageIndex`.

**`kSpriteCursorBehaviorAtomType`**
: Specifies the `cursorID`.

**`kSpriteStatusStringsBehaviorAtomType`**
: Specifies an ID of a string variable contained in a sprite track to display in the status area of the browser.

__Note:__ All sprite media—specifically the leaf data in the QT atom containers for sample and sprite track properties—should be written in big-endian format.

**`kSpriteUsesImageIDsAtomType`**
: This atom allows a sprite to specify which images it uses—in other words, the subset of images that its `imageIndex` property can refer to.

You add an atom of type `kSpriteUsesImageIDsAtomType` as a child of a `kSpriteAtomType` atom, setting its leaf data to an array of QT atom IDs. This array contains the IDs of the images used, not the indices.

Although QuickTime does not currently use this atom internally, tools that edit sprite media can use the information provided to optimize certain operations, such as cut, copy, and paste.

**`kSpriteImageRegistrationAtomType`**
: Sprite images have a default registration point of 0, 0. To specify a different point, you add an atom of type `kSpriteImageRegistrationAtomType` as a child atom of the `kSpriteImageAtomType` and set its leaf data to a `FixedPoint` value with the desired registration point.

**`kSpriteImageGroupIDAtomType`**
: You must assign group IDs to sets of equivalent images in your key frame sample. For example, if the sample contains ten images where the first two images are equivalent, and the last eight images are equivalent, then you could assign a group ID of 1000 to the first two images, and a group ID of 1001 to the last eight images. This divides the images in the sample into two sets. The actual ID does not matter; it just needs to be a unique positive integer.

Each image in a sprite media key frame sample is assigned to a group. You add an atom of type `kSpriteImageGroupIDAtomType` as a child of the `kSpriteImageAtomType` atom and set its leaf data to a long containing the group ID.

__Important:__
You must assign group IDs to your sprite sample if you want a sprite to display images with non-equivalent image descriptions (that is, images with different dimensions).

You use the following atom types, which were added to QuickTime 4, to specify that an image is referenced and how to access it.

**`kSpriteImageDataRefAtomType`**
: Add this atom as a child of the `kSpriteImageAtomType` atom instead of a `kSpriteImageDataAtomType`. Its ID should be 1. Its data should contain the data reference (similar to the `dataRef` parameter of `GetDataHandler`).

**`kSpriteImageDataRefTypeAtomType`**
: Add this atom as a child of the `kSpriteImageAtomType` atom. Its ID should be 1. Its data should contain the data reference type (similar to the `dataRefType` parameter of `GetDataHandler`).

**`kSpriteImageDefaultImageIndexAtomType`**
: You may optionally add this atom as a child of the `kSpriteImageAtomType` atom. Its ID should be 1. Its data should contain a `short`, which specifies an image index of a traditional image to use while waiting for the referenced image to load.

The following constants represent formats of a sprite track. The value of the constant indicates how override samples in a sprite track should be interpreted. You set a sprite track’s format by creating a `kSpriteTrackPropertySampleFormat` atom.

```
enum {
    kKeyFrameAndSingleOverride      = 1L << 1,
    kKeyFrameAndAllOverrides        = 1L << 2
};
```

##### Constant Descriptions

**`kKeyFrameAndSingleOverride`**
: The current state of the sprite track is defined by the most recent key frame sample and the current override sample. This is the default format.

**`kKeyFrameAndAllOverrides`**
: The current state of the sprite track is defined by the most recent key frame sample and all subsequent override samples up to and including the current override sample.

## Sprite Button Behaviors

__Note:__ Sprite media is deprecated in the QuickTime file format. The information that follows is intended to document existing content containing sprite media and should not be used for new development.

In QuickTime 4 and later, sprites in a sprite track can specify simple button behaviors. These behaviors can control the sprite’s image, the system cursor, and the status message displayed in a Web browser. They also provide a shortcut for a common set of actions that may result in more efficient QuickTime movies.

Button behaviors can be added to a sprite. These behaviors are intended to make the common task of creating buttons in a sprite track easy—you basically just fill in a template.

Three types of behaviors are available; you may choose one or more behaviors. Each change a type of property associated with a button and are triggered by the mouse states `notOverNotPressed`, `overNotPressed`, `overPressed`, and `notOverPressed`. The three properties changed are:

- The sprite’s `imageIndex`value
- The ID of a cursor to be displayed
- The ID of a status string variable displayed in the URL status area of a Web browser.

Setting a property’s value to –1 means don’t change it.

__Note:__ The cursor is automatically set back to the default system cursor when leaving a sprite.

The sprite track handles letting one sprite act as an active button at a time.

The behaviors are added at the beginning of the sprite’s list of actions, so they may be overridden by actions if desired.

To use the behaviors, you fill in the new atoms as follows, using the description key specified in [QT Atom Container Description Key](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtknzxgy2q):

```
kSpriteAtomType
    <kSpriteBehaviorsAtomType>, 1

        <kSpriteImageBehaviorAtomType>
            [QTSpriteButtonBehaviorStruct]
        <kSpriteCursorBehaviorAtomType>
            [QTSpriteButtonBehaviorStruct]
        <kSpriteStatusStringsBehaviorAtomType>
            [QTSpriteButtonBehaviorStruct]
```

## QT Atom Container Description Key

Because QT atom container–based data structures are widely used in QuickTime, a description key is presented here. Its usage is illustrated in the following sections, [Sprite Media Handler Track Properties QT Atom Container Format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtknzxg4ya) and [Sprite Media Handler Sample QT Atom Container Formats](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtknzxg43a).

```
[(QTAtomFormatName)] =
    atomType_1, id, index
        data
    atomType_n, id, index
        data
```

The atoms may be required or optional:

```
 // optional atom
 // required atom
<atomType>
atomType
```

The atom ID may be a number if it is required to be a constant, or it may be a list of valid atom IDs, indicating that multiple atoms of this type are allowed.

```
3               // one atom with id of 3
(1..3)          // three atoms with id's of 1, 2, and 3
(1, 5, 7)       // three atoms with id's of 1, 5, and 7
(anyUniqueIDs)  // multiple atoms each with a unique id
```

The atom index may be a 1 if only one atom of this type is allowed, or it may be a range from 1 to some constant or variable.

```
1               // one atom of this type is allowed, index is always  1
(1..3)          // three atoms with indexes 1, 2, and 3
(1..numAtoms)   // numAtoms atoms with indexes of 1 to numAtoms
```

The data may be leaf data in which its data type is listed inside of brackets [], or it may be a nested tree of atoms.

```
[theDataType]   // leaf data of type theDataType
childAtoms      // a nested tree of atoms
```

Nested `QTAtom` format definitions [(AtomFormatName)] may appear in a definition.

## Sprite Media Handler Track Properties QT Atom Container Format

__Note:__ Sprite media is deprecated in the QuickTime file format. The information that follows is intended to document existing content containing sprite media and should not be used for new development.

```
[(SpriteTrackProperties)]
    <kSpriteTrackPropertyBackgroundColor, 1, 1>
        [RGBColor]
    <kSpriteTrackPropertyOffscreenBitDepth, 1, 1>
        [short]
    <kSpriteTrackPropertySampleFormat, 1, 1>
        [long]
    <kSpriteTrackPropertyScaleSpritesToScaleWorld, 1, 1>
        [Boolean]
    <kSpriteTrackPropertyHasActions, 1, 1>
        [Boolean]
    <kSpriteTrackPropertyVisible, 1, 1>
        [Boolean]
    <kSpriteTrackPropertyQTIdleEventsFrequency, 1, 1>
        [UInt32]
```

## Sprite Media Handler Sample QT Atom Container Formats

__Note:__ Sprite media is deprecated in the QuickTime file format. The information that follows is intended to document existing content containing sprite media and should not be used for new development.

```
[(SpriteKeySample)] =
    [(SpritePropertyAtoms)]
    [(SpriteImageAtoms)]

[(SpriteOverrideSample)] =
    [(SpritePropertyAtoms)]

[(SpriteImageAtoms)]
    kSpriteSharedDataAtomType, 1, 1
        <kSpriteVariablesContainerAtomType>, 1
            <kSpriteStringVariableAtomType>, (1..n) ID is  SpriteTrack
                            Variable ID to be set
                                                [CString]
            <kSpriteFloatingPointVariableAtomType>, (1..n)  ID is
                            SpriteTrack Variable ID to be set
                                                [float]

        kSpriteImagesContainerAtomType, 1, 1
            kSpriteImageAtomType, theImageID, (1 .. numImages)
                kSpriteImageDataAtomType, 1, 1
                    [ImageData is ImageDescriptionHandle prepended  to
                                                            image  data]
                <kSpriteImageRegistrationAtomType, 1, 1>
                    [FixedPoint]
                <kSpriteImageNameAtomType, 1, 1>
                    [pString]
                <kSpriteImageGroupIDAtomType, 1, 1>
                    [long]

[(SpritePropertyAtoms)]
    <kQTEventFrameLoaded>, 1, 1
        [(ActionListAtoms)]
        <kCommentAtomType>, (anyUniqueIDs), (1..numComments)
            [CString]

    kSpriteAtomType, theSpriteID, (1 .. numSprites)
        <kSpritePropertyMatrix, 1, 1>
            [MatrixRecord]
        <kSpritePropertyVisible, 1, 1>
            [short]
        <kSpritePropertyLayer, 1, 1>
            [short]
        <kSpritePropertyImageIndex, 1, 1>
            [short]
        <kSpritePropertyGraphicsMode, 1, 1>
            [ModifierTrackGraphicsModeRecord]

        <kSpriteUsesImageIDsAtomType, 1, 1>
            [array of QTAtomID's, one per image used]

        <kSpriteBehaviorsAtomType>, 1

        <kSpriteImageBehaviorAtomType>
            [QTSpriteButtonBehaviorStruct]
        <kSpriteCursorBehaviorAtomType>
            [QTSpriteButtonBehaviorStruct]
        <kSpriteStatusStringsBehaviorAtomType>
            [QTSpriteButtonBehaviorStruct]

        <[(SpriteActionAtoms)]>

[(SpriteActionAtoms)] =
    kQTEventType, theQTEventType, (1 .. numEventTypes)
            [(ActionListAtoms)] //see the next section Wired Action
                                //Grammar for a description
            <kCommentAtomType>, (anyUniqueIDs), (1..numComments)
                [CString]
```

## Wired Action Grammar

The wired action grammar shown in this section allows QT event handlers to be expressed in a QuickTime movie. The sprite, text, VR, 3D, and Flash media handlers all support the embedding of QT event handlers in their media samples.

```
[(ActionListAtoms)] =
    kAction, (anyUniqueIDs), (1..numActions)
        kWhichAction    1, 1
            [long whichActionConstant]
        <kActionParameter>  (anyUniqueIDs), (1..numParameters)
            [(parameterData)] ( whichActionConstant, paramIndex  )
    // either leaf data or child atoms
        <kActionFlags>  parameterID,  (1..numParamsWithFlags)
            [long actionFlags]
        <kActionParameterMinValue>  parameterID,  (1.. numParamsWithMin)
            [data depends on param type]
        <kActionParameterMaxValue>  parameterID,  (1.. numParamsWithMax)
            [data depends on param type]
        [(ActionTargetAtoms)]

        <kCommentAtomType>, (anyUniqueIDs), (1..numComments)
            [CString]

[(ActionTargetAtoms)] =
    <kActionTarget>
        <kTargetMovie>
            [no data]
    <kTargetChildMovieTrackName>
        <PString childMovieTrackName>
    <kTargetChildMovieTrack>
        [IDlong childMovieTrackID]
    <kTargetChildMovieTrackIndex>
            [long childMovieTrackIndex]
        <kTargetChildMovieMovieName>
            [PString childMovieName]
        <kTargetChildMovieMovieID>
            [long childMovieID]
        <kTargetTrackName>
            [PString trackName]
        <kTargetTrackType>
            [OSType trackType]
        <kTargetTrackIndex>
            [long trackIndex]
            OR
            [(kExpressionAtoms)]
        <kTargetTrackID>
            [long trackID]
            OR
            [(kExpressionAtoms)]
        <kTargetSpriteName>
            [PString spriteName]
        <kTargetSpriteIndex>
            [short spriteIndex]
            OR
            [(kExpressionAtoms)]
        <kTargetSpriteID>
            [QTAtomID spriteIID]
            OR
            [(kExpressionAtoms)]
        <kTargetQD3DNamedObjectName>
            [CString objectName]

[(kExpressionAtoms)] =
    kExpressionContainerAtomType, 1, 1
        <kOperatorAtomType, theOperatorType, 1>
            kOperandAtomType, (anyUniqueIDs), (1..numOperands)
                [(OperandAtoms)]
        OR
        <kOperandAtomType, 1, 1>
            [(OperandAtoms)]
[(ActionTargetAtoms)] =
    <kActionTarget>

        <kTargetMovieName>
            [Pstring MovieName]
        OR
        <kTargetMovieID>
            [long MovieID]
            OR
            [(kExpressionAtoms)]

[(OperandAtoms)] =
    <kOperandExpression> 1, 1
        [(kExpressionAtoms)]        // allows for recursion
    OR
    <kOperandConstant> 1, 1
        [ float theConstant ]
    OR
    <kOperandSpriteTrackVariable> 1, 1
        [(ActionTargetAtoms)]
        kActionParameter, 1, 1
            [QTAtomID spriteVariableID]
    OR
    <kOperandKeyIsDown> 1, 1
        kActionParameter, 1, 1
            [UInt16 modifierKeys]
        kActionParameter, 2, 2
            [UInt8 asciiCharCode]
    OR
    <kOperandRandom> 1, 1
        kActionParameter, 1, 1
            [short minimum]
        kActionParameter, 2, 2
            [short maximum]
    OR
    <any other operand atom type>
        [(ActionTargetAtoms)]
```

The format for parameter data depends on the action and parameter index.

In most cases, the `kActionParameter` atom is a leaf atom containing data; for a few parameters, it contains child atoms.

`whichAction` corresponds to the action type that is specified by the leaf data of a `kWhichAction` atom.

`paramIndex` is the index of the parameter’s `kActionParameter` atom.

```
[(parameterData)] ( whichAction, paramIndex ) =
{
    kActionMovieSetVolume:
        param1:     short volume

    kActionMovieSetRate
        param1:     Fixed rate

    kActionMovieSetLoopingFlags
        param1:     long loopingFlags

    kActionMovieGoToTime
        param1:     TimeValue time

    kActionMovieGoToTimeByName
        param1:     Str255 timeName

    kActionMovieGoToBeginning
        no params

    kActionMovieGoToEnd
        no params

    kActionMovieStepForward
        no params

    kActionMovieStepBackward
        no params

    kActionMovieSetSelection
        param1:     TimeValue startTime
        param2:     TimeValue endTime

    kActionMovieSetSelectionByName
        param1:     Str255 startTimeName
        param2:     Str255 endTimeName

    kActionMoviePlaySelection
        param1:     Boolean selectionOnly

    kActionMovieSetLanguage
        param1:     long language

    kActionMovieChanged
        no params

    kActionTrackSetVolume
        param1:     short volume

    kActionTrackSetBalance
        param1:     short balance

    kActionTrackSetEnabled
        param1:     Boolean enabled

    kActionTrackSetMatrix
        param1:     MatrixRecord matrix

    kActionTrackSetLayer
        param1:     short layer

    kActionTrackSetClip
        param1:     RgnHandle clip

    kActionSpriteSetMatrix
        param1:     MatrixRecord matrix

    kActionSpriteSetImageIndex
        parm1:      short imageIndex

    kActionSpriteSetVisible
        param1:     short visible

    kActionSpriteSetLayer
        param1:     short layer

    kActionSpriteSetGraphicsMode
        param1:     ModifierTrackGraphicsModeRecord graphicsMode

    kActionSpritePassMouseToCodec
        no params

    kActionSpriteClickOnCodec
        param1:     Point localLoc

    kActionSpriteTranslate
        param1:     Fixed x
        param2:     Fixed y
        param3:     Boolean isRelative

    kActionSpriteScale
        param1:     Fixed xScale
        param2:     Fixed yScale

    kActionSpriteRotate
        param1:     Fixed degrees

    kActionSpriteStretch
        param1:     Fixed p1x
        param2:     Fixed p1y
        param3:     Fixed p2x
        param4:     Fixed p2y
        param5:     Fixed p3x
        param6:     Fixed p3y
        param7:     Fixed p4x
        param8:     Fixed p4y

    kActionQTVRSetPanAngle
        param1:     float panAngle

    kActionQTVRSetTiltAngle
        param1:     float tileAngle

    kActionQTVRSetFieldOfView
        param1:     float fieldOfView

    kActionQTVRShowDefaultView
        no params

    kActionQTVRGoToNodeID
        param1:     UInt32 nodeID

    kActionMusicPlayNote
        param1:     long sampleDescIndex
        param2:     long partNumber
        param3:     long delay
        param4:     long pitch
        param5:     long velocity
        param6:     long duration

    kActionMusicSetController
        param1:     long sampleDescIndex
        param2:     long partNumber
        param3:     long delay
        param4:     long controller
        param5:     long value

    kActionCase
        param1:     [(CaseStatementActionAtoms)]

    kActionWhile
        param1:     [(WhileStatementActionAtoms)]

    kActionGoToURL
        param1:     CString urlLink

    kActionSendQTEventToSprite
        param1:     [(SpriteTargetAtoms)]
        param2:     QTEventRecord theEvent

    kActionDebugStr
        param1:     Str255 theMessageString

    kActionPushCurrentTime
        no params

    kActionPushCurrentTimeWithLabel
        param1:     Str255 theLabel

    kActionPopAndGotoTopTime
        no params

    kActionPopAndGotoLabeledTime
        param1:     Str255 theLabel

    kActionSpriteTrackSetVariable
        param1:     QTAtomID variableID
        param2:     float value

    kActionApplicationNumberAndString
        param1:     long aNumber
        param2:     Str255 aString
}
```

Both [(CaseStatementActionAtoms)] and [(WhileStatementActionAtoms)] are child atoms of a `kActionParameter` `1`, `1` atom.

```
[(CaseStatementActionAtoms)] =
    kConditionalAtomType, (anyUniqueIDs), (1..numCases)
        [(kExpressionAtoms)]
        kActionListAtomType 1, 1
            [(ActionListAtoms)] // may contain nested conditional  actions

[(WhileStatementActionAtoms)] =
    kConditionalAtomType, 1, 1
        [(kExpressionAtoms)]
        kActionListAtomType 1, 1
            [(ActionListAtoms)] // may contain nested conditional  actions
```

## Tween Media

__Note:__ Tween media is deprecated in the QuickTime file format. The information that follows is intended to document existing content containing tween media and should not be used for new development.

Tween media is used to store pairs of values to be interpolated between in QuickTime movies. These interpolated values modify the playback of other media types by using track references and track input maps. For example, a tween media could generate gradually changing volume levels to cause a sound track to fade out. It has a media type of `'twen'`.

Every tween operation is based on a collection of one or more values from which a range of output values can be algorithmically derived. Each tween is assigned a time duration, and an output value can be generated for any time value within the duration. In the simplest kind of tween operation, a pair of values is provided as input and values between the two values are generated as output.

A tween track is a special track in a movie that is used exclusively as a modifier track. The data it contains, known as tween data, is used to generate values that modify the playback of other tracks, usually by interpolating values. The tween media handler sends these values to other media handlers; it never presents data.

### Tween Sample Description

The tween sample description uses the standard sample description header, as described in [Sample Table Atoms](Movie%20Atoms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgqwtenjwha2q).

The data format field in the sample description is always set to `'twen'`. The tween media handler adds no additional fields to the sample description.

### Tween Sample Data

Tween sample data is stored in QT atom structures.

At the root level, there are one or more tween entry atoms; these atoms have an atom type value of `'twen'`. Each tween entry atom completely describes one interpolation operation. These atoms should be consecutively numbered starting at 1, using the atom ID field.

Each tween entry atom contains several more atoms that describe how to perform the interpolation. The atom ID field in each of these atoms must be set to 1.

**Tween start atom (atom type is `'twst'`).**
: This atom specifies the time at which the interpolation is to start. The time is expressed in the media’s time coordinate system. If this atom is not present, the starting offset is assumed to be 0.

**Tween duration atom (atom type is `'twdu'`).**
: This atom specifies how long the interpolation is to last. The time is expressed in the media’s time coordinate system. If this atom is not present, the duration is assumed to be the length of the sample.

**Tween data atom (atom type is `'twdt'`).**
: This atom contains the actual values for the interpolation. The contents depend on the value of the tween type atom.

**Tween type atom (atom type is `'twnt'`).**
: Describes the type of interpolation to perform.

[Table 4-15](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtqnbzg44a) shows all currently defined tween types. All tween types are currently supported using linear interpolation.

__Table 4-15__  Tween type values

| Tween type | Value | Tween data |
| 16-bit integer | 1 | Two 16-bit integers. |
| 32-bit integer | 2 | Two 32-bit integers. |
| 32-bit fixed-point | 3 | Two 32-bit fixed-point numbers. |
| Point: two 16-bit integers | 4 | Two points. |
| Rectangle: four 16-bit integers | 5 | Two rectangles. |
| QuickDraw region | 6 | Two rectangles and a region. The tween entry atom must contain a `'qdrg'` atom with an atom ID value of 1. The region is transformed through the resulting matrices. |
| Matrix | 7 | Two matrices. |
| RGB color: three 16-bit integers | 8 | Two RGB colors. |
| Graphics mode with RGB color | 9 | Two graphics modes with RGB color. Only the RGB color is interpolated. The graphics modes must be the same. |

Each tween type is distinguished from other types by these characteristics:

- Input values or structures of a particular type
- A particular number of input values or structures (most often one or two)
- Output values or structures of a particular type
- A particular algorithm used to derive the output values

Tween operations for each tween type are performed by a tween component that is specific to that type or, for a number of tween types that are native to QuickTime, by QuickTime itself. Movies and applications that use tweening do not need to specify the tween component to use; QuickTime identifies a tween type by its tween type identifier and automatically routes its data to the correct tween component or to QuickTime.

When a movie contains a tween track, the tween media handler invokes the necessary component (or built-in QuickTime code) for tween operations and delivers the results to another media handler. The receiving media handler can then use the values it receives to modify its playback. For example, the data in a tween track can be used to alter the volume of a sound track.

Tweening can also be used outside of movies by applications or other software that can use the values it generates.

### Tween Type Categories

Each of the tween types supported by QuickTime belongs to one of these categories:

- Numeric tween types, which have pairs of numeric values, such as long integers, as input. For these types, linear interpolation is used to generate output values.
- QuickDraw tween types, most of which have pairs of QuickDraw structures, such as points or rectangles, as input. For these types, one or more structure elements are interpolated, such as the `h` and `v` values for points, and each element that is interpolated is interpolated separately from others.
- 3D tween types, which have a QuickDraw 3D structure such as `TQ3Matrix4x4` or `TQ3RotateAboutAxisTransformData` as input. For these types, a specific 3D transformation is performed on the data to generate output.
- The polygon tween type, which takes three four-sided polygons as input. One polygon (such as the bounds for a sprite or track) is transformed, and the two others specify the start and end of the range of polygons into which the tween operation maps it. You can use the output (a `MatrixRecord` data structure) to map the source polygon into any intermediate polygon. The intermediate polygon is interpolated from the start and end polygons for each particular time in the tween duration.
- Path tween types, which have as input a QuickTime vector data stream for a path. Four of the path tween types also have as input a percentage of path’s length; for these types, either a point on the path or a data structure is returned. Two other path tween types treat the path as a function: one returns the `y` value of the point on the path with a given `x` value, and the other returns the `x` value of the point on the path with a given `y` value.
- The list tween type, which has as input a QT atom container that contains leaf atoms of a specified atom type. For this tween type category, the duration of the tween operation is divided by the number of leaf atoms of the specified type. For time points within the first time division, the data for the first leaf atom is returned; for the second time division, the data for the second leaf atom is returned; and so on. The resulting tween operation proceeds in discrete steps (one step for each leaf atom), instead of the relatively continuous tweening produced by other tween type categories.

### Tween QT Atom Container

The characteristics of a tween are specified by the atoms in a tween QT atom container.

A tween QT atom container can contain the atoms described in the following sections.

#### General Tween Atoms

**`kTweenEntry`**
: Specifies a tween atom, which can be either a single tween atom, a tween atom in a tween sequence, or an interpolation tween atom.

Its parent is the tween QT atom container (which you specify with the constant `kParentAtomIsContainer`).

The index of a `kTweenEntry` atom specifies when it was added to the QT atom container`r`; the first added has the index 1, the second 2, and so on. The ID of a `kTweenEntry` atom can be any ID that is unique among the `kTweenEntry` atoms contained in the same QuickTime atom container.

This atom is a parent atom. It must contain the following child atoms:

- A `kTweenType` atom that specifies the tween type.
- One or more `kTweenData` atoms that contain the data for the tween atom. Each `kTweenData` atom can contain different data to be processed by the tween component, and a tween component can process data from only one `kTweenData` atom a time. For example, an application can use a list tween to animate sprites. The `kTweenEntry` atom for the tween atom could contain three sets of animation data, one for moving the sprite from left to right, one for moving the sprite from right to left, and one for moving the sprite from top to bottom. In this case, the `kTweenEntry` atom for the tween atom would contain three `kTweenData` atoms, one for each data set. The application specifies the desired data set by specifying the ID of the `kTweenData` atom to use.

  A `kTweenEntry` atom can contain any of the following optional child atoms:
- A `kTweenStartOffset` atom that specifies a time interval, beginning at the start of the tween media sample, after which the tween operation begins. If this atom is not included, the tween operation begins at the start of the tween media sample.
- A `kTweenDuration` atom that specifies the duration of the tween operation. If this atom is not included, the duration of the tween operation is the duration of the media sample that contains it.

  If a `kTweenEntry` atom specifies a path tween, it can contain the following optional child atom:
- A `kTweenFlags` atom containing flags that control the tween operation. If this atom is not included, no flags are set.

  Note that interpolation tween tracks are tween tracks that modify other tween tracks. The output of an interpolation tween track must be a time value, and the time values generated are used in place of the input time values of the tween track being modified.

  If a `kTweenEntry` atom specifies an interpolation tween track, it must contain the following child atoms:
- A `kTweenInterpolationID` atom for each `kTweenData` atom to be interpolated. The ID of each `kTweenInterpolationID` atom must match the ID of the `kTweenData` atom to be interpolated. The data for a `kTweenInterpolationID` atom specifies a `kTweenEntry` atom that contains the interpolation tween track to use for the `kTweenData` atom.

  If this atom specifies an interpolation tween track, it can contain either of the following optional child atoms:
- A `kTweenOutputMin` atom that specifies the minimum output value of the interpolation tween atom. The value of this atom is used only if there is also a `kTweenOutputMax` atom with the same parent. If this atom is not included and there is a `kTweenOutputMax` atom with the same parent, the tween component uses `0` as the minimum value when scaling output values of the interpolation tween track.
- A `kTweenOutputMax` atom that specifies the maximum output value of the interpolation tween atom. If this atom is not included, the tween component does not scale the output values of the interpolation tween track.

**`kTweenStartOffset`**
: For a tween atom in a tween track of a QuickTime movie, specifies a time offset from the start of the tween media sample to the start of the tween atom. The time units are the units used for the tween track.

Its parent atom is a `kTweenEntry` atom.

A `kTweenEntry` atom can contain only one `kTweenStartOffset` atom. The ID of this atom is always 1. The index of this atom is always 1.

This atom is a leaf atom. The data type of its data is `TimeValue`.

This atom is optional. If it is not included, the tween operation begins at the start of the tween media sample.

**`kTweenDuration`**
: Specifies the duration of a tween operation. When a QuickTime movie includes a tween track, the time units for the duration are those of the tween track. If a tween component is used outside of a movie, the application using the tween data determines how the duration value and values returned by the component are interpreted.

Its parent atom is a `kTweenEntry` atom.

A `kTweenEntry` atom can contain only one `kTweenDuration` atom. The ID of this atom is always 1. The index of this atom is always 1.

This atom is a leaf atom. The data type of its data is `TimeValue`.

This atom is optional. If it is not included, the duration of the tween operation is the duration of the media sample that contains it.

**`kTweenData`**
: Contains data for a tween atom.

Its parent atom is a `kTweenEntry` atom.

A `kTweenEntry` atom can contain any number of `kTweenData` atoms.

The index of a `kTweenData` atom specifies when it was added to the `kTweenEntry` atom; the first added has the index 1, the second 2, and so on. The ID of a `kTweenData` atom can be any ID that is unique among the `kTweenData` atoms contained in the same `kTweenEntry` atom.

At least one `kTweenData` atom is required in a `kTweenEntry` atom.

For single tween atoms, a `kTweenData` atom is a leaf atom. It can contain data of any type.

For polygon tween atoms, a `kTweenData` atom is a leaf atom. The data type of its data is `Fixed[27]`, which specifies three polygons.

For path tweens, a `kTweenData` atom is a leaf atom. The data type of its data is `Handle`, which contains a QuickTime vector.

In interpolation tween atoms, a `kTweenData` atom is a leaf atom. It can contain data of any type. An interpolation tween atom can be any tween atoms other than a list tween atom that returns a time value.

In list tween atoms, a `kTweenData` atom is a parent atom that must contain the following child atoms:

- A `kListElementType` atom that specifies the atom type of the elements of the tween atom.
- One or more leaf atoms of the type specified by the `kListElementType` atom. The data for each atom is the result of a list tween operation.

**`kNameAtom`**
: Specifies the name of a tween atom. The name, which is optional, is not used by tween components, but it can be used by applications or other software.

Its parent atom is a `kTweenEntry` atom.

A `kTweenEntry` atom can contain only one `kNameAtom` atom. The ID of this atom is always 1. The index of this atom is always 1.

This atom is a leaf atom. Its data type is `String`.

This atom is optional. If it is not included, the tween atom does not have a name.

**`kTweenType`**
: Specifies the tween type (the data type of the data for the tween operation).

Its parent atom is a `kTweenEntry` atom.

A `kTweenEntry` atom can contain only one `kTweenType` atom. The ID of this atom is always 1. The index of this atom is always 1.

This atom is a leaf atom. The data type of its data is `OSType`.

This atom is required.

##### Path Tween Atoms

**`kTweenFlags`**
: Contains flags that control the tween operation. One flag that controls path tween atoms is defined:

- The `kTweenReturnDelta` flag applies only to path tween atoms (tweens of type `kTweenTypePathToFixedPoint`, `kTweenTypePathToMatrixTranslation`, `kTweenTypePathToMatrixTranslationAndRotation`, `kTweenTypePathXtoY`, or `kTweenTypePathYtoX`). If the flag is set, the tween component returns the change in value from the last time it was invoked. If the flag is not set, or if the tween component has not previously been invoked, the tween component returns the normal result for the tween atom.

  Its parent atom is a `kTweenEntry` atom.

  A `kTweenEntry` atom can contain only one `kTweenFlags` atom. The ID of this atom is always 1. The index of this atom is always 1.

  This atom is a leaf atom. The data type of its data is `Long`.

  This atom is optional. If it is not included, no flags are set.

**`kInitialRotationAtom`**
: Specifies an initial angle of rotation for a path tween atom of type `kTweenTypePathToMatrixRotation`, `kTweenTypePathToMatrixTranslation`, or `kTweenTypePathToMatrixTranslationAndRotation`.

Its parent atom is a `kTweenEntry` atom.

A `kTweenEntry` atom can contain only one `kInitialRotationAtom` atom. The ID of this atom is always 1. The index of this atom is always 1.

This atom is a leaf atom. Its data type is `Fixed`.

This atom is optional. If it is not included, no initial rotation of the tween atom is performed.

##### List Tween Atoms

**`kListElementType`**
: Specifies the atom type of the elements in a list tween atom.

Its parent atom is a `kTweenData` atom.

A `kTweenEntry` atom can contain only one `kListElementType` atom. The ID of this atom is always 1. The index of this atom is always 1.

This atom is a leaf atom. Its data type is `QTAtomType`.

This atom is required in the `kTweenData` atom for a list tween atom.

##### 3D Tween Atoms

**`kTween3dInitialCondition`**
: Specifies an initial transform for a 3D tween atom whose tween type is one of the following: `kTweenType3dCameraData`, `kTweenType3dMatrix`, `kTweenType3dQuaternion`, `kTweenType3dRotate`, `kTweenType3dRotateAboutAxis`, `kTweenType3dRotateAboutAxis`, `kTweenType3dRotateAboutPoint`, `kTweenType3dRotateAboutVector`, `kTweenType3dScale`, or `kTweenType3dTranslate`.

Its parent atom is a `kTweenEntry` atom.

A `kTweenEntry` atom can contain only one `kTween3dInitialCondition` atom. The ID of this atom is always 1. The index of this atom is always 1.

This atom is a leaf atom. The data type of its data is one of the values listed in [Table 4-16](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzrgayq).

__Table 4-16__  Tween types

| Tween Type | Data Type |
| `kTweenType3dCameraData` | `TQ3CameraData` |
| `kTweenType3dMatrix` | `TQ3Matrix4x4` |
| `kTweenType3dQuaternion` | `TQ3Quaternion` |
| `kTweenType3dRotate` | `TQ3RotateTransformData` |
| `kTweenType3dRotateAboutAxis` | `TQ3RotateAboutAxisTransformData` |
| `kTweenType3dRotateAboutPoint` | `TQ3RotateAboutPointTransformData` |
| `kTweenType3dRotateAboutVector` | `TQ3PlaneEquation` |
| `kTweenType3dScale` | `TQ3Vector3D` |
| `kTweenType3dTranslate` | `TQ3Vector3D` |

This atom is optional. For each tween type, the default value is the data structure that specifies an identity transform, that is, a transform that does not alter the 3D data.

##### Interpolation Tween Atoms

**`kTweenOutputMax`**
: Specifies the maximum output value of an interpolation tween atom. If a `kTweenOutputMax` atom is included for an interpolation tween, output values for the tween atom are scaled to be within the minimum and maximum values. The minimum value is either the value of the `kTweenOutputMin` atom or, if there is no `kTweenOutputMin` atom, 0. For example, if an interpolation tween atom has values between 0 and 4, and it has `kTweenOutputMin` and `kTweenOutputMax` atoms with values 1 and 2, respectively, a value of 0 (the minimum value before scaling) is scaled to 1 (the minimum specified by the `kTweenOutputMin` atom), a value of 4 (the maximum value before scaling) is scaled to 2 (the maximum specified by the `kTweenOutputMax` atom), and a value of 3 (three-quarters of the way between the maximum and minimum values before scaling) is scaled to 1.75 (three-quarters of the way between the values of the `kTweenOutputMin` and `kTweenOutputMax` atoms).

Its parent atom is a `kTweenEntry` atom.

A `kTweenEntry` atom can contain only one `kTweenOutputMax` atom. The ID of this atom is always 1. The index of this atom is always 1.

This atom is a leaf atom. The data type of its data is `Fixed`.

This atom is optional. If it is not included, QuickTime does not scale interpolation tween values.

**`kTweenOutputMin`**
: Specifies the minimum output value of an interpolation tween atom. If both `kTweenOutputMin` and `kTweenOutputMax` atoms are included for an interpolation tween atom, output values for the tween atom are scaled to be within the minimum and maximum values. For example, if an interpolation tween atom has values between 0 and 4, and it has `kTweenOutputMin` and `kTweenOutputMax` atoms with values 1 and 2, respectively, a value of 0 (the minimum value before scaling) is scaled to 1 (the minimum specified by the `kTweenOutputMin` atom), a value of 4 (the maximum value before scaling) is scaled to 2 (the maximum specified by the `kTweenOutputMax` atom), and a value of 3 (three-quarters of the way between the maximum and minimum values before scaling) is scaled to 1.75 (three-quarters of the way between the values of the `kTweenOutputMin` and `kTweenOutputMax` atoms).

If a `kTweenOutputMin` atom is included but a `kTweenOutputMax` atom is not, QuickTime does not scale interpolation tween values.

Its parent atom is a `kTweenEntry` atom.

A `kTweenEntry` atom can contain only one `kTweenOutputMin` atom. The ID of this atom is always 1. The index of this atom is always 1.

This atom is a leaf atom. The data type of its data is `Fixed`.

This atom is optional. If it is not included but a `kTweenOutputMax` atom is, the tween component uses `0` as the minimum value for scaling values of an interpolation tween atom.

**`kTweenInterpolationID`**
: Specifies an interpolation tween atom to use for a specified `kTweenData` atom. There can be any number of `kTweenInterpolationID` atoms for a tween atom, one for each `kTweenData` atom to be interpolated.

Its parent atom is a `kTweenEntry` atom.

The index of a `kTweenInterpolationID` atom specifies when it was added to the `kTweenEntry` atom; the first added has the index 1, the second 2, and so on. The ID of a `kTweenInterpolationID` atom must match the atom ID of the `kTweenData` atom to be interpolated, and be unique among the `kTweenInterpolationID` atoms contained in the same `kTweenEntry` atom.

This atom is a leaf atom. The data type of its data is `QTAtomID`.

This atom is required for an interpolation tween atom.

##### Region Tween Atoms

**`kTweenPictureData`**
: Contains the data for a QuickDraw picture. Used only by a `kTweenTypeQDRegion` atom.

Its parent atom is a `kTweenEntry` atom.

A `kTweenEntry` atom can contain only one `kTweenPictureData` or `kTweenRegionData` atom. The ID of this atom is always 1. The index of this atom is always 1.

This atom is a leaf atom. The data type of its data is `Picture`.

Either a `kTweenPictureData` or `kTweenRegionData` atom is required for a kTweenTypeQDRegion atom.

**`kTweenRegionData`**
: Contains the data for a QuickDraw region. Used only by a `kTweenTypeQDRegion` atom.

Its parent atom is a `kTweenEntry` atom.

A `kTweenEntry` atom can contain only one `kTweenRegionData` or `kTweenPictureData` atom. The ID of this atom is always 1. The index of this atom is always 1.

This atom is a leaf atom. The data type of its data is `Region`.

Either a `kTweenPictureData` or `kTweenRegionData` atom is required for a `kTweenTypeQDRegion` tween.

##### Sequence Tween Atoms

**`kTweenSequenceElement`**
: Specifies an entry in a tween sequence.

Its parent is the tween QT atom container (which you specify with the constant `kParentAtomIsContainer`).

The ID of a `kTweenSequenceElement` atom must be unique among the `kTweenSequenceElement` atoms in the same QT atom container. The index of a `kTweenSequenceElement` atom specifies its order in the sequence; the first entry in the sequence has the index 1, the second 2, and so on.

This atom is a leaf atom. The data type of its data is `TweenSequenceEntryRecord`, a data structure that contains the following fields:

**`endPercent`**
: A value of type `Fixed` that specifies the point in the duration of the tween media sample at which the sequence entry ends. This is expressed as a percentage; for example, if the value is 75.0, the sequence entry ends after three-quarters of the total duration of the tween media sample have elapsed. The sequence entry begins after the end of the previous sequence entry or, for the first entry in the sequence, at the beginning of the tween media sample.

**`tweenAtomID`**
: A value of type `QTAtomID` that specifies the `kTweenEntry` atom containing the tween for the sequence element. The `kTweenEntry` atom and the `kTweenSequenceElement` atom must both be a child atoms of the same tween QT atom container.

**`dataAtomID`**
: A value of type `QTAtomID` that specifies the `kTweenData` atom containing the data for the tween. This atom must be a child atom of the atom specified by the `tweenAtomID` field.

## Modifier Tracks

The addition of modifier tracks in QuickTime 2.1 introduced the capability for creating dynamic movies. (A modifier track sends data to another track; by comparison, a track reference is an association.) For example, instead of playing video in a normal way, a video track could send its image data to a sprite track. The sprite track then could use that video data to replace the image of one of its sprites. When the movie is played, the video track appears as a sprite.

Modifier tracks are not a new type of track. Instead, they are a new way of using the data in existing tracks. A modifier track does not present its data, but sends it to another track that uses the data to modify how it presents its own data. Any track can be either a sender or a presenter, but not both. Previously, all tracks were presenters.

Another use of modifier tracks is to store a series of sound volume levels, which is what occurs when you work with a tween track. These sound levels can be sent to a sound track as it plays to dynamically adjust the volume. A similar use of modifier tracks is to store location and size information. This data can be sent to a video track to cause it to move and resize as it plays.

Because a modifier track can send its data to more than one track, you can easily synchronize actions between multiple tracks. For example, a single modifier track containing matrices as its samples can make two separate video tracks follow the same path.

See [Creating Movies with Modifier Tracks](Some%20Useful%20Examples%20and%20Scenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqg4wtcojsha2q) for more information about using modifier tracks.

### Limitations of Spatial Modifier Tracks

A modifier track may cause a track to move outside of its original boundary regions. This may present problems, since applications do not expect the dimensions or location of a QuickTime movie to change over time.

To ensure that a movie maintains a constant location and size, the Movie Toolbox limits the area in which a spatially modified track can be displayed. A movie’s “natural” shape is defined by the region returned by the `GetMovieBoundsRgn` function. The toolbox clips all spatially modified tracks against the region returned by `GetMovieBoundsRgn`.
This means that a track can move outside of its initial boundary regions, but it cannot move beyond the combined initial boundary regions of all tracks in the movie. Areas uncovered by a moving track are handled by the toolbox in the same way as areas uncovered by tracks with empty edits.

If a track has to move through a larger area than that defined by the movie’s boundary region, the movie’s boundary region can be enlarged to any desired size by creating a spatial track (such as a video track) of the desired size but with no data. As long as the track is enabled, it contributes to the boundary regions of the movie.

## Track References

Although QuickTime has always allowed the creation of movies that contain more than one track, it has not been able to specify relationships between those tracks. Track references are a feature of QuickTime that allows you to relate a movie’s tracks to one another. The QuickTime track-reference mechanism supports many-to-many relationships. That is, any movie track may contain one or more track references, and any track may be related to one or more other tracks in the movie.

Track references can be useful in a variety of ways. For example, track references can be used to relate timecode tracks to other movie tracks. You can use track references to identify relationships between video and sound tracks such as identifying the track that contains dialog and the track that contains background sounds. Another use of track references is to associate one or more text tracks that contain subtitles with the appropriate sound track or tracks.

Track references are also used to create chapter lists, as described in [Chapter Lists](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtknzygyzq).

Every movie track contains a list of its track references. Each track reference identifies another related track. That related track is identified by its track identifier. The track reference itself contains information that allows you to classify the references by type. This type information is stored in an `OSType` data type. You are free to specify any type value you want. Note, however, that Apple has reserved all lowercase type values.

You may create as many track references as you want, and you may create more than one reference of a given type. Each track reference of a given type is assigned an index value. The index values start at 1 for each different reference type. The Movie Toolbox maintains these index values, so that they always start at 1 and count by 1.

Using the `AddTrackReference` function, you can relate one track to another. The `DeleteTrackReference` function will remove that relationship. The `SetTrackReference` and `GetTrackReference` functions allow you to modify an existing track reference so that it identifies a different track. The `GetNextTrackReferenceType` and `GetTrackReferenceCount` functions allow you to scan all of a track’s track references.

For a list of track reference types, see [Track Reference Atoms](Movie%20Atoms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgqwtenjwga2a).

## Chapter Lists

A chapter list provides a set of named entry points into a movie, allowing the user to jump to a preselected point in the movie from a convenient pop-up list.

The movie controller automatically recognizes a chapter list and will create a pop-up list from it. When the user makes a selection from the pop-up, the controller will jump to the appropriate point in the movie. Note that if the movie is sized so that the controller is too narrow to display the chapter names, the pop-up list will not appear.

To create a chapter list, you must create a text track with one sample for each chapter. The display time for each sample corresponds to the point in the movie that marks the beginning of that chapter. You must also create a track reference of type `'chap'` from an enabled track of the movie to the text track. It is the `'chap'` track reference that makes the text track into a chapter list. The track containing the reference can be of any type (audio, video, MPEG, and so on), but it must be enabled for the chapter list to be recognized.

Given an enabled track `myVideoTrack`, for example, you can use the `AddTrackReference` function to create the chapter reference:

```
    AddTrackReference( myVideoTrack, theTextTrack,
        kTrackReferenceChapterList,
        &addedIndex );
```

`kTrackReferenceChapterList` is defined in `Movies.h`. It has the value `'chap'`.

The text track that constitutes the chapter list does not need to be enabled, and normally is not. If it is enabled, the text track will be displayed as part of the movie, just like any other text track, in addition to functioning as a chapter list.

If more than one enabled track includes a `'chap'` track reference, QuickTime uses the first chapter list that it finds.

## 3D Media

__Note:__ 3D Media is deprecated in the QuickTime file format. The information that follows is intended to document existing content containing 3D media and should not be used for new development.

QuickTime movies store 3D image data in a base media. This media has a media type of `'qd3d'`.

### 3D Sample Description

The 3D sample description uses the standard sample description header, as described in [Sample Table Atoms](Movie%20Atoms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgqwtenjwha2q).

The data format field in the sample description is always set to `'qd3d'`. The 3D media handler adds no additional fields to the sample description.

### 3D Sample Data

The 3D samples are stored in the 3D Metafile format developed for QuickDraw 3D.

## Streaming Media

QuickTime movies store streaming data in a streaming media track. This media has a media type of `'strm'`.

### Streaming Media Sample Description

The streaming media sample description contains information that defines how to interpret streaming media data. This sample description is based on the standard sample description header, as described in [Sample Table Atoms](Movie%20Atoms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgqwtenjwha2q).

The streaming media sample description is documented in the QuickTime header file `QTSMovie.h`, as shown in [Listing 4-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtqnjrga3q).

__Listing 4-1__  Streaming media sample description

```swift
struct QTSSampleDescription {
    long                            descSize;
    long                            dataFormat;
    long                            resvd1;     /* set to 0*/
    short                           resvd2;     /* set to 0*/
    short                           dataRefIndex;
    UInt32                          version;
    UInt32                          resvd3;     /* set to 0*/
    SInt32                          flags;
                                                /* qt atoms follow:*/
                                    /* long size, long type, some  data*/
                                                /* repeat as necessary*/
};
typedef struct QTSSampleDescription     QTSSampleDescription;
```

The sample format depends on the `dataFormat` field of the `QTSSampleDescription`. The `dataFormat` field can be any value you specify. The currently defined values are `'rtsp'` and `'sdp '`.

If `'rtsp'`, the sample can be just an rtsp URL. It can also be any value that you can put in a `.rtsp` file, as defined at

`http://streaming.apple.com/qtstreaming/documentation/userdocs/rtsptags.htm`

If `'sdp '`, then the sample is an SDP file. This would be used to receive a multicast broadcast.

## Hint Media

The QuickTime file format supports streaming of media data over a network as well as local playback. The process of sending protocol data units is time-based, just like the display of time-based data, and is therefore suitably described by a time-based format. A QuickTime file or movie that supports streaming includes information about the data units to stream. This information is included in additional tracks of the movie called hint tracks.

Hint tracks contain instructions for a streaming server which assist in the formation of packets. These instructions may contain immediate data for the server to send (for example, header information) or reference segments of the media data. These instructions are encoded in the QuickTime file in the same way that editing or presentation information is encoded in a QuickTime file for local playback.

Instead of editing or presentation information, information is provided which allows a server to packetize the media data in a manner suitable for streaming, using a specific network transport.

The same media data is used in a QuickTime file which contains hints, whether it is for local playback, or streaming over a number of different transport types. Separate hint tracks for different transport types may be included within the same file and the media will play over all such transport types without making any additional copies of the media itself. In addition, existing media can be easily made streamable by the addition of appropriate hint tracks for specific transports. The media data itself need not be recast or reformatted in any way.

Typically, hinting is performed by media packetizer components. QuickTime selects an appropriate media packetizer for each track and routes each packetizer's output through an Apple-provided packet builder to create a hint track. One hint track is created for each streamable track in the movie.

Hint tracks are quite small compared with audio or video tracks. A movie that contains hint tracks can be played from a local disk or streamed over HTTP, similar to any other QuickTime movie. Hint tracks are only used when streaming a movie over a real-time media streaming protocol, such as RTP.

Support for streaming in the QuickTime file format is based upon the following considerations:

- Media data represented as a set of network-independent standard QuickTime tracks, which may be played or edited, as normal.
- A common declaration and base structure for server hint tracks; this common format is protocol independent, but contains the declarations of which protocols are described in the server tracks.
- A specific design of the server hint tracks for each protocol which may be transmitted; all these designs use the same basic structure.

The resulting streams, sent by the servers under the direction of hint tracks, do not need to contain any trace of QuickTime information. This approach does not require that QuickTime, or its structures or declaration style, be used either in the data on the wire or in the decoding station. For example, a QuickTime file using H.261 video and DVI audio, streamed under Real-Time Protocol (RTP), results in a packet stream which is fully compliant with the IETF specifications for packing those codings into RTP.

Hint tracks are built and flagged, so that when the movie is viewed directly (not streamed), they are ignored.

The next section describes a generic format for streaming hints to be stored in a QuickTime movie.

### Adding Hint Tracks to a Movie

To store packetization hints, one or more hint tracks are added to a movie. Each hint track contains hints for at least one actual media track to be streamed. A streamed media track may have more than one hint track. For example, it might have a separate hint track for the different packet sizes the server supports, or it might have different hint tracks for different protocols. It is not required that all media tracks have corresponding hint tracks in a movie.

The sample time of a hint sample corresponds to the sample time of the media contained in the packets generated by that hint sample. The hint sample may also contain a transmission time for each packet. (The format for the hint sample is specific to the hint track type.)

The hint track may have a different time scale than its referenced media tracks.

The `flags` field in the track header atom (`'tkhd'`) must be set to 0x000000, indicating that the track is inactive and is not part of the movie, preview, or poster.

The `subType` field of the handler description atom (`'hdlr'`) contains `'hint'`, indicating that the media type is packetization hints.

Note that if a QuickTime media track is edited, any previously stored packetization hints may become invalid. Comparing the modification dates of the media track and the hint track is one way to determine this scenario, but it is far from being foolproof. Since the hint track keeps track of which original track media samples and sample descriptions to play at specific times, changes that affect those parts of the original track or media make those hints invalid. Changes to a movie that do not invalidate existing hint tracks include flattening (when there are no edit lists), and adding new tracks. Changes that invalidate hint tracks include:

- Flattening (when there are edit lists)
- Adding or deleting samples
- Changing a track’s time scale
- Changing sample descriptions

  __Warning:__
  Hint tracks are marked as inactive, so calling the `FlattenMovie` function with the `flattenActiveTracksOnly` bit set deletes all hint tracks from a movie.

### Packetization Hint Media Header Atom

In QuickTime movies, the media information atom (`'minf'`) contains header data specific to the media. For hint tracks, the media header is a base media information atom (`'gmhd'`). The hint track must contain the base media information atom.

### Hint Track User Data Atom

Each hint track may contain track user data atoms that apply to only to the corresponding hint track. There are currently two such atoms defined.

- User data atom type `'hinf'`.

This contains statistics for the hint track. The `'hinf'` atom contains child atoms as defined in [Table 4-17](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtqnjtgqza). In some cases, there are both 32-bit and 64-bit counters available. Any unknown types should be ignored.

- User data atom type `'hnti'`.

This may contain child atoms. Child atoms that start with `'sdp '` (note, again, the space) contain SDP text for this track. Text from these child atoms must be inserted into the proper place in the SDP text for the movie, after any common SDP text. This is analogous to the movie-level `'hnti'` atom.

### Movie Hint Info Atom

A movie may contain an `'hnti'` movie user data atom, which may contain one or more child atoms. The child atom contents start with 4 bytes that specify the transport and 4 bytes that specify the type of data contained in the rest of the child atom. Currently, the only defined transport is `'rtp '` (note the space) and the only content data type defined is `'sdp '` (note the space). Child atoms whose transport or type combinations you don’t recognize should be skipped.

The text in an atom of type `'rtp sdp '` should be inserted (in the proper place) into the SDP information generated from this file (for example, by a streaming server) before any SDP information for specific tracks.

[Table 4-17](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtqnjtgqza) describes the type and values of the `'hnti'` atom.

__Table 4-17__  The `'hinf'` atom type containing child atoms

| Type | Value | Description |
| `'trpY´` | 8 bytes | The total number of bytes that will be sent, including 12-byte RTP headers, but not including any network headers. |
| `'totl'` | 4 bytes | 4-byte version of `'trpY´` |
| `'nump'` | 8 bytes | The total number of network packets that will be sent (if the application knows there is a 28-byte network header, it can multiply 28 by this number and add it to the `'trpY´` value to get the true number of bytes sent. |
| `'npck'` | 4 bytes | 4-byte version of `'nump'` |
| `'tpyl'` | 8 bytes | The total number of bytes that will be sent, not including 12-byte RTP headers. |
| `'tpaY´` | 4 bytes | 4-byte version of `'tpyl'` |
| `'maxr'` | 8 bytes | The maximum data rate. This atom contains two numbers: g, followed by m (both 32-bit values). g is the granularity, in milliseconds. m is the maximum data rate given that granularity.  For example, if g is 1 second, then m is the maximum data rate over any 1 second. There may be multiple `'maxr'` atoms, with different values for g. The maximum data rate calculation does not include any network headers (but does include 12-byte RTP headers). |
| `'dmed'` | 8 bytes | The number of bytes from the media track to be sent. |
| `'dimm'` | 8 bytes | The number of bytes of immediate data to be sent. |
| `'drep'` | 8 bytes | The number of bytes of repeated data to be sent. |
| `'tmin'` | 4 bytes | The smallest relative transmission time, in milliseconds. |
| `'tmax'` | 4 bytes | The largest relative transmission time, in milliseconds. |
| `'pmax'` | 4 bytes | The largest packet, in bytes; includes 12-byte RTP header. |
| `'dmax'` | 4 bytes | The largest packet duration, in milliseconds. |
| `'payt'` | Variable | The payload type, which includes payload number (32-bits) followed by `rtpmap` payload string (Pascal string). |

__Note:__ Any of the atoms shown in [Table 4-17](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtqnjtgqza) may or may not be present. These atoms are not guaranteed.

## Finding an Original Media Track From a Hint Track

Like any other QuickTime track, hint tracks can contain track reference atoms. Exactly one of these must be of track reference type `'hint'`, and its internal list must contain at least one track ID, which is the track ID of the original media track. Like other track reference atoms, there may be empty references in this list, indicated by a track ID of 0. For hint tracks that refer to more than one track, the index number (starting at 1, and including any 0 entries) is used in the media track reference index field in some of the packet data table entry modes.

For example, if you have MPEG-1 video at track ID 11 and MPEG-1 layer 2 audio at track ID 12, and you are creating a RTP hint track that encapsulates these in an MPEG-2 transport, you need to refer to both tracks. You can also assume that there are some empty entries and other track references in your hint track atom reference atom’s list. So it might look like this: 11, 0, 0, 14, 0, 12, 0. When you are assembling packets from audio and video tracks 11 and 12, you use their list indexes (1 and 6) in the media track ref index field.

If you have only one media track listed in your hint track reference, you may simply use a 0 in the media track ref index field.

## RTP Hint Tracks

RTP hint tracks contain information that allows a streaming server to create RTP streams from a QuickTime movie, without requiring the server to know anything about the media type, compression, or payload format.

In RTP, each media stream, such as an audio or video track, is sent as a separate RTP stream. Consequently, each media track in the movie has an associated RTP hint track containing the data necessary to packetize it for RTP transport, and each hint track contains a track reference back to its associated media track.

Media tracks that do not have an associated RTP hint track cannot be streamed over RTP and should be ignored by RTP streaming servers.

It is possible for a media track to have more than one associated hint track. The hint track contains information such as the packet size and time scale in the hint track’s sample description. This minimizes the runtime server load, but in order to support multiple packet sizes it is necessary to have multiple RTP hint tracks for each media track, each with different a packet size. A similar mechanism could be used to provide hint tracks for multiple protocols in the future.

It is also possible for a single hint track to refer to more than one media stream. For example, audio and video MPEG elementary streams could be multiplexed into a single systems stream RTP payload format, and a single hint track would contain the necessary information to combine both elementary streams into a single series of RTP packets.

This is the exception rather than the rule, however. In general, multiplexing is achieved by using IP’s port-level multiplexing, not by interleaving the data from multiple streams into a single RTP session.

The hint track is related to each base media track by a track reference declaration. The sample description for RTP declares the maximum packet size that this hint track will generate. Partial session description (SDP) information is stored in the track’s user data atom.

## Hint Sample Data Format

The sample description atom (`'stsd'`) contains information about the hint track samples. It specifies the data format (note that currently only RTP data format is defined) and the data reference to use (if more than one is defined) to locate the hint track sample data. It also contains some general information about this hint track, such as the hint track version number, the maximum packet size allowed by this hint track, and the RTP time scale. It may contain additional information, such as the random offsets to add to the RTP time stamp and sequence number.

The sample description atom can contain a table of sample descriptions to accommodate media that are encoded in multiple formats, but a hint track can be expected to have a single sample description at this time.

The sample description for hint tracks is defined in [Table 4-18](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtsmjqgazq).

__Table 4-18__  Hint track sample description

| Field | Bytes |
| Size | 4 |
| Data format | 4 |
| Reserved | 6 |
| Data reference index | 2 |
| Hint track version | 2 |
| Last compatible hint track version | 2 |
| Max packet size | 4 |
| Additional data table | variable |

##### Field descriptions

**Size**
: A 32-bit integer specifying the size of this sample description in bytes.

**Data format**
: A four-character code indicating the data format of the hint track samples. Only `'rtp '` is currently defined. Note that the fourth character in `'rtp '` is an ASCII blank space (0x20). Do not attempt to packetize data whose format you do not recognize.

**Reserved**
: Six bytes that must be set to 0.

**Data reference index**
: This field indirectly specifies where to find the hint track sample data. The data reference is a file or resource specified by the data reference atom (`'dref'`) inside the data information atom (`'dinf'`) of the hint track. The data information atom can contain a table of data references, and the data reference index is a 16-bit integer that tells you which entry in that table should be used. Normally, the hint track has a single data reference, and this index entry is set to 0.

**Hint track version**
: A 16-bit unsigned integer indicating the version of the hint track specification. This is currently set to 1.

**Last compatible hint track version**
: A 16-bit unsigned integer indicating the oldest hint track version with which this hint track is backward-compatible. If your application understands the hint track version specified by this field, it can work with this hint track.

**Max packet size**
: A 32-bit integer indicating the packet size limit, in bytes, used when creating this hint track. The largest packet generated by this hint track will be no larger than this limit.

**Additional data table**
: A table of variable length containing additional information. Additional information is formatted as a series of tagged entries.

This field always contains a tagged entry indicating the RTP time scale for RTP data. All other tagged entries are optional.

Three data tags are currently defined for RTP data. One tag is defined for use with any type of data. You can create additional tags. Tags are identified using four-character codes. Tags using all lowercase letters are reserved by Apple. Ignore any tagged data you do not understand.

Table entries are structured like atoms. The structure of table entries is shown in [Table 4-19](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtsmjsgyzq).

__Table 4-19__  The structure of table entries

| Field | Format | Bytes |
| Entry length | 32-bit integer | 4 |
| Data tag | 4-char code | 4 |
| Data | Variable | Entry length - 8 |

Tagged entries for the `'rtp '` data format are defined as follows:

**`'tims'`**
: A 32-bit integer specifying the RTP time scale. This entry is required for RTP data.

**`'tsro'`**
: A 32-bit integer specifying the offset to add to the stored time stamp when sending RTP packets. If this entry is not present, a random offset should be used, as specified by the IETF. If this entry is 0, use an offset of 0 (no offset).

**`'snro'`**
: A 32-bit integer specifying the offset to add to the sequence number when sending RTP packets. If this entry is not present, a random offset should be used, as specified by the IETF. If this entry is 0, use an offset of 0 (no offset).

## Packetization Hint Sample Data for Data Format 'rtp '

This section describes the sample data for the `'rtp '` format. The `'rtp '` format assumes that the server is sending data using Real-Time Transport Protocol (RTP). This format also assumes that the server “knows” about RTP headers but does not require that the server know anything about specific media headers, including media headers defined in various IETF drafts.

Each sample in the hint track will generate one or more RTP packets. Each entry in the sample data table in a hint track sample corresponds to a single RTP packet. Samples in the hint track may or may not correspond exactly to samples in the media track. Data in the hint track sample is byte aligned, but not 32-bit aligned.

The RTP timestamps of all packets in a hint sample are the same as the hint sample time. In other words, packets that do not have the same RTP timestamp cannot be placed in the same hint sample.

The RTP hint track time scale should be reasonably chosen so that there is adequate spacing between samples (as well as adequate spacing between transmission times for packets within a sample).

The packetization hint sample data contains the data elements listed in [Table 4-20](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzrgaza).

__Table 4-20__  Packetization hint data elements

| Packetization hint sample data | Bytes |
| Entry count | 2 |
| Reserved | 2 |
| Packet entry table | Variable |
| Additional data | Variable |

##### Field descriptions

**Entry count**
: A 16-bit unsigned integer indicating the number of packet entries in the table. Each entry in the table corresponds to a packet. Multiple entries in a single sample indicate that the media sample had to be split into multiple packets. A sample with an entry count of 0 is reserved and, if encountered, must be skipped.

**Reserved**
: Two bytes that must be set to 0.

**Packet entry table**
: A variable length table containing packet entries. Packet entries are defined below.

**Additional data**
: A variable length field containing data pointed to by the entries in the data table.

The packet entry contains the data elements listed in [Table 4-21](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzrgazq).

__Table 4-21__  Packet entry data elements

| Packet entry | Bytes |
| Relative packet transmission time | 4 |
| RTP header info | 2 |
| RTP sequence number | 2 |
| Flags | 2 |
| Entry count | 2 |
| Extra information TLVs | 0 or variable |
| Data table | variable |

**Relative packet transmission time**
: A 32-bit signed integer value, indicating the time, in the hint track’s time scale, to send this packet relative to the hint sample’s actual time. Negative values mean that the packet will be sent earlier than real time, which is useful for smoothing the data rate. Positive values are useful for repeating packets at later times. Within each hint sample track, each packet time stamp must be non-decreasing.

**RTP header info**
: A 16-bit integer specifying various values to be set in the RTP header. The bits of the field are defined as follows.

（原归档配图获取待重试：`qtff_l_t1.gif`）

The RTP header information field contains the elements listed in [Table 4-22](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzrga2a).

__Table 4-22__  RTP header information elements

| Field | Bit# | Description |
| P | 2 | A 1-bit number corresponding to the padding (P) bit in the RTP header. This bit should probably not be set, since a server that needs different packet padding would need to unpad and repad the packet itself. |
| X | 3 | A 1-bit number corresponding to the extension (X) bit in the RTP header. This bit should probably not be set, since a server that needs to send its own RTP extension would either not be able to, or would be forced to replace any extensions from the hint track. |
| M | 8 | A 1-bit number corresponding to the marker (M) bit in the RTP header. |
| Payload type | 9-15 | A 7-bit number corresponding to the payload type (PT) field of the RTP header. |

All undefined bits are reserved and must be set to zero. Note that the location of the defined bits are in the same bit location as in the RTP header.

**RTP sequence number**
: A 16-bit integer specifying the RTP sequence number for this packet. The RTP server adds a random offset to this sequence number before transmitting the packet. This field allows re-transmission of packets—for example, the same packet can be assembled with the same sequence number and a different (later) packet transmission time. A text sample with a duration of 5 minutes can be retransmitted every 10 seconds, so that clients that miss the original sample transmission (perhaps they started playing the movie in the middle) will be refreshed after a maximum of 10 seconds.

**Flags**
: A 16-bit field indicating certain attributes for this packet. Defined bits are shown in [Figure 4-18](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzrga4a).

__Figure 4-18__  Packet attribute flags

（原归档配图获取待重试：`qtff_l_t2.gif`）

**Entry count**
: A 16-bit unsigned integer specifying the number of entries in the data table.

**Extra information TLVs**
: The extra information TLVs listed in [Table 4-23](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzrga2q) are present if and only if the X bit is set in the flags field. This provides a way of extending the hint track format without changing the version, while allowing backward compatibility.

__Table 4-23__  Extra information TLVs

| Extra information TLVs | Bytes |
| Extra information size | 4 |
| TLV size | 4 |
| TLV type | 4 |
| TLV data | Padded to 4-byte boundary(int(TLV Size -8 +3) / 4 \* 4 |
| TLV size | 4 |
| TLV type | 4 |
| TLV data | Padded to 4-byte boundary(int(TLV Size -8 +3) / 4 \* 4 |
| TLV size and so forth | ... |

**Extra information size**
: A 32-bit number that is the total size of all extra information TLVs in this packet, including the 4 bytes used for this field. An empty Extra information TLVs table would just be the extra information size, having the value 4. (In this case, it would be more efficient simply to not set the X bit and save 4 bytes just to represent the empty table.)

**TLV size**
: A 32-bit number that is the total size of this one TLV entry, including 4 bytes for the size, 4 bytes for the type, and any data bytes, but not including padding required to align to the next 4 byte boundary.

**TLV type**
: A 32-bit tag (a four-character `OSType`) identifying the TLV. Servers must ignore TLV types that they do not recognize. Note that TLV types containing all lowercase letters are reserved by Apple.

**TLV data**
: The data for the TLV.

In order to support MPEG (and other data types) whose RTP timestamp is not monotonically increasing and directly calculated from the sample timestamp, the TLV type listed in [Table 4-24](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzrga3a) is defined.

__Table 4-24__  TLV type

| Size | Type | Data Description |
| 12 | `'rtpo'` | A signed 32-bit integer to be added to the RTP timestamp, which is derived from the hint sample timestamp. |

**Data table**
: A table that defines the data to be put in the payload portion of the RTP packet. This table defines various places the data can be retrieved. Table entries are listed in [Table 4-25](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzrga3q).

__Table 4-25__  Data table entries

| Data table entry | Bytes |
| Data source | 1 |
| Data | 15 |

The data source field of the entry table indicates how the other 15 bytes of the entry are to be interpreted. Values of 0 through 4 are defined. The various data table formats are defined below.

Although there are various schemes, note that the entries in the various schemes are the same size, 16 bytes long.

### Data Modes

#### No-Op Data Mode

The data table entry has the format for no-op mode shown in [Figure 4-19](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzrga4q).

__Figure 4-19__  No-op data mode format

（原归档配图获取待重试：`qtff_l_t3.gif`）

##### Field descriptions

**Data source = 0**
: A value of 0 indicates that this data table entry is to be ignored.

#### Immediate Data Mode

The data table entry has the format for immediate mode shown in [Figure 4-20](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzrgeya).

__Figure 4-20__  Immediate data mode table entry

（原归档配图获取待重试：`qtff_l_t4.gif`）

##### Field descriptions

**Data source = 1**
: A value of 1 indicates that the data is to be immediately taken from the bytes of data that follow.

**Immediate length**
: An 8-bit integer indicating the number of bytes to take from the data that follows. Legal values range from 0 to 14.

**Immediate data**
: 14 bytes of data to place into the payload portion of the packet. Only the first number of bytes indicated by the immediate length field is used.

#### Sample Mode

The data table entry has the format for sample mode shown in [Figure 4-21](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzrgeyq).

__Figure 4-21__  Sample mode table entry format

（原归档配图获取待重试：`qtff_l_t5.gif`）

##### Field descriptions

**Data source = 2**
: A value of 2 indicates that the data is to be taken from a track’s sample data.

**Track ref index**
: A value that indicates which track the sample data will come from. A value of 0 means that there is exactly one media track referenced, so use that. Values from 1 to 127 are indexes into the hint track reference atom entries, indicating which original media track the sample is to be read from. A value of -1 means the hint track itself, that is, get the sample from the same track as the hint sample you are currently parsing.

**Length**
: A 16-bit integer specifying the number of bytes in the sample to copy.

**Sample number**
: A 32-bit integer specifying sample number of the track.

**Offset**
: A 32-bit integer specifying the offset from the start of the sample from which to start copying. If you are referencing samples in the hint track, this will generally points into the Additional Data area.

**Bytes per compression block**
: A 16-bit unsigned integer specifying the number of bytes that results from compressing the number of samples in the Samples per compression block field. A value of 0 is equivalent to a value of 1.

**Samples per compression block**
: A 16-bit unsigned integer specifying the uncompressed samples per compression block. A value of 0 is equivalent to a value of 1.

If the bytes per compression block and/or the samples per compression block is greater than 1, than this ratio is used to translate a sample number into an actual byte offset.

This ratio mode is typically used for compressed sound tracks. Note that for QuickTime sound tracks, the bytes per compression block also factors in the number of sound channels in that stream, so a QuickTime stereo sound stream’s BPCB would be twice that of a mono stream of the same sound format.

(CB = NS \* BPCB / SPCB)

where CB = compressed bytes, NS = number of samples, BPCB = bytes per compression block, and SPCB = samples per compression block.

An example:

A GSM compression block is typically 160 samples packed into 33 bytes.

So, BPCB = 33 and SPCB = 160.

The hint sample requests 33 bytes of data starting at the 161st media sample. Assume that the first QuickTime chunk contains at least 320 samples. So after determining that this data will come from chunk 1, and knowing where chunk 1 starts, you must use this ratio to adjust the offset into the file where the requested samples will be found:

```
chunk_number = 1; /* calculated by walking the sample-to-chunk atom  */
first_sample_in_this_chunk = 1; /* also calculated from that atom  */
chunk_offset = chunk_offsets[chunk_number]; /* from the stco atom  */
data_offset = (sample_number - first_sample_in_this_chunk) * BPCB  / SPCB;
read_from_file(chunk_offset + data_offset, length); /* read our  data */
```

#### Sample Description Mode

The data table entry has the format for sample description mode shown in [Figure 4-22](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzrgeza).

__Figure 4-22__  Sample description mode format

（原归档配图获取待重试：`qtff_l_t6.gif`）

##### Field descriptions

**Data source = 3**
: A value of 3 indicates that the data is to be taken from the media track's sample description table.

**Track ref index**
: A value that indicates which track the sample description will come from. A value of 0 means that there is exactly one hint track reference, so use that. Values from 1 to 127 are indexes into the hint track reference atom entries, indicating which original media track the sample is to be read from. A value of -1 means the hint track itself, that is, get the sample description from the same track as the hint sample you are currently parsing.

**Length**
: A 16-bit integer specifying the number of bytes to copy.

**Sample description index**
: A 32-bit integer specifying the index into the media's sample description table.

**Offset**
: A 32-bit integer specifying the offset from the start of the sample description from which to start copying.

**Reserved**
: Four bytes that must be set to 0.

**Additional data**
: A variable length field containing data pointed to by hint track sample mode entries in the data table.

## VR Media

__Note:__ VR Media is deprecated in the QuickTime file format. The information that follows is intended to document existing content containing VR Media and should not be used for new development.

This section describes the QuickTime VR world and node information atom containers, which can be obtained by calling the QuickTime VR Manager routines `QTVRGetVRWorld` and `QTVRGetNodeInfo`. Those routines, as well as a complete discussion of QuickTime VR and how your application can create QuickTime VR movies, are described in detail in _[QuickTime VR](../QuickTime%20VR.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnbu)_.

Many atom types contained in the VR world and node information atom containers are unique within their container. For example, each has a single header atom. Most parent atoms within an atom container are unique as well, such as the node parent atom in the VR world atom container or the hot spot parent atom in the node information atom container. For these one-time-only atoms, the atom ID is always set to 1. Unless otherwise mentioned in the descriptions of the atoms that follow, assume that the atom ID is 1.

Note that many atom structures contain two version fields, `majorVersion` and `minorVersion`. The values of these fields correspond to the constants `kQTVRMajorVersion` and `kQTVRMinorVersion` found in the header file `QuickTimeVRFormat.h`. For QuickTime 2.0 files, these values are 2 and 0.

QuickTime provides a number of routines for both creating and accessing atom containers.

Some of the leaf atoms within the VR world and node information atom containers contain fields that specify the ID of string atoms that are siblings of the leaf atom. For example, the VR world header atom contains a field for the name of the scene. The string atom is a leaf atom whose atom type is `kQTVRStringAtomType` (`'vrsg'`)`.` Its atom ID is that specified by the referring leaf atom.

A string atom contains a string. The structure of a string atom is defined by the `QTVRStringAtom` data type.

```c
typedef struct QTVRStringAtom {
    UInt16                              stringUsage;
    UInt16                              stringLength;
    unsigned char                       theString[4];
} QTVRStringAtom, *QTVRStringAtomPtr;
```

##### Field descriptions

**`stringUsage`**
: The string usage. This field is unused.

**`stringLength`**
: The length, in bytes, of the string.

**`theString`**
: The string. The string atom structure is extended to hold this string.

Each string atom may also have a sibling leaf atom, called the string encoding atom. The string encoding atom’s atom type is `kQTVRStringEncodingAtomType` (`'vrse'`). Its atom ID is the same as that of the corresponding string atom. The string encoding atom contains a single variable, `TextEncoding`, a `UInt32`, as defined in the header file `TextCommon.h`. The value of `TextEncoding` is handed, along with the string, to the routine `QTTextToNativeText` for conversion for display on the current machine. The routine `QTTextToNativeText` is found in the header file `Movies.h.`

__Note:__ The header file `TextCommon.h` contains constants and routines for generating and handling text encodings.

### VR World Atom Container

The VR world atom container (VR world for short) includes such information as the name for the entire scene, the default node ID, and default imaging properties, as well as a list of the nodes contained in the QTVR track.

A VR world can also contain custom scene information. QuickTime VR ignores any atom types that it doesn’t recognize, but you can extract those atoms from the VR world using standard QuickTime atom functions.

The structure of the VR world atom container is shown in [Figure 4-23](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtmojtguzq). The component atoms are defined and their structures are shown in the sections that follow.

__Figure 4-23__  Structure of the VR world atom container

（原归档配图获取待重试：`qtvr_l_10.gif`）

#### VR World Header Atom Structure

The VR world header atom is a leaf atom. Its atom type is `kQTVRWorldHeaderAtomType` (`'vrsc'`). It contains the name of the scene and the default node ID to be used when the file is first opened as well as fields reserved for future use.

The structure of a VR world header atom is defined by the `QTVRWorldHeaderAtom` data type.

```c
typedef struct VRWorldHeaderAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    QTAtomID                            nameAtomID;
    UInt32                              defaultNodeID;
    UInt32                              vrWorldFlags;
    UInt32                              reserved1;
    UInt32                              reserved2;
} VRWorldHeaderAtom, *QTVRWorldHeaderAtomPtr;
QT
QT
```

##### Field descriptions

**`majorVersion`**
: The major version number of the file format.

**`minorVersion`**
: The minor version number of the file format.

**`nameAtomID`**
: The ID of the string atom that contains the name of the scene. That atom should be a sibling of the VR world header atom. The value of this field is 0 if no name string atom exists.

**`defaultNodeID`**
: The ID of the default node (that is, the node to be displayed when the file is first opened).

**`vrWorldFlags`**
: A set of flags for the VR world. This field is unused.

**`reserved1`**
: Reserved. This field must be 0.

**`reserved2`**
: Reserved. This field must be 0.

#### Imaging Parent Atom

The imaging parent atom is the parent atom of one or more node-specific imaging atoms. Its atom type is  `kQTVRImagingParentAtomType` (`'imgp'`). Only panoramas have an imaging atom defined.

#### Panorama-Imaging Atom

A panorama-imaging atom describes the default imaging characteristics for all the panoramic nodes in a scene. This atom overrides QuickTime VR’s own defaults.

The panorama-imaging atom has an atom type of `kQTVRPanoImagingAtomType` (`'impn'`). Generally, there is one panorama-imaging atom for each imaging mode, so the atom ID, while it must be unique for each atom, is ignored. QuickTime VR iterates through all the panorama-imaging atoms.

The structure of a panorama-imaging atom is defined by the `QTVRPanoImagingAtom` data type:

```c
typedef struct QTVRPanoImagingAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    UInt32                              imagingMode;
    UInt32                              imagingValidFlags;
    UInt32                              correction;
    UInt32                              quality;
    UInt32                              directDraw;
    UInt32                              imagingProperties[6];
    UInt32                              reserved1;
    UInt32                              reserved2;
} QTVRPanoImagingAtom, *VRPanoImagingAtomPtr;
```

##### Field descriptions

**`majorVersion`**
: The major version number of the file format.

**`minorVersion`**
: The minor version number of the file format.

**`imagingMode`**
: The imaging mode to which the default values apply. Only `kQTVRStatic` and `kQTVRMotion` are allowed here.

**`imagingValidFlags`**
: A set of flags that indicate which imaging property fields in this structure are valid.

**`correction`**
: The default correction mode for panoramic nodes. This can be either `kQTVRNoCorrection`, `kQTVRPartialCorrection`, or `kQTVRFullCorrection`.

**`quality`**
: The default imaging quality for panoramic nodes.

**`directDraw`**
: The default direct-drawing property for panoramic nodes. This can be `true` or `false`.

**`imagingProperties`**
: Reserved for future panorama-imaging properties.

**`reserved1`**
: Reserved. This field must be 0.

**`reserved2`**
: Reserved. This field must be 0.

The `imagingValidFlags` field in the panorama-imaging atom structure specifies which imaging property fields in that structure are valid. You can use these bit flags to specify a value for that field:

```
enum {
    kQTVRValidCorrection                        = 1 << 0,
    kQTVRValidQuality                           = 1 << 1,
    kQTVRValidDirectDraw                        = 1 << 2,
    kQTVRValidFirstExtraProperty                = 1 << 3
};
```

##### Constant Descriptions

**`kQTVRValidCorrection`**
: The default correction mode for panorama-imaging properties. If this bit is set, the `correction` field holds a default correction mode.

**`kQTVRValidQuality`**
: The default imaging quality for panorama-imaging properties. If this bit is set, the `quality` field holds a default imaging quality.

**`kQTVRValidDirectDraw`**
: The default direct-draw quality for panorama-imaging properties. If this bit is set, the `directDraw` field holds a default direct-drawing property.

**`kQTVRValidFirstExtraProperty`**
: The default imaging property for panorama-imaging properties. If this bit is set, the first element in the array in the `imagingProperties` field holds a default imaging property. As new imaging properties are added, they will be stored in this array.

## Node Parent Atom

__Note:__ VR Media is deprecated in the QuickTime file format. The information that follows is intended to document existing content containing VR Media and should not be used for new development.

The node parent atom is the parent of one or more node ID atoms. The atom type of the node parent atom is `kQTVRNodeParentAtomType` (`'vrnp'`) and the atom type of the each node ID atom is `kQTVRNodeIDAtomType` (`'vrni'`).

There is one node ID atom for each node in the file. The atom ID of the node ID atom is the node ID of the node. The node ID atom is the parent of the node location atom. The node location atom is the only child atom defined for the node ID atom. Its atom type is `kQTVRNodeLocationAtomType` (`'nloc'`).

## Node Location Atom Structure

__Note:__ VR Media is deprecated in the QuickTime file format. The information that follows is intended to document existing content containing VR Media and should not be used for new development.

The node location atom is the only child atom defined for the node ID atom. Its atom type is `kQTVRNodeLocationAtomType` (`'nloc'`). A node location atom describes the type of a node and its location.

The structure of a node location atom is defined by the `QTVRNodeLocationAtom` data type:

```c
typedef struct VRNodeLocationAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    OSType                              nodeType;
    UInt32                              locationFlags;
    UInt32                              locationData;
    UInt32                              reserved1;
    UInt32                              reserved2;
} VRNodeLocationAtom, *QTVRNodeLocationAtomPtr;
QT
QT
```

##### Field descriptions

**`majorVersion`**
: The major version number of the file format.

**`minorVersion`**
: The minor version number of the file format.

**`nodeType`**
: The node type. This field should contain either `kQTVRPanoramaType` or `kQTVRObjectType`.

**`locationFlags`**
: The location flags. This field must contain the value `kQTVRSameFile`, indicating that the node is to be found in the current file. In the future, these flags may indicate that the node is in a different file or at some URL location.

**`locationData`**
: The location of the node data. When the `locationFlags` field is `kQTVRSameFile`, this field should be 0. The nodes are found in the file in the same order that they are found in the node list.

**`reserved1`**
: Reserved. This field must be 0.

**`reserved2`**
: Reserved. This field must be 0.

## Custom Cursor Atoms

__Note:__ VR Media is deprecated in the QuickTime file format. The information that follows is intended to document existing content containing VR Media and should not be used for new development.

The hot spot information atom, discussed in [Hot Spot Information Atom](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtkobqgy3a), allows you to indicate custom cursor IDs for particular hot spots that replace the default cursors used by QuickTime VR. QuickTime VR allows you to store your custom cursors in the VR world of the movie file.

__Note:__

The use of resource forks for the storage of QuickTime media is deprecated in the QuickTime file format. The information that follows is intended to document existing content and should not be used for new development.

In Mac OS with a two-fork file system, custom cursors could be stored in the resource fork of the movie file. However, this implementation does not work on any other operating system platform (such as Windows).

The cursor parent atom is the parent of all of the custom cursor atoms stored in the VR world. Its atom type is `kQTVRCursorParentAtomType` (`'vrcp'`). The child atoms of the cursor parent are either cursor atoms or color cursor atoms. Their atom types are `kQTVRCursorAtomType` (`'CURS'`) and `kQTVRColorCursorAtomType` (`'crsr'`). These atoms are stored exactly as cursors or color cursors would be stored as a resource.

## Node Information Atom Container

__Note:__ VR Media is deprecated in the QuickTime file format. The information that follows is intended to document existing content containing VR Media and should not be used for new development.

The node information atom container includes general information about the node such as the node’s type, ID, and name. The node information atom container also contains the list of hot spot atoms for the node. A QuickTime VR movie contains one node information atom container for each node in the file. The routine `QTVRGetNodeInfo` allows you to obtain the node information atom container for the current node or for any other node in the movie.

[Figure 4-24](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtmojtgu3q) shows the structure of the node information atom container.

__Figure 4-24__  Structure of the node information atom container

（原归档配图获取待重试：`qtvr_l_11.gif`）

### Node Header Atom Structure

A node header atom is a leaf atom that describes the type and ID of a node, as well as other information about the node. Its atom type is `kQTVRNodeHeaderAtomType` (`'ndhd'`).

The structure of a node header atom is defined by the `QTVRNodeHeaderAtom` data type:

```c
typedef struct VRNodeHeaderAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    OSType                              nodeType;
    QTAtomID                            nodeID;
    QTAtomID                            nameAtomID;
    QTAtomID                            commentAtomID;
    UInt32                              reserved1;
    UInt32                              reserved2;
} VRNodeHeaderAtom, *VRNodeHeaderAtomPtr;
```

##### Field descriptions

**`majorVersion`**
: The major version number of the file format.

**`minorVersion`**
: The minor version number of the file format.

**`nodeType`**
: The node type. This field should contain either `kQTVRPanoramaType` or `kQTVRObjectType`.

**`nodeID`**
: The node ID.

**`nameAtomID`**
: The ID of the string atom that contains the name of the node. This atom should be a sibling of the node header atom. The value of this field is 0 if no name string atom exists.

**`commentAtomID`**
: The ID of the string atom that contains a comment for the node. This atom should be a sibling of the node header atom. The value of this field is 0 if no comment string atom exists.

**`reserved1`**
: Reserved. This field must be 0.

**`reserved2`**
: Reserved. This field must be 0.

### Hot Spot Parent Atom

The hot spot parent atom is the parent for all hot spot atoms for the node. The atom type of the hot spot parent atom is `kQTVRHotSpotParentAtomType` (`'hspa'`) and the atom type of the each hot spot atom is `kQTVRHotSpotAtomType` (`'hots'`)`.` The atom ID of each hot spot atom is the hot spot ID for the corresponding hot spot. The hot spot ID is determined by its color index value as it is stored in the hot spot image track.

The hot spot track is an 8-bit video track that contains color information that indicates hot spots. For more information, refer to Programming With QuickTime VR.

Each hot spot atom is the parent of a number of atoms that contain information about each hot spot.

### Hot Spot Information Atom

The hot spot information atom contains general information about a hot spot. Its atom type is `kQTVRHotSpotInfoAtomType` (`'hsin'`). Every hot spot atom should have a hot spot information atom as a child.

The structure of a hot spot information atom is defined by the `QTVRHotSpotInfoAtom` data type:

```c
typedef struct VRHotSpotInfoAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    OSType                              hotSpotType;
    QTAtomID                            nameAtomID;
    QTAtomID                            commentAtomID;
    SInt32                              cursorID[3];
    Float32                             bestPan;
    Float32                             bestTilt;
    Float32                             bestFOV;
    FloatPoint                          bestViewCenter;
    Rect                                hotSpotRect;
    UInt32                              flags;
    UInt32                              reserved1;
    UInt32                              reserved2;
} VRHotSpotInfoAtom, *QTVRHotSpotInfoAtomPtr;
```

##### Field descriptions

**`majorVersion`**
: The major version number of the file format.

**`minorVersion`**
: The minor version number of the file format.

**`hotSpotType`**
: The hot spot type. This type specifies which other information atoms—if any—are siblings to this one. QuickTime VR recognizes three types: `kQTVRHotSpotLinkType`, `kQTVRHotSpotURLType`, and `kQTVRHotSpotUndefinedType`.

**`nameAtomID`**
: The ID of the string atom that contains the name of the hot spot. This atom should be a sibling of the hot spot information atom. This string is displayed in the QuickTime VR controller bar when the mouse is moved over the hot spot.

**`commentAtomID`**
: The ID of the string atom that contains a comment for the hot spot. This atom should be a sibling of the hot spot information atom. The value of this field is 0 if no comment string atom exists.

**`cursorID`**
: An array of three IDs for custom hot spot cursors (that is, cursors that override the default hot spot cursors provided by QuickTime VR). The first ID (`cursorID[0]`) specifies the cursor that is displayed when it is in the hot spot. The second ID (`cursorID[1]`) specifies the cursor that is displayed when it is in the hot spot and the mouse button is down. The third ID (`cursorID[2]`) specifies the cursor that is displayed when it is in the hot spot and the mouse button is released. To retain the default cursor for any of these operations, set the corresponding cursor ID to 0. Custom cursors should be stored in the VR world atom container, as described in [VR World Atom Container](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtknzzhaya).

**`bestPan`**
: The best pan angle for viewing this hot spot.

**`bestTilt`**
: The best tilt angle for viewing this hot spot.

**`bestFOV`**
: The best field of view for viewing this hot spot.

**`bestViewCenter`**
: The best view center for viewing this hot spot; applies only to object nodes.

**`hotSpotRect`**
: The boundary box for this hot spot, specified as the number of pixels in full panoramic space. This field is valid only for panoramic nodes.

**`flags`**
: A set of hot spot flags. This field is unused.

**`reserved1`**
: Reserved. This field must be 0.

**`reserved2`**
: Reserved. This field must be 0.

__Note:__ In QuickTime VR movie files, all angular values are stored as 32-bit floating-point values that specify degrees. In addition, all floating-point values conform to the IEEE Standard 754 for binary floating-point arithmetic, in big-endian format.

### Specific Information Atoms

Depending on the value of the `hotSpotType` field in the hot spot info atom there may also be a type specific information atom. The atom type of the type-specific atom is the hot spot type.

### Link Hot Spot Atom

The link hot spot atom specifies information for hot spots of type `kQTVRHotSpotLinkType` (`'link'`). Its atom type is thus `'link'`. The link hot spot atom contains specific information about a link hot spot.

The structure of a link hot spot atom is defined by the `QTVRLinkHotSpotAtom` data type:

```c
typedef struct VRLinkHotSpotAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    UInt32                              toNodeID;
    UInt32                              fromValidFlags;
    Float32                             fromPan;
    Float32                             fromTilt;
    Float32                             fromFOV;
    FloatPoint                          fromViewCenter;
    UInt32                              toValidFlags;
    Float32                             toPan;
    Float32                             toTilt;
    Float32                             toFOV;
    FloatPoint                          toViewCenter;
    Float32                             distance;
    UInt32                              flags;
    UInt32                              reserved1;
    UInt32                              reserved2;
} VRLinkHotSpotAtom, *VRLinkHotSpotAtomPtr;
```

##### Field descriptions

**`majorVersion`**
: The major version number of the file format.

**`minorVersion`**
: The minor version number of the file format.

**`toNodeID`**
: The ID of the destination node (that is, the node to which this hot spot is linked).

**`fromValidFlags`**
: A set of flags that indicate which source node view settings are valid.

**`fromPan`**
: The preferred from-pan angle at the source node (that is, the node containing the hot spot).

**`fromTilt`**
: The preferred from-tilt angle at the source node.

**`fromFOV`**
: The preferred from-field of view at the source node.

**`fromViewCenter`**
: The preferred from-view center at the source node.

**`toValidFlags`**
: A set of flags that indicate which destination node view settings are valid.

**`toPan`**
: The pan angle to use when displaying the destination node.

**`toTilt`**
: The tilt angle to use when displaying the destination node.

**`toFOV`**
: The field of view to use when displaying the destination node.

**`toViewCenter`**
: The view center to use when displaying the destination node.

**`distance`**
: The distance between the source node and the destination node.

**`flags`**
: A set of link hot spot flags. This field is unused and should be set to 0.

**`reserved1`**
: Reserved. This field must be 0.

**`reserved2`**
: Reserved. This field must be 0.

Certain fields in the link hot spot atom are not used by QuickTime VR. The `fromValidFlags` field is generally set to 0 and the other `from` fields are not used. However, these fields could be quite useful if you have created a transition movie from one node to another. The `from` angles can be used to swing the current view of the source node to align with the first frame of the transition movie. The `distance` field is intended for use with 3D applications, but is also not used by QuickTime VR.

#### Link Hot Spot Valid Flags

The `toValidFlags` field in the link hot spot atom structure specifies which view settings are to be used when moving to a destination node from a hot spot. You can use these bit flags to specify a value for that field:

```
enum {
    kQTVRValidPan                               = 1 << 0,
    kQTVRValidTilt                              = 1 << 1,
    kQTVRValidFOV                               = 1 << 2,
    kQTVRValidViewCenter                        = 1 << 3
};
```

##### Constant Descriptions

**`kQTVRValidPan`**
: The setting for using the destination pan angle.

**`kQTVRValidTilt`**
: The setting for using the destination tilt angle.

**`kQTVRValidFOV`**
: The setting for using the destination field of view.

**`kQTVRValidViewCenter`**
: The setting for using the destination view center.

## URL Hot Spot Atom

__Note:__ VR Media is deprecated in the QuickTime file format. The information that follows is intended to document existing content containing VR Media and should not be used for new development.

The URL hot spot atom has an atom type of `kQTVRHotSpotURLType` (`'url '`). The URL hot spot atom contains a URL string for a particular Web location (for example, `http://quicktimevr.apple.com`). QuickTime VR automatically links to this URL when the hot spot is clicked.

## Support for Wired Actions

__Note:__ VR Media is deprecated in the QuickTime file format. The information that follows is intended to document existing content containing VR Media and should not be used for new development.

Certain actions on a QuickTime VR movie can trigger wired actions if the appropriate event handler atoms have been added to the file. This section discusses what atoms must be included in the QuickTime VR file to support wired actions.

As with sprite tracks, the presence of a certain atom in the media property atom container of the QTVR track enables the handling of wired actions. This atom is of type `kSpriteTrackPropertyHasActions`, which has a single Boolean value that must be set to `true`.

When certain events occur and the appropriate event handler atom is found in the QTVR file, then that atom is passed to QuickTime to perform any actions specified in the atom. The event handler atoms themselves must be added to the node information atom container in the QTVR track. There are two types of event handlers for QTVR nodes: global and hot spot specific. The currently supported global event handlers are `kQTEventFrameLoaded` and `kQTEventIdle`. The event handler atoms for these are located at the root level of the node information atom container. A global event handler atom’s type is set to the event type and its ID is set to 1.

Hot spot–specific event handler atoms are located in the specific hot spot atom as a sibling to the hot spot info atom. For these atoms, the atom type is always `kQTEventType` and the ID is the `event` type. Supported hot spot–specific event types are `kQTEventMouseClick`, `kQTEventMouseClickEnd`, `kQTEventMouseClickEndTriggerButton`, and `kQTEventMouseEnter`, `kQTEventMouseExit`.

The specific actions that cause these events to be generated are described as follows:

**`kQTEventFrameLoaded` (`'fram'`)**
: A wired action that is generated when a node is entered, before any application-installed entering-node procedure is called (this event processing is considered part of the node setup that occurs before the application’s routine is called).

**`kQTEventIdle` (`'idle'`)**
: A wired action that is generated every n ticks, where n is defined by the contents of the `kSpriteTrackPropertyQTIdleEventsFrequency` atom (`SInt32`) in the media property atom container. When appropriate, this event is triggered before any normal idle processing occurs for the QuickTime VR movie.

**`kQTEventMouseClick` (`'clik'`)**
: A wired action that is generated when the mouse goes down over a hot spot.

**`kQTEventMouseClickEnd` (`'cend'`)**
: A wired action that is generated when the mouse goes up after a `kQTEventMouseClick` is generated, regardless of whether the mouse is still over the hot spot originally clicked. This event occurs prior to QuickTime VR’s normal mouse-up processing.

**`kQTEventMouseClickEndTriggerButton` (`'trig'`)**
: A wired action that is generated when a click end triggers a hot spot (using the same criterion as used by QuickTime VR in 2.1 for link/url hot spot execution). This event occurs prior to QuickTime VR’s normal hot spot–trigger processing.

**`kQTEventMouseEnter` (`'entr'`), `kQTEventMouseExit`(`'exit'`)**
: Wired action that are generated when the mouse rolls into or out of a hot spot, respectively. These events occur whether or not the mouse is down and whether or not the movie is being panned. These events occur after any application-installed `MouseOverHotSpotProc` is called, and will be cancelled if the return value from the application’s routine indicates that QuickTimeVR’s normal over–hot spot processing should not take place.

## QuickTime VR File Format

__Note:__ VR Media is deprecated in the QuickTime file format. The information that follows is intended to document existing content containing VR Media and should not be used for new development.

A QuickTime VR movie is stored on disk in a format known as the QuickTime VR file format. Beginning in QuickTime VR 2.0, a QuickTime VR movie could contain one or more nodes. Each node is either a panorama or an object. In addition, a QuickTime VR movie could contain various types of hot spots, including links between any two types of nodes.

__Important:__
This section describes the file format supported by version 2.1 of the QuickTime VR Manager.

All QuickTime VR movies contain a single QTVR track, a special type of QuickTime track that maintains a list of the nodes in the movie. Each individual sample in a QTVR track contains general information and hot spot information for a particular node.

If a QuickTime VR movie contains any panoramic nodes, that movie also contains a single panorama track, and if it contains any object nodes, it also contains a single object track. The panorama and object tracks contain information specific to the panoramas or objects in the movie. The actual image data for both panoramas and objects is usually stored in standard QuickTime video tracks, hereafter referred to as image tracks. (An image track can also be any type of track that is capable of displaying an image, such as a QuickTime 3D track.) The individual frames in the image track for a panorama make up the diced frames of the original single panoramic image. The frames for the image track of an object represent the many different views of the object. Hot spot image data is stored in parallel video tracks for both panoramas and objects.

### Single-Node Panoramic Movies

[Figure 4-25](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtmojtgyyq) illustrates the basic structure of a single-node panoramic movie. As you can see, every panoramic movie contains at least three tracks: a QTVR track, a panorama track, and a panorama image track.

__Figure 4-25__  The structure of a single-node panoramic movie file

（原归档配图获取待重试：`qtvr_l_08.gif`）

For a single-node panoramic movie, the QTVR track contains just one sample. There is a corresponding sample in the panorama track, whose time and duration are the same as the time and duration of the sample in the QTVR track. The time base of the movie is used to locate the proper video samples in the panorama image track. For a panoramic movie, the video sample for the first diced frame of a node’s panoramic image is located at the same time as the corresponding QTVR and panorama track samples. The total duration of all the video samples is the same as the duration of the corresponding QTVR sample and the panorama sample.

A panoramic movie can contain an optional hot spot image track and any number of standard QuickTime tracks. A panoramic movie can also contain panoramic image tracks with a lower resolution. The video samples in these low-resolution image tracks must be located at the same time and must have the same total duration as the QTVR track. Likewise, the video samples for a hot spot image track, if one exists, must be located at the same time and must have the same total duration as the QTVR track.

### Single-Node Object Movies

[Figure 4-26](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtmojtgy2q) illustrates the basic structure of a single-node object movie. As you can see, every object movie contains at least three tracks: a QTVR track, an object track, and an object image track.

__Figure 4-26__  The structure of a single-node object movie file

（原归档配图获取待重试：`qtvr_l_07.gif`）

For a single-node object movie, the QTVR track contains just one sample. There is a corresponding sample in the object track, whose time and duration are the same as the time and duration of the sample in the QTVR track. The time base of the movie is used to locate the proper video samples in the object image track.

For an object movie, the frame corresponding to the first row and column in the object image array is located at the same time as the corresponding QTVR and object track samples. The total duration of all the video samples is the same as the duration of the corresponding QTVR sample and the object sample.

In addition to these three required tracks, an object movie can also contain a hot spot image track and any number of standard QuickTime tracks (such as video, sound, and text tracks). A hot spot image track for an object is a QuickTime video track that contains images of colored regions delineating the hot spots; an image in the hot spot image track must be synchronized to match the appropriate image in the object image track. A hot spot image track should be 8 bits deep and can be compressed with any lossless compressor (including temporal compressors). This is also true of panoramas.

__Note:__ To assign a single fixed-position hot spot to all views of an object, you should create a hot spot image track that consists of a single video frame whose duration is the entire node time.

To play a time-based track with the object movie, you must synchronize the sample data of that track to the start and stop times of a view in the object image track. For example, to play a different sound with each view of an object, you might store a sound track in the movie file with each set of sound samples synchronized to play at the same time as the corresponding object’s view image. (This technique also works for video samples.) Another way to add sound or video is simply to play a sound or video track during the object’s view animation; to do this, you need to add an active track to the object that is equal in duration to the object’s row duration.

__Important:__
In a QuickTime VR movie file, the panorama image tracks and panorama hot spot tracks must be disabled. For an object, the object image tracks must be enabled and the object hot spot tracks must be disabled.

### Multinode Movies

A multinode QuickTime VR movie can contain any number of object and panoramic nodes. [Figure 4-27](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtmojtgy4q) illustrates the structure of a QuickTime VR movie that contains five nodes (in this case, three panoramic nodes and two object nodes).

__Figure 4-27__  The structure of a multinode movie file

（原归档配图获取待重试：`qtvr_l_09.gif`）

__Important:__
Panoramic tracks and object tracks must never be located at the same time.

## QTVR Track

__Note:__ VR Media is deprecated in the QuickTime file format. The information that follows is intended to document existing content containing VR Media and should not be used for new development.

A QTVR track is a special type of QuickTime track that maintains a list of all the nodes in a movie. The media type for a QTVR track is `'qtvr'`. All the media samples in a QTVR track share a common sample description. This sample description contains the VR world atom container. The track contains one media sample for each node in the movie. Each QuickTime VR media sample contains a node information atom container.

### QuickTime VR Sample Description Structure

Whereas the QuickTime VR media sample is simply the node information itself, all sample descriptions are required by QuickTime to have a certain structure for the first several bytes. The structure for the QuickTime VR sample description is as follows:

```c
typedef struct QTVRSampleDescription {
    UInt32                              size;
    UInt32                              type;
    UInt32                              reserved1;
    UInt16                              reserved2;
    UInt16                              dataRefIndex;
    UInt32                              data;
} QTVRSampleDescription, *QTVRSampleDescriptionPtr, **QTVRSampleDescriptionHandle;
```

##### Field descriptions

**`size`**
: The size, in bytes, of the sample description header structure, including the VR world atom container contained in the `data` field.

**`type`**
: The sample description type. For QuickTime VR movies, this type should be `'qtvr'`.

**`reserved1`**
: Reserved. This field must be 0.

**`reserved2`**
: Reserved. This field must be 0.

**`dataRefIndex`**
: Reserved. This field must be 0.

**`data`**
: The VR world atom container. The sample description structure is extended to hold this atom container.

## Panorama Tracks

__Note:__ VR Media is deprecated in the QuickTime file format. The information that follows is intended to document existing content containing VR Media and should not be used for new development.

A movie’s panorama track is a track that contains information about the panoramic nodes in a scene. The media type of the panorama track is `'pano'`. Each sample in a panorama track corresponds to a single panoramic node. This sample parallels the corresponding sample in the QTVR track. Panorama tracks do not have a sample description (although QuickTime requires that you specify a dummy sample description when you call `AddMediaSample` to add a sample to a panorama track). The sample itself contains an atom container that includes a panorama sample atom and other optional atoms.

### Panorama Sample Atom Structure

A panorama sample atom has an atom type of `kQTVRPanoSampleDataAtomType` (`'pdat'`). It describes a single panorama, including track reference indexes of the scene and hot spot tracks and information about the default viewing angles and the source panoramic image.

The structure of a panorama sample atom is defined by the `QTVRPanoSampleAtom` data type:

```c
typedef struct VRPanoSampleAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    UInt32                              imageRefTrackIndex;
    UInt32                              hotSpotRefTrackIndex;
    Float32                             minPan;
    Float32                             maxPan;
    Float32                             minTilt;
    Float32                             maxTilt;
    Float32                             minFieldOfView;
    Float32                             maxFieldOfView;
    Float32                             defaultPan;
    Float32                             defaultTilt;
    Float32                             defaultFieldOfView;
    UInt32                              imageSizeX;
    UInt32                              imageSizeY;
    UInt16                              imageNumFramesX;
    UInt16                              imageNumFramesY;
    UInt32                              hotSpotSizeX;
    UInt32                              hotSpotSizeY;
    UInt16                              hotSpotNumFramesX;
    UInt16                              hotSpotNumFramesY;
    UInt32                              flags;
    OSType                              panoType;
    UInt32                              reserved2;
} VRPanoSampleAtom, *VRPanoSampleAtomPtr;
```

##### Field descriptions

**`majorVersion`**
: The major version number of the file format.

**`minorVersion`**
: The minor version number of the file format.

**`imageRefTrackIndex`**
: The index of the image track reference. This is the index returned by the `AddTrackReference` function when the image track is added as a reference to the panorama track. There can be more than one image track for a given panorama track and hence multiple references. (A panorama track might have multiple image tracks if the panoramas have different characteristics, which could occur if the panoramas were shot with different size camera lenses.) The value in this field is 0 if there is no corresponding image track.

**`hotSpotRefTrackIndex`**
: The index of the hot spot track reference.

**`minPan`**
: The minimum pan angle, in degrees. For a full panorama, the value of this field is usually 0.0.

**`maxPan`**
: The maximum pan angle, in degrees. For a full panorama, the value of this field is usually 360.0.

**`minTilt`**
: The minimum tilt angle, in degrees. For a high-resolution panorama, a typical value for this field is –42.5.

**`maxTilt`**
: The maximum tilt angle, in degrees. For a high-resolution panorama, a typical value for this field is +42.5.

**`minFieldOfView`**
: The minimum vertical field of view, in degrees. For a high-resolution panorama, a typical value for this field is 5.0. The value in this field is 0 for the default minimum field of view, which is 5 percent of the maximum field of view.

**`maxFieldOfView`**
: The maximum vertical field of view, in degrees. For a high-resolution panorama, a typical value for this field is 85.0. The value in this field is 0 for the default maximum field of view, which is `maxTilt` – `minTilt.`

**`defaultPan`**
: The default pan angle, in degrees.

**`defaultTilt`**
: The default tilt angle, in degrees.

**`defaultFieldOfView`**
: The default vertical field of view, in degrees.

**`imageSizeX`**
: The width, in pixels, of the panorama stored in the highest resolution image track.

**`imageSizeY`**
: The height, in pixels, of the panorama stored in the highest resolution image track.

**`imageNumFramesX`**
: The number of frames into which the panoramic image is diced horizontally. The width of each frame (which is `imageSizeX`/`imageNumFramesX`) should be divisible by 4.

**`imageNumFramesY`**
: The number of frames into which the panoramic image is diced vertically. The height of each frame (which is `imageSizeY`/`imageNumFramesY`) should be divisible by 4.

**`hotSpotSizeX`**
: The width, in pixels, of the panorama stored in the highest resolution hot spot image track.

**`hotSpotSizeY`**
: The height, in pixels, of the panorama stored in the highest resolution hot spot image track.

**`hotSpotNumFramesX`**
: The number of frames into which the panoramic image is diced horizontally for the hot spot image track.

**`hotSpotNumFramesY`**
: The number of frames into which the panoramic image is diced vertically for the hot spot image track.

**`flags`**
: A set of panorama flags. `kQTVRPanoFlagHorizontal` has been superseded by the `panoType` field. It is used only when the `panoType` field is `nil` to indicate a horizontally-oriented cylindrical panorama. `kQTVRPanoFlagAlwaysWrap` is set if the panorama should wrap horizontally, regardless of whether or not the pan range is 360 degrees. Note that these flags are currently supported only under OS X.

**`panoType`**
: An `OSType` describing the type of panorama. Types supported are:

- `kQTVRHorizontalCylinder`
- `kQTVRVerticalCylinder`
- `kQTVRCube`

**`reserved2`**
: Reserved. This field must be 0.

__Important:__
A new flag has been added to the flags field of the `QTVRPanoSampleAtom` data structure. This flag controls how panoramas wrap horizontally. If `kQTVRPanoFlagAlwaysWrap` is set, then the panorama wraps horizontally, regardless of the number of degrees in the panorama. If the flag is not set, then the panorama wraps only when the panorama range is 360 degrees. This is the default behavior.

The minimum and maximum values in the panorama sample atom describe the physical limits of the panoramic image. QuickTime VR allows you to set further constraints on what portion of the image a user can see by calling the `QTVRSetConstraints` routine. You can also preset image constraints by adding constraint atoms to the panorama sample atom container. The three constraint atom types are `kQTVRPanConstraintAtomType`, `kQTVRTiltConstraintAtomType`, and `kQTVRFOVConstraintAtomType`. Each of these atom types share a common structure defined by the `QTVRAngleRangeAtom` data type:

```c
typedef struct QTVRAngleRangeAtom {
    Float32                             minimumAngle;
    Float32                             maximumAngle;
} QTVRAngleRangeAtom, *QTVRAngleRangeAtomPtr;
```

##### Field descriptions

**`minimumAngle`**
: The minimum angle in the range, in degrees.

**`maximumAngle`**
: The maximum angle in the range, in degrees.

### Panorama Image Track

The actual panoramic image for a panoramic node is contained in a panorama image track, which is a standard QuickTime video track. The track reference to this track is stored in the `imageRefTrackIndex` field of the panorama sample atom.

QuickTime VR 2.1 required the original panoramic image to be rotated 90 degrees counterclockwise. This orientation has changed in QuickTime VR 2.2, however, as discussed later in this section.

The rotated image is diced into smaller frames, and each diced frame is then compressed and added to the video track as a video sample, as shown in [Figure 4-28](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtmojtg4zq). Frames can be compressed using any spatial compressor; however, temporal compression is not allowed for panoramic image tracks.

__Figure 4-28__  Creating an image track for a panorama

（原归档配图获取待重试：`qtvr_ls_05.gif`）

QuickTime VR 2.2 does not require the original panoramic image to be rotated 90 degrees counterclockwise, as was the case in QuickTime VR 2.1. The rotated image is still diced into smaller frames, and each diced frame is then compressed and added to the video track as a video sample, as shown in [Figure 4-29](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtmojtg43q).

__Figure 4-29__  Creating an image track for a panorama, with the image track oriented horizontally

（原归档配图获取待重试：`qt_l_214.gif`）

In QuickTime 3.0, a panorama sample atom (which contains information about a single panorama) contains the `panoType` field, which indicates whether the diced panoramic image is oriented horizontally or vertically.

### Cylindrical Panoramas

The primary change to cylindrical panoramas in QuickTime VR 2.2 is that the panorama, as stored in the image track of the movie, can be oriented horizontally. This means that the panorama does not need to be rotated 90 degrees counterclockwise, as required previously.

To indicate a horizontal orientation, the field in the `VRPanoSampleAtom` data structure formerly called `reserved1` has been renamed `panoType`. Its type is `OSType`. The `panoType` field value for a horizontally oriented cylinder is `kQTVRHorizontalCylinder` (`'hcyl'`), while a vertical cylinder is `kQTVRVerticalCylinder` (`'vcyl'`). For compatibility with older QuickTime VR files, when the `panoType` field is `nil`, then a cylinder is assumed, with the low order bit of the flags field set to 1 to indicate if the cylinder is horizontal and 0 if the cylinder is vertical.

One consequence of reorienting the panorama horizontally is that, when the panorama is divided into separate tiles, the order of the samples in the file is now the reverse of what it was for vertical cylinders. Since vertical cylinders were rotated 90 degrees counterclockwise, the first tile added to the image track was the rightmost tile in the panorama. For unrotated horizontal cylinders, the first tile added to the image track is the left-most tile in the panorama.

## Cubic Panoramas

__Note:__ VR Media is deprecated in the QuickTime file format. The information that follows is intended to document existing content containing VR Media and should not be used for new development.

A new type of panorama was introduced in the current version of QuickTime: the cubic panorama. This panorama in its simplest form is represented by six faces of a cube, thus enabling the viewer to see all the way up and all the way down. The file format and the cubic rendering engine actually allow for more complicated representations, such as special types of cubes with elongated sides or cube faces made up of separate tiles. Atoms that describe the orientation of each face allow for these nonstandard representations. If these atoms are not present, then the simplest representation is assumed. The following describes this simplest representation: a cube with six square sides.

Tracks in a cubic movie are laid out as they are for cylindrical panoramas. This includes a QTVR track, a panorama track, and an image track. Optionally, there may also be a hot spot track and a fast-start preview track. The image, hot spot, and preview tracks are all standard QuickTime video tracks.

### Image Tracks in Cubic Nodes

For a cubic node the image track contains six samples that correspond to the six square faces of the cube. The same applies to hot spot and preview tracks. [Figure 4-30](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwvgvzrgezq) shows how the order of samples in the track corresponds to the orientation of the cube faces.

__Figure 4-30__  Cubic node sample order versus cube face orientation

（原归档配图获取待重试：`qt_l_217.gif`）
（原归档配图获取待重试：`qt_l_218.gif`）

Note that the frames are oriented horizontally. There is no provision for frames that are rotated 90 counterclockwise as there are for cylindrical panoramas.

## Panorama Tracks in Cubic Nodes

__Note:__ VR Media is deprecated in the QuickTime file format. The information that follows is intended to document existing content containing VR Media and should not be used for new development.

The media sample for a panorama track contains the pano sample atom container. For cubes, some of the fields in the pano sample data atom have special values, which provide compatibility back to QuickTime VR 2.2. The cubic projection engine ignores these fields. They allow one to view cubic movies in older versions of QuickTime VR using the cylindrical engine, although the view will be somewhat incorrect, and the top and bottom faces will not be visible. The special values are shown in [Table 4-26](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtqobzheya).

__Table 4-26__  Fields and their special values as represented in the pano sample data atom, providing backward compatibility to QuickTime VR 2.2

| Field | Value |
| `imageNumFramesX` | 4 |
| `imageNumFramesY` | 1 |
| `imageSizeX` | Frame width \* 4 |
| `imageSizeY` | Frame height |
| `minPan` | 0.0 |
| `maxPan` | 360.0 |
| `minTilt` | -45.0 |
| `maxTilt` | 45.0 |
| `minFieldOfView` | 5.0 |
| `maxFieldOfView` | 90.0 |
| `flags` | 1 |

A 1 value in the flags field tells QuickTime VR 2.2 that the frames are not rotated. QuickTime VR 2.2 treats this as a four-frame horizontal cylinder. The `panoType` field (formerly `reserved1`) must be set to `kQTVRCube` (`'cube'`) so that QuickTime VR 3.0 can recognize this panorama as a cube.

Since certain viewing fields in the pano sample data atom are being used for backward compatibility, a new atom must be added to indicate the proper viewing parameters for the cubic image. This atom is the cubic view atom (atom type `'cuvw'`). The data structure of the cubic view atom is as follows:

```swift
struct QTVRCubicViewAtom {
    Float32         minPan;
    Float32         maxPan;
    Float32         minTilt;
    Float32         maxTilt;
    Float32         minFieldOfView;
    Float32         maxFieldOfView;

    Float32         defaultPan;
    Float32         defaultTilt;
    Float32         defaultFieldOfView;
};
typedef struct QTVRCubicViewAtom    QTVRCubicViewAtom;
```

The fields are filled in as desired for the cubic image. This atom is ignored by older versions of QuickTime VR. Typical minimum and maximum field values are shown in [Table 4-27](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtqojsga3q).

__Table 4-27__  Values for min and max fields

| Field | Value |
| `minPan` | 0.0 |
| `maxPan` | 360.0 |
| `minTilt` | -90.0 |
| `maxTilt` | 90.0 |
| `minFieldOfView` | 5.0 |
| `maxFieldOfView` | 120.0 |

You add the cubic view atom to the pano sample atom container (after adding the pano sample data atom). Then use `AddMediaSample` to add the atom container to the panorama track.

## Nonstandard Cubes

__Note:__ VR Media is deprecated in the QuickTime file format. The information that follows is intended to document existing content containing VR Media and should not be used for new development.

Although the default representation for a cubic panorama is that of six square faces of a cube, it is possible to depart from this standard representation. When doing so, a new atom must be added to the pano sample atom container. The atom type is `'cufa'`. The atom is an array of data structures of type `QTVRCubicFaceData`. Each entry in the array describes one face of whatever polyhedron is being defined. `QTVRCubicFaceData` is defined as follows:

```swift
struct QTVRCubicFaceData {
    float   orientation[4];
    float   center[2];
    float   aspect;
    float   skew;
};
typedef struct QTVRCubicFaceData    QTVRCubicFaceData;
```

The mathematical explanation of these data structures is beyond the scope of this document but will be described in a separate Apple Technote. [Table 4-28](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtqojugqza) shows what values QuickTime VR uses for the default representation of six square sides.

__Table 4-28__  Values used for representing sides

| Orien- tation | Orien- tation | Orien- tation | Orien- tation | Center | Center | Aspect | Skew | Side |
| 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | # front |
| –.5 | 0 | .5 | 0 | 0 | 0 | 1 | 0 | # right |
| 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | # back |
| .5 | 0 | .5 | 0 | 0 | 0 | 1 | 0 | # left |
| .5 | .5 | 0 | 0 | 0 | 0 | 1 | 0 | # top |
| –.5 | .5 | 0 | 0 | 0 | 0 | 1 | 0 | # bottom |

## Hot Spot Image Tracks

__Note:__ VR Media is deprecated in the QuickTime file format. The information that follows is intended to document existing content containing VR Media and should not be used for new development.

When a panorama contains hot spots, the movie file contains a hot spot image track, a video track that contains a parallel panorama, with the hot spots designated by colored regions. Each diced frame of the hot spot panoramic image must be compressed with a lossless compressor (such as QuickTime’s graphics compressor). The dimensions of the hot spot panoramic image are usually the same as those of the image track’s panoramic image, but this is not required. The dimensions must, however, have the same aspect ratio as the image track’s panoramic image. A hot spot image track should be 8 bits deep.

### Low-Resolution Image Tracks

It’s possible to store one or more low-resolution versions of a panoramic image in a movie file; those versions are called low-resolution image tracks. If there is not enough memory at runtime to use the normal image track, QuickTime VR uses a lower resolution image track if one is available. A low-resolution image track contains diced frames just like the higher resolution track, but the reconstructed panoramic image is half the height and half the width of the higher resolution image.

__Important:__
The panoramic images in the lower resolution image tracks and the hot spot image tracks, if present, must have the same orientation (horizontal or vertical) as the panorama image track.

### Track Reference Entry Structure

Since there are no fields in the pano sample data atom to indicate the presence of low-resolution image tracks, a separate sibling atom must be added to the panorama sample atom container. The track reference array atom contains an array of track reference entry structures that specify information about any low-resolution image tracks contained in a movie. Its atom type is `kQTVRTrackRefArrayAtomType` (`'tref'`).

A track reference entry structure is defined by the `QTVRTrackRefEntry` data type:

```c
typedef struct QTVRTrackRefEntry {
    UInt32                              trackRefType;
    UInt16                              trackResolution;
    UInt32                              trackRefIndex;
} QTVRTrackRefEntry;
```

##### Field descriptions

**`trackRefType`**
: The track reference type.

**`trackResolution`**
: The track resolution.

**`trackRefIndex`**
: The index of the track reference.

The number of entries in the track reference array atom is determined by dividing the size of the atom by `sizeof` (`QTVRTrackRefEntry`).

`kQTVRPreviewTrackRes` is a special value for the `trackResolution` field in the `QTVRTrackRefEntry` structure. This is used to indicate the presence of a special preview image track.

## Object Tracks

__Note:__ VR Media is deprecated in the QuickTime file format. The information that follows is intended to document existing content containing VR Media and should not be used for new development.

A movie’s object track is a track that contains information about the object nodes in a scene. The media type of the object track is `'obje'`. Each sample in an object track corresponds to a single object node in the scene. The samples of the object track contain information describing the object images stored in the object image track.

These object information samples parallel the corresponding node samples in the QTVR track and are equal in time and duration to a particular object node’s image samples in the object’s image track as well as the object node’s hot spot samples in the object’s hot spot track.

Object tracks do not have a sample description (although QuickTime requires that you specify a dummy sample description when you call `AddMediaSample` to add a sample to an object track). The sample itself is an atom container that contains a single object sample atom and other optional atoms.

### Object Sample Atom Structure

object sample atom describes a single object, including information about the default viewing angles and the view settings. The structure of an object sample atom is defined by the `QTVRObjectSampleAtom` data type:

```c
typedef struct VRObjectSampleAtom {
    UInt16                              majorVersion;
    UInt16                              minorVersion;
    UInt16                              movieType;
    UInt16                              viewStateCount;
    UInt16                              defaultViewState;
    UInt16                              mouseDownViewState;
    UInt32                              viewDuration;
    UInt32                              columns;
    UInt32                              rows;
    Float32                             mouseMotionScale;
    Float32                             minPan;
    Float32                             maxPan;
    Float32                             defaultPan;
    Float32                             minTilt;
    Float32                             maxTilt;
    Float32                             defaultTilt;
    Float32                             minFieldOfView;
    Float32                             fieldOfView;
    Float32                             defaultFieldOfView;
    Float32                             defaultViewCenterH;
    Float32                             defaultViewCenterV;
    Float32                             viewRate;
    Float32                             frameRate;
    UInt32                              animationSettings;
    UInt32                              controlSettings;
} VRObjectSampleAtom, *VRObjectSampleAtomPtr;
QT
QT
QT
```

##### Field descriptions

**`majorVersion`**
: The major version number of the file format.

**`minorVersion`**
: The minor version number of the file format.

**`movieType`**
: The movie controller type.

**`viewStateCount`**
: The number of view states of the object. A view state selects an alternate set of images for an object’s views. The value of this field must be positive.

**`defaultViewState`**
: The 1-based index of the default view state. The default view state image for a given view is displayed when the mouse button is not down.

**`mouseDownViewState`**
: The 1-based index of the mouse-down view state. The mouse-down view state image for a given view is displayed while the user holds the mouse button down and the cursor is over an object movie.

**`viewDuration`**
: The total movie duration of all image frames contained in an object’s view. In an object that uses a single frame to represent a view, the duration is the image track’s sample duration time.

**`columns`**
: The number of columns in the object image array (that is, the number of horizontal positions or increments in the range defined by the minimum and maximum pan values). The value of this field must be positive.

**`rows`**
: The number of rows in the object image array (that is, the number of vertical positions or increments in the range defined by the minimum and maximum tilt values). The value of this field must be positive.

**`mouseMotionScale`**
: The mouse motion scale factor (that is, the number of degrees that an object is panned or tilted when the cursor is dragged the entire width of the VR movie image). The default value is 180.0.

**`minPan`**
: The minimum pan angle, in degrees. The value of this field must be less than the value of the `maxPan` field.

**`maxPan`**
: The maximum pan angle, in degrees. The value of this field must be greater than the value of the `minPan` field.

**`defaultPan`**
: The default pan angle, in degrees. This is the pan angle used when the object is first displayed. The value of this field must be greater than or equal to the value of the `minPan` field and less than or equal to the value of the `maxPan` field.

**`minTilt`**
: The minimum tilt angle, in degrees. The default value is +90.0. The value of this field must be less than the value of the `maxTilt` field.

**`maxTilt`**
: The maximum tilt angle, in degrees. The default value is –90.0. The value of this field must be greater than the value of the `minTilt` field.

**`defaultTilt`**
: The default tilt angle, in degrees. This is the tilt angle used when the object is first displayed. The value of this field must be greater than or equal to the value of the `minTilt` field and less than or equal to the value of the `maxTilt` field.

**`minFieldOfView`**
: The minimum field of view to which the object can zoom. The valid range for this field is from 1 to the value of the `fieldOfView` field. The value of this field must be positive.

**`fieldOfView`**
: The image field of view, in degrees, for the entire object. The value in this field must be greater than or equal to the value of the `minFieldOfView` field.

**`defaultFieldOfView`**
: The default field of view for the object. This is the field of view used when the object is first displayed. The value in this field must be greater than or equal to the value of the `minFieldOfView` field and less than or equal to the value of the `fieldOfView` field.

**`defaultViewCenterH`**
: The default horizontal view center.

**`defaultViewCenterV`**
: The default vertical view center.

**`viewRate`**
: The view rate (that is, the positive or negative rate at which the view animation in the object plays, if view animation is enabled). The value of this field must be from –100.0 through +100.0, inclusive.

**`frameRate`**
: The frame rate (that is, the positive or negative rate at which the frame animation in a view plays, if frame animation is enabled). The value of this field must be from –100.0 through +100.0, inclusive.

**`animationSettings`**
: A set of 32-bit flags that encode information about the animation settings of the object.

**`controlSettings`**
: A set of 32-bit flags that encode information about the control settings of the object.

The `movieType` field
of the object sample atom structure specifies an object controller type, that is, the user interface to be used to manipulate the object.

QuickTime VR supports the following controller types:

```swift
enum ObjectUITypes {
    kGrabberScrollerUI                          = 1,
    kOldJoyStickUI                              = 2,
    kJoystickUI                                 = 3,
    kGrabberUI                                  = 4,
    kAbsoluteUI                                 = 5
};
```

##### Constant Descriptions

**`kGrabberScrollerUI`**
: The default controller, which displays a hand for dragging and rotation arrows when the cursor is along the edges of the object window.

**`kOldJoyStickUI`**
: A joystick controller, which displays a joystick-like interface for spinning the object. With this controller, the direction of panning is reversed from the direction of the grabber.

**`kJoystickUI`**
: A joystick controller, which displays a joystick-like interface for spinning the object. With this controller, the direction of panning is consistent with the direction of the grabber.

**`kGrabberUI`**
: A grabber-only interface, which displays a hand for dragging but does not display rotation arrows when the cursor is along the edges of the object window.

**`kAbsoluteUI`**
: An absolute controller, which displays a finger for pointing. The absolute controller switches views based on a row-and-column grid mapped into the object window.

#### Animation Settings

The `animationSettings` field of the object sample atom is a long integer that specifies a set of animation settings for an object node. Animation settings specify characteristics of the movie while it is playing. Use these constants to specify animation settings:

```swift
enum QTVRAnimationSettings {
    kQTVRObjectAnimateViewFramesOn              = (1 << 0),
    kQTVRObjectPalindromeViewFramesOn           = (1 << 1),
    kQTVRObjectStartFirstViewFrameOn            = (1 << 2),
    kQTVRObjectAnimateViewsOn                   = (1 << 3),
    kQTVRObjectPalindromeViewsOn                = (1 << 4),
    kQTVRObjectSyncViewToFrameRate              = (1 << 5),
    kQTVRObjectDontLoopViewFramesOn             = (1 << 6),
    kQTVRObjectPlayEveryViewFrameOn             = (1 << 7)
};
```

##### Constant Descriptions

**`kQTVRObjectAnimateViewFramesOn`**
: The animation setting to play all frames in the current view state.

**`kQTVRObjectPalindromeViewFramesOn`**
: The animation setting to play a back-and-forth animation of the frames of the current view state.

**`kQTVRObjectStartFirstViewFrameOn`**
: The animation setting to play the frame animation starting with the first frame in the view (that is, at the view start time).

**`kQTVRObjectAnimateViewsOn`**
: The animation setting to play all views of the current object in the default row of views.

**`kQTVRObjectPalindromeViewsOn`**
: The animation setting to play a back-and-forth animation of all views of the current object in the default row of views.

**`kQTVRObjectSyncViewToFrameRate`**
: The animation setting to synchronize the view animation to the frame animation and use the same options as for frame animation.

**`kQTVRObjectDontLoopViewFramesOn`**
: The animation setting to stop playing the frame animation in the current view at the end.

**`kQTVRObjectPlayEveryViewFrameOn`**
: The animation setting to play every view frame regardless of play rate. The play rate is used to adjust the duration in which a frame appears but no frames are skipped so the rate is not exact.

##### Control Settings

The `controlSettings` field of the object sample atom is a long integer that specifies a set of control settings for an object node. Control settings specify whether the object can wrap during panning and tilting, as well as other features of the node. The control settings are specified using these bit flags:

```swift
enum QTVRControlSettings {
    kQTVRObjectWrapPanOn                        = (1 << 0),
    kQTVRObjectWrapTiltOn                       = (1 << 1),
    kQTVRObjectCanZoomOn                        = (1 << 2),
    kQTVRObjectReverseHControlOn                = (1 << 3),
    kQTVRObjectReverseVControlOn                = (1 << 4),
    kQTVRObjectSwapHVControlOn                  = (1 << 5),
    kQTVRObjectTranslationOn                    = (1 << 6)
};
```

##### Constant Descriptions

**`kQTVRObjectWrapPanOn`**
: The control setting to enable wrapping during panning. When this control setting is enabled, the user can wrap around from the current pan constraint maximum value to the pan constraint minimum value (or vice versa) using the mouse or arrow keys.

**`kQTVRObjectWrapTiltOn`**
: The control setting to enable wrapping during tilting. When this control setting is enabled, the user can wrap around from the current tilt constraint maximum value to the tilt constraint minimum value (or vice versa) using the mouse or arrow keys.

**`kQTVRObjectCanZoomOn`**
: The control setting to enable zooming. When this control setting is enabled, the user can change the current field of view using the zoom-in and zoom-out keys on the keyboard (or using the VR controller buttons).

**`kQTVRObjectReverseHControlOn`**
: The control setting to reverse the direction of the horizontal control.

**`kQTVRObjectReverseVControlOn`**
: The control setting to reverse the direction of the vertical control.

**`kQTVRObjectSwapHVControlOn`**
: The control setting to exchange the horizontal and vertical controls.

**`kQTVRObjectTranslationOn`**
: The control setting to enable translation. When this setting is enabled, the user can translate using the mouse when either the translate key is held down or the controller translation mode button is toggled on.

## Track References for Object Tracks

__Note:__ VR Media is deprecated in the QuickTime file format. The information that follows is intended to document existing content containing VR Media and should not be used for new development.

The track references to an object’s image and hot spot tracks are not handled the same way as track references to panoramas. The track reference types are the same (`kQTVRImageTrackRefType` and `kQTVRHotSpotTrackRefAtomType`), but the location of the reference indexes is different. There is no entry in the object sample atom for the track reference indexes. Instead, separate atoms using the `VRTrackRefEntry` structure are stored as siblings to the object sample atom. The types of these atoms are `kQTVRImageTrackRefAtomType` and `kQTVRHotSpotTrackRefAtomType`. If either of these atoms is not present, then the reference index to the corresponding track is assumed to be 1.

__Note:__ The `trackResolution` field in the `VRTrackRefEntry` structure is ignored for object tracks.

The actual views of an object for an object node are contained in an object image track, which is usually a standard QuickTime video track. (An object image track can also be any type of track that is capable of displaying an image, such as a QuickTime 3D track.)

As described in Chapter 1 of _[QuickTime VR](../QuickTime%20VR.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnbu)_, these views are often captured by moving a camera around the object in a defined pattern of pan and tilt angles. The views must then be ordered into an object image array, which is stored as a one-dimensional sequence of frames in the movie’s video track (see [Figure 4-31](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtmojthayq)).

__Figure 4-31__  The structure of an image track for an object

（原归档配图获取待重试：`qtvr_l_03.gif`）

For object movies containing frame animation, each animated view in the object image array consists of the animating frames. It is not necessary that each view in the object image array contain the same number of frames, but the view duration of all views in the object movie must be the same.

For object movies containing alternate view states, alternate view states are stored as separate object image arrays that immediately follow the preceding view state in the object image track. Each state does not need to contain the same number of frames. However, the total movie time of each view state in an object node must be the same.

## Movie Media

Movie media is used to encapsulate embedded movies within QuickTime movies. This feature is available in QuickTime 4.1.

### Movie Sample Description

The movie media doesn’t have a unique sample description. It uses the minimum sample description, which is `SampleDescriptionRecord`.

### Movie Media Sample Format

Each sample in the movie media is a QuickTime atom container. All root-level atoms and their contents are enumerated in the following list. Note that the contents of all atoms are stored in big-endian format.

**`kMovieMediaDataReference`**
: A data reference type and a data reference. The data reference type is stored as an `OSType` at the start of the atom. The data reference is stored following the data reference type. If the data reference type is URL and the data reference is for a movie on the Apple website, the contents of the atom would be `url http://www.apple.com/foo.mov`.

There may be more than one atom of this type. The first atom of this type should have an atom ID of 1. Additional data references should be numbered sequentially.

**`kMovieMediaDefaultDataReferenceID`**
: This atom contains a `QTAtomID` that indicates the ID of the data reference to use when instantiating the embedded movie for this sample. If this atom is not present, the data reference with an ID of 1 is used.

**`kMovieMediaSlaveTime`**
: A Boolean that indicates whether or not the `TimeBase` of the embedded movie should be slaved to the `TimeBase` of the parent movie. If the `TimeBase` is slaved, the embedded movie’s zero time will correspond to the start time of its movie media sample. Further, the playback rate of the embedded movie will always be the same as the parent movie’s. If the `TimeBase` is not slaved, the embedded movie will default to a rate of 0, and a default time of whatever default time value it instantiated with (which may not be 0). If the `TimeBase` is not slaved, the embedded movie can be played by either including an `AutoPlay` atom in the movie media sample or by using a wired action. If this atom is not present, the embedded movie defaults to not slaved.

**`kMovieMediaSlaveAudio`**
: A Boolean that indicates whether or not the audio properties of the embedded movie should be slaved to those of the parent movie. When audio is slaved, all audio properties of the containing track are duplicated in the embedded movie. These properties include sound volume, balance, bass and treble, and level metering. If this atom is not present, the embedded movie defaults to not slaved audio.

**`kMovieMediaSlaveGraphicsMode`**
: A Boolean that indicates how the graphics mode of the containing track is applied to the embedded movie. If the graphics mode is not slaved, then the entire embedded movie is imaged using its own graphics modes. The result of the drawing of the embedded movie is composited onto the containing movie using the graphics mode of the containing track. If the graphics mode is slaved, then the graphics mode of each track in the embedded movie is ignored and instead the graphics mode of the containing track is used. In this case, the tracks of the embedded movie composite their drawing directly into the parent movie’s contents. If this atom is not present, the graphics mode defaults to not slaved. Graphics mode slaving is useful for compositing semi-transparent media––for example, a PNG with an alpha channel––on top of other media.

**`kMovieMediaSlaveTrackDuration`**
: A Boolean that indicates how the Movie Media Handler should react when the duration of the embedded movie is different than the duration of the movie media sample that it is contained by. When the movie media sample is created, the duration of the embedded movie may not yet be known. Therefore, the duration of the media sample may not be correct. In this case, the Movie Media Handler can do one of two things. If this atom is not present or it contains a value of false, the Movie Media Handler will respect the duration of media sample that contains the embedded movie. If the embedded movie has a longer duration than the movie media sample, the embedded movie will be truncated to the duration of the containing movie media sample. If the embedded movie is shorter, there will be a gap after it is finished playing. If this atom contains a value of true, the duration of the movie media sample will be adjusted to match the actual duration of the embedded movie. Because it is not possible to change an existing media sample, this will cause a new media sample to be added to the movie and the track’s edit list to be updated to reference the new sample instead of the original sample.

__Note:__ When the duration of the embedded movie’s sample is adjusted, by default no other tracks are adjusted. This can cause the overall temporal composition to change in unintended ways. To maintain the complete temporal composition, a higher-level data structure which describes the temporal relationships between the various tracks must also be included with the movie.

**`kMovieMediaAutoPlay`**
: A Boolean that indicates whether or not the embedded movie should start playing immediately after being instantiated. This atom is only used if the `TimeBase` of the embedded movie is not slaved to the parent movie. See the `kMovieMediaSlaveTime` atom in [Movie Media Sample Format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtkobuge3a) for more information. If auto play is requested, the movie will be played at its preferred rate after being instantiated. If this atom is not present, the embedded movie will not automatically play.

**`kMovieMediaLoop`**
: A `UInt8` that indicates how the embedded movie should loop. This atom is only used if the `TimeBase` of the embedded movie is not slaved to the parent movie. See the `kMovieMediaSlaveTime` atom in [Movie Media Sample Format](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqguwtkobuge3a) for more information. If this atom contains a 0, or if this atom is not present, the embedded movie will not loop. If this atom contains a value of 1, the embedded movie loops normally—that is, when it reaches the end it loops back to the beginning. If this atom contains a value of 2, the embedded movie uses palindromic looping. All other values are reserved.

**`kMovieMediaUseMIMEType`**
: Text (not a C string or a pascal string) that indicates the MIME type of the movie import component that should be used to instantiate this media. This is useful in cases where the data reference may not contain MIME type information. If this atom is not present, the MIME type of the data reference as determined at instantiation time is used. This atom is intended to allow content creators a method for working around MIME type binding problems. It should not typically be required, and should not be included in movie media samples by default.

**`kMovieMediaTitle`**
: Currently unused. It would contain text indicating the name of the embedded movie.

**`kMovieMediaAltText`**
: Text (not a C string or a pascal string) that is displayed to the user when the embedded movie is being instantiated or if the embedded movie cannot be instantiated. If this atom is not present, the name of the data reference (typically the file name) is used.

**`kMovieMediaClipBegin`**
: A `MovieMediaTimeRecord` that indicates the time of the embedded movie that should be used. The clip begin atom provides a way to specify that a portion of the beginning of the embedded movie should not be used. If this atom is not present, the beginning of the embedded movie is not changed. Note that this atom does not change the time at which the embedded movie begins playing in the parent movie’s time line. If the time specified in the clip begin atom is greater than the duration of the embedded movie, then the embedded movie will not play at all.

```swift
struct MovieMediaTimeRecord {
 wide            time;
TimeScale       scale;
};
```

**`kMovieMediaClipDuration`**
: A `MovieMediaTimeRecord` that indicates the duration of the embedded movie that should be used. The clip duration atom is applied by removing media from end of the embedded movie. If the clip duration atom is not present, then no media is removed from the end of the embedded movie. In situations where the sample contains both a clip duration and a clip begin atom, the clip begin is applied first. If the clip duration specifies a value that is larger than the duration of the embedded movie, no change is made to the embedded movie.

**`kMovieMediaEnableFrameStepping`**
: A Boolean that indicates whether or not the embedded movie should be considered when performing step operations, specifically using the interesting time calls with the `nextTimeStep` flag. If this atom is not present or is set to `false`, the embedded movie is not included in step calculations. If the atom is set to `true`, it is included in step calculations.

**`kMovieMediaBackgroundColor`**
: An `RGBColor` that is used for filling the background when the movie is being instantiated or when it fails to instantiate.

**`kMovieMediaRegionAtom`**
: A number of child atoms, shown below, which describe how the Movie Media Handler should resize the embedded movie. If this atom is not present, the Movie Media Handler resizes the child movie to completely fill the containing track’s box.

**`kMovieMediaSpatialAdjustment`**
: This atom contains an `OSType` that indicates how the embedded movie should be scaled to fit the track box. If this atom is not present, the default value is `kMovieMediaFitFill`. These modes are all based on SMIL layout options.

**`kMovieMediaFitClipIfNecessary`**
: If the media is larger than the track box, it will be clipped; if it is smaller, any additional area will be transparent.

**`kMovieMediaFitFill`**
: The media will be scaled to completely fill the track box.

**`kMovieMediaFitMeet`**
: The media is proportionally scaled so that it is entirely visible in the track box and fills the largest area possible without changing the aspect ratio.

**`kMovieMediaFitSlice`**
: The media is scaled proportionally so that the smaller dimension is completely visible.

**`kMovieMediaFitScroll`**
: Not currently implemented. It currently has the same behavior as `kMovieMediaFitClipIfNecessary`. When implemented, it will have the behavior described in the SMIL specification for a scrolling layout element.

**`kMovieMediaRectangleAtom`**
: Four child atoms that define a rectangle. Not all child atoms must be present: top and left must both appear together, width and height must both appear together. The dimensions contained in this rectangle are used in place of the track box when applying the contents of the spatial adjustment atom. If the top and left are not specified, the top and left of the containing track’s box are used. If the width and height are not specified, the width and height of the containing track’s box are used. Each child atom contains a `UInt32`.

**`kMovieMediaTop`**
: If present, the top of the rectangle

**`kMovieMediaLeft`**
: If present, the left boundary of the rectangle

**`kMovieMediaWidth`**
: If present, width of rectangle

**`kMovieMediaHeight`**
: If present, height of rectangle

[Next](Basic%20Data%20Types.md)[Previous](Metadata.md)
