---
title: Calling CloseOpenTransport When Writing an App
apple_id: DTS10001448
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-07-03'
source_url: https://developer.apple.com/library/archive/qa/nw/nw36.html
archived_at: '2026-07-18T02:29:46.140530Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/Networking/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Networking/idxCarbon-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Networking > Carbon](https://developer.apple.com/referencelibrary/Networking/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A NW36Calling CloseOpenTransport When Writing an App |

|  |  |  |  |
| --- | --- | --- | --- |
| ---   Q:I read somewhere that you don't have to call `CloseOpenTransport` if you're writing an application. Is this true?  A: Yes and no. The original OT programming documentation stated that calling `CloseOpenTransport` was optional for applications. There is however a bug in OT 1.1 and earlier which will not properly clean up PPC native applications when they terminate unless `CloseOpenTransport` is called.  Here are some rules of thumb:   1. Non-application code must always call `CloseOpenTransport` when it    terminates. 2. It is best if 68K applications call `CloseOpenTransport`, but they will be    cleaned up automatically if they don't. 3. Make sure that PPC applications running under OT 1.1 or earlier call    CloseOpenTransport when terminating.   One way of ensuring that you comply with point 3 is to use a CFM terminate procedure in your main application fragment, such as:   |  | | --- | | ``` static Boolean gOTInited = false; void CFMTerminate(void) {    if (gOTInited) {        gOTInited = false;        (void) CloseOpenTransport();    } } void main(void) {     OSStatus err;     err = InitOpenTransport();     gOTInited = (err == noErr);     // the rest of your application     if (gOTInited) {         (void) CloseOpenTransport();         gOTInited = false;     } } ``` |     |  | | --- | | __Note:__  Calling CloseOpenTransport is always required for non-application programs. |       |  | | --- | | __Note:__  When the Mac OS provides an automatic clean up mechanism, it's normally intended as a "safety net." It's generally a good idea to do your own clean up, at least for normal application termination. | |

#### [Jul 03 1996]

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

---
