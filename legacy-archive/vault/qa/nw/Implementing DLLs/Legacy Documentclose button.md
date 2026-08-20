---
title: Implementing DLLs
apple_id: DTS10001418
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/nw/nw06.html
archived_at: '2026-07-18T02:29:44.224050Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxNetworking-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Networking](https://developer.apple.com/referencelibrary/Networking/index.html)

|  |
| --- |
| Technical Q&A NW06Implementing DLLs |

|  |
| --- |
| ---   Q: What are the different ways of implementing a DLL (Dynamic Linked Library) on the Macintosh and the PowerPC?  A: Apple has developed a complete technology solution for Dynamic Linked Libraries (DLLs) on the Macintosh. Part of this solution is available today, with additional parts becoming available in the months ahead.  There are three key components to the Macintosh DLL strategy:   1. the Apple Shared Library Manager (ASLM), 2. the Code Fragment Manager (CFM), 3. IBM's System Object Model (SOM).   Here is a brief summary of ASLM, CFM, and SOM:  Apple Shared Library Manager is an integral part of Apple's DLL strategy and product offering. Shipping products (such as MacSNMP), as well as future development including the OpenTransport Networking architecture, are based on ALSM. For the latest information, check your E.T.O.  ASLM is a good bet when:   - you need DLLs on 68K today (it's shipping) - you want elegance with C++ (but it supports C, Pascal, and ASM, too) - you have performance-sensitive needs (like networking)   IBM's System Object Model (SOM) technology is a multi-platform standard that provides system-level sharable objects in a language-neutral way. SOM also solves the "fragile base class" problem, avoiding the need for client libraries to be recompiled when the base class they inherit from is in a different library and is changed. SOM also runs on top of CFM, and thus is available on both 68K and PowerPC Macintosh computers. In addtion, SOM is an integral component technology of OpenDoc.  SOM and ASLM both live in a CFM run-time environment, and are available on both the 68K and PowerPC Macintosh. There is no impediment to co-existence, or to applications that use both. A SOM class, for example, could easily call an ASLM class or vice-versa. |

#### [May 01 1995]

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
