---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/OpenGLES.html
archived_at: '2026-07-18T02:56:56.864993Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# OpenGLES Changes for Swift

### OpenGLES

Modified [EAGLContext](https://developer.apple.com/documentation/opengles/eaglcontext)

|  | Declaration |
| --- | --- |
| From | ``` class EAGLContext : NSObject {     convenience init!(API api: EAGLRenderingAPI)     init!(API api: EAGLRenderingAPI, sharegroup sharegroup: EAGLSharegroup!)     class func setCurrentContext(_ context: EAGLContext!) -> Bool     class func currentContext() -> EAGLContext!     var API: EAGLRenderingAPI { get }     var sharegroup: EAGLSharegroup! { get }     var debugLabel: String!     var multiThreaded: Bool } extension EAGLContext {     func renderbufferStorage(_ target: Int, fromDrawable drawable: EAGLDrawable!) -> Bool     func presentRenderbuffer(_ target: Int) -> Bool } ``` |
| To | ``` class EAGLContext : NSObject {     convenience init!()     convenience init!(API api: EAGLRenderingAPI)     init!(API api: EAGLRenderingAPI, sharegroup sharegroup: EAGLSharegroup!)     class func setCurrentContext(_ context: EAGLContext!) -> Bool     class func currentContext() -> EAGLContext!     var API: EAGLRenderingAPI { get }     var sharegroup: EAGLSharegroup! { get }     var debugLabel: String!     var multiThreaded: Bool } extension EAGLContext {     func renderbufferStorage(_ target: Int, fromDrawable drawable: EAGLDrawable!) -> Bool     func presentRenderbuffer(_ target: Int) -> Bool } ``` |

Modified [EAGLDrawable.drawableProperties](https://developer.apple.com/documentation/opengles/eagldrawable/1622263-drawableproperties)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified [EAGLRenderingAPI [enum]](https://developer.apple.com/documentation/opengles/eaglrenderingapi)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

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
