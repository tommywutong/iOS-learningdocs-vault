---
title: Getting NSWindow's toolbar actions to show up in Interface Builder
apple_id: DTS10001582
resource_type: QA
platform: Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2001-05-03'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1030.html
archived_at: '2026-07-18T02:38:03.601357Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Cocoa](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxCocoa-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Cocoa > Tools](https://developer.apple.com/referencelibrary/Cocoa/idxTools-date.html)

|  |
| --- |
| Technical Q&A QA1030Getting NSWindow's toolbar actions to show up in Interface Builder |

|  |
| --- |
| ---   Q: I'm trying to add NSToolbars to my Cocoa application. I'm supposed to hook up my "Hide Toolbar" and "Customize Toolbar..." menu items to the First Responder's -toggleToolbarShown: and -runToolbarCustomizationPalette: actions, respectively, but I don't see those actions in Interface Builder! How do I wire them up?  A: Those two actions are indeed implemented by NSWindow (and they are already in NSWindow.h), but Interface Builder doesn't list them by default (a bug). They handle some of the processing of the window's toolbar for you, so you don't have to write it yourself. You need to manually add them to the First Responder in Interface Builder, the same way you would add actions to your own custom classes (select First Responder in the Classes tab, choose "Add Action" from the Classes menu, and enter the action's name, for example). Then you can wire up your menu items to those actions.     ---  [May 03 2001] |

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
