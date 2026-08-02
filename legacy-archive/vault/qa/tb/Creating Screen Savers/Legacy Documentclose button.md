---
title: Creating Screen Savers
apple_id: DTS10002191
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/tb/tb05.html
archived_at: '2026-07-18T02:38:55.159440Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A TB05Creating Screen Savers |

|  |
| --- |
| Q I am trying to create a simple screen saver. I have some questions about the QuickDraw global qd and current Grafport. My code patches a _GetNextEvent trap to determine the amount of time the machine is idle, performs an operation, and then calls the real _GetNextEvent, which is saved at load time. My problem is that there is no qd, because my code is not an application, and it resides in the system heap. All of my attempts to get current GrafPort have failed. Therefore, I cannot draw anything on the screen. How can I accomplish this? If the system calls my code, what is the current GrafPort (or how can I get one)? I tried creating my own GrafPort, but it didn't work. A Avoid patching anything, if at all possible -- especially _GetNextEvent. You can install a JGNEFilter procedure to check for system activity. The current GrafPort is a QuickDraw global, and QuickDraw globals are part of the A5 world. Since your screen saver is stand-alone code, and you don't have your own A5 world, you can't obtain the current GrafPort. If you attempt to, you are likely to get a window or dialog GrafPort, probably from the front-most application. This isn't much use in a screen saver, as you can save only the portion of the screen where the window or dialog is drawn.  To avoid the GrafPort problem, you could construct your own A5 world, but this approach will quickly transform your "simple screen saver" into a technical nightmare that would have an even greater compatibility risk than your present code does. For more information on JGNEFilter, see [Technote 1060, Controlling Apps with Synthesized Events, or jGNEFilter -- the Untold Story.](https://developer.apple.com/library/archive/technotes/tn/tn1060.html)  One approach is to launch an application that creates a window over the entire screen. Since the amount of time it takes to activate a screen saver isn't critical, you could do this when it's time for your screen saver to take control, or you could have it constantly running in the background, and send it to the front. Once your application is in the foreground, you can safely draw anything you want on the screen. To restore the screen, simply close the application, or send it to the background. [May 01 1995] |

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
