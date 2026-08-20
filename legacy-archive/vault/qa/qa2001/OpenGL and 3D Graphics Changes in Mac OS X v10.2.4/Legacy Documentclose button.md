---
title: OpenGL and 3D Graphics Changes in Mac OS X v10.2.4
apple_id: DTS10001759
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2003-02-18'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1239.html
archived_at: '2026-07-18T02:38:20.458311Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Graphics & Imaging > OpenGL](https://developer.apple.com/referencelibrary/GraphicsImaging/idxOpenGL-date.html)

|  |
| --- |
| Technical Q&A QA1239OpenGL and 3D Graphics Changes in Mac OS X v10.2.4 |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| ---   Q: What changes were made in OpenGL and 3D graphics for Mac OS X v10.2.4?  A: Mac OS X v10.2.4 adds additional OpenGL extension support, better automatic mipmap generation and compressed texture handling, Rage 128 updates, and other general improvements and bug fixes to the 3D graphics pipeline. The extensions outlined in Listing 1 have been added to OpenGL for Mac OS X v10.2.4. Developers can check the extensions string for specific renderer support and see the [Mac OS X OpenGL Extensions Guide](https://developer.apple.com/opengl/extensions.html) to learn about extension use and read the specification.   |  | | --- | | - `GL_ATI_texture_env_combine3` - `GL_SGIS_generate_mipmap` (added ATI support) | | __Listing 1__. New OpenGL Extensions |    Use of the `ATI_texture_env_combine3` extension requires additional definitions to those provided in the OpenGL frameworks `glext.h` header file. A future developer tools update should contain these additions; in the mean time, developers can create a `glextadditions.h` file in their own headers, adding what is shown in Listing 2. When an updated `glext.h` is provided, this file can be removed.   |  | | --- | | ``` #define GL_ATI_texture_env_combine3       1  #if GL_ATI_texture_env_combine3 #define GL_MODULATE_ADD_ATI               0x8744 #define GL_MODULATE_SIGNED_ADD_ATI        0x8745 #define GL_MODULATE_SUBTRACT_ATI          0x8746 #endif ``` | | __Listing 2__. glextadditions.h |    In addition to the new extensions covered previously, Table 1 shows a representative list of 3D graphics improvements and bugs fixed in Mac OS X v10.2.4 which may affect developers.   |  | | --- | | __Table 1__. 3D Graphics Bug Fixes | | - Improve imaging subset (r. 3048152) - Better secondary display handling (r. 3108024, 3000884) - Add automatic mipmap generation support (r. 3126508, 3139985, 3066752, 3110486) - Add ATI_texture_env_combine3 (r. 3132941, 3139801, 3132943, 3132944) - Update handling of vertex program invariance (r. 3139060) - Fix GLUT keyboard and menu handling from terminal (r. 3129836) - Improve vertex programs (r. 3093442, 3106677, 3147093) - Fix X11 resize issue in certain configurations (r. 3127840) - Improve error handling for 0 width 0 height surfaces (r. 3133552) - Fix errant case in glCopyTexSubImage (r. 3139085) - Texture Shader improvements (r. 3140650) - Surface texture improvements (r. 3142044, 3096252) - Better texture compression (r. 3153058) - Fix array initializer issue in fragment programs (r. 3124583) - Improve depth buffer paging (r. 3143357) - Fix glFinishObject issue in certain configurations (r. 3150801) - Rage 128 improvements (r. 3145747) |      ---  [Feb 18 2003] |

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
