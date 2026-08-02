---
title: Moving the Menu Bar
apple_id: DTS10002240
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1998-12-22'
source_url: https://developer.apple.com/library/archive/qa/tb/tb54.html
archived_at: '2026-07-18T02:38:57.673254Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Carbon/index.html) > [Human Interface Toolbox](https://developer.apple.com/library/archive/technicalqas/Carbon/idxHumanInterfaceToolbox-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Human Interface Toolbox](https://developer.apple.com/referencelibrary/Carbon/idxHumanInterfaceToolbox-date.html)

|  |
| --- |
| Technical Q&A TB54Moving the Menu Bar |

|  |
| --- |
| ---   Q: Under certain conditions, I want to move the menu bar from the main Macintosh display to some other display. Is this possible?  A: We have found that in most cases users find it highly confusing when this is done any other way than through the Monitors & Sound control panel. In general, we like to discourage this sort of thing and instead recommend that developers implement a floating tool palette which the user can move between displays at will; she is likely to understand this better and in all probability will find it more useful, since she'll have control over the palette's placement in both the X and Y axes.  However, there is indeed a function which will allow you to move the menu bar to another display -- assuming you're willing to accept a few more changes than you might like. `DMSetMainDisplay`, a Display Manager function, sets the main display to an arbitrary display, and a side effect of this is that the menu bar moves to the new main display. However, this causes a lot of window reconfiguration, and Finder icons even move around on the desktop, so we think that doing this is almost always more trouble for the user than it's worth.  Further Reference:  [Inside Macintosh: Menu Manager](https://developer.apple.com/documentation/macos8/HumanInterfaceToolbox/MenuManager/menumanager.html)  [Display Manager documentation](https://developer.apple.com/documentation/hardware/DeviceManagers/displaydevices/displaydevices.html)  [Human Interface Guidelines](https://developer.apple.com/documentation/macos8/HumanInterfaceToolbox/HumanInterfaceGuide/humaninterfaceguide.html) [Dec 22 1998] |

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
