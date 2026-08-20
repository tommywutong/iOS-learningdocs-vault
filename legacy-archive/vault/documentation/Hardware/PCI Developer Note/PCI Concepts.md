---
title: PCI Developer Note
apple_id: TP40003027
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-04-28'
source_url: https://developer.apple.com/library/archive/documentation/Hardware/Conceptual/HWtech_PCI/Articles/pci_concepts.html
archived_at: '2026-07-15T07:40:48.448148Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [PCI Developer Note](Introduction%20to%20PCI%20Developer%20Note.md)


[Next](PCI%20Product-Specific%20Details.md)[Previous](Introduction%20to%20PCI%20Developer%20Note.md)

# PCI Concepts

The Peripheral Component Interconnect (PCI) local bus standard specifies a high-performance interconnection for expansion cards, integrated I/O controller ICs, and the computer’s main memory and processor.

The PCI bus was standardized in the early 1990s as a replacement for a variety of I/O buses. Apple incorporated PCI in Mac computers in 1995, replacing the Nubus used in the Power Macintosh 6100/7100/8100 and earlier models. The benefits of PCI include the following:

- A single method for connecting both ASIC chips and plug-in expansion cards to a computer’s main memory and processing circuitry
- Support for lower-voltage (3.3 V) signals
- 32-bit and 64-bit bus widths
- Cross-platform compatibility of expansion cards
- Easier implementation of plug-and-play capabilities
- Clock rate of up to 66 MHz

As the speeds of processors and other components increased, limitations of the PCI bus were addressed with the introduction of the Accelerated Graphics Port (AGP bus) for video support and PCI-X for other high-bandwidth needs such as I/O expansion cards.

At today's high clock rates, the parallel nature of the PCI bus (and the derivative AGP bus) exacerbates data transmission problems. Even the smallest differences in bus board traces can magnify noise, waveform quality degradation, and signal timing errors. The serial PCI Express architecture is an industry-standard third generation I/O bus designed to overcome such limitations of the parallel PCI bus architecture.

A PCI Express connection (known as a _link_) consists of one or more point-to-point connections called _lanes_, each of which has two pairs of conductors, a transmit pair and a receive pair. PCI Express uses low-voltage differential (LVD) signaling and an 8B/10B encoding scheme on these lanes, preserving signal integrity at high transmission rates. A link can comprise 1, 2, 4, 8, 12, 16, or 32 lanes.

PCI Express retains most of the best features of the previous generation PCI and PCI-X architectures. PCI Express has the same usage model and load-storage communication model as PCI and PCI-X. It supports the same IO read/write and configuration read/write transactions. The memory read/write transactions and IO and configuration address space model is the same. Because the address space model is the same, existing OS and driver software will run on a PCI Express system, providing backwards software compatibility.

[Next](PCI%20Product-Specific%20Details.md)[Previous](Introduction%20to%20PCI%20Developer%20Note.md)

