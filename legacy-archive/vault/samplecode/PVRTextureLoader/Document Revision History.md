---
title: PVRTextureLoader
apple_id: DTS40008121
resource_type: Sample Code
platform: iOS
topic: Graphics & Animation
technology: OpenGLES
published: '2014-03-25'
source_url: https://developer.apple.com/library/archive/samplecode/PVRTextureLoader/History/History.html
archived_at: '2026-07-18T03:18:39.117952Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PVRTextureLoader](PVRTextureLoader.md)


[Previous](Classes-PVRTextureLoaderAppDelegate.m.md)

# Document Revision History

This table describes the changes to _PVRTextureLoader_.

| __Date__ | __Notes__ |
| 2014-03-25 | Removed warnings. Updated for iOS 7. Updated for 64-bit. |
| 2010-06-25 | Changed deployment target back to iPhone OS 3.2 and added CFBundleIconFiles in Info.plist. |
| 2010-06-18 | Upgraded project to build with the iOS 4 SDK. |
| 2010-04-30 | Modified the script so that it works regardless of where texturetool is installed. |
| 2010-01-29 | The availability of GL extensions referenced in this sample are now checked before they are used. The proper min filter texture parameter is set depending on if a texture is going to be mipmapped or not. This provides a hint to GL in order to decrease memory usage. Texture generation now sets the kCGBlendModeCopy blend mode before drawing since the previous contents of memory aren't used. This avoids unnecessary blending. |
| 2009-04-07 | Fixed a bug in the Encode Images script. |
| 2008-12-08 | This application illustrates how to load PVR texture files and then display them using OpenGL. |

[Previous](Classes-PVRTextureLoaderAppDelegate.m.md)

