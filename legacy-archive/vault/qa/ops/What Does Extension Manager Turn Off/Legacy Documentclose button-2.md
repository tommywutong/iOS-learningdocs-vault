---
title: Shift Booting under System 7
apple_id: DTS10001487
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-09-15'
source_url: https://developer.apple.com/library/archive/qa/ops/ops06.html
archived_at: '2026-07-18T02:29:49.115313Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md) · [What Does Extension Manager Turn Off?](Legacy%20Documentclose%20button.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A OPS06Shift Booting under System 7 |

|  |
| --- |
| Q What does holding the Shift key at bootup turn off under System 7?   A This information is not documented, and the following list is not guaranteed complete or accurate and is certain to change in the future. Under System 7.0 through System 7.5 the following files are explicitly skipped:  - MacsBug will not load under System 7.0; under System 7.5 MacsBug will load if   the Option key is held down along with the Shift key. - A/ROSE - Virtual Memory - files of type:   ```     'scri' (Roman still works)     'cdev'     'RDEV'     'INIT'     'cbnd'     'fbnd'     'tbnd'     'adev'     'ddev'     'appe'     'fext'     'AINI'     'thng' ```   - Shift booting also turns off the Finder Startup and Shutdown items, since the   extension Finder Scripting Extension controls these tasks. - Under System 7.0 the disk cache is set to 64K; System 7.5 sets it to 96K.   See [OPS 07](Legacy%20Documentclose%20button.md) for items turned off with the Extension Manager.    Updated: 15-Sept-95 |

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
