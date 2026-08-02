---
title: QTKit Capture - Video Compression Options And Preview
apple_id: DTS40007992
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: QTKit
published: '2008-09-16'
source_url: https://developer.apple.com/library/archive/qa/qa1583/_index.html
archived_at: '2026-07-18T02:32:19.998393Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1583

# QTKit Capture - Video Compression Options And Preview

## Q:  When I change the Compression Options for a Movie File Output I see differences in my Video Preview View. Is the `QTCaptureView` previewing the compressed video?

A: When I change the Compression Options for a Movie File Output I see differences in my Video Preview View. Is the `QTCaptureView` previewing the compressed video?

No, `QTCaptureView` does not preview compressed frames. What you are seeing are resolution changes on the input device since the input device is automatically configured to provide optimal frame size for a capture sessions output.

For example, lets assume you have two file outputs connected to the capture session, one of which is set to compress at 640x480 and another is set to compress at 320x240. In this case, the input device will be configured to output frames of at least 640x480 to accommodate the higher resolution output. If the 640x480 output were removed, the input device could be dropped down to 320x240 since that would be the highest resolution requirement.

The `QTCaptureView` and underlying `QTCaptureVideoPreviewOutput` do not influence the camera resolution, they are purely part of the preview mechanism. Therefore, if you configure a file output in such a way that it compresses to a lower resolution, the preview view will reflect that resolution since the session is receiving frames at that resolution from the camera.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-09-16 | New document that describes how video compression options may influence the resolution of previewed video. |

