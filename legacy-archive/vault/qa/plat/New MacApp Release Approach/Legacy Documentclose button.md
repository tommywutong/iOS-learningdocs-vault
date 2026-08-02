---
title: New MacApp Release Approach
apple_id: DTS10001535
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-08-21'
source_url: https://developer.apple.com/library/archive/qa/plat/plat25.html
archived_at: '2026-07-18T02:29:53.427362Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxCarbon-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Carbon](https://developer.apple.com/referencelibrary/Carbon/index.html)

|  |
| --- |
| NOTE: This Technical Q&A has been [retired](https://developer.apple.com/library/archive/qa/index.html). Please see the [Technical Q&As](https://developer.apple.com/library/archive/qa/index.html) page for current documentation. |

|  |
| --- |
| Technical Q&A PLAT25New MacApp Release Approach |

|  |
| --- |
| ---   Q: Why is Apple now making the latest versions of MacApp available under a Release approach, instead of the previous Product Approach?  A: In response to the many messages we received from developers requesting early access to new framework features and timely support for new technologies, Apple has implemented a Release approach with MacApp that allows us to get new improvements and features in our frameworks into your hands more quickly than was possible with the Product approach.  Previous to the Release approach, our Product approach required that we implement all planned features before the MacApp product was considered final. We found that the Product approach was keeping us from getting new features to you simply because other more time-consuming work was delaying the completion of the product. Under the new Release approach, each framework release will be made up of features at various levels of certification. Most features will be of final quality, while others may be of beta or alpha quality. You can choose the features with which to build your MacApp-based application, and by doing so you will choose the quality level of the resulting application. Our build tools will indicate the quality level you have chosen from those build flags you have passed to them. The release notes which accompany each MacApp release will list the features included in the framework and their quality status.  Important: For each MacApp release, ALWAYS refer to the release notes for the quality status. For some releases, we recommend that you do not build applications which you intend to rely on as "final" quality applications. Releases that have final quality status are suitable for building final-quality MacApp-based applications.  Over the course of multiple releases, every feature will proceed through alpha, beta, and final quality phases. Some features will move rapidly from development into final quality, perhaps in as little time as one release, while other features may require several releases. This approach ensures that the software features Apple provides to you are of the highest possible quality, while still allowing you to experiment with new, unproven features.  In addition to giving you an early indication of the direction Apple is taking with MacApp, the release approach will also improve the timeliness of Apple's support for new technologies, because feedback regarding your needs and requirements can direct which module we enhance first.  Apple will create a new Release version of MacApp approximately once every six to nine months, and the MacApp product will ship once each ETO delivery cycle. Releases of MacApp that occur between ETO shipment dates will be posted to the Web. |

#### [Aug 21 1996]

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
