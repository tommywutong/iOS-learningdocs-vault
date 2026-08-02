---
title: GLCameraRipple
apple_id: DTS40011222
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2013-02-21'
source_url: https://developer.apple.com/library/archive/samplecode/GLCameraRipple/Introduction/Intro.html
archived_at: '2026-07-18T03:09:50.720227Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# GLCameraRipple

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2013-02-21 Remove bridge cast when CVEAGLContext is defined to be a EAGLContext. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmrsgiwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | iOS SDK 5.0 or later. |
| __Runtime Requirements:__ | iOS 5.0 or later. This app will only work on device because of camera input requirement. Due to the app's heavy use of CPU, performance may be sub-optimal when running debug builds on certain devices. |

This sample demonstrates how to use the AVFoundation framework to capture YUV frames from the camera and process them using shaders in OpenGL ES 2.0. CVOpenGLESTextureCache, which is new to iOS 5.0, is used to provide optimal performance when using the AVCaptureOutput as an OpenGL texture. In addition, a ripple effect is applied by modifying the texture coordinates of a densely tessellated quad.

[Next](ReadMe.txt.md)

