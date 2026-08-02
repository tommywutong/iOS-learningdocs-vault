---
title: Ethernet Driver Message Blocks
apple_id: DTS10001279
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-07-15'
source_url: https://developer.apple.com/library/archive/qa/hw/hw09.html
archived_at: '2026-07-18T02:29:35.535862Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > PCI and PC Card](https://developer.apple.com/referencelibrary/HardwareDrivers/idxPCIandPCCard-date.html)

|  |
| --- |
| Technical Q&A HW09Ethernet Driver Message Blocks |

|  |
| --- |
| ---   Q: I'm developing a PCI Ethernet driver, and I have two questions about receive buffer handling:   1. The sample driver uses `allocb` to create a message block. After a period of time, allocb returns a NULL pointer. How should I handle this situation? 2. How and when is the receive block deallocated? Should my driver handle this, or does something else in the stack handle it?   A:   1. If you call allocb to create a message block and the call returns a null pointer, your driver has hit a low memory situation, which means it's time to start discarding packets. 2. The client should deallocate message blocks when finished. In the case you describe, they are not yet finished.   In terms of networking services, everyone, including OpenTransport, is a client to the driver. As packets come in, you need to use `allocb` or `esballoc` to create the message block to pass along to Open Transport. Once it is passed along, a client, most likely OpenTransport, processes the packet and releases (deallocates) the memory for that packet.  The `esballoc` routine may be more suitable for your needs, since you can use it to allocate DMA memory and to pass along a notifier function that is called when the client is through using the memory. These are all standard STREAMS calls documented in _Designing Cards and Drivers for PCI._  `esballoc` is used primarily to set up a message block for a buffer that is supplied by the driver (i.e., a DMA buffer). As part of the `esballoc` message, you pass a pointer to a `free_rtn` structure, which in turn points to a free routine.  On packet receipt, the driver needs to allocate a message block for use in passing the packet data to it's clients. In this case, it is the clients responsibility to call `freemsg`. To allocate a message block, there are two options: `allocb` and `esballoc`. In one case, the memory for the data buffer comes from the available system memory, while in the case of `esballoc`, memory is allocated for the message block only. It is the responsibility of the driver to provide the memory from DMA, e.g., for the data. As such, it is useful to attach a `free_rtn` parameter so that when the data has been processed, the driver will know memory is now available for use in processing another message. |

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
