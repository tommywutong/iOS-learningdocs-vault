---
title: iOS 9.3 API Diffs
apple_id: TP40016662
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-03-01'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS93APIDiffs/Swift/OpenGLES.html
archived_at: '2026-07-18T02:57:16.386327Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.3 API Diffs](iOS%209.2%20to%20iOS%209.3%20API%20Differences.md)


# OpenGLES Changes for Swift

### OpenGLES

Modified glAlphaFunc(_: GLenum, _: GLclampf)

|  | Declaration |
| --- | --- |
| From | ``` func glAlphaFunc(_ `func`: GLenum, _ ref: GLclampf) ``` |
| To | ``` func glAlphaFunc(_ func: GLenum, _ ref: GLclampf) ``` |

Modified [glAlphaFuncx(_: GLenum, _: GLclampx)](https://developer.apple.com/documentation/opengles/1622706-glalphafuncx)

|  | Declaration |
| --- | --- |
| From | ``` func glAlphaFuncx(_ `func`: GLenum, _ ref: GLclampx) ``` |
| To | ``` func glAlphaFuncx(_ func: GLenum, _ ref: GLclampx) ``` |

Modified [glDepthFunc(_: GLenum)](https://developer.apple.com/documentation/opengles/1617331-gldepthfunc)

|  | Declaration |
| --- | --- |
| From | ``` func glDepthFunc(_ `func`: GLenum) ``` |
| To | ``` func glDepthFunc(_ func: GLenum) ``` |

Modified [glStencilFunc(_: GLenum, _: GLint, _: GLuint)](https://developer.apple.com/documentation/opengles/1617221-glstencilfunc)

|  | Declaration |
| --- | --- |
| From | ``` func glStencilFunc(_ `func`: GLenum, _ ref: GLint, _ mask: GLuint) ``` |
| To | ``` func glStencilFunc(_ func: GLenum, _ ref: GLint, _ mask: GLuint) ``` |

Modified [glStencilFuncSeparate(_: GLenum, _: GLenum, _: GLint, _: GLuint)](https://developer.apple.com/documentation/opengles/1617222-glstencilfuncseparate)

|  | Declaration |
| --- | --- |
| From | ``` func glStencilFuncSeparate(_ face: GLenum, _ `func`: GLenum, _ ref: GLint, _ mask: GLuint) ``` |
| To | ``` func glStencilFuncSeparate(_ face: GLenum, _ func: GLenum, _ ref: GLint, _ mask: GLuint) ``` |

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
