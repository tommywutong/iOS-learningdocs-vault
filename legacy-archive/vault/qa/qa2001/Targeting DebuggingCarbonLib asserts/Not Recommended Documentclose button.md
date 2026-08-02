---
title: Targeting DebuggingCarbonLib asserts
apple_id: DTS10001585
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2001-05-04'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1033.html
archived_at: '2026-07-18T02:38:03.775479Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Carbon/index.html) > [Runtime Architecture](https://developer.apple.com/library/archive/technicalqas/Carbon/idxRuntimeArchitecture-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Runtime Architecture](https://developer.apple.com/referencelibrary/Carbon/idxRuntimeArchitecture-date.html)

|  |
| --- |
| Technical Q&A QA1033Targeting DebuggingCarbonLib asserts |

|  |  |
| --- | --- |
| ---   Q: When I replace `CarbonLib` with `DebuggingCarbonLib` in my extensions folder and reboot I get all the asserts for all Carbon applications that run on my machine. Is there any way to only get the asserts for the application that I'm debugging?  A: Yes; First reboot with the non-debugging `CarbonLib` in your extensions folder. Now change `DebuggingCarbonLib`'s file type to `'shlb'` so CFM thinks it's a shared library and then put it into the same folder as the Carbon application that you want to debug. Now when CFM launches this application it will load and link to the `DebuggingCarbonLib` shared library in your application's folder instead of connecting to the non-debugging `CarbonLib` in your extensions folder - only your application will generate the `DebuggingCarbonLib` asserts.   |  | | --- | | __Note:__  `CarbonLib` verifies at runtime that the same `CarbonLib` version installed at system startup time is the same as the version of the `CarbonLib` being used at runtime. Since the technique described in this Technical Q&A uses two different `CarbonLib`s, it is the developer's responsibility to verify that the version number for the debugging version of `CarbonLib` they are using is the same as the version number of the `CarbonLib` installed at system startup time. |       ---  [May 04 2001] |

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
