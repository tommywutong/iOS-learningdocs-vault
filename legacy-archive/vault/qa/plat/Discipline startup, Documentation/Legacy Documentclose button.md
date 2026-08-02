---
title: Discipline startup, Documentation
apple_id: DTS10001512
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/plat/plat02.html
archived_at: '2026-07-18T02:29:50.781887Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| NOTE: This Technical Q&A has been [retired](https://developer.apple.com/library/archive/qa/index.html). Please see the [Technical Q&As](https://developer.apple.com/library/archive/qa/index.html) page for current documentation. |

|  |
| --- |
| Technical Q&A PLAT02Discipline startup, Documentation |

|  |  |
| --- | --- |
| ---   Q: I need to know where to put the Discipline startup and how to set up MacsBug to ignore Discipline at the system level. Where is documentation for Discipline?  A: If you are using Discipline with MacsBug, and you install Discipline as an INIT, you should drag both Discipline and the Discipline startup file you want to use (either Lenient or Strict) into your System Folder (don't forget to restart the computer after doing this).  Since Discipline is turned off initially, it doesn't check trap calls until you turn it on by entering __DSC ON__ in MacsBug. To have Discipline check only the toolbox calls your application makes, enter __DSCA__ in MacsBug. To turn Discipline off, enter __DSC OFF__ (or __DSCA OFF__) in MacsBug.  If you install Discipline as an application, drag Discipline and the Discipline startup file of your choice into any folder on your hard disk. You do not have to copy these files into your System Folder.  When you launch Discipline as an application, it may indicate that there is a problem with the Finder's method of accessing system calls. To avoid this, enter __DSCA__ in MacsBug. To turn Discipline off, enter __DSC OFF__ (or __DSCA OFF__) in MacsBug, or close it with Command + Q. If Discipline crashes, you must turn if off using __DSC[A] OFF__ before you use the __ES__ (Exit to Shell) command.  There is a chapter on Discipline in the MacsBug Reference and Dubugging Guide, which is available from APDA. You can find additional material on the Developer CD Tool Chest. There are also Release Notes for Discipline 2.0.2 on ETO 16.    |  | | --- | | __Important:__  Discipline has not been updated since 1991, and there are no plans to update it. | |

#### [May 01 1995]

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
