---
title: NSMutableData
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmutabledata
source_url: 'https://developer.apple.com/documentation/foundation/nsmutabledata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutabledata.json'
content_hash: 'sha256:85817c79bfaf5c59'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMutableData

<sub>Class</sub>

An object representing a dynamic byte buffer in memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSMutableData
```

## Overview

In Swift, this object bridges to [Data](data.md); use [NSMutableData](nsmutabledata.md) when you need reference semantics or other Foundation-specific behavior.

`NSMutableData` and its superclass `NSData` provide data objects, or object-oriented wrappers for byte buffers. Data objects let simple allocated buffers (that is, data with no embedded pointers) take on the behavior of Foundation objects. They are typically used for data storage and are also useful in Distributed Objects applications, where data contained in data objects can be copied or moved between applications. `NSData` creates static data objects, and `NSMutableData` creates dynamic data objects. You can easily convert one type of data object to the other with the initializer that takes an `NSData` object or an  `NSMutableData` object as an argument.

The following [NSData](nsdata.md) methods change when used on a mutable data object:

- [- initWithBytesNoCopy:length:freeWhenDone:](<nsdata/init(bytesnocopy_length_freewhendone_).md>)
- [- initWithBytesNoCopy:length:deallocator:](<nsdata/init(bytesnocopy_length_deallocator_).md>)
- [- initWithBytesNoCopy:length:](<nsdata/init(bytesnocopy_length_).md>)
- [dataWithBytesNoCopy:length:freeWhenDone:](nsdata/datawithbytesnocopy_length_freewhendone_.md)
- [dataWithBytesNoCopy:length:](nsdata/datawithbytesnocopy_length_.md)

When called, the bytes are immediately copied and then the buffer is freed.

`NSMutableData` is “toll-free bridged” with its Core Foundation counterpart, [CFData](../corefoundation/cfdata.md). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

> [!important] Important
> The Swift overlay to the Foundation framework provides the [Data](data.md) structure, which bridges to the [NSMutableData](nsmutabledata.md) class and its immutable superclass [NSData](nsdata.md). For more information about value types, see [Working with Foundation Types](../swift/working-with-foundation-types.md).

## Relationships

- **Inherits From**: [NSData](nsdata.md)

- **Inherited By**: [NSPurgeableData](nspurgeabledata.md)

- **Conforms To**: [BidirectionalCollection](../swift/bidirectionalcollection.md), [CVarArg](../swift/cvararg.md), [Collection](../swift/collection.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [DataProtocol](dataprotocol.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSMutableCopying](nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [RandomAccessCollection](../swift/randomaccesscollection.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Sequence](../swift/sequence.md)

## Topics

### Creating Mutable Data

- [- initWithCapacity:](<nsmutabledata/init(capacity_).md>) — Returns an initialized mutable data object capable of holding the specified number of bytes.
- [- initWithLength:](<nsmutabledata/init(length_).md>) — Initializes and returns a mutable data object containing a given number of zeroed bytes.

### Accessing Raw Bytes

- [mutableBytes](nsmutabledata/mutablebytes.md) — A pointer to the data contained by the mutable data object.

### Counting Bytes

- [length](nsmutabledata/length.md) — The number of bytes contained in the mutable data object.

### Adding Bytes

- [- appendBytes:length:](<nsmutabledata/append(__length_).md>) — Appends to the receiver a given number of bytes from a given buffer.
- [- appendData:](<nsmutabledata/append(__).md>) — Appends the content of another data object to the receiver.
- [- increaseLengthBy:](<nsmutabledata/increaselength(by_).md>) — Increases the length of the receiver by a given number of bytes.

### Modifying Bytes

- [- replaceBytesInRange:withBytes:](<nsmutabledata/replacebytes(in_withbytes_).md>) — Replaces with a given set of bytes a given range within the contents of the receiver.
- [- replaceBytesInRange:withBytes:length:](<nsmutabledata/replacebytes(in_withbytes_length_).md>) — Replaces with a given set of bytes a given range within the contents of the receiver.
- [- resetBytesInRange:](<nsmutabledata/resetbytes(in_).md>) — Replaces with zeroes the contents of the receiver in a given range.
- [- setData:](<nsmutabledata/setdata(__).md>) — Replaces the entire contents of the receiver with the contents of another data object.

### Compressing and Decompressing Data

- [- compressUsingAlgorithm:error:](<nsmutabledata/compress(using_).md>) — Compresses the data object’s bytes using an algorithm that you specify.
- [- decompressUsingAlgorithm:error:](<nsmutabledata/decompress(using_).md>) — Decompresses the data object’s bytes.
- [CompressionAlgorithm](nsdata/compressionalgorithm.md) — An algorithm that indicates how to compress or decompress data.
- [NSCompressionErrorMaximum](nscompressionerrormaximum-swift.var.md) — The end of the range of error codes reserved for compression errors.
- [NSCompressionErrorMinimum](nscompressionerrorminimum-swift.var.md) — The start of the range of error codes reserved for compression errors.
- [NSCompressionFailedError](nscompressionfailederror-swift.var.md) — An error code value that indicates a failure to compress data using the provided algorithm.
- [NSDecompressionFailedError](nsdecompressionfailederror-swift.var.md) — An error code value that indicates a failure to decompress data using the provided algorithm.
