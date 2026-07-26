---
title: 'CFSwapInt64HostToBig(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfswapint64hosttobig(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfswapint64hosttobig(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfswapint64hosttobig%28_%3A%29.json'
content_hash: 'sha256:481034c1170aee06'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSwapInt64HostToBig(_:)

<sub>Function</sub>

Converts a 64-bit integer from the host’s native byte order to big-endian format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSwapInt64HostToBig(_ arg: UInt64) -> UInt64
```

## Parameters

- `arg` — The integer whose bytes should be swapped.

## Return Value

The integer with its bytes swapped. If the host is big-endian, this function returns `arg` unchanged.

## See Also

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
