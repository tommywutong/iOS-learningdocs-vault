---
title: Setting Port Speed on a Modem Port
apple_id: DTS10001166
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-02-23'
source_url: https://developer.apple.com/library/archive/qa/dv/dv25.html
archived_at: '2026-07-18T02:29:26.605915Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > Serial](https://developer.apple.com/referencelibrary/HardwareDrivers/idxSerial-date.html)

|  |
| --- |
| Technical Q&A DV25Setting Port Speed on a Modem Port |

|  |
| --- |
| ---   Q: I have some questions concerning setting port speed on the modem port:   1.  What is the maximum baud rate available for connection to an external modem? 2. If not all speeds are available on all platforms, how do I test for the    availability of various speeds on a machine? 3. How do I set the port to various speeds, particularly the higher speeds    (e.g., 115K).   A: Availability of serial speeds is one thing; success, reliability and usage is another entirely. To understand limitations of serial IO rates requires a little understanding of the background information first.  The 3 Types of Serial Operation:  Macintosh CPUs' async serial operations have all been based on the Zilog 8530 SCC. Apple has included this chip in several combination chips, but all such variations have had three basic types:  A - straight SCC and programmed IO  This is the classic setup. Every SCC interrupt must be handled by the CPU and Serial Driver explicitly. All Macintosh CPUs aside from the ones listed below (and future models, of course) can be assumed to have this hardware architecture.  B - SCC with Input-Output Processor (IOP) and programmed IO  The Macintosh IIfx, Quadra 900 and 950 models have a simple IOP architecture which offloads some of the SCC interrupt handling operations from the CPU. The Zilog SCC is combined into a custom chip and is not directly available. These are the machines that have the Serial Switch control panel: it allows native operation of the IOP/SCC for best performance, and emulates the Zilog SCC interface when set into Compatible mode for those few applications that access the SCC directly. The Serial Driver for these machines remains interrupt driven and must respond to IOP/SCC interrupts via the CPU.  C - SCC with Direct Memory Access (DMA) controller  The Quadra 840AV, 660AV and Power Macintosh 6100/7100/7200/7500/8100/8500/9500 CPUs (and their Performa derivatives) are equipped with a custom controller which completely offloads the SCC interrupts from the CPU. A low level chip protocol shuttles bytes directly out of the SCC into memory. The Serial Driver's need for CPU interrupt handling is much reduced to almost nonexistent since the SCC is completely decoupled from the CPU in normal operations.  From these facts you can see that there are several parameters which constrain serial IO rate. The particular CPU and its speed, the SCC itself, the clock speed which we can supply it, how fast an individual CPU can cycle the interrupt handlers (on the CPUs that matter), how dependent a particular hardware/software implementation of the serial port and Serial Driver are upon CPU interrupt handling, how much interrupt overhead there is in a given execution environment with other (possibly interrupt dependent) processes running, and precisely what a given process' serial IO needs are all have a great impact upon the success of using async serial IO at different speeds.  So how fast can you go?  The Serial Driver API, from the earliest days of the Macintosh, has supported bps rates from 300bps to 57,600bps. How successful a specific computer model and application are at using the higher end of these rates depends on all the factors above, plus the application's own IO algorithms.  In very general terms, the classic hardware type A on older, slower machines would normally be expected to handle typical terminal and file transfer needs up to 9600bps, assuming proper implementations, software or hardware handshaking, etc. Faster speeds than that start to get dicey, depending upon the model and its configuration. LocalTalk and other network services, floppy disk access, heavy SCSI disk IO can all occlude essential interrupt handling and cause input stream byte losses. The faster machines of this class can often support commensurately higher speeds; it's rare, however, that you could expect to sustain full bi-directional async IO at rates of 38.4 or 57.6 without some dropouts, particularly if other interrupt driven processes are running. With some applications and very aggressive coding techniques, short bursts of 57.6 speeds can be sustained, but they are rare and not to be counted on for general purpose use.  The type B hardware, run in native mode, can do pretty much as above but the higher end of the spectrum is more robust. While the IOPs do offload interrupt dependency to some degree, the Serial Driver itself is subject to the limits of how busy the CPU is and how other processes are driving the interrupt environment. It's a win but not a big one.  The type C hardware, with DMA serial capability, moves into a completely new range of IO speed handling with reliability. The first generation DMA Serial Driver was optimized for high speed data streams and quite successful at them; however it had several architectural problems that caused some of the more normal services (like software handshake and duplex terminal operations) to be compromised. We've completely revised the driver for all DMA capable CPUs now (see the "System 7.5.2 Printing Update v1.1" on the various Apple FTP servers). Since the primary goal of the DMA Serial Driver is complete compatibility with earlier application usage, the API has remained unchanged until now with the ceiling IO rate being 57.6Kbps. The new version of the driver is far more capable of being used to advantage at higher IO rates and we have added new Control codes to support both 115 and 230Kbps speeds. These are documented in [Technote 1018 "Understanding the DMA Serial Driver"](https://developer.apple.com/library/archive/technotes/tn/tn1018.html). So, in sum:   1. Speeds available are 300-57600 bps on all Mac CPUs. 115200 and 230400 bps    are available on DMA serial hardware CPUs with the latest driver. Varying    degrees of reliability, total throughput, etc. will depend upon the specific    CPU and execution environment. 2. To test for the availability of various speeds, check the Serial Driver    version with `Status` call `csCode` == 9. 3. For high speed use of the DMA Serial Driver, and the above version info,    read [Technote 1018 "Understanding the DMA Serial Driver"](https://developer.apple.com/library/archive/technotes/tn/tn1018.html). |

#### [Feb 09 1996]

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
