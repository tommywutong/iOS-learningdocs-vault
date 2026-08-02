---
title: From A View to A Movie
apple_id: DTS40009025
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: null
published: '2013-01-02'
source_url: https://developer.apple.com/library/archive/samplecode/From_A_View_to_A_Movie/Introduction/Intro.html
archived_at: '2026-07-18T03:09:14.770447Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Sources-Classes-Application-Controller-OpenGLPlasmaExhibitsPrefPanelUIController.md)

# From A View to A Movie

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2013-01-02 Printing fix, more of the classes use opaque data references, updated math classes, updated color correction classes, Xcode project update, ReadMe update. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmbsguwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Mac OS X v10.8 Xcode v3.2 Xcode v3.2 |
| __Runtime Requirements:__ | Mac OS X v10.8 |

This application extends the sample "From A View to A picture", and further demonstrates hardware accelerated capture, HD color correction, and movie authoring pipeline from a view.

Again, the contents are 3D animated objects generated using OpenGL The individual (uncompressed) frames during a capture session are written into a framebuffer object. From there, starting with median white-point and color primaries provided by ColorSync for a display profile, linear transformations are computed, HD color correction is applied using a shader, and the results are captured as frames from an offscreen framebuffer using pixel buffer objects. Finally, the frames are written into a movie using QuickTime media authoring interfaces.

[Next](Sources-Classes-Application-Controller-OpenGLPlasmaExhibitsPrefPanelUIController.md)

