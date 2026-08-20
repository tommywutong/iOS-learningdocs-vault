---
title: Getting the Processor Type and Speed on a PCI Mac
apple_id: DTS10001290
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-07-15'
source_url: https://developer.apple.com/library/archive/qa/hw/hw18.html
archived_at: '2026-07-18T02:29:36.058187Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > Apple Hardware](https://developer.apple.com/referencelibrary/HardwareDrivers/idxAppleHardware-date.html)

|  |
| --- |
| Technical Q&A HW18Getting the Processor Type and Speed on a PCI Mac |

|  |  |
| --- | --- |
| ---   Q: I am trying to write an application that, when run on a PCI Mac, queries the Name Registry database for the processor type and speed. I've been unable to find anything in _Inside Macintosh: Designing PCI Cards and Drivers_ on this topic. Where can I find this information?  A: The Name Registry does not contain this information, but you can obtain it from the Gestalt Manager, just as you did on 68K Macs. This is discussed in ___Inside Macintosh: Operating System Utilities___.  If you have a utility that already does this on a 68K Mac, it should also work on a PCI Mac. The code snippet below shows how to get the processor type:   |  | | --- | | ``` //    This snippet calls the Gestalt Manager to read the machine type. #include <stdio.h> #include <GestaltEqu.h>  // prototypes void    main(void); void    main(void) {     OSErr iErr = 0;     OSType selector = 'mach';     long response = 0;      printf("DTS Absolutely Free (Gratis) Snippet\n\n");     iErr = Gestalt(selector,&response);     if(!iErr)         printf("The informational selector 'mach' is %ld \n", response);     else         printf("Sorry, an error has occurred\n"); } ``` | |

#### [Jul 15 1995]

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
