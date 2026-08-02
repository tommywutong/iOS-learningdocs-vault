---
title: Activating CrashReporter in OS X
apple_id: DTS10001609
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2001-05-13'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1057.html
archived_at: '2026-07-18T02:38:06.117494Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [User Experience](https://developer.apple.com/library/archive/technicalqas/UserExperience/index.html) > [Tools](https://developer.apple.com/library/archive/technicalqas/UserExperience/idxTools-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [User Experience > Tools](https://developer.apple.com/referencelibrary/UserExperience/idxTools-date.html)

|  |
| --- |
| Technical Q&A QA1057Activating CrashReporter in OS X |

|  |
| --- |
| ---   Q: How can I get a dump of all active thread states at the time of an application crash?  A: When a crash occurs in Mac OS X (10.0.x), state information can be automatically output to the console by enabling the CrashReporter. This will cause the state of all active threads to be dumped to the console at the time of the application crash. This can be useful to debugging your application, or for submission of an Apple software defect through [Bug Reporter](http://bugreport.apple.com/).  To enable CrashReporter:   1. Open Console (in /Applications/Utilities). 2. Select __Preferences...__ from the Application Menu. 3. Select the __Crashes__ tab. 4. Check the __Log crash information in...__ checkbox.   Now, when an application crashes, you should receive a confirmation for CrashReporter to write state information to the console. Choose "Yes", open the console window, and happy debugging!  If you have CrashReporter enabled, please include the information obtained from it when reporting an Apple software defect through Bug Reporter, as it could prove useful in investigating the problem.   ---  [May 13 2002] |

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
