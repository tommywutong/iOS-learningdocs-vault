---
title: Byte-Order Utilities
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/byte-order-utilities
source_url: 'https://developer.apple.com/documentation/corefoundation/byte-order-utilities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/byte-order-utilities.json'
content_hash: 'sha256:fe03a9f43532d4df'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# Byte-Order Utilities

<sub>API Collection</sub>

## Overview

When handling binary data transmitted or shared across platforms, you need be concerned with how each platform stores numerical values. A platform stores values either in big-endian or little-endian format. On big-endian machines, such as PowerPC machines, values are stored with the most-significant bytes first in memory; on little-endian machines, such as Pentium machines, values are stored with the least-significant bytes first. A multibyte value transmitted to a platform with a different format will be misinterpreted if it is not converted properly by one of the computers.

You identify the native format of the current platform using the [CFByteOrderGetCurrent](<cfbyteordergetcurrent().md>) function. Use functions such as [CFSwapInt32BigToHost](<cfswapint32bigtohost(__).md>) and [CFConvertFloat32HostToSwapped](<cfconvertfloat32hosttoswapped(__).md>) to convert values between different byte order formats.

## Topics

### Core Foundation Byte Order Utilities Miscellaneous Functions

- [CFByteOrderGetCurrent](<cfbyteordergetcurrent().md>) — Returns the byte order of the current computer.
- [CFConvertDoubleHostToSwapped](<cfconvertdoublehosttoswapped(__).md>) — Converts a 64-bit double from the host’s native byte order to a platform-independent format.
- [CFConvertDoubleSwappedToHost](<cfconvertdoubleswappedtohost(__).md>) — Converts a 64-bit double from a platform-independent format to the host’s native byte order.
- [CFConvertFloat32HostToSwapped](<cfconvertfloat32hosttoswapped(__).md>) — Converts a 32-bit float from the host’s native byte order to a platform-independent format.
- [CFConvertFloat32SwappedToHost](<cfconvertfloat32swappedtohost(__).md>) — Converts a 32-bit float from a platform-independent format to the host’s native byte order.
- [CFConvertFloat64HostToSwapped](<cfconvertfloat64hosttoswapped(__).md>) — Converts a 64-bit float from the host’s native byte order to a platform-independent format.
- [CFConvertFloat64SwappedToHost](<cfconvertfloat64swappedtohost(__).md>) — Converts a 64-bit float from a platform-independent format to the host’s native byte order.
- [CFConvertFloatHostToSwapped](<cfconvertfloathosttoswapped(__).md>) — Converts a 32-bit float from the host’s native byte order to a platform-independent format.
- [CFConvertFloatSwappedToHost](<cfconvertfloatswappedtohost(__).md>) — Converts a 32-bit float from a platform-independent format to the host’s native byte order.
- [CFSwapInt16](<cfswapint16(__).md>) — Swaps the bytes of a 16-bit integer.
- [CFSwapInt16BigToHost](<cfswapint16bigtohost(__).md>) — Converts a 16-bit integer from big-endian format to the host’s native byte order.
- [CFSwapInt16HostToBig](<cfswapint16hosttobig(__).md>) — Converts a 16-bit integer from the host’s native byte order to big-endian format.
- [CFSwapInt16HostToLittle](<cfswapint16hosttolittle(__).md>) — Converts a 16-bit integer from the host’s native byte order to little-endian format.
- [CFSwapInt16LittleToHost](<cfswapint16littletohost(__).md>) — Converts a 16-bit integer from little-endian format to the host’s native byte order.
- [CFSwapInt32](<cfswapint32(__).md>) — Swaps the bytes of a 32-bit integer.
- [CFSwapInt32BigToHost](<cfswapint32bigtohost(__).md>) — Converts a 32-bit integer from big-endian format to the host’s native byte order.
- [CFSwapInt32HostToBig](<cfswapint32hosttobig(__).md>) — Converts a 32-bit integer from the host’s native byte order to big-endian format.
- [CFSwapInt32HostToLittle](<cfswapint32hosttolittle(__).md>) — Converts a 32-bit integer from the host’s native byte order to little-endian format.
- [CFSwapInt32LittleToHost](<cfswapint32littletohost(__).md>) — Converts a 32-bit integer from little-endian format to the host’s native byte order.
- [CFSwapInt64](<cfswapint64(__).md>) — Swaps the bytes of a 64-bit integer.
- [CFSwapInt64BigToHost](<cfswapint64bigtohost(__).md>) — Converts a 64-bit integer from big-endian format to the host’s native byte order.
- [CFSwapInt64HostToBig](<cfswapint64hosttobig(__).md>) — Converts a 64-bit integer from the host’s native byte order to big-endian format.
- [CFSwapInt64HostToLittle](<cfswapint64hosttolittle(__).md>) — Converts a 64-bit integer from the host’s native byte order to little-endian format.
- [CFSwapInt64LittleToHost](<cfswapint64littletohost(__).md>) — Converts a 64-bit integer from little-endian format to the host’s native byte order.

### Data Types

- [CFSwappedFloat32](cfswappedfloat32.md) — Structure holding a 32-bit float value in a platform-independentbyte order.
- [CFSwappedFloat64](cfswappedfloat64.md) — Structure holding a 64-bit float value in a platform-independentbyte order.

### Constants

- [CFByteOrder](cfbyteorder.md) — Flags that identify byte order.

## See Also

### Related Documentation

- [Memory Management Programming Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/CFMemoryMgmt.html#//apple_ref/doc/uid/10000127i)

### Utilities

- [Base Utilities](base-utilities.md)
- [Core Foundation URL Access Utilities](core-foundation-url-access-utilities.md)
- [Preferences Utilities](preferences-utilities.md)
- [Socket Name Server Utilities](socket-name-server-utilities.md)
- [Time Utilities](time-utilities.md)
