---
title: OpenGL and 3D Graphics Changes in Mac OS X v10.2.3
apple_id: DTS10001752
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2003-01-03'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1229.html
archived_at: '2026-07-18T02:38:20.021840Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Graphics & Imaging > OpenGL](https://developer.apple.com/referencelibrary/GraphicsImaging/idxOpenGL-date.html)

|  |
| --- |
| Technical Q&A QA1229OpenGL and 3D Graphics Changes in Mac OS X v10.2.3 |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| ---   Q: What changes were made in OpenGL and 3D graphics for Mac OS X v10.2.3?  A: Mac OS X v10.2.3 adds support for OpenGL 1.4, 13 new OpenGL extensions, improved stereo support and an OpenGL Utility Toolkit (GLUT) update. Additionally, the update has a number of improvements and bug fixes in the 3D graphics pipeline. For graphics processors which support OpenGL 1.4, the capabilities in Listing 1 are now included in the core OpenGL functionality. Developers should query the current renderer's `GL_VERSION` string to determine if it supports OpenGL 1.4.     |  | | --- | | - __Automatic Mipmap Generation__ by setting the texture parameter `GL_GENERATE_MIPMAP` to `GL_TRUE`. This introduces a side effect to any modification of the levelbase of a mipmap array, wherein all higher levels of the mipmap pyramid are recomputed automatically by successive filtering of the base level array. - __Blend Squaring__ extends the set of supported source and destination blend functions to permit squaring RGB and alpha values during blending. - __Imaging Subset__ changes to include BlendEquation, BlendColor, and the BlendFunc modes `GL_CONSTANT_COLOR`, `GL_ONE_MINUS_CONSTANT_COLOR`, `GL_CONSTANT_ALPHA`, and `GL_ONE_MINUS_CONSTANT_ALPHA`. These features previously were available only in the optional imaging subset in versions 1.2 and 1.3 of the OpenGL specification. - __Depth and Shadow textures__ define a new texture internal format, `GL_DEPTH`, normally used to represent depth values. Applications include image-based shadow casting, displacement mapping, and image-based rendering. Image-based shadowing is enabled with a new texture application mode defined by the parameter `GL_TEXTURE_COMPARE_MODE`. - __Fog Coordinates__ can be used in computing fog for a fragment, instead of using eye distance to the fragment, useful for more complex fog models - __Multiple Draw Arrays__ allows multiple primitives to be drawn in a single call using the `glMultiDrawArrays` and `glMultiDrawElements` commands. - __Point Parameters__ support additional geometric characteristics of points, allowing the size of a point to be affected by linear or quadratic distance attenuation, and increasing control of the mapping from point size to raster point area and point transparency. This effect may be used for distance attenuation in rendering particles or light points. - __Secondary Color__ may be varied even when lighting is disabled by specifying it as a vertex parameter with the `glSecondaryColor` commands. - __Separate Blend Functions__ allow independent setting of the RGB and alpha blend functions for blend operations that require source and destination blend factors. - __Stencil Wrap__ operations `GL_INCR_WRAP` and `GL_DECR_WRAP` allow the stencil value to wrap around the range of stencil values instead of saturating to the minimum or maximum values on decrement or increment. - __Texture Crossbar Environment Mode__ extends the texture combine environment mode `GL_COMBINE` by allowing use of the texture color from different texture units as sources to the texture combine function. - __Texture level of detail (LOD) bias__ may be set to bias the computed lambda parameter used in texturing for mipmap level of detail selection, providing a means to blur or sharpen textures. LOD bias may be used for depth of field and other special visual effects, as well as for some types of image processing. - __Texture Mirrored Repeat__ extends the set of texture wrap modes with the mode `GL_MIRRORED_REPEAT`. This effectively defines a texture map twice as large as the original texture image in which the additional half, for each mirrored texture coordinate, is a mirror image of the original texture. Mirrored repeat can be used for seamless tiling of a surface. - __Window Raster Position__ allows the raster position to be set directly to specified window coordinates with the `glWindowPos` commands, bypassing the transformation applied to `glRasterPos`. | | __Listing 1__. OpenGL 1.4 Features |    The extensions outlined in Listing 2 are have been added to OpenGL for Mac OS X. Developers can check the extensions string for specific renderer support and see the [Mac OS X OpenGL Extensions Guide](https://developer.apple.com/opengl/extensions.html) to learn about extension use and read the specification.     |  | | --- | | - `GL_APPLE_float_pixels` - `GL_ARB_fragment_program` - `GL_ARB_shadow_ambient` - `GL_ARB_vertex_blend` - `GL_ARB_window_pos` - `GL_EXT_multi_draw_arrays` - `GL_EXT_s3tc_texture_compression` - `GL_EXT_shadow_funcs` - `GL_EXT_stencil_two_side` - `GL_ATI_point_cull` - `GL_ATI_texture_mirror_once` - `GL_NV_light_max_exponent` - `GL_SGIS_generate_mipmap` | | __Listing 2__. New OpenGL Extensions |    GLUT was updated to add support for joysticks and stereo contexts. Also, significant improvements were made to event handling which should result more consistent performance and use less CPU in many cases.  In addition to the additions and improvements covered previously, Listing 3 shows a representative list of 3D graphics bugs fixed in Mac OS X v10.2.3 which may affect developers.     |  | | --- | | - iPhoto slide show fix (r. 2851438) - Screen saver fixes (r. 2947854, 2981882, 2983532, 3049055) - Added additional OpenGL stability (r. 2987229, 3010024, 3044963) - DVD visual fixes (r. 2988472, 3034700, 3065118, 3099283, 3102416, 3102431, 3109605) - Improve smoothness in Bugdom (r. 3002070, 3108864) - Improved Shader Builder support (r. 3003329) - Java graphics support improvements (r. 3007437) - Improvements to `GL_ATI_text_fragment_shader` (r. 3023059) - Fixed LOD bias issues (r. 3039061, 33039007) - Texturing fixes (r. 3063842, 3063845, 3033919) - Improved external display support (r. 3071846, 3081613, 3101551, 3122070, 2999184, 3003635, 3025839, 3088102) - Improved `glReadPixels` robustness (r. 3110816, 3113045, 3103065) - Fixed cursor issues (r. 3058957) - Line mode fixes (r. 3092958) - Fixed some w = 0 issues (r. 3093070) - Improved texture range support (r. 3093739) - Fixed some OpenGL header declarations to be in line with OpenGL specification (r. 3013229, 3014102) - Fix some OpenGL queries (r. 3116500) - Add multiple display support to GLUT (r. 2932866) - GLUT conformance test fixes (r. 3094824, 3110053) - GLUT improved window and visibility handling (r. 3094828, 3065960, 3110804) - Fixed GLUT full screen background window resize issue (r. 3094832) - Eliminate GLUT console spew (r. 3095226) - Improved GLUT passive motion and menu handling (r. 3065960, 3091508, 3082250) - Improved overall GLUT event and timer handling (r. 3032121) | | __Listing 3__. 3D Graphics Bug Fixes |      ---  [Jan 03 2003] |

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
