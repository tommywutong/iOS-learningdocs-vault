---
title: Writing PCI Drivers
apple_id: TP40000975
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2006-04-04'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WritingPCIDrivers/about/about.html
archived_at: '2026-07-15T07:31:53.090537Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](PCI%20Family%20Architecture.md)

# About This Book

This document assumes some basic familiarity with programming the OS X kernel. See _[Kernel Programming Guide](../../Darwin/Kernel%20Programming%20Guide/About%20This%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbv)_ for a broad overview.

_Writing PCI Drivers_ is intended for anyone who wants to develop PCI drivers for OS X. This book assumes a basic understanding of PCI (Peripheral Component Interface), as well as a basic understanding of the I/O Kit (Apple’s object-oriented framework for developing device drivers in OS X).

This book covers the issues specific to PCI driver development on OS X. It does not cover the PCI architecture itself except as it pertains to the I/O Kit PCI framework. It also does not discuss general driver writing or porting. For books on these subjects, see [Other Apple Publications](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnbufvkfawcsivddcmbu).

This book only covers communication between your driver and PCI-based hardware. It does not cover the code you need to write to allow your driver to be accessed by the rest of the system. For information on writing a specific category of device driver, such as a network or video driver, see the documentation for the appropriate I/O Kit family.

[Chapter 2, PCI Family Architecture,](PCI%20Family%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnbvfvkfaoi) describes the basic I/O Kit classes in OS X that are relevant if you are developing a PCI driver.

[Chapter 3, Writing a Driver for a PCI Bridge,](Writing%20a%20Driver%20for%20a%20PCI%20Bridge.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnbwfvkfaoi) explains the basic types of PCI bridges and provides information on how to develop drivers for them.

[Chapter 4, Writing a Driver for a PCI Device,](Writing%20a%20Driver%20for%20a%20PCI%20Device.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnbxfvkfaoi) covers matching and device setup for all PCI devices.

[Chapter 5, Writing a Driver for an AGP Device,](Writing%20a%20Driver%20for%20an%20AGP%20Device.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnbyfvkfaoi) adds information specific to AGP devices.

[Chapter 6, Taking Primary Interrupts,](Taking%20Primary%20Interrupts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqnjqfvkfaoi) gives additional information about handling interrupts in a PCI device driver.

[Chapter 7, Endianness and Addressing,](Endianness%20and%20Addressing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnbzfvbuqrcjjbeuora) explains the difference between byte-invariant addressing and register endianness and their importance to PCI driver developers.

Apple has a series of documents on OS X software development. You can obtain other books in this series from Apple’s Developer Documentation website, [http://developer.apple.com/Documentation](https://developer.apple.com/Documentation).

Other documents that are of interest to device driver developers are _[Kernel Programming Guide](../../Darwin/Kernel%20Programming%20Guide/About%20This%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbv)_ and _[IOKit Fundamentals](../IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_.

In addition, the book [Designing PCI Cards and Drivers for Power Macintosh Computers](https://developer.apple.com/documentation/Hardware/DeviceManagers/pci_srvcs/pci_cards_drivers/index.html), while not specific to OS X, may be helpful in understanding PCI concepts and in understanding how Open Firmware and declaration ROMs interact with PCI devices. You can find this document in the hardware section of Apple’s Developer Documentation website.

Apple maintains several websites where developers can go for general and technical information on OS X.

- The Darwin Documentation project website, [http://www.opensource.apple.com/projects/documentation](http://www.opensource.apple.com/projects/documentation).
- Apple Product Information ([http://www.apple.com/macosx](http://www.apple.com/macosx))—provides general information on OS X.
- Apple Developer Documentation ([http://developer.apple.com/Documentation](https://developer.apple.com/Documentation))—features the same documentation that is installed on OS X, except that often the documentation is more up-to-date. Also includes legacy documentation.
- AppleCare Knowledge ([http://www.apple.com/support/](http://www.apple.com/support/))—contains technical articles, tutorials, FAQs, technical notes, and other information.
- Apple Developer Connection OS X Development page ([http://developer.apple.com/macosx](https://developer.apple.com/macosx))—offers SDKs, release notes, product notes, product reviews, and other resources and information related to OS X.

[Next](PCI%20Family%20Architecture.md)

