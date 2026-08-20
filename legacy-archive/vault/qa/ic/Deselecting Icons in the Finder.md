---
title: Deselecting Icons in the Finder
apple_id: DTS10001375
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-07-11'
source_url: https://developer.apple.com/library/archive/qa/ic/ic04.html
archived_at: '2026-07-18T02:29:40.529392Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Carbon/index.html) > [Interapplication Communication](https://developer.apple.com/library/archive/technicalqas/Carbon/idxInterapplicationCommunication-date.html) >

|  |
| --- |
| Technical Q&A IC04Deselecting Icons in the Finder |

|  |
| --- |
| ---   Q: Is there any way to programmatically deselect icons that were previously selected in the Finder?  A: Yes, actually, there are a few different methods you can use. You can deselect all icons that are selected in the Finder by doing the following:   1. You can do this through AppleScript by doing the following: ignoring application responses tell application "Finder" to set selection to {} end ignoring. This is equivalent to sending the event with `kAENoReply`. 2. If you want to do this from within your application and don't want to go through the trouble of building up the proper AppleEvents to send to the Finder, you can pre-compile the above script and use `OSALoadExecute`() to invoke it. You can pre-compile the script and use `OSALoadExecute`() to invoke it. This is covered in [Inside Macintosh - Interapplication Communication](https://developer.apple.com/documentation/mac/IAC/IAC-2.html) pages 10-61 thru 10-63.   These two methods will deselect ALL icons that are selected in the Finder. On the other hand, if you only want to deselect the icon for a particular item, you would need to ask the Finder for the selection, walk through the list of selected items, remove your item, then set the selection to the resulting list. Check out the _develop_ issue 20 article "[Scripting the Finder From Your Application](https://developer.apple.com/dev/techsupport/develop/issue20/20anderson.html)" for details on getting and setting the Finder selection. An alternate way of performing the action would be to build an Apple event procedurally and send the event by calling `AESend`. |

#### [Jul 11 1997]

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
