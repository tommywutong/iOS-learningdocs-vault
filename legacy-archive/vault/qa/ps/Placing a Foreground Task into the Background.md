---
title: Placing a Foreground Task into the Background
apple_id: DTS10001553
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-09-27'
source_url: https://developer.apple.com/library/archive/qa/ps/ps04.html
archived_at: '2026-07-18T02:29:54.635851Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Process Management](https://developer.apple.com/referencelibrary/Carbon/idxProcessManagement-date.html)

|  |
| --- |
| Technical Q&A PS04Placing a Foreground Task into the Background |

|  |
| --- |
| ---   Q: How do you run a "foreground" task to place itself in the background?  A You should use `LaunchApplication` call in the Process Manager with the `launchDontSwitch` flag set in the `launchControlFlags` field. You can find more information about `LaunchApplication` in [_Inside Macintosh: Processes_, Chapter 2](https://developer.apple.com/library/archive/documentation/mac/Processes/Processes-21.html). |

#### [Sep 27 1996]

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
