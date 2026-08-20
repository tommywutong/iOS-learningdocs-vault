---
title: Writing PCI Drivers
apple_id: TP40000975
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2006-04-04'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WritingPCIDrivers/endianness/endianness.html
archived_at: '2026-07-15T07:31:53.120563Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Writing PCI Drivers](About%20This%20Book.md)


[Next](Document%20Revision%20History.md)[Previous](Taking%20Primary%20Interrupts.md)

# Endianness and Addressing

The subject of endianness, or byte order, is rarely fully explained in the context of mixed-endian environments. This chapter explains the various issues involved in endianness as it relates to PCI on PowerPC-based and Intel-based Macintosh hardware.

In Jonathan Swift’s _Gulliver’s Travels_, the Lilliputians were split into two factions over the matter of which end of an egg to break open when consuming it. Big Endians broke their egg on the large end, while Little Endians broke it on the small end. In much the same way, computer designers are in a constant state of disagreement over which end of a multi-byte value to consume first.

For simplicity, endianness in 32-bit numbers is often represented by the letters ABCD, where the letters are used to describe the order in which the most, second to most, second to least, and least-significant bytes are stored in memory.

Little endian refers to storing the little end of a multibyte value at the lowest address. The number 513 in a 32-bit value, for example, is stored as `0x01020000` (DCBA), with the `02` representing 512, and the `01` representing the other 1. The address pointer for the start of the value points at the `01`.

Big endian refers to storing the big end of a multibyte value first. This is the order in which you are probably accustomed to seeing numbers represented in print. The number 513 is represented as `0x00000201` (ABCD), and an address pointer for the start of this value points to the leftmost `00`.

To be pedantic, there are actually _n!_ byte orders where n is the number of bytes in a word on a given architecture, and thus there can be arbitrarily many byte orders if you consider infinitely long word sizes.

A few arcane systems once represented 513 as `0x00000102` (BADC). This is equivalent to storing a 32-bit word as two little endian 16-bit words. In theory, CDAB ordering would also be possible, as would twenty other possible byte orders. Fortunately, though, it is unlikely that you will ever encounter a system whose byte ordering is anything other than ABCD (big endian) or DCBA (little endian).

On the Macintosh platform, PowerPC-based Macintosh computers use big endian addressing, while Intel-based Macs use little-endian addressing.

PCI busses are, by design, little endian. Most non-Intel-based computers are big endian. This presents a number of issues for hardware designers and programmers alike. These issues mostly deal with munging data between the PCI bus and the rest of the system.

There are two fundamental ways in which data must be transformed when dealing with PCI devices: changing the byte order of the data itself and preserving byte-invariant ordering. These are two separate issues and must not be confused.

Byte-invariant addressing is a property of the bus bridge itself. What byte-invariant addressing means is that when you access a PCI device’s address space byte by byte, you obtain the data in the order in which it is stored in the device’s memory.

From the software designer’s perspective, this means that the hardware does not byte swap the data. However, from the hardware designer’s perspective, the hardware must byte swap _all_ data. This difference in perspective is explained in [Natural Byte Order and Preserving Byte Invariant Addressing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnbzfvbuqrcdivceosi).

Data structure order, however, refers to the order in which the bytes of a multibyte number are stored in the card’s memory. If the data structure order is different than the byte order of the host machine, additional byte-swapping must be done in software. This is described in [Data Structure Order](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnbzfvbuqrciirbeisi).

From a hardware point of view, all data on a PCI bus is little endian. However, on PowerPC hardware, the main CPU bus is big endian. The physical ordering of bytes on the two busses are actually opposite. If data were read from a PCI bus using a big endian processor _without_ any manipulation, the bytes would be reversed in 32-bit chunks (or 64-bit chunks for 64-bit PCI transactions).

The effect of such a reordering would be that address zero would correspond to address three on the opposite side of the bridge, address one would correspond to address two, and so on. This is clearly not desirable.

Instead, at the hardware level, most PCI host bridge chips can swap the byte order. This ensures that per-byte addresses on one side of the bridge are equal to the per-byte addresses on the other side of the bridge.

Thus, if you are writing a driver for a host bridge chip on PowerPC-based computers or other big-endian architectures, you probably want to turn automatic byte swapping on to ensure byte-invariant addressing. However, if you are writing a driver for a host bridge chip on Intel or other little-endian architectures, you probably do not want to do this swapping.

You should note, however, that from a device driver point of view, byte 0 is still byte 0 and byte 1 is still byte 1. Thus, you shouldn’t refer to this process as byte swapping. This swapping process is more accurately called preserving byte-invariant addressing or preserving natural byte order.

Data structure order is what most developers think of when they hear the phrase “byte swap.” PCI devices may lay out their registers in any way that the card designer sees fit. In most cases, the register map for a card contains some combination of 1-byte, 2-byte, and often 4-byte registers. Each of these registers can be big or little endian. For most devices, registers are little endian, but this is not guaranteed.

When accessing a device register, you generally must know the register’s address (usually as an offset from the start of the card’s memory space), the register’s endianness, and the register’s size. For single byte addresses, you need to know only the address and size, since endianness only affects multibyte values.

The basic rules are straightforward:

- If a register’s order is specified as little endian—that is, if the byte with the lowest offset is defined in the device specifications as being the least significant byte (LSB)—then you should store data into it using a byte-reversing function on PowerPC-based computers, or a non–byte-reversing function on Intel architecture systems.
- If a register’s order is specified as big endian—that is, if the byte with the lowest offset is defined in the device specifications as being the most significant byte (MSB)—then you should use a byte-reversing function on Intel systems and a non–byte-reversing function on PowerPC systems.
- All writes to PCI configuration space are little endian. However, for configuration space changes, you should use special configuration space functions, rather than generic byte-swapping functions.

In short, the hardware byte swapping ensures that the byte order as seen by software is the same as the byte order specified in the chip documentation for the device. If the device registers are big endian, store values as big endian. If the device registers are little endian, store values as little endian.

Of course, manual byte swapping is tedious at best, error-prone at worst, and generally unpleasant on the whole. For this reason, several functions and methods exist in OS X to facilitate reading and writing registers of various sizes in both little and big endian modes.

For operations on PCI configuration space, the PCI framework provides methods such as `configRead16` and `configWrite16`.

The `libkern` byte-access functions, such as `OSReadLittleInt16` and `OSWriteLittleInt16`, provide generic byte swapping for data based on the size and endianness of the register being read or written. Similar functions, such as `OSReadBigInt16` and `OSWriteBigInt16`, are available for big-endian device registers, in the rare event that you might run into such a register.

These functions, found in `libkern/OSByteOrder.h` perform byte swapping if the host memory ordering is not the same as the register's byte order. You should always write drivers using these platform-independent macros and functions rather than using explicit swap functions like `OSWriteSwap16` directly.

For more information, see the header file for these functions, `/System/Library/Frameworks/Kernel.framework/Headers/libkern/OSByteOrder.h`, and any of the example PCI drivers.

Many people mistakenly assume that addresses cannot be treated like other data because of byte ordering issues. In fact, you can treat addresses in the same way as you treat any other data.

When accessing addresses on the PCI bus from software, addresses are translated as needed within the bridge, just as any other data; thus the bytes of an address are stored in the same byte-invariant fashion in a device’s registers as they appear on the CPU side of the bridge. However, when addresses are handed off to a PCI device that operates on those addresses, you must take care.

Generally, registers on PCI devices are in little-endian order, while addresses (at least on PowerPC and other big-endian architectures) are stored in big-endian order. Thus, they must be byte swapped. Just like any other data, though, if a PCI device uses big-endian ordering for that register, you should not byte swap. The reverse applies on Intel and other little-endian architectures.

In other words, treat addresses just as you would treat any other data. Addresses should be stored as little endian when storing them into little-endian registers, and big endian for big-endian registers.

[Next](Document%20Revision%20History.md)[Previous](Taking%20Primary%20Interrupts.md)

