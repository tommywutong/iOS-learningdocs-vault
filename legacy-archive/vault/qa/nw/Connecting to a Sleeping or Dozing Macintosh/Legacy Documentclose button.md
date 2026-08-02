---
title: Connecting to a Sleeping or Dozing Macintosh
apple_id: DTS10001458
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-01-31'
source_url: https://developer.apple.com/library/archive/qa/nw/nw46.html
archived_at: '2026-07-18T02:29:46.827181Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxNetworking-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Networking > Hardware & Drivers](https://developer.apple.com/referencelibrary/Networking/idxHardwareDrivers-date.html)

|  |
| --- |
| Technical Q&A NW46Connecting to a Sleeping or Dozing Macintosh |

|  |
| --- |
| ---   Q: We are writing an application that requires us to connect to a remote machine via TCP/IP and talk to a background application running on that machine. However, we cannot connect to that machine when it is in sleep mode. Is there a way to keep the network services alive when a machine is in sleep mode? I've seen how you can keep the serial port alive, but not the network services.  A: When a Macintosh (usually a PowerBook) goes into the "sleep" state, it is incapable of responding to network requests - the connections actually shut down. There are some Macintosh computers, however, that will attempt to go into an energy-efficient mode know as "doze."  The sleep state is easy to prevent and is pretty well documented in the [Power Manager chapter of __Inside Mac: Devices__](https://developer.apple.com/documentation/mac/Devices/Devices-230.html) under "The Sleep Queue" and "Sleep Procedures", and there is more information in [TN 1046: __Inside Macintosh: Devices__ - Power Manager Addenda](https://developer.apple.com/library/archive/technotes/tn/tn1046.html).  If you wanted to prevent the system from sleeping or dozing, you would:   1. Allocate a `SleepQRec` (preferably in the system heap). 2. Set it up to call into your `sleepHandler`. 3. When the computer attempts to sleep or doze, it will call your    `sleepHandler` with a `sleepRequest` or `dozeRequest` selector. 4. To prevent sleep from occurring, you simply return a nonzero value.   In the doze state, Open Transport networking is still enabled and TCP connections that are set up should still function. But it might take several packets received within a short period (try 10 per second) to wake the machine from its doze state. You might also consider pinging the machine first to get it out of doze.  Either way, you should be aware that it will take some time for the networking to reactivate, especially if virtual memory is enabled and the disk drive must spin up.  There is more information on controlling the Energy Manager in [TN 1086: Power Management & The Energy Saver API](https://developer.apple.com/library/archive/technotes/tn/tn1086.html). |

#### [Jan 31 1997]

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
