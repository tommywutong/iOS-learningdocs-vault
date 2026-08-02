---
title: Comparing selectors in Cocoa-Java code
apple_id: DTS10001621
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2001-08-31'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1069.html
archived_at: '2026-07-18T02:38:06.493059Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Cocoa](https://developer.apple.com/library/archive/technicalqas/Cocoa/index.html) > [Java](https://developer.apple.com/library/archive/technicalqas/Cocoa/idxJava-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Cocoa > Java](https://developer.apple.com/referencelibrary/Cocoa/idxJava-date.html)

|  |
| --- |
| Technical Q&A QA1069Comparing selectors in Cocoa-Java code |

|  |  |
| --- | --- |
| ---   Q: I'm comparing an `NSSelector` in my Cocoa Java code to an action from my nib, and they look like they are equal, but the test for equality fails. Why?  A: Interface Builder is on the other side of the Java Bridge that translates between Objective-C and your Java code, and thus the actions it archives in the nib are saved as Objective-C selectors. At runtime, the Objective-C selectors have names that end in ":" while the Java selectors don't, and thus two selectors that appear to point to the same code fail an equality test against their names. The solution is to check for both flavors of selector (like the following example comparing two actions) or strip off the colons yourself:       |  | | --- | | ```     if (someControl.action().name().equals("someActionSelector:")     || someControl.action().name().equals("someActionSelector")) {          // do something      } ``` |      ---  [Aug 31 2001] |

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
