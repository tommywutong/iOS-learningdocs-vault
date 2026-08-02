---
title: iOS 8.0 API Diffs
apple_id: TP40014455
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS80APIDiffs/frameworks/GLKit.html
archived_at: '2026-07-18T02:55:58.028716Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.0 API Diffs](iOS%207.1%20to%20iOS%208.0%20API%20Differences.md)


# GLKit Changes

## GLKit

GLKTextureLoader.hModified [-[GLKTextureLoader initWithSharegroup:]](https://developer.apple.com/documentation/glkit/glktextureloader/1620707-initwithsharegroup)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithSharegroup:(EAGLSharegroup *)sharegroup ``` |
| To | ``` - (instancetype)initWithSharegroup:(EAGLSharegroup *)sharegroup ``` |

Modified [GLKTextureLoaderErrorIncompatibleFormatSRGB](https://developer.apple.com/documentation/glkit/glktextureloadererror/glktextureloadererrorincompatibleformatsrgb)

|  | Introduction |
| --- | --- |
| From | iOS 7.0 |
| To | iOS 5.0 |

GLKView.hRemoved [-[GLKView snapshot]](https://developer.apple.com/documentation/glkit/glkview/1615562-snapshot)Added [GLKView.snapshot](https://developer.apple.com/documentation/glkit/glkview/1615562-snapshot)Modified [-[GLKView initWithFrame:context:]](https://developer.apple.com/documentation/glkit/glkview/1615609-initwithframe)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithFrame:(CGRect)frame context:(EAGLContext *)context ``` |
| To | ``` - (instancetype)initWithFrame:(CGRect)frame context:(EAGLContext *)context ``` |

Modified [GLKViewDrawableColorFormatSRGBA8888](https://developer.apple.com/documentation/glkit/glkviewdrawablecolorformat/glkviewdrawablecolorformatsrgba8888)

|  | Introduction |
| --- | --- |
| From | iOS 7.0 |
| To | iOS 5.0 |

GLKViewController.hModified [-[GLKViewControllerDelegate glkViewController:willPause:]](https://developer.apple.com/documentation/glkit/glkviewcontrollerdelegate/1620776-glkviewcontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

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
