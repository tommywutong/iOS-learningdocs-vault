---
title: Setting request headers in URL Access
apple_id: DTS10001625
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2002-09-10'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1073.html
archived_at: '2026-07-18T02:38:06.581088Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/Networking/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Networking/idxCarbon-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Networking > Carbon](https://developer.apple.com/referencelibrary/Networking/idxCarbon-date.html)

|  |
| --- |
| Technical Q&A QA1073Setting request headers in URL Access |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| ---   Q: Why do transfers fail using URL Access when I use kURLHTTPRequestHeader to set the header?  A: Due to a bug in URL Access (r. 2644424) on Mac OS 8.6 through Mac OS X 10.0.4, trying to set the entire header for a transfer by using kURLHTTPRequestHeader will cause duplicate headers, and the transfer will most likely fail. This bug was fixed in Mac OS X 10.1, but to workaround the problem in older versions of Mac OS, simply use the other URL Access constants to set the individual components of the header instead of trying to set the entire header at once. The other constants being...   |  |  | | --- | --- | | __kURLHTTPRequestMethod__ | - examples are 'GET' or 'POST'. | | __kURLHTTPUserAgent__ | - your desired user agent string. | | __kURLHTTPRequestHeader__ | - the remaining content of your header. |      ---  [Sep 10 2002] |

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
