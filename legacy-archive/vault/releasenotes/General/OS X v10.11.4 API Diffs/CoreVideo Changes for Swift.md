---
title: OS X v10.11.4 API Diffs
apple_id: TP40016680
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11_4/Swift/CoreVideo.html
archived_at: '2026-07-18T02:53:50.956204Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11.4 API Diffs](OS%20X%20v10.11.4%20API%20Diffs.md)


# CoreVideo Changes for Swift

### CoreVideo

Modified [CVBuffer](https://developer.apple.com/documentation/corevideo/cvbufferref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CVBufferRef | ``` typealias CVBufferRef = CVBuffer ``` |
| To | CVBuffer | ``` class CVBuffer { } ``` |

Modified [CVDisplayLink](https://developer.apple.com/documentation/corevideo/cvdisplaylink)

|  | Name | Declaration |
| --- | --- | --- |
| From | CVDisplayLinkRef | ``` typealias CVDisplayLinkRef = CVDisplayLink ``` |
| To | CVDisplayLink | ``` class CVDisplayLink { } ``` |

Modified [CVMetalTextureCache](https://developer.apple.com/documentation/corevideo/cvmetaltexturecache)

|  | Name | Declaration |
| --- | --- | --- |
| From | CVMetalTextureCacheRef | ``` typealias CVMetalTextureCacheRef = CVMetalTextureCache ``` |
| To | CVMetalTextureCache | ``` class CVMetalTextureCache { } ``` |

Modified [CVOpenGLBufferPool](https://developer.apple.com/documentation/corevideo/cvopenglbufferpoolref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CVOpenGLBufferPoolRef | ``` typealias CVOpenGLBufferPoolRef = CVOpenGLBufferPool ``` |
| To | CVOpenGLBufferPool | ``` class CVOpenGLBufferPool { } ``` |

Modified [CVOpenGLTextureCache](https://developer.apple.com/documentation/corevideo/cvopengltexturecache)

|  | Name | Declaration |
| --- | --- | --- |
| From | CVOpenGLTextureCacheRef | ``` typealias CVOpenGLTextureCacheRef = CVOpenGLTextureCache ``` |
| To | CVOpenGLTextureCache | ``` class CVOpenGLTextureCache { } ``` |

Modified [CVPixelBufferPool](https://developer.apple.com/documentation/corevideo/cvpixelbufferpool)

|  | Name | Declaration |
| --- | --- | --- |
| From | CVPixelBufferPoolRef | ``` typealias CVPixelBufferPoolRef = CVPixelBufferPool ``` |
| To | CVPixelBufferPool | ``` class CVPixelBufferPool { } ``` |

Modified [CVMetalTexture](https://developer.apple.com/documentation/corevideo/cvmetaltexture)

|  | Declaration |
| --- | --- |
| From | ``` typealias CVMetalTextureRef = CVMetalTexture ``` |
| To | ``` typealias CVMetalTexture = CVImageBuffer ``` |

Modified [CVOpenGLTexture](https://developer.apple.com/documentation/corevideo/cvopengltexture)

|  | Declaration |
| --- | --- |
| From | ``` typealias CVOpenGLTextureRef = CVOpenGLTexture ``` |
| To | ``` typealias CVOpenGLTexture = CVImageBuffer ``` |

Modified [CVPixelBuffer](https://developer.apple.com/documentation/corevideo/cvpixelbufferref)

|  | Declaration |
| --- | --- |
| From | ``` typealias CVPixelBufferRef = CVPixelBuffer ``` |
| To | ``` typealias CVPixelBuffer = CVImageBuffer ``` |

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
