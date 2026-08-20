---
title: What Does Extension Manager Turn Off?
apple_id: DTS10001488
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-09-15'
source_url: https://developer.apple.com/library/archive/qa/ops/ops07.html
archived_at: '2026-07-18T02:29:49.211238Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Apple Applications](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxAppleApplications-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Apple Applications](https://developer.apple.com/referencelibrary/AppleApplications/index.html)

|  |
| --- |
| Technical Q&A OPS07What Does Extension Manager Turn Off? |

|  |
| --- |
| Q What does turning everything off in the Extension Manager actually turn off?   A The only files which Extension Manager turns off are those which it shows. Conversely, those items not shown by the Extension Manager will not be turned off. This information is not documented, and the following list is not guaranteed complete or accurate and is certain to change in the future. There are four creator types that Extension Manager does not show in its list: 'mntr', 'DMOV', 'extE', and '8INI'. Items of type 'extE' and '8INI' are not shown because the Extension Manager extension has the creator of 'extE' and the Extension Manager control panel has the creator of '8INI'. This way you can not use Extension Manager to disable itself.  Also, Extension Manager will not show any item of type 'INIT', 'RDEV', or 'cdev' if they have the "No INITs" Finder flag set.  Extension Manager only shows items whose types are:   ``` 'INIT' 'RDEV' 'cdev' 'PRES' 'PRER' 'adev' 'fext' 'scri' 'cbnd' 'fbdn' 'tbnd' 'ddev' 'appe' 'gc24' 'adrp' 'dbgr' 'dfil' 'APPL' 'FFIL' 'pext' 'vbnd' ```   See [OPS 06](Legacy%20Documentclose%20button-2.md) for items turned off with Shift Booting. Updated: 15-Sept-95 |

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
