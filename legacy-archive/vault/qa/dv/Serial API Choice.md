---
title: Serial API Choice
apple_id: DTS10001180
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2001-07-02'
source_url: https://developer.apple.com/library/archive/qa/dv/dv39.html
archived_at: '2026-07-18T02:29:27.929308Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/HardwareDrivers/index.html) > [Serial](https://developer.apple.com/library/archive/technicalqas/HardwareDrivers/idxSerial-date.html) >

|  |
| --- |
| Technical Q&A DV39Serial API Choice |

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ---   Q: Given that the Carbon specification says that classic serial won't be supported in Carbon but the Open Transport API will be, should I convert my serial code to use Open Transport serial endpoints?  A: No. There is no point converting your code to use the Open Transport API because the Open Transport compatibility layer on Mac OS X will not support serial endpoints. If you read the Carbon specification carefully, it says that Carbon only guarantees TCP/IP protocol endpoint support (TCP, UDP, RawIP). Other endpoint types may work (for example, on traditional Mac OS, serial endpoints work just fine from within Carbon), but this won't always be the case.  The following table summarizes the support for the two APIs in the various environments.   |  |  |  | | --- | --- | --- | |  | Supports Classic Serial? | Supports OT Serial? | | Traditional Mac OS | Yes | Yes | | Carbon on traditional Mac OS | No | Yes | | Carbon on Mac OS X | No | No |   For more details on what will and won't be supported by Carbon, read the [Carbon Specification](https://developer.apple.com/documentation/Carbon/CarbonSpecification/CarbonSpecTOC.html).  Q: What serial API should I use for new development?  A: There are a number of considerations here:   - Open Transport serial will continue to be supported   on traditional Mac OS, both for Carbon and non-Carbon   applications. - Open Transport serial will not be supported under   Carbon on Mac OS X. - Classic serial will not be supported under Carbon on   traditional Mac OS or Mac OS X. - To talk to serial ports on Mac OS X you should use a   combination of the IOKit API (to enumerate the ports) and   the BSD "termios" API (to actually talk to a port). The   DTS sample code [SerialPortSample](https://developer.apple.com/samplecode/Sample_Code/Devices_and_Hardware/Serial/SerialPortSample.htm)   shows how to do this. - On traditional Mac OS, Open Transport serial is   layered on top of classic serial by a compatibility shim   inside Open Transport. - When deciding which serial API to use, you should   take into account the following points.   - Classic serial offers the best flexibility,     performance and responsiveness.   - Open Transport serial is easier to use if you are     already working within the Open Transport world (for     example, you are turning telnet code into terminal     code, or building a STREAMS plug-in that needs     serial).   - If you have working code, there is no future     compatibility benefit to be gained by moving it from     classic serial to Open Transport serial, or vice     versa. - When writing a serial driver for traditional Mac OS,   you should write a Device Manager (either   `'ndrv'` or `'DRVR'`) driver and   register it with Communications Resource Manager. Open   Transport's serial shim will then work with your driver   automatically, and both Open Transport and classic serial   clients will be able to use it. If you write an Open   Transport (TPI) driver, only Open Transport serial   clients will be able to use your driver.   Regardless of the serial API you choose, you should be familiar with the information in Technote 1119, [Serial Port Apocrypha](https://developer.apple.com/library/archive/technotes/tn/tn1119.html). |

#### [Jul 02 2001]

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
