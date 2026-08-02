---
title: How do I ring the Doorbell?
apple_id: DTS10001202
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-05-17'
source_url: https://developer.apple.com/library/archive/qa/fw/fw02.html
archived_at: '2026-07-18T02:29:29.265611Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A FW02How do I ring the Doorbell? |

|  |  |
| --- | --- |
| ---   Q: How do I ring the Doorbell?  A: Ringing the Doorbell is rather simple, once you have the SBP2 device's fetch agent address. The Doorbell's address is 16 bytes past the fetch agent's address. To ring the Doorbell, you write any value into the Doorbell's address using the `FWWrite` command.  You get the address of the fetch agent from the login status notification (because each login could have its own fetch agent, and therefore Doorbell register). Make sure that you register a login status notification function before you log into your SBP2 device; otherwise, you won't get the address of the SBP2 device's fetch agent.    |  | | --- | | __Tip:__  Because the four-byte payload of the write to the Doorbell is ignored, you can put diagnostic information in it (but only four bytes), and examine the data with a FireWire packet analyzer. Even if you do not send diagnostic data, you must set a valid pointer in the asynchronous command object (the memory must be able to be held, for example). | |

#### [May 17 1999]

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
