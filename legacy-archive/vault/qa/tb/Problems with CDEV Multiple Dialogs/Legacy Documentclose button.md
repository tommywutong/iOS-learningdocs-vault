---
title: Problems with CDEV Multiple Dialogs
apple_id: DTS10002198
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-05-01'
source_url: https://developer.apple.com/library/archive/qa/tb/tb12.html
archived_at: '2026-07-18T02:38:55.628876Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A TB12Problems with CDEV Multiple Dialogs |

|  |
| --- |
| Q I'm trying to write a CDEV with two levels of dialog boxes. I've seen examples of control panels such as Date & Time that have these, so I know it can be done, but I'm still having a problem. Here's what I'm doing: I'm using GetNewDialog and passing the resource number when the user clicks on a button to bring up a second dialog box. I'm not using a pre-allocated block of memory, and I want the dialog box to be displayed in the foreground. My call looks something like this:   ``` DialogPtr dptr;    dptr = GetNewDialog(-4048, nil, (DialogPtr)-1);    if (dptr == null)      return; ```   I placed SysBeep calls around the GetNewDialog call, but I never got the second beep. Do you bring up second-level dialog boxes for a CDEV differently than you do for a regular application? Am I doing something wrong, or is there some reason you can't use GetNewDialog this way? A There is nothing particularly special about writing CDEVs with two (or more) levels of dialog boxes. Basically, what you need to do is to create and handle the dialogs in your CDEV code. This is the approach that is used in the Time & Date CDEV. There is one caveat to consider when doing this: you don't have a normal event loop, so the CDEV dialog doesn't get activated and deactivated properly if you bring up a modal dialog (which you should do, since you cannot pass control back to the parent dialog). The easiest way around this is to send the old dialog a deactivate event manually and let it manage the current text-edit info itself. If you don't do this, your CDEVs with edit-text items won't get reselected properly.  There are a few likely causes for the system hang you described. It's possible that there is a resource ID conflict, so check to be sure that the dialog and all related resources are in the CDEV range for this dialog (the types accessed in creating the dialog include DLOG, DITL, dctb, ictb, hdlg). Also, ensure that you aren't simply running out of memory by replacing the SysBbeeps with debugger() statements, and then check the heap in MacsBug before and after the call. It's also possible that one of your resources is not loading successfully, so try using a trap recording in MacsBug to see where GetNewDialog is stalling. [May 01 1995] |

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
