---
title: How can I add the ability to read and write Keynote 2 documents to my application?
apple_id: DTS10003507
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2005-09-13'
source_url: https://developer.apple.com/library/archive/qa/qa2005/qa1412.html
archived_at: '2026-07-18T02:38:32.738695Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



|  |  |
| --- | --- |
|  |  |
| [ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Apple Applications](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxAppleApplications-date.html) > | [ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Apple Applications](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxAppleApplications-date.html) > |
|  |  |

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Apple Applications > Keynote](https://developer.apple.com/referencelibrary/AppleApplications/idxKeynote-date.html)

|  |
| --- |
| Technical Q&A QA1412How can I add the ability to read and write Keynote 2 documents to my application? |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Q: How can I add the ability to read and write Keynote 2 documents to my application? A: Keynote 2 introduced several new features, and with them, a significantly expanded and revised document file format. Existing applications which read and write the Keynote 1.x file format will need to be updated to read and write the new format.  Although the complete XML schema for Keynote is not available and will not be made public, the "iWork Programming Guide" (which covers Keynote and Pages) provides details on the new file format. This programming guide is available in the Developer Reference Library under [Apple Applications > Keynote](https://developer.apple.com/documentation/AppleApplications/Keynote-date.html).  __Note:__ Keynote 2 will read existing Keynote 1.x files, so you can continue creating documents in the older file format programmatically from your application. The original file will be converted to the new format and overwritten when it is saved from within Keynote 2. __However, Apple strongly recommends you do not continue creating Keynote 1.x files unless you are targeting Keynote 1.x users.__ You should create Keynote 2.x files for Keynote 2.x users. Document Revision History  | Date | Notes | | --- | --- | | 2005-09-13 | Updated to reflect publication of the iWork Programming Guide. | | 2005-03-22 | Describes where to find information about the Keynote 2 file format. | |

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
