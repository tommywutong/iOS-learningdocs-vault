---
title: Large Image Downsizing
apple_id: DTS40011173
resource_type: Sample Code
platform: watchOS|iOS
topic: Graphics & Animation
technology: null
published: '2014-03-27'
source_url: https://developer.apple.com/library/archive/samplecode/LargeImageDownsizing/Introduction/Intro.html
archived_at: '2026-07-18T03:13:26.190231Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# Large Image Downsizing

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2014-03-27 Updated for iOS 7 SDK. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmjxgmwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | iOS SDK 7 or later |
| __Runtime Requirements:__ | iOS 6 or later |

This code sample demonstrates a way to support displaying very large images in limited memory environments by turning a large image on disk into a smaller image in memory. This is useful in situations where the original image is too large to fit into memory as required for it to be displayed.

Having useful implications in supporting user defined documents, it should be noted that the photo roll or document sharing drop are the locations that a large image would exist. For simplicity this sample reads a large image from the bundle.

Supported formats are: PNG, TIFF, JPEG. Unsupported formats: GIF, BMP, interlaced images.

[Next](ReadMe.txt.md)

