---
title: Resource chain corruption when using Navigation Services dialogs and Carbon
  Events
apple_id: DTS10001618
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2001-08-21'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1066.html
archived_at: '2026-07-18T02:38:06.408355Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxCarbon-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Carbon](https://developer.apple.com/referencelibrary/Carbon/index.html)

|  |
| --- |
| Technical Q&A QA1066Resource chain corruption when using Navigation Services dialogs and Carbon Events |

|  |
| --- |
| ---   Q: Why does my resource chain get corrupted when I call any of the Navigation Services dialogs since I started using Carbon Events?  A: If you detect this behavior, then you are most likely running Mac OS 8.5 to Mac OS 9.0.4 and using or handling Carbon Events.  Due to a Navigation Services bug, fixed only in Mac OS 9.2, the resource chain state would be saved before each call to WaitNextEvent and be restored to that state after the event had been handled. Any changes to the resource chain (ie. opening or closing files) would be lost and thus the resource chain would become corrupt.  Prior to the Carbon Events model, it was mostly unlikely that this would ever happen since it could only happen if the developer was modifying the resource chain while in a patch of WaitNextEvent.  Due to the fact that Carbon Events handlers can be executed at any time, including while there is a Navigation dialog open, the probability that this bug would show up is a lot higher.  This bug has been fixed in Mac OS 9.2 (the resource chain state is saved after the call to WaitNextEvent and restored after the event handling thus preserving changes happening at WaitNextEvent time) but cannot, for architectural reasons, be fixed in CarbonLib as well. Thus, developers must, to be safe, avoid opening or closing resource files in Carbon Events handlers while a Navigation dialog is opened, but they still can do so in Navigation event proc callbacks.   ---  [Aug 21 2001] |

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
