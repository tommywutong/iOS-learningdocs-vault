---
title: Understanding the bytes per row value returned by CVPixelBufferGetBytesPerRow
apple_id: DTS40014453
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: null
published: '2014-05-01'
source_url: https://developer.apple.com/library/archive/qa/qa1829/_index.html
archived_at: '2026-07-18T02:35:06.092869Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1829

# Understanding the bytes per row value returned by CVPixelBufferGetBytesPerRow

## Q:  Why does `CVPixelBufferGetBytesPerRow` not always return a value equal to the width of the pixel buffer multiplied by the bytes per pixel?

A: There are differences in the hardware alignment requirements between the various hardware platforms. The `CVPixelBufferGetBytesPerRow` function will correctly report the buffer alignment (stride) being used by the particular hardware.

You should always write your code to account for any padding so that it works across all platforms. Do not assume the buffer alignment will be the same on different hardware. Pay attention to the bytes per row when you are processing each row of data.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-05-01 | New document that discusses why CVPixelBufferGetBytesPerRow may not return a value equal to the width of the pixel buffer multiplied by the bytes per pixel. |

