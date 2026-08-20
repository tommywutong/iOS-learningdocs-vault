---
title: Submenus not Updating With Mac OS Screen MenuBar
apple_id: DTS10001703
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2002-07-12'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1171.html
archived_at: '2026-07-18T02:38:16.988026Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Java](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxJava-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Java > User Experience](https://developer.apple.com/referencelibrary/Java/idxUserExperience-date.html)

|  |
| --- |
| Technical Q&A QA1171Submenus not Updating With Mac OS Screen MenuBar |

|  |  |  |
| --- | --- | --- |
| ---   Q: When I use the screenMenuBar property from Q&A 1003, submenus in my Swing application do not update if I add or remove JMenuItems to them.  A: This is a known problem with the current screenMenuBar implementation, and does not occur when using AWT, or using Swing without the screenMenuBar property set. The only current workaround is to remove and rebuild the submenu so the changed contents are forced to repaint in the Mac OS Screen MenuBar. Listing 1 shows how this might be done.     |  | | --- | | ``` // Workaround:  Get all components of the subMenu and rebuild/replace it // Call this code whenever adding or removing a Component of any kind // (including JSeparators etc.) to a submenu Component[] subMenuItems = subMenu.getMenuComponents(); topMenu.remove(subMenu); subMenu = new JMenu("Open Recent"); for (int i=0; i < subMenuItems.length; i++) {   subMenu.add(subMenuItems[i]); } topMenu.add(subMenu); ``` | | __Listing 1__. (Workaround) Removal of `JMenuItem`s from submenus. |       ---  [Jul 12 2002] |

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
