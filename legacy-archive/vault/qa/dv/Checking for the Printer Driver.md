---
title: Checking for the Printer Driver
apple_id: DTS10001183
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-06-19'
source_url: https://developer.apple.com/library/archive/qa/dv/dv42.html
archived_at: '2026-07-18T02:29:28.144896Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/HardwareDrivers/index.html) > [Printing](https://developer.apple.com/library/archive/technicalqas/HardwareDrivers/idxPrinting-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > Printing](https://developer.apple.com/referencelibrary/HardwareDrivers/idxPrinting-date.html)

|  |
| --- |
| Technical Q&A DV42Checking for the Printer Driver |

|  |
| --- |
| ---   Q: On the latest Power Macintosh systems, the iBook, iMac, and PowerBook systems which have USB built-in, if I write to the Printer driver, `.BOut`, the system hangs. I can use Macsbug to see that there is a unit table entry for these drivers. What should I do?  A: One should never assume that the modem port drivers, `.AIn` and `.AOut`, and the printer port drivers, `.BIn` and `.BOut`, are present. The supported method to access any serial port is to first check with the Communications Toolbox Communications Resource Manager as documented in [Tech Note 1119, "Serial Port Apocrypha"](https://developer.apple.com/library/archive/technotes/tn/tn1119.html). The Technote provides sample code on how to detect the available serial ports.  Do not use the `OpenDriver` call success to check for the presence of these ports. It's a known issue that on the new Power Macintosh systems with built-in USB, one can call `OpenDriver` successfully to try and open the `.BOut` port, but that an asynchronous write to the driver can cause the system to hang. The unit table drivers for the printer port exist to support USB to Serial adapters on these newer systems. |

#### [Jun 19 2000]

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
