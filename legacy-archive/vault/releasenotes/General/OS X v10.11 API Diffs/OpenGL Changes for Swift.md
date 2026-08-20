---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/OpenGL.html
archived_at: '2026-07-18T02:53:40.556441Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# OpenGL Changes for Swift

### OpenGL

Removed CGLCPContextPriorityRequest.valueAdded CGLCPContextPriorityRequest.init(rawValue: UInt32)Added CGLCPContextPriorityRequest.rawValueModified CGLCPContextPriorityRequest [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CGLCPContextPriorityRequest {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct CGLCPContextPriorityRequest : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified CGLTexImageIOSurface2D(_: CGLContextObj, _: GLenum, _: GLenum, _: GLsizei, _: GLsizei, _: GLenum, _: GLenum, _: IOSurface, _: GLuint) -> CGLError

|  | Declaration |
| --- | --- |
| From | ``` func CGLTexImageIOSurface2D(_ ctx: CGLContextObj, _ target: GLenum, _ internal_format: GLenum, _ width: GLsizei, _ height: GLsizei, _ format: GLenum, _ type: GLenum, _ ioSurface: IOSurface!, _ plane: GLuint) -> CGLError ``` |
| To | ``` func CGLTexImageIOSurface2D(_ ctx: CGLContextObj, _ target: GLenum, _ internal_format: GLenum, _ width: GLsizei, _ height: GLsizei, _ format: GLenum, _ type: GLenum, _ ioSurface: IOSurface, _ plane: GLuint) -> CGLError ``` |

Modified kCGLPFAStereo

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.0 | OS X 10.11 |

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
