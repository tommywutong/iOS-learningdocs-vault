---
title: Common Problems when Installing QuickTime VR
apple_id: DTS10002067
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-09-27'
source_url: https://developer.apple.com/library/archive/qa/qtvr/qtvr23.html
archived_at: '2026-07-18T02:38:51.631610Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > Virtual Reality](https://developer.apple.com/referencelibrary/QuickTime/idxVirtualReality-date.html)

|  |
| --- |
| Technical Q&A QTVR23Common Problems when Installing QuickTime VR |

|  |
| --- |
| Technical Q&AQTVR 23 - Common Problems when Installing QuickTime VR (27-September-96)  Q I am installing the QuickTime VR Authoring Tools following the instructions in Chapter 2 and I've run into a problem at step 12. When I double-click the the QTVR Templates file, I receive the following message: The document "QTVR Templates" could not be opened, because the application "ResEdit" could not be found.  Coincidentally, my coworker also ran into a problem at step 12 when he was installing the QuickTime VR Authoring Tools, yet when he double-clicked the QTVR Templates file, his Eudora Pro email application launched and displayed this error message:  This file is a resource plug-in for Eudora. Put it in your Eudora Folder or the system Preferences folder or the same folder as the Eudora application  What's going on? A The problems that you and your coworker are experiencing both arise from the fact that neither of you copied the ResEdit application to your hard drives before installing the QuickTime VR Authoring Tools. ResEdit is conveniently included with the QuickTime VR Authoring Tools, and is found on the ETO disc at the following location:  ``` E.T.O. #20   Other Development Tools     ResEdit       ResEdit 2.1.3 ```   Furthermore, your coworker's problem differs from yours because he has Eudora installed on his hard drive, whereas you do not. Eudora plug-ins have the same file type, "rsrc", as the QTVR Templates file. If Eudora Pro (or Eudora Light) is installed, it will launch when attempting to install the QTVR Templates when ResEdit is not found.  **__Note:__** : When ResEdit is launched for the first time, it creates the ResEdit Preferences file. You should then quit and relaunch ResEdit to force ResEdit to finish writing it's Preferences file to disk so that you can later open and edit it without a problem. Otherwise, when you try to open the ResEdit Preferences file, you will receive the following error message:  : Sorry, this file is damaged beyond repair. You should restore a backup copy, if possible. |

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
