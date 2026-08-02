---
title: Calling InitializeQTML from DLL Main
apple_id: DTS10002157
resource_type: QA
platform: macOS
topic: Cross Platform
technology: null
published: '1998-09-21'
source_url: https://developer.apple.com/library/archive/qa/qtw/qtw89.html
archived_at: '2026-07-18T02:38:53.118669Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > QuickTime for Windows](https://developer.apple.com/referencelibrary/QuickTime/idxQuickTimeforWindows-date.html)

|  |
| --- |
| Technical Q&A QTW89Calling InitializeQTML from DLL Main |

|  |
| --- |
| Q Is there a known problem calling the QuickTime 3 for Windows `InitializeQTML(0)` function from the `DllMain` procedure of a DLL?   A Yes, but there's more to it than that. It's a known problem on Windows with calling `LoadLibrary` or `FreeLibrary` (or any of several other APIs) from the `DllMain` procedure of a DLL. The basic rule of thumb on Windows is: "Don't do anything significant in your DLL Main." Moreover, don't \*ever\* call DLL-related APIs. Instead, I would recommend adding an Initialize call to your DLL that calls `InitializeQTML`, and a Terminate call that calls `TerminateQTML`. That avoids the problem entirely. [Sep 21 1998] |

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
