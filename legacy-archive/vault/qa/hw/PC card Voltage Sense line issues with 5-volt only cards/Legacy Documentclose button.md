---
title: PC card Voltage Sense line issues with 5-volt only cards
apple_id: DTS10001346
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1999-10-18'
source_url: https://developer.apple.com/library/archive/qa/hw/hw74.html
archived_at: '2026-07-18T02:29:38.985444Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > PCI and PC Card](https://developer.apple.com/referencelibrary/HardwareDrivers/idxPCIandPCCard-date.html)

|  |
| --- |
| Technical Q&A HW74PC card Voltage Sense line issues with 5-volt only cards |

|  |
| --- |
| ---   Q: Why is my 5-volt PC card not correctly recognized by PowerPC model PowerBooks even though the CIS can be read at 3.3 or 5 volts?  A: There is a known bug (RADAR # 2385712) in either the PC card manager or socket services that can incorrectly determine the operating voltage for 5-volt only PC cards. This bug affects all PowerPC-based PowerBooks with PC card slots, ranging from the Powerbook 5300 up to and including the newest G3s.  If the Voltage Sense pin (pin 43, OS#) of a 5-volt PC card is grounded, indicating that the card is capable of 3.3 volt operation, the PowerBook will set the card's operational voltage to 3.3 volts to conserve power.  The problem occurs when a card's Configuration Entry Tuple (CISTPL_CE) specifies an operating voltage (Vcc) or a programming voltage (Vpp) but not both. The OS will assume "default" values for the configuration, over the value designated in the tuple. In this case, 3.3V.  This means that the 5-volt PC card will have a 3.3-volt power supply as long as it is in the PowerBook. Since CIS of the card can be read at 3.3 volts, the PowerBook will not fail the card but try to access the card's 5-volt only functions, producing unusual behavior.  The bug is scheduled to be fixed in later versions of Mac OS.  Once the card has been designed and shipped in the configuration above, there is little that can be done to work around the bug.  There are at least 2 things that can be done in design to eliminate the problem. One is a hardware fix the other is a firmware/ tuple entry fix.   1. Ensure that pins 43 (VS1#) and 57 (VS2#) are pulled up (not floating) to +5V (or Vcc) at card power up. This tells the PowerBook (and any other PC Card host) that the card is a 5-volt only card. 2. Include both the operating voltage (`Vcc`) and a programming voltage (`Vpp`) in the Configuration Entry Tuple (`CISTPL_CE`). If the card has no real programming voltage (`Vpp`), ensure that it entered as the same voltage as `Vcc`.   Either workaround will solve the problem. |

#### [Oct 18 1999]

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
