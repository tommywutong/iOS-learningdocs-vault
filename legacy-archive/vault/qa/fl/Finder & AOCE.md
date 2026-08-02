---
title: Finder & AOCE
apple_id: DTS10001188
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-11-01'
source_url: https://developer.apple.com/library/archive/qa/fl/fl02.html
archived_at: '2026-07-18T02:29:28.573460Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [User Experience](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxUserExperience-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > User Experience](https://developer.apple.com/referencelibrary/UserExperience/index.html)

|  |
| --- |
| Technical Q&A FL02Finder & AOCE |

|  |
| --- |
| ---   Q: Why doesn't the Finder show AOCE's Mail Enclosures volume?  A: AOCE's Mail Enclosures volume is hidden because it should not be accessed directly by the user. The Finder hides AOCE's Mail Enclosures volume because its root directory has the `kIsInvisible` Finder flag set.  You can use the routine `SetIsInvisible` in the DTS sample code `MoreFiles` to make the root directory of any volume invisible and the next time the volume is mounted, the Finder won't show that volume. There is no way to force the Finder to notice the change and make the volume invisible on the fly.  Note that the Finder did not support invisible volumes until System 7 Pro (System 7.1.1). So, with System 7.1 and earlier, you can't make volumes invisible. |

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
