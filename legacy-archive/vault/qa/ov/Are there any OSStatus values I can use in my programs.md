---
title: Are there any OSStatus values I can use in my programs?
apple_id: DTS10001509
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-11-22'
source_url: https://developer.apple.com/library/archive/qa/ov/ov02.html
archived_at: '2026-07-18T02:29:50.646683Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Carbon/index.html) > [Design Guidelines](https://developer.apple.com/library/archive/technicalqas/Carbon/idxDesignGuidelines-date.html) >

|  |
| --- |
| Technical Q&A OV02Are there any OSStatus values I can use in my programs? |

|  |
| --- |
| ---   Q: My code is careful about runtime errors, but sometimes I need to generate an error which does not correspond to anything in the system. Are there any `OSStatus` values I can use in my programs without fear of colliding with Apple values (past, present, or future)?  A: Yep. You can use any value from 1000 to 9999, inclusive. We've verified that our internal registry of error values in use by past and present versions of the system contains no values in this range, and we've now registered this range for use by developers so that future versions of the system won't return any of these values.  Don't allow any of these error values to propagate into code whose interface you don't control. If you define the value 1000 to mean something specific to your program, don't expect the system or another program to understand unless you also control that other program.  Furthermore, don't attempt to reserve values within the developer range, even if you intend to use those values for a public interface, such as a Code Fragment Manager shared library or a Component Manager component. There is no registry for values within the developer range, and thus there is no way to avoid collisions with values used by other developer programs.  Another example of a public interface would be a plug-in architecture; potential clients of such an architecture may want to reuse code that already has meanings associated with some values in the developer range. You probably want to minimize the chance that potential plug-in developers will need to expend effort to resolve error code collisions. Similarly, if you are developing a plug-in, don't return errors within the developer range to your host program unless you know your host expects them.  Finally, if you're presently using other values in your program and hoping to get away with it because they're not in <MacErrors.h>, don't. Apple presently reserves all values which are not in the developer range. |

#### [Nov 22 1999]

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
