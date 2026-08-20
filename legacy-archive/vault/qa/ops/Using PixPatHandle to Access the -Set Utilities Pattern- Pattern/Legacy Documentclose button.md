---
title: Using PixPatHandle to Access the "Set Utilities Pattern" Pattern
apple_id: DTS10001493
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-09-27'
source_url: https://developer.apple.com/library/archive/qa/ops/ops12.html
archived_at: '2026-07-18T02:29:49.500876Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A OPS12Using PixPatHandle to Access the "Set Utilities Pattern" Pattern |

|  |
| --- |
| Q How can I access the "Set Utilities Pattern" pattern? (This pattern is set by holding down the option key in the Desktop Patterns Control Panel.)   A This control panel uses resources of type 'ppat' to store this pattern. The `ppat' resource is stored in the System file in your System Folder; the desktop pattern has an ID of 16 and the utilities pattern has an ID of 42. Since this is not documented, it could be subject to change at any moment. You should be careful when using this. A snippet of code is included here to show you how you can get to these two `ppat' resources.   ```  PixPatHandle ppatHandle;        ppatHandle = (PixPatHandle) GetPixPat(42);       if (ppatHandle != NULL) {           SetRect(&destRect;, 15, 125, 197, 164);           FrameRect(&destRect;);           FillCRect(&destRect;, ppatHandle);           DisposePixPat(ppatHandle);       } ```   **__Note:__** : You can just use GetPixPat to access a `ppat' resource -- the additional code just shows how to draw with it and dispose of it when done.   Updated: 27-September-96 |

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
