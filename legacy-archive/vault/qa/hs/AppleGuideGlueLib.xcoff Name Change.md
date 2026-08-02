---
title: AppleGuideGlueLib.xcoff Name Change
apple_id: DTS10001102
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-05-14'
source_url: https://developer.apple.com/library/archive/qa/hs/ag02.html
archived_at: '2026-07-18T02:29:35.104848Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [User Experience](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxUserExperience-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [User Experience > Help Technologies](https://developer.apple.com/referencelibrary/UserExperience/idxHelpTechnologies-date.html)

|  |
| --- |
| Technical Q&A AG02AppleGuideGlueLib.xcoff Name Change |

|  |
| --- |
| Q We are developing an application that uses Apple Guide for its help. This is working well on 68K Macs, but is presenting a problem on PowerMacs, because of AppleGuideGlue. If we import this library as "weak," the program runs but crashes when we call any Apple Guide routines. If we import "strong," the program simply refuses to run.   A The .xcoff produces a reference to a shared library named "AppleGuideGlue". Unfortunately, the Apple Guide extension provides a library named "AppleGuideGlueLib" instead. Consequently, the reference is not resolved and the application fails to launch. The AppleGuideGlue.xcoff has been changed to AppleGuideGlueLib.xcoff on the current Mac OS SDK. You just need to rename the one you have before including it in your project.  In MPW, you can rename the library in the link process. Using either Symantec or MetroWerks, however, the name has to match for it to be found at runtime. Note that Metrowerks ignores the ".xcoff" if it is present in the name, while Symantec must have the ".xcoff" to properly include the file in the project. Updated: 14-May-96 |

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
