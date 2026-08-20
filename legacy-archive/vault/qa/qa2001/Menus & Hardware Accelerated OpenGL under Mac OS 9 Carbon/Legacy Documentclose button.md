---
title: Menus & Hardware Accelerated OpenGL under Mac OS 9 Carbon
apple_id: DTS10001594
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2001-07-10'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1042.html
archived_at: '2026-07-18T02:38:05.622119Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Graphics & Imaging > OpenGL](https://developer.apple.com/referencelibrary/GraphicsImaging/idxOpenGL-date.html)

|  |
| --- |
| Technical Q&A QA1042Menus & Hardware Accelerated OpenGL under Mac OS 9 Carbon |

|  |
| --- |
| ---   Q: What can be done to prevent asynchronous OpenGL animation driven via a Carbon Timer from drawing over menus?  A: There are two cases to discuss in handling menus and asynchronous animation.  - Using Carbon Events  - Using WaitNextEvent  Carbon Events:  One needs to support two events and toggle animation when these are received. `kEventMenuBeginTracking` and `kEventMenuEndTracking` indicate when the menu is being drawn for normal menus, pop-up menus and contextual menus (which may actually track outside the window bounds). When the `kEventMenuBeginTracking` event is received the application should stop any asynchronous OpenGL animation. This is best achieved by setting a flag for your timer callback to read and not animate. One can still respond to update events as the application normally would. When the `kEventMenuEndTracking` is received re-enable the applications animations and proceed as normal  `WaitNextEvent`:  One wants to stop animating when receiving mouseDown type events whose part code is `inMenuBar`. Also do not initiate any contextual or pop-up menus which are under application control without toggling the hardware accelerated animation off. Once the `MenuSelect`, etc. function has returned, it is safe to animate once again. This will take care of most cases but will not handle system initiated pop-up type menus such as on a navigation services dialog. These situations can be handled on a case by case basis by toggling the animation off prior to bring up the system dialog.  These techniques allow simple handling of the deconfliction of Mac OS 9 menus with asynchronous hardware accelerated OpenGL blitting.  Mac OS X, of course, handles this integration automatically and does not need any of these techniques.   ---  [Jul 10 2001] |

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
