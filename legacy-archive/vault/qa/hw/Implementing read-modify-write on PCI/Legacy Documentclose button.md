---
title: Implementing read-modify-write on PCI
apple_id: DTS10001278
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-07-15'
source_url: https://developer.apple.com/library/archive/qa/hw/hw08.html
archived_at: '2026-07-18T02:29:35.481591Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Hardware & Drivers > PCI and PC Card](https://developer.apple.com/referencelibrary/HardwareDrivers/idxPCIandPCCard-date.html)

|  |
| --- |
| Technical Q&A HW08Implementing read-modify-write on PCI |

|  |  |  |
| --- | --- | --- |
| ---   Q: We are converting our Nubus card to a PCI card, and we need to know how to implement read-modify-write to lock the PCI target device.  A: _Designing PCI Cards and Drivers_, which is on the PCI Driver Development Kit (DDK), explains this as follows:  Atomic Memory Operations  The Driver Services Library provides the following 32-, 16-, and 8-bit atomic memory operations for use by device drivers.   |  | | --- | | ``` Boolean CompareAndSwap(long oldValue, long newValue, long *Value); SInt32            IncrementAtomic( SInt32 *value ); SInt32            DecrementAtomic( SInt32 *value ); SInt32            AddAtomic( SInt32 amount, SInt32 *value ); UInt32        BitAndAtomic( UInt32 mask, UInt32 *value ); UInt32        BitOrAtomic( UInt32 mask, UInt32 *value ); UInt32        BitXorAtomic( UInt32 mask, UInt32 *value ); SInt8             IncrementAtomic8( SInt8 *value ); SInt8             DecrementAtomic8( SInt8 *value ); SInt8             AddAtomic8( SInt32 amount, SInt8 *value ); UInt8             BitAndAtomic8( UInt32 mask, UInt8 *value ); UInt8             BitOrAtomic8( UInt32 mask, UInt8 *value ); UInt8             BitXorAtomic8( UInt32 mask, UInt8 *value ); SInt16            IncrementAtomic16( SInt16 *value ); SInt16            DecrementAtomic16( SInt16 *value ); SInt16            AddAtomic16( SInt32 amount, SInt16 *value ); UInt16        BitAndAtomic16( UInt32 mask, UInt16 *value ); UInt16        BitOrAtomic16( UInt32 mask, UInt16 *value ); UInt16        BitXorAtomic16( UInt32 mask, UInt16 *value ); ``` |   The atomic routines perform various operations on the memory address specified by value:   - `IncrementAtomic` increments the value by one and `DecrementAtomic` decrements it   by one. These functions return the value as it was before the change. - `AddAtomic` adds the specified amount to the value at the specified address and returns the result. - `BitAndAtomic` performs a logical and operation between the bits of the specified mask and the value at the specified address, returning the result. Similarly, `BitOrAtomic` performs a logical or operation and `BitXorAtomic` performs a logical `XOR` operation. - The `CompareAndSwap` routine compares the value at the specified address with `oldValue`. The value of `newValue` is written to the specified address only if `oldValue` and the value at the specified address are equal. `CompareAndSwap` returns true if `newValue` is written to the specified address; otherwise it returns false. A false return value does not imply that `oldValue` and the value at the specified address are not equal; it only implies that `CompareAndSwap` did not write newValue to the specified address.   These routines take logical address pointers and ensure that the operations are atomic with respect to all devices (for example, other processors, DMA engines) that participate in the coherency architecture of the Macintosh system.   |  | | --- | | ``` TestAndSet        (UInt32            theBit                   UInt8            *theAddress); TestAndClear    (UInt32            theBit                   UInt8               *theAddress); theBit            The bit number in the range 0 through 7. theAddress        The address of the byte in which the bit is located. ``` |   `TestAndSet` and `TestAndClear` set and clear a single bit in a byte at a specified address. |

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
