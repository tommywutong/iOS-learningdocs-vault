---
title: API Changes in Snow Leopard
apple_id: TP40007673
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2008-06-09'
source_url: https://developer.apple.com/library/archive/releasenotes/MacOSX/SnowLeopard_API_ReleaseNote/OpenGL.html
archived_at: '2026-07-18T02:58:45.197902Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [API Changes in Snow Leopard](API%20Changes%20in%20Snow%20Leopard.md)


[ADC Home](https://developer.apple.com/) >
[Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) >
Release Notes >
OS X >
[API Changes in Snow Leopard Developer Preview](API%20Changes%20in%20Snow%20Leopard.md) >

# OpenGL Changes

## OpenGL

CGLDevice.hAdded CGLGetCGLContextShareGroup()Added CGLShareGroupCGLMacro.hRemoved #def glGetTexParameterIiuvEXTAdded #def glClampColorARBAdded #def glGetTexParameterIuivEXTCGLRenderers.hAdded #def kCGLRendererIDMatchingMaskAdded #def kCGLRendererIntelX3100IDOpenGL.hAdded CGLSetFullScreenOnDisplay()glext.hRemoved #def GL_COLOR_INDEX12_EXTRemoved #def GL_COLOR_INDEX16_EXTRemoved #def GL_COLOR_INDEX1_EXTRemoved #def GL_COLOR_INDEX2_EXTRemoved #def GL_COLOR_INDEX4_EXTRemoved #def GL_COLOR_INDEX8_EXTRemoved #def GL_EXT_paletted_textureRemoved #def GL_TEXTURE_INDEX_SIZE_EXTRemoved glGetTexParameterIiuvEXT()Removed glGetTexParameterIiuvEXTProcPtr (no architecture available)Added #def GL_ARB_color_buffer_floatAdded #def GL_CLAMP_FRAGMENT_COLOR_ARBAdded #def GL_CLAMP_READ_COLOR_ARBAdded #def GL_CLAMP_VERTEX_COLOR_ARBAdded #def GL_FIXED_ONLY_ARBAdded #def GL_RGBA_FLOAT_MODE_ARBAdded glClampColorARB()Added glClampColorARBProcPtr (no architecture available)Added glGetTexParameterIuivEXT()Added glGetTexParameterIuivEXTProcPtr (no architecture available)Modified glGetColorTableParameterfvEXT()

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

Modified glGetColorTableParameterivEXT()

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

Modified glGetColorTableEXT()

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

Modified glColorSubTableEXT()

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

Modified glColorTableEXT()

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64,i386,x86_64 |
| New | none? |

gliContext.hAdded GLIShared

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
