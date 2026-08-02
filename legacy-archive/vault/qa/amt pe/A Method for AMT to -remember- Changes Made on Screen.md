---
title: A Method for AMT to "remember" Changes Made on Screen
apple_id: DTS10001118
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-08-01'
source_url: https://developer.apple.com/library/archive/qa/amt_pe/amt_pe16.html
archived_at: '2026-07-18T02:29:23.531238Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Apple Applications](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxAppleApplications-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Apple Applications](https://developer.apple.com/referencelibrary/AppleApplications/index.html)

|  |
| --- |
| Technical Q&A AMTPE16A Method for AMT to "remember" Changes Made on Screen |

|  |  |  |
| --- | --- | --- |
| ---   The Apple Media Tool and Apple Media Tool Programming Environment products have been discontinued. For more information check out: [AMT/PE Discontinued](https://developer.apple.com/library/archive/qa/amt_pe/whatsup.html).  Q: I'm working on a project that requires the user to make selections on Screen1, then travel to Screen2. But I need AMTPE to "remember" the selections the user made on Screen1. Upon returning to Screen1 from Screen2, the selections initially made on Screen1 must show, for example, that the user moved an object from the default coordinates(100,100) to (150,150). How do I store the new Object Coordinates and have the Object recall the new coordinates instead of the default coordinates when you return to this screen?  Screen1 code looks like this:   |  | | --- | | ``` object MoveMe is MediaScroller has       MouseDown(theX, theY)               do                 self.moveto(theX, theY);               end;  -- stuff here with        X is 100, Y is 100 --etc. end; ``` |    When I leave Screen1, then return the object, `MoveMe` has returned to its initial Coordinates of x=100 and Y=100. Is there a way for AMT to "remember" changes made on a Screen?  A: After you use `MoveTo` to move your object from 100,100 to 150,150, add these lines:   |  | | --- | | ``` Self.StartX := Self.X; Self.StartY := Self.Y; ``` |    `StartX` and `StartY` determine where the object is initially drawn on the screen. Change them and it should behave the way you want when you return to the screen. |

#### [Aug 01 1995]

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
