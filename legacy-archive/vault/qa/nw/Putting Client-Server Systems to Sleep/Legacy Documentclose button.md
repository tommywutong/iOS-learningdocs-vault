---
title: Putting Client/Server Systems to Sleep
apple_id: DTS10001457
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1997-01-09'
source_url: https://developer.apple.com/library/archive/qa/nw/nw45.html
archived_at: '2026-07-18T02:29:46.772358Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxNetworking-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Networking](https://developer.apple.com/referencelibrary/Networking/index.html)

|  |
| --- |
| Technical Q&A NW45Putting Client/Server Systems to Sleep |

|  |
| --- |
| ---   Q: I am writing a fax client/server system and I have encountered a problem after I put the server to sleep: on waking, the server software does not seem to re-register on the network (using `RegisterMyName`).  On the client side, (when receiving a `sleepDemand` request), I wait until network activity has ceased, then return control to the system. The client wakes and reconnects to the server with no problems.  What action should I take to correct this problem?  A: In general, you might want to disable sleep on your server by informing the Power Manager with `AutoSleepControl(false)`. Otherwise, the clients might never know that your server is sleeping, and will be unable to connect. But if you do want to support sleep, then a server should install a sleep procedure through the Power Manager using `SleepQInstall`.  The exact interaction of how your server should handle `sleepRequest/SleepDemand` is detailed in table 6-1 on [pg 6-10 of _Inside Macintosh: Devices_](https://developer.apple.com/documentation/mac/Devices/Devices-231.html#MARKER-9-43). Ultimately, you close and deregister your server from the network. Later, when you get the `sleepWakeUp` call, you should reopen and re-register.  Q: I installed a sleep procedure. But the Power Manager will issue a `sleepDemand` if the user selects Sleep from the Special menu. The `AutoSleepControl(false)` call will stop `sleepRequests` but will it also stop `SleepDemands`?  A: Your Application can (should) not refuse a `sleepDemand`, as documented in [_Inside Macintosh: Devices_ pg 6-11](https://developer.apple.com/documentation/mac/Devices/Devices-231.html#MARKER-9-43):  When your sleep procedure receives a sleep demand, however, your procedure has no way to determine whether it originated as a conditional sleep demand or an unconditional sleep demand. Your device driver or application must prepare for the sleep state and return control promptly to the Power Manager when it receives a sleep demand.  As for `AutoSleepControl`, please refer to [_Inside Macintosh: Devices_ pg 6-44](https://developer.apple.com/documentation/mac/Devices/Devices-270.html#HEADING270-0):  When `enableSleep` is set to `false`, the computer will not go into the sleep mode unless it is forced to either by some user action --for example, by the user's selecting Sleep from the Special menu of the Finder--or in a low battery situation. |

#### [Jan 09 1997]

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
