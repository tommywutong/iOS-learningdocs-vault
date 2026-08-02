---
title: Finding the VM Backing Store
apple_id: DTS10001411
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2001-03-30'
source_url: https://developer.apple.com/library/archive/qa/me/me07.html
archived_at: '2026-07-18T02:29:43.888436Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > File Management](https://developer.apple.com/referencelibrary/Carbon/idxFileManagement-date.html)

|  |
| --- |
| Technical Q&A ME07Finding the VM Backing Store |

|  |
| --- |
| Q I'm writing a backup program and I'd like to find the VM Storage file, so as to avoid backing it up. How do I do this?    A The best way of finding the current VM Storage file is to use a previously undocumented Gestalt selector:  ``` enum {     gestaltVMBackingStoreFileRefNum = 'vmbs' }; ```   The result of this selector is an file reference number to the active "VM Storage" file. You can convert that reference number to an FSSpec by calling `PBGetFCBInfoSync`, as shown below:   ``` OSErr FindVMStorage(FSSpec *fss) {     OSErr err;     long gestaltResult;     FCBPBRec fcbPB;     Str255 theName;      err = Gestalt(gestaltVMBackingStoreFileRefNum, &gestaltResult);     if (err == noErr) {         fcbPB.ioNamePtr = theName;         fcbPB.ioVRefNum = 0;         fcbPB.ioRefNum = gestaltResult;         fcbPB.ioFCBIndx = 0;         err = PBGetFCBInfoSync(&fcbPB);         if (err == noErr) {             err = FSMakeFSSpec(fcbPB.ioFCBVRefNum,                     fcbPB.ioFCBParID, theName, fss);         }     }     return err; } ```  [Mar 30 2001] |

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
