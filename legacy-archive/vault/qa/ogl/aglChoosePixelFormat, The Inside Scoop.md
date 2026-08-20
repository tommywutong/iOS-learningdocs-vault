---
title: aglChoosePixelFormat, The Inside Scoop
apple_id: DTS10001480
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-04-03'
source_url: https://developer.apple.com/library/archive/qa/ogl/ogl01.html
archived_at: '2026-07-18T02:29:48.154848Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Graphics & Imaging > OpenGL](https://developer.apple.com/referencelibrary/GraphicsImaging/idxOpenGL-date.html)

|  |
| --- |
| Technical Q&A OGL01aglChoosePixelFormat, The Inside Scoop |

|  |
| --- |
| ---   Q: So, having read the documentation, I still do not understand why `aglChoosePixelFormat` fails to return a hardware accelerated (HWA) and/or valid pixel format. Can you explain what it is doing and how to fix it?  A: Okay, here is how it works.  The key is the way `aglChoosePixelFormat` handles graphics devices. Obviously, by specifying a `GDevice` or set of `GDevices`, `aglChoosePixelFormat` just considers the supplied set. If you don't pass a `GDevice` it considers all devices, including the overlapping case (where a window spans more than one monitor), which can only be handled by the software renderer.  So, assume you pass NULL in the device list parameter. `aglChoosePixelFormat` will look at all devices and pick the best renderer on each device that can satisfy the pixel format request given. If any device (including the overlapping case) fails to find an applicable format, `aglChoosePixelFormat` fails and returns NULL. This could be due to an error in the supplied parameters or just due to no match being found. In any case, you should check `aglGetError` after the call to `aglChoosePixelFormat` and pass non-zero results to `aglErrorString` to find the error. This does not mean that a pixel format was not found; it would mean at some level an error was seen. It is up to the application to determine what to do if an error occurs and a valid (non-NULL) pixel format is returned.  Q: Where does this fail?  A: In the above case, if you pass `AGL_ACCELERATED` as a parameter, you WILL fail since the software renderer (which covers the overlapping case) is not accelerated. If you have a non-compliant (i.e., RAGE II) renderer driving a display and do not pass `AGL_ALL_RENDERERS` you WILL fail. Also, if there is anything that you requested that cannot be satisfied on ALL renderers you will fail.  Q: What this does NOT mean?  A: This does NOT mean that `aglChoosePixelFormat` will look at all the renderers and pick the least common denominator; that is not how it works. For example, I have a Mach64-based card and an ATI Rage 128 card and I request a basic RGBA, double-buffered format. If my window is wholly on the Rage 128 monitor, I will see the HWA renderer. If it is between monitors or on the Mach64 driven display, I will see the software renderer.  Q: What happens when `GDevices` are passed to `aglChoosePixelFormat`?  A: It will only consider that/those device(s) when choosing the format; everything else will be the same. Thus, you will not get the default to software in the overlapping case and if your drawable is on a `GDevice` not passed to `aglChoosePixelFormat`, nothing will draw since no pixel format was chosen.  Q: What are the signs that things are working?  A: Try passing in all the `GDevices` on your system and see what happens. This should just eliminate the overlapping case, which currently is only supported by the software renderer. If you cannot choose a pixel format, then one of your devices does not support one of the attributes you requested. If your application now works, it is very likely that some of your drawable was crossing over between monitors.  Q: Is it appropriate to explicitly request `AGL_ACCELERATED`?  A: You do not have to explicitly request `AGL_ACCELERATED`. If you do, you cannot pass NULL as the `GDevice` into `aglChoosePixelFormat` or you will not find any matches since the software renderer will not match the accelerated case. If you do not, an accelerated renderer will still be chosen for devices that can provide a hardware renderer that support your other parameters, and the software renderer will support the other displays and the overlapping case. If you explicitly need a HWA context for your application, request `AGL_ACCELERATED` and pass the `GDevices` you are interested in using into `aglChoosePixelFormat`. If possible, this will choose HWA renderers for all the devices passed in. A failure here means that one of the devices could not support the pixel format request.  Q: `If AGL_ACCELERATED` is not requested, why might the context not end up being accelerated?  A: The basic case occurs when the `GDevice`'s HWA renderer does not support the specific pixel format you request while the software renderer can support it; thus, you get the software renderer on that `GDevice`. As part of its renderer selection `aglChoosePixelFormat` uses current pixel depth as part of its selection criteria. It assumes you want the renderer right now, not later after you change the depth. If you call `aglChoosePixelFormat` on an 8-bit device you will like get only a software renderer since almost no HWA renderers support 8 bits per pixel acceleration.  Q: Is there any more information on the pixel format options than that found in the SDK documentation?  A: `AGL_ACCELERATED`: all returned pixel formats must be HWA or else fail.  `AGL_ALL_RENDERERS`: Renderers do NOT need to be OpenGL compliant (i.e., would use HWA RAGE II as an option). This allows consideration of non-compliant renderers.  `AGL_NO_RECOVERY`: You will not get a software fallback renderer for a hardware accelerated context (such as in a case where HWA runs out of resources). This does not affect the software renderer in the overlapping window case. Updated: 03-April-2000 |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
