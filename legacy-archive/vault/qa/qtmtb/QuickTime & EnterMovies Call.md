---
title: QuickTime & EnterMovies Call
apple_id: DTS10002006
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb36.html
archived_at: '2026-07-18T02:38:48.468317Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > QuickTime](https://developer.apple.com/referencelibrary/QuickTime/index.html)

|  |
| --- |
| Technical Q&A QTMTB36QuickTime & EnterMovies Call |

|  |
| --- |
| Q The QuickTime 1.0 documentation states that you can use the EnterMovies call multiple times, as long as you balance each EnterMovies with ExitMovies. However, an article in issue 13 of _develop_ says, not to call ExitMovies, as ExitToShell does this for me. This seems to destroy the balance of these routines. Which is the correct technique?   A EnterMovies creates a new QuickTime environment if the current A5 world doesn't already have one. If the current A5 world has a QuickTime environment from a previous EnterMovies call, then nothing is done except to increment a counter that keeps track of the number of times EnterMovies was called. This is done to account for DAs which use an application's A5 world, so that if an application has already called EnterMovies, the movie toolbox knows that it doesn't have to reinitialize when the DA calls EnterMovies. When the DA calls ExitMovies, it decrements the counter, and as long as all EnterMovies and ExitMovies calls are balanced, the Movie Toolbox doesn't dispose of the QuickTime world until the last ExitMovies call is made. Since ExitToShell automatically calls ExitMovies for you, you can avoid some of the problems that developers have with disposing of movie structures improperly and in the wrong order. Letting ExitToShell do the final cleanup avoids these problems, because the entire A5 world and heap is disposed of as well.  If you currently have nested EnterMovies and ExitMovies calls, this is what we recommend:  1. If you're writing an application, and you call EnterMovies, but don't call ExitMovies, any external that uses the same A5 world and calls EnterMovies and ExitMovies increments the counter and then decrements the counter and does nothing else.  2. If you're writing an external that runs under someone else's application, you have two choices:  A. Call EnterMovies, but never call ExitMovies. This causes QuickTime to initialize once during the first call to any of your externals.  B. Call EnterMovies at the beginning of each external and ExitMovies at the end of each external. Be aware that this can waste a lot of CPU time if the main application (or something else in the A5 world) doesn't call EnterMovies first, since each of the EnterMovies calls in your externals requires QuickTime to reinitialize. This can be a serious problem if your external is called often. However, if your external has an initialization routine and a close routine that is called before and after all your other routines, you can call EnterMovies in the initialization routine, and then call ExitMovies in your close routine. Of course, each of the routines called in between could call either EnterMovies and ExitMovies, or not call either of them at all, depending on your implementation. [May 01 1995] |

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
