---
title: Creating a Menu with an Icon as its Title
apple_id: DTS10002192
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/tb/tb06.html
archived_at: '2026-07-18T02:38:55.225732Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A TB06Creating a Menu with an Icon as its Title |

|  |
| --- |
| Q How do I create a menu with an icon as its title, such as AppleScript(TM) and other products use?   A The menu data for the menu title must be 0x0501<handle> where <handle> is replaced by the the results of calling GetIconSuite(). An example snippet of code follows. This snippet assumes that the menu title is already 5 bytes long.  ``` void ChangeToIconMenu() {                 Handle              theIconSuite = nil;                 MenuHandle         menuHandle;      GetIconSuite(&theIconSuite, cIcon, svAllSmallData);     if (theIconSuite)     {         menuHandle = GetMenuHandle(mIcon);         if (menuHandle)         {             // second byte must be a 1, followed by the icon suite handle             (**menuHandle).menuData[1] = 0x01;             *((long *)&((**menuHandle).menuData[2])) = (long)theIconSuite;             // update display (typically you do this on startup)             DeleteMenu(mIcon);             InsertMenu(menuHandle, 0);             InvalMenuBar();         }     } } ```  [May 01 1995] |

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
