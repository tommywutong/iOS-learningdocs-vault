---
title: The InterfaceLibSys7.additions Stub Library
apple_id: DTS10001533
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-11-14'
source_url: https://developer.apple.com/library/archive/qa/plat/plat23.html
archived_at: '2026-07-18T02:29:52.570421Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxCarbon-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Carbon](https://developer.apple.com/referencelibrary/Carbon/index.html)

|  |
| --- |
| Technical Q&A PLAT23The InterfaceLibSys7.additions Stub Library |

|  |
| --- |
| ---   Q: I'm trying to use the `SystemSevenFiveOrLater` gestalt.h functions `NewGestaltValue` and `SetGestaltValue` from a PPC application. They are not defined in InterfaceLib. Could you tell me where I can find them?  A: It might seem that Apple should ship an new InterfaceLib stub library with the additional System 7.5 symbols. By default, however, the new symbols would not be weak linked, and they would therefore send developers down the path of creating binaries that don't run on System 7.1.  Instead, Apple has created a separate stub library, InterfaceLibSys7.additions, which contains only the new System 7.5 InterfaceLib symbols. Since it is a separate file, it is easier to weak-link (and to remember to weak-link!).  In Metrowerks, use the pop up next to the file-in-project window and mark the whole library weak-linked. In MPW, use `-weak` and list the new System 7.5 functions used.  [bluebook.gif Download Binhexed MetroWerks library file (2K)](https://developer.apple.com/library/archive/qa/plat/downloads/plat23.hqx) |

#### [Nov 14 1996]

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
