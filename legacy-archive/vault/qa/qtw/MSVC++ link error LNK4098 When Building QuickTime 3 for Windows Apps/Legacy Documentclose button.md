---
title: MSVC++ link error LNK4098 When Building QuickTime 3 for Windows Apps
apple_id: DTS10002162
resource_type: QA
platform: macOS
topic: Cross Platform
technology: null
published: '1998-09-21'
source_url: https://developer.apple.com/library/archive/qa/qtw/qtw94.html
archived_at: '2026-07-18T02:38:53.229076Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > QuickTime for Windows](https://developer.apple.com/referencelibrary/QuickTime/idxQuickTimeforWindows-date.html)

|  |
| --- |
| Technical Q&A QTW94MSVC++ link error LNK4098 When Building QuickTime 3 for Windows Apps |

|  |  |
| --- | --- |
| ---   Q: I am getting the following link errors when building a QuickTime 3 for Windows application using the Microsoft Visual C++ development environment:     |  | | --- | | ``` LINK : warning LNK4098: defaultlib "LIBCMT" conflicts with use of other libs; use /NODEFAULTLIB:library ``` |    What's going on?  A: QuickTime 3 for Windows is carefully linked with the multi-threaded version of the C runtime (`LIBCMT`). This can cause a conflict with your build settings. To avoid the conflict, you'll need to adjust your build settings to link with `LIBCMT` and recompile all your code (the runtime library is actually chosen in MSVC++ as a compile-time option, not a link-time option).  Go to the MSVC++ "Project", "Settings" dialog (ALT+F7 will work too), select the "C/C++" tab, then the "Code Generation" category. Under the popup menu for "Use run-time library", select "multi-threaded" or "multi-threaded DLL" as needed by your project. QuickTime 3 for Windows is built with "multi-threaded" selected.  If you don't use the IDE, use the C command-line option /MT. [Sep 21 1998] |

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
