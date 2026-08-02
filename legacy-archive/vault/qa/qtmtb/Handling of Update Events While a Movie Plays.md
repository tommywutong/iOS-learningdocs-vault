---
title: Handling of Update Events While a Movie Plays
apple_id: DTS10002015
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-09-15'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb45.html
archived_at: '2026-07-18T02:38:48.980753Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/QuickTime/index.html) > [Movie Basics](https://developer.apple.com/library/archive/technicalqas/QuickTime/idxMovieBasics-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Movie Basics](https://developer.apple.com/referencelibrary/QuickTime/idxMovieBasics-date.html)

|  |
| --- |
| Technical Q&A QTMTB45Handling of Update Events While a Movie Plays |

|  |
| --- |
| Q We are writing a screen saver that plays QuickTime movies. Our `WaitNextEvent` loop and code is very basic. We have noticed that other background applications don't get any time, even if we use `WaitNextEvent` and make sure `MoviesTask` does not spend too much time playing the movie. However, if we add code to track the `updateEvents` with `BeginUpdate` and `EndUpdate` the problem is gone. Why?   A QuickTime and other parts are sending update events to your application. If these update events are not handled, they are resent, resulting in no time yield to other applications. By calling `BeginUpdate/EndUpdate` or otherwise taking care of the update event inside your `WaitNextEventLoop`, you allow yielding to other applications. See Technote [TB 37 Pending Update Perils](https://developer.apple.com/library/archive/technotes/tb/tb_37.html), which discusses this situation [Sep 15 1995] |

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
