---
title: QuickTime File Format Specification
apple_id: TP40000939
resource_type: Guide
platform: macOS
topic: Data Management
technology: QuickTime
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/QTFF/QTFFChap4/qtff4.html
archived_at: '2026-07-27T06:57:06.537209Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [QuickTime File Format Specification](Introduction%20to%20QuickTime%20File%20Format%20Specification.md)


[Next](Some%20Useful%20Examples%20and%20Scenarios.md)[Previous](Media%20Data%20Atom%20Types.md)

# Basic Data Types

This chapter describes a number of common data types that are used in QuickTime files.

## Language Code Values

Some elements of a QuickTime file may be associated with a particular spoken language. To indicate the language associated with a particular object, the QuickTime file format uses either language codes from the Macintosh Script Manager or ISO language codes (as specified in _ISO 639-2/T_).

QuickTime stores language codes as unsigned 16-bit fields. All Macintosh language codes have a value that is less than 0x400 except for the single value 0x7FFF indicating an unspecified language. ISO language codes are three-character codes, and are stored inside the 16-bit language code field as packed arrays, as described in [ISO Language Codes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgywtgnjrgazq). If treated as an unsigned 16-bit integer, an ISO language code always has a value of 0x400 or greater unless the code is equal to the value 0x7FFF indicating an Unspecified Macintosh language code.

If the language is specified using a Macintosh language code, any associated text uses Macintosh text encoding.

If the language is specified using an ISO language code, any associated text uses Unicode text encoding. When Unicode is used, the text is in UTF-8 unless it starts with a byte-order-mark (BOM, 0xFEFF. ), whereupon the text is in UTF-16. Both the BOM and the UTF-16 text should be big-endian.

__Note:__ ISO language codes cannot be used for all elements of a QuickTime file. Currently, ISO language codes can be used _only for user data text_. All other elements, including text tracks, must be specified using Macintosh language codes.

__Note:__ ISO 639-2/T codes do not distinguish between certain language variations. Use an extended language tag atom ('elng') to make these distinctions. For example, ISO 639-2T does not distinguish between traditional and simplified Chinese, so also use 'elng' with the value "zh-Hant" or "zh-Hans", respectively. See [Extended Language Tag Atom](Movie%20Atoms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgqwvgvzrgy).

### Macintosh Language Codes

[Table 5-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgywtgnbtguzq) lists some of the Macintosh language codes supported by QuickTime.

__Table 5-1__  QuickTime language code values

| Language | Value | Language | Value |
| English | 0 | Georgian | 52 |
| French | 1 | Moldavian | 53 |
| German | 2 | Kirghiz | 54 |
| Italian | 3 | Tajiki | 55 |
| Dutch | 4 | Turkmen | 56 |
| Swedish | 5 | Mongolian | 57 |
| Spanish | 6 | MongolianCyr | 58 |
| Danish | 7 | Pashto | 59 |
| Portuguese | 8 | Kurdish | 60 |
| Norwegian | 9 | Kashmiri | 61 |
| Hebrew | 10 | Sindhi | 62 |
| Japanese | 11 | Tibetan | 63 |
| Arabic | 12 | Nepali | 64 |
| Finnish | 13 | Sanskrit | 65 |
| Greek | 14 | Marathi | 66 |
| Icelandic | 15 | Bengali | 67 |
| Maltese | 16 | Assamese | 68 |
| Turkish | 17 | Gujarati | 69 |
| Croatian | 18 | Punjabi | 70 |
| Traditional Chinese | 19 | Oriya | 71 |
| Urdu | 20 | Malayalam | 72 |
| Hindi | 21 | Kannada | 73 |
| Thai | 22 | Tamil | 74 |
| Korean | 23 | Telugu | 75 |
| Lithuanian | 24 | Sinhala | 76 |
| Polish | 25 | Burmese | 77 |
| Hungarian | 26 | Khmer | 78 |
| Estonian | 27 | Lao | 79 |
| Lettish | 28 | Vietnamese | 80 |
| Latvian | 28 | Indonesian | 81 |
| Saami | 29 | Tagalog | 82 |
| Sami | 29 | MalayRoman | 83 |
| Faroese | 30 | MalayArabic | 84 |
| Farsi | 31 | Amharic | 85 |
| Russian | 32 | Galla | 87 |
| Simplified Chinese | 33 | Oromo | 87 |
| Flemish | 34 | Somali | 88 |
| Irish | 35 | Swahili | 89 |
| Albanian | 36 | Kinyarwanda | 90 |
| Romanian | 37 | Rundi | 91 |
| Czech | 38 | Nyanja | 92 |
| Slovak | 39 | Malagasy | 93 |
| Slovenian | 40 | Esperanto | 94 |
| Yiddish | 41 | Welsh | 128 |
| Serbian | 42 | Basque | 129 |
| Macedonian | 43 | Catalan | 130 |
| Bulgarian | 44 | Latin | 131 |
| Ukrainian | 45 | Quechua | 132 |
| Belarusian | 46 | Guarani | 133 |
| Uzbek | 47 | Aymara | 134 |
| Kazakh | 48 | Tatar | 135 |
| Azerbaijani | 49 | Uighur | 136 |
| AzerbaijanAr | 50 | Dzongkha | 137 |
| Armenian | 51 | JavaneseRom | 138 |
| Unspecified | 32767 |  |  |

### ISO Language Codes

Because the language codes specified by ISO 639-2/T are three characters long, they must be packed to fit into a 16-bit field. The packing algorithm must map each of the three characters, which are always lowercase, into a 5-bit integer and then concatenate these integers into the least significant 15 bits of a 16-bit integer, leaving the 16-bit integer’s most significant bit set to zero.

One algorithm for performing this packing is to treat each ISO character as a 16-bit integer. Subtract 0x60 from the first character and multiply by 2^10 (0x400), subtract 0x60 from the second character and multiply by 2^5 (0x20), subtract 0x60 from the third character, and add the three 16-bit values. This will result in a single 16-bit value with the three codes correctly packed into the 15 least significant bits and the most significant bit set to zero.

Example: The ISO language code `'jpn'` consists of the three hexadecimal values 0x6A, 0x70, 0x6E. Subtracting 0x60 from each value yields the values 0xA, 0x10, 0xE, as shown in [Table 5-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgywtgnjrgmzq).

__Table 5-2__  5-bit values of UTF-8 characters

| Character | UTF-8 code | 5-bit value | Shifted value |
| j | 0x6A | 0xA (01010) | 0x2800 (01010..........) |
| p | 0x70 | 0x10 (10000) | 0x200 (.....10000.....) |
| n | 0x6E | 0xE (01110) | 0xE (..........01110) |

The first value is shifted 10 bits to the left (multiplied by 0x400) and the second value is shifted 5 bits to the left (multiplied by 0x20). This yields the values 0x2800, 0x200, 0xE. When added, this results in the 16-bit packed language code value of 0x2A0E.

## Calendar Date and Time Values

QuickTime movies store date and time information in Macintosh date format: a 32-bit value indicating the number of seconds that have passed since midnight January 1, 1904.

This value does not specify a time zone. Common practice is to use local time for the time zone where the value is generated.

It is strongly recommended that all calendar date and time values be stored using UTC time, so that all files have a time and date relative to the same time zone.

## Matrices

QuickTime files use matrices to describe spatial information about many objects, such as tracks within a movie.

A transformation matrix defines how to map points from one coordinate space into another coordinate space. By modifying the contents of a transformation matrix, you can perform several standard graphics display operations, including translation, rotation, and scaling. The matrix used to accomplish two-dimensional transformations is described mathematically by a 3-by-3 matrix.

All values in the matrix are 32-bit fixed-point numbers divided as 16.16, except for the {u, v, w} column, which contains 32-bit fixed-point numbers divided as 2.30. [Figure 5-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgywtcobxgazq) and [Figure 5-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgywtcobxga3q) depict how QuickTime uses matrices to transform displayed objects.

__Figure 5-1__  How display matrices are used in QuickTime

（原归档配图获取待重试：`qt_l_054.gif`）

__Figure 5-2__  Applying the transform

（原归档配图获取待重试：`qt_l_028.gif`）

## Graphics Modes

QuickTime files use graphics modes to describe how one video or graphics layer should be combined with the layers beneath it. Graphics modes are also known as transfer modes. Some graphics modes require a color to be specified for certain operations, such as blending to determine the blend level. QuickTime uses the graphics modes defined by Apple’s QuickDraw.

The most common graphics modes are and `ditherCopy`, which simply indicate that the image should not blend with the image behind it, but overwrite it. QuickTime also defines several additional graphics modes.

[Table 5-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgywtemzsge2a) lists the additional graphics modes supported by QuickTime.

__Table 5-3__  QuickTime graphics modes

| Mode | Uses opcolor | Code | Description |
| Copy |  | 0x0 | Copy the source image over the destination. |
| Dither copy |  | 0x40 | Dither the image (if needed), otherwise do a copy. |
| Blend | yes | 0x20 | Replaces destination pixel with a blend of the source and destination pixel colors, with the proportion for each channel controlled by that channel in the opcolor. |
| Transparent | yes | 0x24 | Replaces the destination pixel with the source pixel if the source pixel isn't equal to the opcolor. |
| Straight alpha |  | 0x100 | Replaces the destination pixel with a blend of the source and destination pixels, with the proportion controlled by the alpha channel. |
| Premul white alpha |  | 0x101 | Premultiplied with white means that the color components of each pixel have already been blended with a white pixel, based on their alpha channel value. Effectively, this means that the image has already been combined with a white background. First, remove the white from each pixel and then blend the image with the actual background pixels. |
| Premul black alpha |  | 0x102 | Premultiplied with black is the same as pre-multiplied with white, except the background color that the image has been blended with is black instead of white. |
| Straight alpha blend | yes | 0x104 | Similar to straight alpha, but the alpha value used for each channel is the combination of the alpha channel and that channel in the opcolor. |
| Composition (dither copy) |  | 0x103 | (Tracks only) The track is drawn offscreen, and then composed onto the screen using dither copy |

## RGB Colors

Many atoms in the QuickTime file format contain RGB color values. These are usually stored as three consecutive unsigned 16-bit integers in the following order: red, green, blue.

## Balance

Balance values are represented as 16-bit, fixed-point numbers that range from -1.0 to +1.0. The high-order 8 bits contain the integer portion of the value; the low-order 8 bits contain the fractional part. Negative values weight the balance toward the left speaker; positive values emphasize the right channel. Setting the balance to 0 corresponds to a neutral setting.

[Next](Some%20Useful%20Examples%20and%20Scenarios.md)[Previous](Media%20Data%20Atom%20Types.md)
