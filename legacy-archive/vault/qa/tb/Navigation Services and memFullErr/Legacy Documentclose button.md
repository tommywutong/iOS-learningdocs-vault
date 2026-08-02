---
title: Navigation Services and memFullErr
apple_id: DTS10002226
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-07-06'
source_url: https://developer.apple.com/library/archive/qa/tb/tb40.html
archived_at: '2026-07-18T02:38:57.102501Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Human Interface Toolbox](https://developer.apple.com/referencelibrary/Carbon/idxHumanInterfaceToolbox-date.html)

|  |
| --- |
| Technical Q&A TB40Navigation Services and memFullErr |

|  |
| --- |
| Q When I make one of the Navigation Services browsing calls, like `NavGetFolder`, nothing happens on the screen and I get -108 (`memFullErr`) as a return value, even though MacsBug tells me there are megabytes of free memory in the application, system, and process manager heaps. Why?   A There are two known potential reasons for this phenomemon:  - The classic 68K glue (a.k.a. `Navigation.o`) for Navigation Services 1.0 makes Code Fragment Manager and Mixed Mode Manager calls to invoke the appropriate routine in the Navigation Services shared library. The glue starts out with the assumption that it   will fail due to `memFullErr`. If, however, it fails for one of   several other reasons, it doesn't update its assumption and   reports the failure as if it exhausted available memory. One   problem which is masked this way is the absence of the shared   library. By calling `NavServicesAvailable` before attempting to use   the rest of `Nav`, as documented, you will know that `Nav` is not   installed and avoid the confusing `memFullErr`. - Navigation Services is able to make a reasonable estimate of   the minimum amount of memory it will need to display a browsing   dialog. If this amount of memory is not available, the call   returns `memFullErr` without any on-screen evidence of the failure.   If your application failed to call `MaxApplZone` before calling `Nav`,   `Nav` will be fooled into believing your heap is tiny or nearly   full. `MaxApplZone` is an important part of a balanced breakfast.   Call it.  [Jul 06 1998] |

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
