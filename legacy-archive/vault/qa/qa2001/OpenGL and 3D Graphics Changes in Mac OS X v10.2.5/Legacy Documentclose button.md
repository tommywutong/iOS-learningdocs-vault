---
title: OpenGL and 3D Graphics Changes in Mac OS X v10.2.5
apple_id: DTS10002293
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2003-04-29'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1258.html
archived_at: '2026-07-18T02:38:21.665232Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Graphics & Imaging > OpenGL](https://developer.apple.com/referencelibrary/GraphicsImaging/idxOpenGL-date.html)

|  |
| --- |
| Technical Q&A QA1258OpenGL and 3D Graphics Changes in Mac OS X v10.2.5 |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ---    Q: What changes were made in OpenGL and 3D graphics for Mac OS X v10.2.5?  A: The Mac OS X v10.2.5 software update adds support for the ATI Radeon 9700 Pro graphics processor and the `ATI_separate_stencil` OpenGL extension. In addition, this update provides numerous bug fixes, stability enhancements and performance improvements. Table 1 shows a representative list of 3D graphics improvements and bugs fixed which may affect developers.   |  | | --- | | __Table 1__. 3D Graphics Bug Fixes | | - Add ATI_separate_stencil support. (r. 3124619) - Fix ARB vertex program parser's ALIAS handling. (r. 3144510) - Fix ARB vertex blending interaction with lighting. (r. 3201658) - Correct glGenTextures case where duplicate texture names could be produced. (r. 3205529) - Reduce processing time for large display lists when they contain many primitives. (r. 3220938) - Correct NVIDIA driver versioning. (r. 3108918) - Update cube map texture alignment on NVIDIA to fix corruption issues. (r. 3123328) - Improved mirrored and external display handling. (r. 3132806, 3192127, 2948026) - Vertex array range operations improved, including correct handling of large index values on some NVIDIA hardware and handling large numbers of vertex array objects with vertex array ranges on ATI hardware. Note, developers should use `glGetIntegerv(MAX_VERTEX_ARRAY_RANGE_ELEMENT_APPLE, &maxindex)` to determine maximum array indexes which can be handled. (r. 3133247, 3176602) - DVD playback improved. (r. 3143872, 3133061, 3133209, 3155766) - Accelerate depth buffer writes. (r. 3179715) - glDrawPixels, glReadPixels and glCopyPixels stability improvements. (r. 3210478, 3205289, 3203371) - Add vertex buffers VRAM storage support for ATI. (r. 3091902) - Add variable ATI AGP memory mapping allowing larger amounts of AGP memory. (r. 3148822) - Improve GL_TRIANGLES acceleration on Radeon. (r. 3154410) - Fix COMPRESSED_ALPHA_ARB for ATI. (r. 3171044) - ATI color scaling updates to correct handling of scale factors for DOT3 case of GL_TEXTURE_ENV_COMBINE on some ATI hardware. (r. 3196041) - Fix texture compression to correctly compress uncompressed RGBA 4444 textures on some ATI hardware when requested. (r. 3199377, 3172440) - Improve low VRAM texture handling. (r. 3202818) - Improve VBL syncing methods for buffer flushes. (r. 3203896) - Accelerated glCopyTexSubImage2D for rectangular textures on ATI. (r. 3203906) - Improve UT2003 rendering on ATI. (r. 3205128, 3205193, 3205211, 3205222, 3132946, 3208100) - Fix texture creation with packed pixel data types and GL_UNPACK_SWAP_BYTES enabled. (r. 3196165) |   The `ATI_separate_stencil` extension provides the ability to modify the stencil buffer differently based on the facing direction of the primitive that generated the fragment. Use of this extension requires additional definitions to those provided in the OpenGL frameworks `glext.h` header file. A future developer tools update should contain these additions; in the mean time, developers can create a `glextadditions.h` file in their own headers, adding what is shown in Listing 1. When an updated `glext.h` is provided, this file can be removed.   |  | | --- | | ``` // switches to providing function pointers //#define GL_GLEXT_FUNCTION_POINTERS 1  #define GL_ATI_separate_stencil             1  #if GL_ATI_separate_stencil #define GL_STENCIL_BACK_FUNC_ATI            0x8800                 #define GL_STENCIL_BACK_FAIL_ATI            0x8801                 #define GL_STENCIL_BACK_PASS_DEPTH_FAIL_ATI 0x8802                 #define GL_STENCIL_BACK_PASS_DEPTH_PASS_ATI 0x8803                 #endif  #if GL_ATI_separate_stencil #ifdef GL_GLEXT_FUNCTION_POINTERS typedef void (* glStencilOpSeparateATIProcPtr)      (GLenum face, GLenum sfail, GLenum dpfail, GLenum dppass); typedef void (* glStencilFuncSeparateATIProcPtr)      GLenum frontfunc, GLenum backfunc, GLint ref, GLuint mask); #else extern void glStencilOpSeparateATI      (GLenum face, GLenum sfail, GLenum dpfail, GLenum dppass); extern void glStencilFuncSeparateATI     (GLenum frontfunc, GLenum backfunc, GLint ref, GLuint mask); #endif /* GL_GLEXT_FUNCTION_POINTERS */ #endif ``` | | __Listing 1__. `glextadditions.h` |      ---  [Apr 29, 2003] |

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
