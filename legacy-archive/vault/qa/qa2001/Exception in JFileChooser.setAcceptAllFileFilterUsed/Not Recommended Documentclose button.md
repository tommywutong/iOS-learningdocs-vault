---
title: Exception in JFileChooser.setAcceptAllFileFilterUsed
apple_id: DTS10002332
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2003-10-07'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1280.html
archived_at: '2026-07-18T02:38:30.738011Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Java](https://developer.apple.com/library/archive/technicalqas/Java/index.html) > [User Experience](https://developer.apple.com/library/archive/technicalqas/Java/idxUserExperience-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Java > User Experience](https://developer.apple.com/referencelibrary/Java/idxUserExperience-date.html)

|  |
| --- |
| Technical Q&A QA1280Exception in JFileChooser.setAcceptAllFileFilterUsed |

|  |
| --- |
| ---   Q: After installing the Java 1.4.1 Update 1 on Mac OS X 10.2, my application throws an `ArrayIndexOutOfBoundsException` whenever I call `JFileChooser.setAcceptAllFileFilterUsed` . What's the problem?  A: This is a known problem that emerged with 1.4.1 Update 1 for Jaguar systems. The problem occurs when a `JFileChooser` has already received calls to `addChoosableFileFilter`  or `setFileFilter` . If the call to `setAcceptAllFileFilterUsed` is made before any other state management is done on the `JFileChooser` , the problem can be avoided. This workaround should be manageable in any circumstance.  Some applications reuse a single `JFileChooser` that may have `setAcceptAllFileFilterUsed` called on the fly, based on changing runtime conditions. In such a case, you would need to construct a separate `JFileChooser` for each "Accept All" or "Don't Accept All" scenario to sufficiently work around this problem.   ---  [Oct 07, 2003] |

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
