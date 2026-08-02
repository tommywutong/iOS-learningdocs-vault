---
title: Requirements for Quartz GL
apple_id: DTS10004412
resource_type: QA
platform: macOS
topic: Performance
technology: AppKit
published: '2008-08-08'
source_url: https://developer.apple.com/library/archive/qa/qa1536/_index.html
archived_at: '2026-07-18T02:32:15.350870Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1536

# Requirements for Quartz GL

## Q:  What are the system requirements for Quartz GL?

A: Quartz GL requires a video card that supports the [GL_ARB_fragment_program](https://developer.apple.com/graphicsimaging/opengl/extensions.html#GL_ARB_fragment_program) and [GL_ARB_texture_non_power_of_two](https://developer.apple.com/graphicsimaging/opengl/extensions.html#GL_ARB_texture_non_power_of_two) OpenGL extensions.

You can enable Quartz GL for all windows in your application by adding the `QuartzGLEnable` key to your `Info.plist`. A value of `true` indicates that you are requesting Quartz GL when available, and a value of `false` indicates that you do not wish to use Quartz GL, even if you request it programatically. When enabling Quartz GL through your `Info.plist` there is an additional requirement that at least 1GB of RAM must be installed.

Cocoa applications can programatically enable Quartz GL for a specific window using the NSWindow method [setPreferredBackingLocation:](https://developer.apple.com/documentation/appkit/nswindow/1419102-preferredbackinglocation). Carbon applications can call `HIWindowSetBackingLocation` to enable Quartz GL for a specific window. In both cases specifying the location of the window backing store as video memory enables Quartz GL for that window.

If you need to test your application under Quartz GL and your system does not meet these requirements, you can forcibly enable Quartz GL using Quartz Debug in `/Developer/Applications/Performance Tools/`.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-03-06 | Document the QuartzGLEnable property list key and HIWindowSetBackingLocation(). Fixed typos. |
| 2008-08-08 | Document the QuartzGLEnable property list key and HIWindowSetBackingLocation(). Fixed typos. |
| 2007-12-12 | New document that describes the requirements for enabling Quartz GL. |

