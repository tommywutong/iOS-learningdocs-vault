---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/OpenGL.html
archived_at: '2026-07-18T02:51:32.086514Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# OpenGL Changes for Swift

### OpenGL

Modified [IOSurfaceRef](https://developer.apple.com/documentation/iosurface/iosurfaceref)

|  | Declaration |
| --- | --- |
| From | ``` class IOSurface { } ``` |
| To | ``` class IOSurfaceRef { } ``` |

Modified CGLChoosePixelFormat(_: UnsafePointer<CGLPixelFormatAttribute>, _: UnsafeMutablePointer<CGLPixelFormatObj?>, _: UnsafeMutablePointer<GLint>) -> CGLError

|  | Declaration |
| --- | --- |
| From | ``` func CGLChoosePixelFormat(_ attribs: UnsafePointer<CGLPixelFormatAttribute>, _ pix: UnsafeMutablePointer<CGLPixelFormatObj>, _ npix: UnsafeMutablePointer<GLint>) -> CGLError ``` |
| To | ``` func CGLChoosePixelFormat(_ attribs: UnsafePointer<CGLPixelFormatAttribute>, _ pix: UnsafeMutablePointer<CGLPixelFormatObj?>, _ npix: UnsafeMutablePointer<GLint>) -> CGLError ``` |

Modified CGLCreateContext(_: CGLPixelFormatObj, _: CGLContextObj?, _: UnsafeMutablePointer<CGLContextObj?>) -> CGLError

|  | Declaration |
| --- | --- |
| From | ``` func CGLCreateContext(_ pix: CGLPixelFormatObj, _ share: CGLContextObj, _ ctx: UnsafeMutablePointer<CGLContextObj>) -> CGLError ``` |
| To | ``` func CGLCreateContext(_ pix: CGLPixelFormatObj, _ share: CGLContextObj?, _ ctx: UnsafeMutablePointer<CGLContextObj?>) -> CGLError ``` |

Modified CGLDescribeRenderer(_: CGLRendererInfoObj, _: GLint, _: CGLRendererProperty, _: UnsafeMutablePointer<GLint>?) -> CGLError

|  | Declaration |
| --- | --- |
| From | ``` func CGLDescribeRenderer(_ rend: CGLRendererInfoObj, _ rend_num: GLint, _ prop: CGLRendererProperty, _ value: UnsafeMutablePointer<GLint>) -> CGLError ``` |
| To | ``` func CGLDescribeRenderer(_ rend: CGLRendererInfoObj, _ rend_num: GLint, _ prop: CGLRendererProperty, _ value: UnsafeMutablePointer<GLint>?) -> CGLError ``` |

Modified CGLGetCurrentContext() -> CGLContextObj?

|  | Declaration |
| --- | --- |
| From | ``` func CGLGetCurrentContext() -> CGLContextObj ``` |
| To | ``` func CGLGetCurrentContext() -> CGLContextObj? ``` |

Modified CGLGetPixelFormat(_: CGLContextObj) -> CGLPixelFormatObj?

|  | Declaration |
| --- | --- |
| From | ``` func CGLGetPixelFormat(_ ctx: CGLContextObj) -> CGLPixelFormatObj ``` |
| To | ``` func CGLGetPixelFormat(_ ctx: CGLContextObj) -> CGLPixelFormatObj? ``` |

Modified CGLGetShareGroup(_: CGLContextObj) -> CGLShareGroupObj?

|  | Declaration |
| --- | --- |
| From | ``` func CGLGetShareGroup(_ ctx: CGLContextObj) -> CGLShareGroupObj ``` |
| To | ``` func CGLGetShareGroup(_ ctx: CGLContextObj) -> CGLShareGroupObj? ``` |

Modified CGLGetVersion(_: UnsafeMutablePointer<GLint>?, _: UnsafeMutablePointer<GLint>?)

|  | Declaration |
| --- | --- |
| From | ``` func CGLGetVersion(_ majorvers: UnsafeMutablePointer<GLint>, _ minorvers: UnsafeMutablePointer<GLint>) ``` |
| To | ``` func CGLGetVersion(_ majorvers: UnsafeMutablePointer<GLint>?, _ minorvers: UnsafeMutablePointer<GLint>?) ``` |

Modified CGLPixelFormatObj

|  | Declaration |
| --- | --- |
| From | ``` typealias CGLPixelFormatObj = COpaquePointer ``` |
| To | ``` typealias CGLPixelFormatObj = OpaquePointer ``` |

Modified CGLQueryRendererInfo(_: GLuint, _: UnsafeMutablePointer<CGLRendererInfoObj?>, _: UnsafeMutablePointer<GLint>) -> CGLError

|  | Declaration |
| --- | --- |
| From | ``` func CGLQueryRendererInfo(_ display_mask: GLuint, _ rend: UnsafeMutablePointer<CGLRendererInfoObj>, _ nrend: UnsafeMutablePointer<GLint>) -> CGLError ``` |
| To | ``` func CGLQueryRendererInfo(_ display_mask: GLuint, _ rend: UnsafeMutablePointer<CGLRendererInfoObj?>, _ nrend: UnsafeMutablePointer<GLint>) -> CGLError ``` |

Modified CGLRendererInfoObj

|  | Declaration |
| --- | --- |
| From | ``` typealias CGLRendererInfoObj = COpaquePointer ``` |
| To | ``` typealias CGLRendererInfoObj = OpaquePointer ``` |

Modified CGLSetCurrentContext(_: CGLContextObj?) -> CGLError

|  | Declaration |
| --- | --- |
| From | ``` func CGLSetCurrentContext(_ ctx: CGLContextObj) -> CGLError ``` |
| To | ``` func CGLSetCurrentContext(_ ctx: CGLContextObj?) -> CGLError ``` |

Modified CGLSetGlobalOption(_: CGLGlobalOption, _: UnsafePointer<GLint>?) -> CGLError

|  | Declaration |
| --- | --- |
| From | ``` func CGLSetGlobalOption(_ pname: CGLGlobalOption, _ params: UnsafePointer<GLint>) -> CGLError ``` |
| To | ``` func CGLSetGlobalOption(_ pname: CGLGlobalOption, _ params: UnsafePointer<GLint>?) -> CGLError ``` |

Modified CGLShareGroupObj

|  | Declaration |
| --- | --- |
| From | ``` typealias CGLShareGroupObj = COpaquePointer ``` |
| To | ``` typealias CGLShareGroupObj = OpaquePointer ``` |

Modified CGLTexImageIOSurface2D(_: CGLContextObj, _: GLenum, _: GLenum, _: GLsizei, _: GLsizei, _: GLenum, _: GLenum, _: IOSurfaceRef, _: GLuint) -> CGLError

|  | Declaration |
| --- | --- |
| From | ``` func CGLTexImageIOSurface2D(_ ctx: CGLContextObj, _ target: GLenum, _ internal_format: GLenum, _ width: GLsizei, _ height: GLsizei, _ format: GLenum, _ type: GLenum, _ ioSurface: IOSurface, _ plane: GLuint) -> CGLError ``` |
| To | ``` func CGLTexImageIOSurface2D(_ ctx: CGLContextObj, _ target: GLenum, _ internal_format: GLenum, _ width: GLsizei, _ height: GLsizei, _ format: GLenum, _ type: GLenum, _ ioSurface: IOSurfaceRef, _ plane: GLuint) -> CGLError ``` |

Modified cl_device_id

|  | Declaration |
| --- | --- |
| From | ``` typealias cl_device_id = COpaquePointer ``` |
| To | ``` typealias cl_device_id = OpaquePointer ``` |

Modified GLhandleARB

|  | Declaration |
| --- | --- |
| From | ``` typealias GLhandleARB = UnsafeMutablePointer<Void> ``` |
| To | ``` typealias GLhandleARB = UnsafeMutableRawPointer ``` |

Modified GLsync

|  | Declaration |
| --- | --- |
| From | ``` typealias GLsync = COpaquePointer ``` |
| To | ``` typealias GLsync = OpaquePointer ``` |

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
