---
title: iOS 8.0 API Diffs
apple_id: TP40014455
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS80APIDiffs/frameworks/OpenGLES.html
archived_at: '2026-07-18T02:55:59.568602Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.0 API Diffs](iOS%207.1%20to%20iOS%208.0%20API%20Differences.md)


# OpenGLES Changes

## OpenGLES

EAGL.hModified [-[EAGLContext initWithAPI:]](https://developer.apple.com/documentation/opengles/eaglcontext/1624895-initwithapi)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithAPI:(EAGLRenderingAPI)api ``` |
| To | ``` - (instancetype)initWithAPI:(EAGLRenderingAPI)api ``` |

Modified [-[EAGLContext initWithAPI:sharegroup:]](https://developer.apple.com/documentation/opengles/eaglcontext/1624877-initwithapi)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithAPI:(EAGLRenderingAPI)api sharegroup:(EAGLSharegroup *)sharegroup ``` |
| To | ``` - (instancetype)initWithAPI:(EAGLRenderingAPI)api sharegroup:(EAGLSharegroup *)sharegroup ``` |

ES3/gl.hRemoved GLbitfieldRemoved GLbooleanRemoved GLbyteRemoved GLcharRemoved GLclampfRemoved GLenumRemoved GLfixedRemoved GLfloatRemoved GLhalfRemoved GLintRemoved GLint64Removed GLintptrRemoved GLshortRemoved GLsizeiRemoved GLsizeiptrRemoved GLsyncRemoved GLubyteRemoved GLuintRemoved GLuint64Removed GLushortRemoved GLvoidES2/gl.hRemoved GLbitfieldRemoved GLbooleanRemoved GLbyteRemoved GLclampfRemoved [GLclampx](https://developer.apple.com/documentation/opengles/glclampx)Removed GLenumRemoved GLfixedRemoved GLfloatRemoved GLintRemoved GLintptrRemoved GLshortRemoved GLsizeiRemoved GLsizeiptrRemoved GLubyteRemoved GLuintRemoved GLushortRemoved GLvoidModified GLchar

|  | Header |
| --- | --- |
| From | OpenGLES/ES2/gl.h |
| To | OpenGLES/gltypes.h |

ES1/gl.hModified GLbitfield

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLboolean

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLbyte

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLclampf

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified [GLclampx](https://developer.apple.com/documentation/opengles/glclampx)

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLenum

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLfixed

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLfloat

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLint

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLintptr

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLshort

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLsizei

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLsizeiptr

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLubyte

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLuint

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLushort

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLvoid

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

ES2/glext.hAdded [#def GL_APPLE_clip_distance](https://developer.apple.com/documentation/opengles/gl_apple_clip_distance)Added [#def GL_APPLE_color_buffer_packed_float](https://developer.apple.com/documentation/opengles/gl_apple_color_buffer_packed_float)Added [#def GL_APPLE_texture_packed_float](https://developer.apple.com/documentation/opengles/gl_apple_texture_packed_float)Added [#def GL_CLIP_DISTANCE0_APPLE](https://developer.apple.com/documentation/opengles/gl_clip_distance0_apple)Added [#def GL_CLIP_DISTANCE1_APPLE](https://developer.apple.com/documentation/opengles/gl_clip_distance1_apple)Added [#def GL_CLIP_DISTANCE2_APPLE](https://developer.apple.com/documentation/opengles/gl_clip_distance2_apple)Added [#def GL_CLIP_DISTANCE3_APPLE](https://developer.apple.com/documentation/opengles/gl_clip_distance3_apple)Added [#def GL_CLIP_DISTANCE4_APPLE](https://developer.apple.com/documentation/opengles/gl_clip_distance4_apple)Added [#def GL_CLIP_DISTANCE5_APPLE](https://developer.apple.com/documentation/opengles/gl_clip_distance5_apple)Added [#def GL_CLIP_DISTANCE6_APPLE](https://developer.apple.com/documentation/opengles/gl_clip_distance6_apple)Added [#def GL_CLIP_DISTANCE7_APPLE](https://developer.apple.com/documentation/opengles/gl_clip_distance7_apple)Added [#def GL_MAX_CLIP_DISTANCES_APPLE](https://developer.apple.com/documentation/opengles/gl_max_clip_distances_apple)Added [#def GL_R11F_G11F_B10F_APPLE](https://developer.apple.com/documentation/opengles/gl_r11f_g11f_b10f_apple)Added [#def GL_RGB9_E5_APPLE](https://developer.apple.com/documentation/opengles/gl_rgb9_e5_apple)Added [#def GL_UNSIGNED_INT_10F_11F_11F_REV_APPLE](https://developer.apple.com/documentation/opengles/gl_unsigned_int_10f_11f_11f_rev_apple)Added [#def GL_UNSIGNED_INT_5_9_9_9_REV_APPLE](https://developer.apple.com/documentation/opengles/gl_unsigned_int_5_9_9_9_rev_apple)Modified GLhalf

|  | Header |
| --- | --- |
| From | OpenGLES/ES2/glext.h |
| To | OpenGLES/gltypes.h |

Modified GLint64

|  | Header |
| --- | --- |
| From | OpenGLES/ES2/glext.h |
| To | OpenGLES/gltypes.h |

Modified GLsync

|  | Header |
| --- | --- |
| From | OpenGLES/ES2/glext.h |
| To | OpenGLES/gltypes.h |

Modified GLuint64

|  | Header |
| --- | --- |
| From | OpenGLES/ES2/glext.h |
| To | OpenGLES/gltypes.h |

ES3/glext.hAdded [#def GL_APPLE_clip_distance](https://developer.apple.com/documentation/opengles/gl_apple_clip_distance)Added [#def GL_APPLE_color_buffer_packed_float](https://developer.apple.com/documentation/opengles/gl_apple_color_buffer_packed_float)Added [#def GL_CLIP_DISTANCE0_APPLE](https://developer.apple.com/documentation/opengles/gl_clip_distance0_apple)Added [#def GL_CLIP_DISTANCE1_APPLE](https://developer.apple.com/documentation/opengles/gl_clip_distance1_apple)Added [#def GL_CLIP_DISTANCE2_APPLE](https://developer.apple.com/documentation/opengles/gl_clip_distance2_apple)Added [#def GL_CLIP_DISTANCE3_APPLE](https://developer.apple.com/documentation/opengles/gl_clip_distance3_apple)Added [#def GL_CLIP_DISTANCE4_APPLE](https://developer.apple.com/documentation/opengles/gl_clip_distance4_apple)Added [#def GL_CLIP_DISTANCE5_APPLE](https://developer.apple.com/documentation/opengles/gl_clip_distance5_apple)Added [#def GL_CLIP_DISTANCE6_APPLE](https://developer.apple.com/documentation/opengles/gl_clip_distance6_apple)Added [#def GL_CLIP_DISTANCE7_APPLE](https://developer.apple.com/documentation/opengles/gl_clip_distance7_apple)Added [#def GL_COMPRESSED_RGBA_ASTC_10x10_KHR](https://developer.apple.com/documentation/opengles/gl_compressed_rgba_astc_10x10_khr)Added [#def GL_COMPRESSED_RGBA_ASTC_10x5_KHR](https://developer.apple.com/documentation/opengles/gl_compressed_rgba_astc_10x5_khr)Added [#def GL_COMPRESSED_RGBA_ASTC_10x6_KHR](https://developer.apple.com/documentation/opengles/gl_compressed_rgba_astc_10x6_khr)Added [#def GL_COMPRESSED_RGBA_ASTC_10x8_KHR](https://developer.apple.com/documentation/opengles/gl_compressed_rgba_astc_10x8_khr)Added [#def GL_COMPRESSED_RGBA_ASTC_12x10_KHR](https://developer.apple.com/documentation/opengles/gl_compressed_rgba_astc_12x10_khr)Added [#def GL_COMPRESSED_RGBA_ASTC_12x12_KHR](https://developer.apple.com/documentation/opengles/gl_compressed_rgba_astc_12x12_khr)Added [#def GL_COMPRESSED_RGBA_ASTC_4x4_KHR](https://developer.apple.com/documentation/opengles/gl_compressed_rgba_astc_4x4_khr)Added [#def GL_COMPRESSED_RGBA_ASTC_5x4_KHR](https://developer.apple.com/documentation/opengles/gl_compressed_rgba_astc_5x4_khr)Added [#def GL_COMPRESSED_RGBA_ASTC_5x5_KHR](https://developer.apple.com/documentation/opengles/gl_compressed_rgba_astc_5x5_khr)Added [#def GL_COMPRESSED_RGBA_ASTC_6x5_KHR](https://developer.apple.com/documentation/opengles/gl_compressed_rgba_astc_6x5_khr)Added [#def GL_COMPRESSED_RGBA_ASTC_6x6_KHR](https://developer.apple.com/documentation/opengles/gl_compressed_rgba_astc_6x6_khr)Added [#def GL_COMPRESSED_RGBA_ASTC_8x5_KHR](https://developer.apple.com/documentation/opengles/gl_compressed_rgba_astc_8x5_khr)Added [#def GL_COMPRESSED_RGBA_ASTC_8x6_KHR](https://developer.apple.com/documentation/opengles/gl_compressed_rgba_astc_8x6_khr)Added [#def GL_COMPRESSED_RGBA_ASTC_8x8_KHR](https://developer.apple.com/documentation/opengles/gl_compressed_rgba_astc_8x8_khr)Added [#def GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x10_KHR](https://developer.apple.com/documentation/opengles/gl_compressed_srgb8_alpha8_astc_10x10_khr)Added [#def GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x5_KHR](https://developer.apple.com/documentation/opengles/gl_compressed_srgb8_alpha8_astc_10x5_khr)Added [#def GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x6_KHR](https://developer.apple.com/documentation/opengles/gl_compressed_srgb8_alpha8_astc_10x6_khr)Added [#def GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x8_KHR](https://developer.apple.com/documentation/opengles/gl_compressed_srgb8_alpha8_astc_10x8_khr)Added [#def GL_COMPRESSED_SRGB8_ALPHA8_ASTC_12x10_KHR](https://developer.apple.com/documentation/opengles/gl_compressed_srgb8_alpha8_astc_12x10_khr)Added [#def GL_COMPRESSED_SRGB8_ALPHA8_ASTC_12x12_KHR](https://developer.apple.com/documentation/opengles/gl_compressed_srgb8_alpha8_astc_12x12_khr)Added [#def GL_COMPRESSED_SRGB8_ALPHA8_ASTC_4x4_KHR](https://developer.apple.com/documentation/opengles/gl_compressed_srgb8_alpha8_astc_4x4_khr)Added [#def GL_COMPRESSED_SRGB8_ALPHA8_ASTC_5x4_KHR](https://developer.apple.com/documentation/opengles/gl_compressed_srgb8_alpha8_astc_5x4_khr)Added [#def GL_COMPRESSED_SRGB8_ALPHA8_ASTC_5x5_KHR](https://developer.apple.com/documentation/opengles/gl_compressed_srgb8_alpha8_astc_5x5_khr)Added [#def GL_COMPRESSED_SRGB8_ALPHA8_ASTC_6x5_KHR](https://developer.apple.com/documentation/opengles/gl_compressed_srgb8_alpha8_astc_6x5_khr)Added [#def GL_COMPRESSED_SRGB8_ALPHA8_ASTC_6x6_KHR](https://developer.apple.com/documentation/opengles/gl_compressed_srgb8_alpha8_astc_6x6_khr)Added [#def GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x5_KHR](https://developer.apple.com/documentation/opengles/gl_compressed_srgb8_alpha8_astc_8x5_khr)Added [#def GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x6_KHR](https://developer.apple.com/documentation/opengles/gl_compressed_srgb8_alpha8_astc_8x6_khr)Added [#def GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x8_KHR](https://developer.apple.com/documentation/opengles/gl_compressed_srgb8_alpha8_astc_8x8_khr)Added [#def GL_KHR_texture_compression_astc_ldr](https://developer.apple.com/documentation/opengles/gl_khr_texture_compression_astc_ldr)Added [#def GL_MAX_CLIP_DISTANCES_APPLE](https://developer.apple.com/documentation/opengles/gl_max_clip_distances_apple)Added [#def GL_R11F_G11F_B10F_APPLE](https://developer.apple.com/documentation/opengles/gl_r11f_g11f_b10f_apple)Added [#def GL_RGB9_E5_APPLE](https://developer.apple.com/documentation/opengles/gl_rgb9_e5_apple)gltypes.h (Added)Modified GLbitfield

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLboolean

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLbyte

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLchar

|  | Header |
| --- | --- |
| From | OpenGLES/ES2/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLclampf

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified [GLclampx](https://developer.apple.com/documentation/opengles/glclampx)

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLenum

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLfixed

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLfloat

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLhalf

|  | Header |
| --- | --- |
| From | OpenGLES/ES2/glext.h |
| To | OpenGLES/gltypes.h |

Modified GLint

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLint64

|  | Header |
| --- | --- |
| From | OpenGLES/ES2/glext.h |
| To | OpenGLES/gltypes.h |

Modified GLintptr

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLshort

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLsizei

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLsizeiptr

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLsync

|  | Header |
| --- | --- |
| From | OpenGLES/ES2/glext.h |
| To | OpenGLES/gltypes.h |

Modified GLubyte

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLuint

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLuint64

|  | Header |
| --- | --- |
| From | OpenGLES/ES2/glext.h |
| To | OpenGLES/gltypes.h |

Modified GLushort

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

Modified GLvoid

|  | Header |
| --- | --- |
| From | OpenGLES/ES1/gl.h |
| To | OpenGLES/gltypes.h |

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
