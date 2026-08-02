---
title: qtreadwritejpeg
apple_id: DTS10000873
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/qtreadwritejpeg/Introduction/Intro.html
archived_at: '2026-07-26T19:52:46.764251Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](QTReadWriteJPEG.c.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

# qtreadwritejpeg

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Illustrates how to compress and decompress JPEG images using QuickTime. |
| __Build Requirements:__ | Code Warrior |
| __Runtime Requirements:__ | Carbon |

__Important__ This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

Legacy - While this sample shows some internals of the JPEG format, developers should either use QuickTime Graphics Importers/Exporters or the ImageIO framework which is part of Application Services on Mac OS X 10.4.x+.
This sample code has been updated for QuickTime 5.0 and illustrates how to compress and decompress JPEG images using QuickTime. We use the FCompressImage function, but you could also use the CompressImage function. Although this sample demonstrates only JPEG compression/decompression, you could use this as a framework for other types of compression (except for the decoding of the JPEG header). This code is based largely on the existing code sample "JPEG Sample". This newer version is uncoupled from the Mac application framework they used and now runs on Windows. It is a single utility C source file.

[Next](QTReadWriteJPEG.c.md)

