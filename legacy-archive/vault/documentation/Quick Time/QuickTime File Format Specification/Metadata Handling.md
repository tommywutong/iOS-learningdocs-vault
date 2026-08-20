---
title: QuickTime File Format Specification
apple_id: TP40000939
resource_type: Guide
platform: macOS
topic: Data Management
technology: QuickTime
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/QuickTime/QTFF/QTFFAppenD/QTFFAppenD.html
archived_at: '2026-07-27T06:57:06.744316Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [QuickTime File Format Specification](Introduction%20to%20QuickTime%20File%20Format%20Specification.md)


[Next](Summary%20of%20VR%20World%20and%20Node%20Atom%20Types.md)[Previous](Random%20Access.md)

# Metadata Handling

This appendix describes how metadata is handled when QuickTime imports other file formats. (For more information about metadata, refer to [Overview of QTFF](Overview%20of%20QTFF.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgmwueqsdi5ceircg) and [Compressed Movie Resources](Movie%20Atoms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrqgqwtgmztgezq)).

These formats are grouped into the following categories and sections:

- [Digital Video File Formats](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgewtembtgayq)
- [Digital Audio File Formats](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgewtembtgizq)
- [Still Image File Formats](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgewtembtgu4a)
- [Animation and 3D File Formats](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzzfvbuqmrrgewtembthe3q)

Each section includes a table with specific details on the following, where applicable:

- The format supported by QuickTime—for example, the movie import component or the graphics import component
- The Macintosh file type—for example, `'Mp3 '`
- File name extensions––for example, `.mp3`
- Specific details for metadata handling—for example, all Microsoft-defined “tombstone” data is transferred to the imported movie’s user data. metadata fields that have QuickTime equivalents are mapped as follows.
- Software required—for example, QuickTime 3 or later

## Digital Video File Formats

| OpenDML and other AVI files | Description |
| --- | --- |
| Supported by | Movie import component |
| Macintosh file type | `'VfW '` |
| File name extensions | `.avi` |
| metadata handling | All Microsoft-defined “tombstone” data is transferred to the imported movie’s user data. metadata fields that have QuickTime equivalents are mapped as follows: `'ICOP'` maps to `kUserDataTextCopyright`, `'ISBJ'` maps to `kUserDataTextInformation`, `'INAM'` maps to `kUserDataTextFullName`, `'ICRD'` maps to `'©day'`, `'IMED'` maps to `'©fmt'`, `'ISRC'` maps to `'©src'`.Where no QuickTime equivalent exists, the metadata item’s four-character code is modified by replacing the initial `I` with the symbol `©`. All other characters remain unchanged. |
| Software required | QuickTime 3 |

## Digital Audio File Formats

| MPEG 1 layer 3 | Description |
| --- | --- |
| Supported by | Movie import component |
| Macintosh file type | `'Mp3 '`, `'SwaT'`, `'MPEG'`, `'PLAY'`, `'MPG3'`, `'MP3 '` |
| File name extensions | `.mp3, .swa` |
| Metadata handling | Metadata from ID3v1-style MP3 files is imported into the QuickTime movie.Title maps to `kUserDataTextFullName`, artist maps to `'©ART'`, album maps to `'©alb'`, year maps to `'©day'`, comment maps to `'©cmt'`, and track number maps to `'©des'`. |
| Software required | QuickTime 4 |

| WAV | Description |
| --- | --- |
| Supported by | Movie import component |
| Macintosh file type | `'WAVE'`, `'.WAV'` |
| File name extensions | `.wav` |
| Metadata handling | All Microsoft-defined “tombstone” data is transferred to the imported movie’s user data. metadata fields that have QuickTime equivalents are mapped as follows: `'ICOP'` maps to `kUserDataTextCopyright`, `'ISBJ'` maps to `kUserDataTextInformation`, `'INAM'` maps to `kUserDataTextFullName`, `'ICRD'` maps to `'©day'`, `'IMED'` maps to `'©fmt'`, `'ISRC'` maps to `'©src'`.Where no QuickTime equivalent exists, the metadata item’s four-character code is modified by replacing the initial `I` with the symbol `©`. All other characters remain unchanged. |
| Software required | QuickTime 2.5 or later |

## Still Image File Formats

| FlashPix | Description |
| --- | --- |
| Supported by | Graphics import component |
| Macintosh file type | `'FPix'` |
| File name extensions | `.fpx` |
| Metadata handling | Information about copyright, authorship, caption text, content description notes, camera manufacturer name, camera model name are transferred to `kUserDataTextCopyright`, `kUserDataTextArtistField`, `kUserDataTextFullName`, `kParameterInfoWindowTitle`, `kParameterInfoManufacturer`, `kUserDataTextMakeField` user data items, respectively. |
| Formats supported | 1.0 |
| Software required | QuickTime 4 |

| GIF | Description |
| --- | --- |
| Supported by | Graphics import component |
| Macintosh file type | `'GIFf'`, or `'GIF '` |
| File name extensions | `.gif` |
| Metadata handling | The GIF comment field is transferred to the `kUserDataDateTextInformation` user data item. |
| Software required | QuickTime 2.5 or later |

| JFIF/JPEG | Description |
| --- | --- |
| Supported by | Graphics import component |
| Macintosh file type | `'JPEG’` |
| File name extensions | `.jpg` |
| Metadata handling | The JFIF comment field is transferred to the imported Movie’s user data in the `kUserDataTextInformation` field. |
| Software required | QuickTime 2.5 or later |

| Photoshop | Description |
| --- | --- |
| Supported by | Graphics import component |
| Macintosh file type | `'8BPS'` |
| File name extensions | `.psd` |
| Metadata handling | Photoshop files store their metadata based on the IPTC-NAA Information Interchange Model and Digital Newsphoto Parameter Record. This information is transferred into the importer Movie’s user data. The entire ITPC-NAA record is placed into a user data item of type `'iptc'`. In addition, those metadata items which are defined by QuickTime are mapped directly to QuickTime types as follows: 116 to `kUserDataTextCopyright`, 120 to `kUserDataTextInformation`, 105 to `kUserDataTextFullName`, 55 to `'©day'`, 115 to `'©src'`. |
| Software required | QuickTime 2.5 or later. QuickTime 3 is required for metadata handling. |

| QuickTime Image File | Description |
| --- | --- |
| Supported by | Graphics import component |
| Macintosh file type | `'qtif'` |
| File name extensions | `.qtif`, `.qif`, `.qti` |
| Metadata handling | Metadata that is stored in `quickTimeImageFileMetaDataAtom` atom is copied directly to the Movie’s user data. |
| Formats supported | All |
| Software required | QuickTime 2.5 or later |

| TIFF | Description |
| --- | --- |
| Supported by | Graphics Import Component |
| Macintosh file type | `'TIFF'` |
| File name extensions | `.tif`, `.tiff` |
| Metadata handling | Extracted from standard tags and from IPTC block |
| Software required | QuickTime 3 or later |

## Animation and 3D File Formats

| Animated GIF | Description |
| --- | --- |
| Supported by | Movie import component |
| Macintosh file type | `'GIFf'` |
| File name extensions | `.gif` |
| Metadata handling | The GIF comment field is transferred to `kUserDataTextInformation` user data item. |
| Software required | QuickTime 3 or later |

[Next](Summary%20of%20VR%20World%20and%20Node%20Atom%20Types.md)[Previous](Random%20Access.md)
