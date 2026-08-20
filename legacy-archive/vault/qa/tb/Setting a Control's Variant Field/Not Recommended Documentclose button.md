---
title: Setting a Control's Variant Field
apple_id: DTS10002249
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-05-03'
source_url: https://developer.apple.com/library/archive/qa/tb/tb63.html
archived_at: '2026-07-18T02:38:58.124768Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Carbon/index.html) > [Human Interface Toolbox](https://developer.apple.com/library/archive/technicalqas/Carbon/idxHumanInterfaceToolbox-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Human Interface Toolbox](https://developer.apple.com/referencelibrary/Carbon/idxHumanInterfaceToolbox-date.html)

|  |
| --- |
| Technical Q&A TB63Setting a Control's Variant Field |

|  |
| --- |
| ---   Q: Given that there is no `SetControlVariant`, what is the proper method to set a control's variant field?  A: None. There is no good way to set a control's variant; standard controls do not support dynamic variants. If you need to change the variant of a custom control after creating the control, it's better not to use variants at all. Instead, let the clients of your control call `SetControlData` to change the behavior and/or appearance of your control. [May 03 1999] |

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
