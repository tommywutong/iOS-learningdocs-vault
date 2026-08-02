---
title: Control Panel Problems with Popup Menu's Click Area
apple_id: DTS10002190
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/tb/tb04.html
archived_at: '2026-07-18T02:38:55.087794Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A TB04Control Panel Problems with Popup Menu's Click Area |

|  |
| --- |
| Q In developing the Control Panel for our driver, I'm having a problem getting a popup menu's click area to register correctly. Currently, you can click on the popup's title to activate the control, but clicking on the popup box does not seem to register. Using Resedit, I have tried to compare the DITL's bounds information with that found in the `'ctrl'` resource, but I haven't been able to make any connections between the two sets of coordinates. We are using a ProcID of 1008.   A The problem you describe is most often the result of having improper values in the `'ctrl'` resource. Here are some guidelines for the values for the various fields: BoundsRect: The bounds rect should be big enough to frame both the popup menu title and the popup menu indicator.  Value: Holds the constant which allows you to specify the style and justification of the popup.  Max: The width of the popup menu title.  Min: The resource ID of the 'MENU' resource.  ProcID: 1008 + a variation code, if desired.  RefCon: For your application to use.  Title: Whatever you'd like.  It is important to have values for Bounds and Max that make sense. The following figure shows the relationship between the numbers:   ```     Popup: [Popup Item ]  |    >                           bounds.left |                           >    bounds.right       |     >                    title width (Max) ```  [May 01 1995] |

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
