---
title: Drag Manager & the -600 (procNotFound) Error
apple_id: DTS10002208
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-08-21'
source_url: https://developer.apple.com/library/archive/qa/tb/tb22.html
archived_at: '2026-07-18T02:38:56.434851Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A TB22Drag Manager & the -600 (procNotFound) Error |

|  |
| --- |
| Q Sometimes my application's calls to the Drag Manager fail with a -600 (procNotFound) error. This is not one of the errors listed for these calls. What's up?   A There are three known common causes of this error:  1. The use of high-level debuggers. Since Drag Manager interacts    heavily with Process Manager, as does the typical high-level debugger,    conflicts inevitably develop. There's no work-around for this problem    except to ask your debugger vendor to improve its behavior when debugging    Drag Manager code. If your code is encountering such a problem, it should    run fine when the debugger is not involved. 2. Passing TrackDrag an EventRecord whose 'where' field is    expressed in local coordinates. (This can also result in a crash, but    sometimes simply results in a -600 error.) Such 'where' fields often    point outside the window in which the drag originates. 3. Attempting to use the Drag Manager with Text Services Manager    windows when the 'gestaltDragMgrFloatingWind' bit is not defined in the    response to the 'gestaltDragMgrAttr' Gestalt selector. The value of this    bit denotes whether a Drag Manager bug with TSM windows is fixed on the    system under which your app is running.   In the second and third cases, Drag Manager has a hard time associating the source window with a process. Some operations can succeed even without a clear owning process, so Drag Manager limps along as best it can for a while in the hopes that it won't be asked to do anything which requires a ProcessSerialNumber. When it is, the operation fails. [Aug 21 1996] |

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
