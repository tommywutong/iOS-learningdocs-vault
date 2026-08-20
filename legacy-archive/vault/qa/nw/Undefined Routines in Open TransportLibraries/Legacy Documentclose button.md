---
title: Undefined Routines in Open TransportLibraries
apple_id: DTS10001446
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-06-01'
source_url: https://developer.apple.com/library/archive/qa/nw/nw34.html
archived_at: '2026-07-18T02:29:46.031629Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxNetworking-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Networking](https://developer.apple.com/referencelibrary/Networking/index.html)

|  |
| --- |
| Technical Q&A NW34Undefined Routines in Open TransportLibraries |

|  |  |
| --- | --- |
| ---   Q: I'm trying to link the Open Transport libraries with the Symantec C++ compiler but it complains that `SetSelfAsClient`, `LoadClass`, `SetCurrentClient` and `UnloadClass` aren't defined. What's going wrong?  A: The routines that are undefined (`LoadClass`, etc) are part of the ASLM interface. OT uses ASLM as its underlying shared library system, with the ASLM bits wrapped inside standard ".o" (for 68K) and XCOFF/PEF (for PPC) files.  The missing routines are only used by two routines, `OTLoadASLMLibrary` and `OTUnloadASLMLibrary`. These routines themselves aren't referenced anywhere, either by the API or by any other OT library.  This works just fine with other environments since they parse libraries from the top down, starting at main and branching outwards to each referenced routine. Because `OTLoadASLMLibrary` is never referenced, they never detect that `LoadClass` is undefined.  Symantec C++, however, is more rigorous and notices the missing routines. Symantec's linker has been updated to ignore routines that are undefined and referenced only from routines that are never called. You can enable this update by using the "Smart Check Link" linker option in the latest release of the SC++ environment.  If you don't have this latest update, you can simply 'stub out' these routines in your own source file as shown:   |  | | --- | | ``` #ifdef __cplusplus extern "C" { #endif  void SetSelfAsClient(void) {         DebugStr("\pSetSelfAsClient -- This is not good."); } void LoadClass(void) {         DebugStr("\pLoadClass -- This is not good."); } void SetCurrentClient(void) {         DebugStr("\pSetCurrentClient -- This is not good."); } void UnloadClass(void) {         DebugStr("\pUnloadClass -- This is not good."); } #ifdef __cplusplus } #endif ``` |   This works because these routines are never actually called by any code. The `DebugStrs` are there just in case that assertion turns out to be untrue.  Note that the sample uses conditional compilation to ensure that the routines are defined inside an extern "C" { } block, lest the link fail because of the name mangler. |

#### [Jun 01 1996]

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
