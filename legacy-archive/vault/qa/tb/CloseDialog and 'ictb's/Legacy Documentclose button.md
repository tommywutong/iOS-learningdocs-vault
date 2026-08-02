---
title: CloseDialog and 'ictb's
apple_id: DTS10002252
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-01-18'
source_url: https://developer.apple.com/library/archive/qa/tb/tb66.html
archived_at: '2026-07-18T02:38:58.310777Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Human Interface Toolbox](https://developer.apple.com/referencelibrary/Carbon/idxHumanInterfaceToolbox-date.html)

|  |
| --- |
| Technical Q&A TB66CloseDialog and 'ictb's |

|  |  |
| --- | --- |
| ---   Q: I have a dialog that I create using `GetNewDialog`, passing in a pointer to the `dStorage` parameter so that I can control the memory used by the dialog. When I close the dialog, I follow the guidelines in [Inside Macintosh](https://developer.apple.com/documentation/mac/Toolbox/Toolbox-406.html) and call `CloseDialog` rather than `DisposeDialog`. However, if my dialog has an `'ictb'` resource associated with it, I find that `CloseDialog` fails to dispose of the Dialog Manager's copy of the `'ictb'`, and my application leaks. What should I do?  A: There are a number of things that you can do to solve this problem. The best solution is to simply pass `nil` to the `dStorage` parameter of `GetNewDialog` (and dispose of your dialog by calling `DisposeDialog`). This will avoid the memory leak (`DisposeDialog` does dispose of the Dialog Manager's copy of your `'ictb'`) and, as an added bonus, will make your application easier to port to Carbon. Under Carbon, it is required that you let the toolbox allocate storage for your windows and dialog by passing `nil` to the storage parameter of the creation routines.  Alternatively, you can replace your `'ictb'` resource with the more modern `'dftb'` resource, which supports most of the useful functionality of an `'ictb'` and will not suffer from this bug.  The worst solution we can think of is to plug the memory leak with the following code:   |  | | --- | | ``` static void MyCloseDialog(DialogRef dlg) {     AuxWinHandle auxWH;     Handle ictbH;       ictbH = nil;     if ( GetAuxWin(dlg, &auxWH) ) {         ictbH = (**auxWH).reserved;     }     CloseDialog(dlg);     if (ictbH != nil) {         DisposeHandle(ictbH);     } } ``` |    Since many applications in use today assume that `CloseDialog` does not dispose of the dialog's `'ictb'` data, there is no plan for changing this behavior. [Jan 18 2000] |

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
