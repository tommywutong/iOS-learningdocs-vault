---
title: Creating Sample Descriptor Atoms for a Non-Mac Device
apple_id: DTS10002038
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '1995-08-01'
source_url: https://developer.apple.com/library/archive/qa/qtpc/qtpc06.html
archived_at: '2026-07-18T02:38:50.080970Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Design Guidelines](https://developer.apple.com/referencelibrary/QuickTime/idxDesignGuidelines-date.html)

|  |
| --- |
| Technical Q&A QTPC06Creating Sample Descriptor Atoms for a Non-Mac Device |

|  |
| --- |
| Q We have a non-Mac device that creates and reads QuickTime movies, and we need to pass additional information about the images between the non-Mac device and our QuickTime codec. It seems that the logical place to put this information is in an ImageDescription extension (within the 'stsd' atom), since this is about all that's accessible to a codec. Is the format of this extension documented anywhere? We've managed to look at the extension created by SetImageDescriptionExtension, and the format seems simple, but it'd be nice to know what the "official" format for this is.   A __Appendix A of _Inside Macintosh: QuickTime_has a listing of the atoms and their formats on page 4-35.__ Note that each media format has its own sample-description tables. In some cases, these are not directly accessible (Music architecture) unless you dump the information yourself. The official guideline is to use, if possible, the provided APIs for creating sample descriptor atoms. If you are working on a platform for which we don't have these toolbox APIs, you have to either reverse-engineer it, or ask for a source-code license agreement to get real source code showing how the atoms are constructed. For details regarding licensing part or all of the QuickTime source code, Contact Apple Software Licensing (AppleLink SW.LICENSE). [Aug 01 1995] |

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
