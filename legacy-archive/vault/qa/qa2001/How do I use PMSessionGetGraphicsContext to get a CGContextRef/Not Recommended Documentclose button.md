---
title: How do I use PMSessionGetGraphicsContext to get a CGContextRef?
apple_id: DTS10001739
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2003-02-25'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1216.html
archived_at: '2026-07-18T02:38:19.451813Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Carbon/index.html) > [Printing](https://developer.apple.com/library/archive/technicalqas/Carbon/idxPrinting-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Printing](https://developer.apple.com/referencelibrary/Carbon/idxPrinting-date.html)

|  |
| --- |
| Technical Q&A QA1216How do I use PMSessionGetGraphicsContext to get a CGContextRef? |

|  |  |  |
| --- | --- | --- |
| ---   Q: How do I use `PMSessionGetGraphicsContext` to get a `CGContextRef`?  A: As documented in the [Carbon Printing Manager Reference](https://developer.apple.com/Developer/Documentation/Carbon/graphics/CarbonPrintingManager/CarbonPrintingManager_Ref/cpmref_reference/_Creating_a_sion_Object.html#TPXREF345) for the `PMSessionSetDocumentFormatGeneration` API, you must call `PMSessionSetDocumentFormatGeneration` with the `kPMGraphicsContextCoreGraphics` context type before you call `PMSessionBeginDocument` and then call `PMSessionBeginPage` in order for `PMSessionGetGraphicsContext` to return a `CGContextRef`. Keep in mind that the coordinate system for a `CGContextRef` (origin in the lower left corner of page and not the imageable area, +y up) is not the same as for a QuickDraw port (origin in upper left, +y down). Also, note that even though these APIs are available in CarbonLib 1.1 and later, Quartz 2D didn't exist before Mac OS X 10.0 and so requesting `kPMGraphicsContextCoreGraphics` doesn't make sense if you aren't running on Mac OS X. Listing 1 below is a modified version of the code found in the [Carbon Printing Manager Reference](https://developer.apple.com/Developer/Documentation/Carbon/graphics/CarbonPrintingManager/CarbonPrintingManager_Ref/cpmref_reference/_Creating_a_sion_Object.html#TPXREF345) section on `PMSessionSetDocumentFormatGeneration`.     |  | | --- | | __Listing 1__. Getting a `CGContextRef` for printing | | ```     CFStringRef         strings[1];     CFArrayRef          ourGraphicsContextsArray;     CGContextRef        printingContext;     OSErr               err = noErr;     PMPrintSession      printSession;          //     //    at this point you've already created a print session     //     strings[0] = kPMGraphicsContextCoreGraphics; // This is important!     ourGraphicsContextsArray = CFArrayCreate (kCFAllocatorDefault,                         (const void **)strings,                         1, &kCFTypeArrayCallBacks);     if (ourGraphicsContextsArray != NULL)     {             err = PMSessionSetDocumentFormatGeneration (printSession,                             kPMDocumentFormatPDF,                             ourGraphicsContextsArray, NULL);             CFRelease (ourGraphicsContextsArray);     }          //     //    more of your print loop     //          //     //    then you call PMSessionBeginDocument and PMSessionBeginPage     //          //    Now you are ready to request the printing context     err = PMSessionGetGraphicsContext (printSession,         kPMGraphicsContextCoreGraphics, (void **) &printingContext);              //     //    render your content to the printingContext using Quartz      //    2D and continue your print loop     // ``` |     Both the `PMSessionSetDocumentFormatGeneration` and `PMSessionGetGraphicsContext` APIs can be found in the "PMCore.h" header file while the `kPMGraphicsContextCoreGraphics` constant can be found in the "PMDefinitions.h" header file.   ---  [Feb 25 2003] |

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
