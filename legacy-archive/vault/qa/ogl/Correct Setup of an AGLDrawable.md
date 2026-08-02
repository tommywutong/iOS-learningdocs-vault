---
title: Correct Setup of an AGLDrawable
apple_id: DTS10001481
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-10-04'
source_url: https://developer.apple.com/library/archive/qa/ogl/ogl02.html
archived_at: '2026-07-18T02:29:48.201638Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Graphics & Imaging > OpenGL](https://developer.apple.com/referencelibrary/GraphicsImaging/idxOpenGL-date.html)

|  |
| --- |
| Technical Q&A OGL02Correct Setup of an AGLDrawable |

|  |
| --- |
| ---   __Q: How do I correctly set up and `AGLDrawable`?__  A. One uses `aglSetDrawable` to attach an `AGLDrawable` to an `AGLContext`. This function is declared as follows:   ```     GLboolean aglSetDrawable (AGLContext context, AGLDrawable drawable); ```  - where context is a valid context return from `aglCreateContext`.    drawable is an `AGLDrawable`, which is defined in `<AGL.h>` as a `CGrafPtr`. This `AGLDrawable` must be a `CGrafPtr` obtained from a valid window. Under Mac OS 9 one can directly cast a `WindowPtr` to an `AGLDrawable`. Carbon is more restrictive due to it's opaque data references. One must use the function `GetWindowPort` to properly obtain a `AGLDrawable` from an opaque `WindowPtr` or `WindowRef`.    The following example code can be used, on Mac OS 9 without Carbon and on Mac OS 9 and Mac OS X with Carbon, to ensure the proper type is passed to the `aglSetDrawable` function:   ```     #if TARGET_API_MAC_CARBON         aglSetDrawable (context, GetWindowPort (pWindow));     #else         aglSetDrawable (context, (AGLDrawable) pWindow);     #endif // TARGET_API_MAC_CARBON ```    __Q. What about DrawSprocket's front buffer? Isn't that really just a `CGrafPtr`?__  A. Not really, DrawSprocket's front buffer is a non-standard `CGrafPtr` that causes problems for OpenGL when trying to identify the correct display device for rendering. This front buffer should never be used as an `AGLDrawable`. Instead one should create a window on top of the DrawSprocket blanking window and use this window to get your `AGLDrawable`.      __Q. So I've done all this and my application is still crashing on the call to `AGLSetDrawable`. How can I fix this?__  A. If you're using pre-compiled headers such as `<MacHeaders.h>`, you will need to instead use MacHeadersCarbon.h. Since the pre-compiled headers set the compiler flags when they are pre-compiled not when you compile your code, there is no way for these headers to know if you are targeting Carbon or not. When not compiling for Carbon `GetWindowPort` is defined in `<MacWindows.h>` as:   ```     #define GetWindowPort(w) ((CGrafPtr) (w)) ```  This results in a simple cast which does not work with Carbon's opaque data structures. To avoid this problem ensure you are using the correct pre-compiled headers for the environment you are building.     ---  Updated: 4-October-2000 |

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
