---
title: ExampleCodec
apple_id: DTS10000816
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ExampleCodec/Introduction/Intro.html
archived_at: '2026-07-18T03:07:53.336953Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](examplecodec.c.md)

# ExampleCodec

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 An example of am image compression codec that handles both compression and decompression of images. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

This is an example of am image compression codec that handles both compression and decompression of images as passed to it by the Image Compression manager. It is built as a Component Manager Component. The compression scheme here is 411 YUV. The image is stored as separate luminance and chrominance channels. For each 2x2 block of pixels in the source image we store 4 luminance (Y) components, 1 Y-Red component (U) and 1 Y-Blue (V) component. Each Y-component is stored as 6-bits, resulting in a savings of 2.4:1 over a 24-bit/pixel image (6\*4 + 2\*8)/4 = 10 bits/pixel. Requires: QuickTime Keywords: QuickTime, codec

[Next](examplecodec.c.md)

