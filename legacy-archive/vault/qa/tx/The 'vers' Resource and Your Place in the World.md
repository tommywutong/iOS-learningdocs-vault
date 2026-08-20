---
title: The 'vers' Resource and Your Place in the World
apple_id: DTS10002266
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-05-01'
source_url: https://developer.apple.com/library/archive/qa/tx/tx14.html
archived_at: '2026-07-18T02:38:59.384562Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Carbon/index.html) > [Resource Management](https://developer.apple.com/library/archive/technicalqas/Carbon/idxResourceManagement-date.html) >

|  |
| --- |
| Technical Q&A TX14The 'vers' Resource and Your Place in the World |

|  |
| --- |
| ---   Q: I am having trouble getting fonts to display correctly in my localized application. Is there anything that I should check?  A: You should ensure that the country code in the `'vers'` resource is set correctly for the country for which the application is localized. This is particularly important under current systems (OS 9.0 and later) since the language manager is present by default. Since the system uses the region code in the `'vers'` resource to determine the appropriate fonts to employ for the user interface (menus, dialogs, window titles, and so on), having an incorrect region code can lead to illegible text.  Both Resorcerer and ResEdit support setting the proper country code in an applications `'vers'` resource. The possible region codes are enumerated in the latest Universal Headers Script.h file, listed under Region codes. Developers should look to this reference for current region codes. More information on script systems and regions codes can be found in [Inside Macintosh: Text](https://developer.apple.com/documentation/mac/Text/Text-2.html). [May 01 2000] |

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
