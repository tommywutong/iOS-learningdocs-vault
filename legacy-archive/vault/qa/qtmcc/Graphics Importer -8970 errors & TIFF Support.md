---
title: Graphics Importer -8970 errors & TIFF Support
apple_id: DTS10001961
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2011-07-11'
source_url: https://developer.apple.com/library/archive/qa/qtmcc/qtmcc18.html
archived_at: '2026-07-18T02:38:47.403099Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/QuickTime/index.html) > [Import & Export](https://developer.apple.com/library/archive/technicalqas/QuickTime/idxImportExport-date.html) >

|  |
| --- |
| Technical Q&A QTMCC18Graphics Importer -8970 errors & TIFF Support |

|  |
| --- |
| ---   Q: My application uses graphics importers extensively for importing TIFF files. I have encountered a problem that only occurs when trying to import certain TIFF files. I first call `GetGraphicsImporterForFile`, which correctly returns an importer instance and no error. I then call `GraphicsImportGetImageDescription`, which returns a `-8970` error. I can't figure out what might be going on since the importer instance seems to be perfectly valid. What does this error signify?  A: Graphics importers and image decompressors will return `codecDataVersErr (-8970)` if they find that the compressed data is an unsupported format or variant and will return `codecBadDataErr (-8969)` if they find the compressed data corrupted -- i.e., the data violates some part of the specification.  The TIFF specification does not restrict the possible variations of TIFF files, but only attempts to codify how a variation would be described so that independent implementations can interoperate. QuickTime's TIFF support does not attempt to implement arbitrary variations and also does not support some specific TIFF compression formats -- TIFF/JPEG 6 and TIFF/JPEG 7 in particular.  QuickTime's TIFF graphics importer supports most of the TIFF variations in common use, and some strange variations.  As of QuickTime 4.1.2, this support includes:   - Big and little-endian byte layout; - Uncompressed, PackBits, LZW, CCITT 1D, Group 3 (T.4) Fax (both 1D and 2D) and Group 4 (T.6) Fax compression; - 1, 2, 4, 8 and 16 bit Grayscale (both `BlackIsZero` and `WhiteIsZero`, both with and without alpha channels); - 1, 2, 4 and 8 bit RGB Palette (and 8-bit RGB Palette with alpha channel); - 4, 8 and 16 bit per channel RGB; - 4, 8 and 16 bit per channel RGB with alpha channel; - 8 bit per channel CMYK; - 8 bit per channel YCbCr (with chroma subsampling up to 4x4); - Both chunky and planar channel layouts for most depths; - Both strips and tiles; and - Both normal and reversed bit order for fax files.   If you have a TIFF file (or a file in any other still image format supported by QuickTime) that cannot be viewed with the PictureViewer application, but can be viewed with other applications, let us know.  There are two ways to do this:  1. Write up a bug report using the Apple Bug Reporting form [http://developer.apple.com/bugreporter/](https://developer.apple.com/bugreporter/), and include a URL to the sample file.  2. Send an e-mail message with the sample file to [dts@apple.com](mailto:dts@apple.com).  We cannot reliably fix issues we cannot reproduce; therefore, it is vital that you include the image file. It is also useful to mention what process was used to create the file and what applications are able to view the file correctly if this information is available. [Nov 29 2000] |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
