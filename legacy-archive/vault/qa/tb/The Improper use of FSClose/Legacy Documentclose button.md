---
title: The Improper use of FSClose
apple_id: DTS10002222
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-02-10'
source_url: https://developer.apple.com/library/archive/qa/tb/tb36.html
archived_at: '2026-07-18T02:38:56.946872Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Human Interface Toolbox](https://developer.apple.com/referencelibrary/Carbon/idxHumanInterfaceToolbox-date.html)

|  |
| --- |
| Technical Q&A TB36The Improper use of FSClose |

|  |
| --- |
| Q When running an application, I launch a second application. When I quit the first application, the second application quits and the Finder reports that "the server that contains it has been disconnected". Both applications are on local volumes. What's going on?   A The most likely reason for this is that the Resource Manager's tables have become corrupted. One way to trigger this is to call `OpenResFile` (to read a preferences file, for instance) and then incorrectly call `FSClose` to close the preferences file instead of correctly calling `CloseResFile`. Along the same lines, make sure that you do not substitute a call to `DisposeHandle` when you should call `ReleaseResource`. [Feb 10 1998] |

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
