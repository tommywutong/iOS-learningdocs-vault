---
title: CIVideoDemoGL
apple_id: DTS10003623
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: QuartzCore
published: '2007-10-03'
source_url: https://developer.apple.com/library/archive/samplecode/CIVideoDemoGL/History/History.html
archived_at: '2026-07-18T03:02:41.844407Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CIVideoDemoGL](CIVideoDemoGL.md)


[Previous](VideoView.m.md)

# Document Revision History

This table describes the changes to _CIVideoDemoGL_.

| __Date__ | __Notes__ |
| 2007-10-03 | Added the ability to use a custom 'trick' profile with the kQTVisualContextOutputColorSpaceKey key. |
| 2007-05-22 | Now creates a CIContext and QTOpenGL Texture Context with the current display color space. Removed the use of kCVPixelBufferWidthKey and kCVPixelBufferHeightKey which would cause scaling with multi-track movies having different image dimensions in each track resulting in different visuals when compared with QuickTime Player. Added support for iPod export. Fixed <r.4751589>. |
| 2005-10-14 | Updated to produce a universal binary, a minor code change in VideoView.m was required work around <Radar #4295828> on Developer Transition Kit . |

[Previous](VideoView.m.md)

