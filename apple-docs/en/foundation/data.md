---
title: Data
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/data
source_url: 'https://developer.apple.com/documentation/foundation/data'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data.json'
content_hash: 'sha256:42623980286ff7fb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# Data

<sub>Structure</sub>

A byte buffer in memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Data
```

## Overview

The [Data](data.md) value type allows simple byte buffers to take on the behavior of Foundation objects. You can create empty or pre-populated buffers from a variety of sources and later add or remove bytes. You can filter and sort the content, or compare against other buffers. You can manipulate subranges of bytes and iterate over some or all of them.

[Data](data.md) bridges to the [NSData](nsdata.md) class and its mutable subclass, [NSMutableData](nsmutabledata.md). You can use these interchangeably in code that interacts with Objective-C APIs.

## Relationships

- **Conforms To**: [Attachable](../testing/attachable.md), [BidirectionalCollection](../swift/bidirectionalcollection.md), [CKRecordValueProtocol](../cloudkit/ckrecordvalueprotocol.md), [CVAttachmentValueRepresentable](../corevideo/cvattachmentvaluerepresentable.md), [Collection](../swift/collection.md), [ContiguousBytes](contiguousbytes.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [DataProtocol](dataprotocol.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [MutableCollection](../swift/mutablecollection.md), [MutableDataProtocol](mutabledataprotocol.md), [RandomAccessCollection](../swift/randomaccesscollection.md), [RangeReplaceableCollection](../swift/rangereplaceablecollection.md), [ReferenceConvertible](referenceconvertible.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Sequence](../swift/sequence.md), [Transferable](../coretransferable/transferable.md)

## Topics

### Creating Empty Data

- [init()](<data/init().md>) — Creates an empty data buffer.
- [init(capacity:)](<data/init(capacity_).md>) — Creates an empty data buffer of a specified size.
- [init(count:)](<data/init(count_).md>) — Creates a new data buffer with the specified count of zeroed bytes.
- [resetBytes(in:)](<data/resetbytes(in_).md>) — Sets a region of the data buffer to `0`.

### Creating Populated Data

- [init()](<data/init().md>) — Creates an empty data buffer.
- [init(buffer:)](<data/init(buffer_)-75sng.md>) — Creates a data buffer with copied memory content using a buffer pointer.
- [init(buffer:)](<data/init(buffer_)-6xgv4.md>) — Creates a data buffer with copied memory content using a mutable buffer pointer.
- [init(bytes:count:)](<data/init(bytes_count_).md>) — Creates data with copied memory content.
- [init(bytesNoCopy:count:deallocator:)](<data/init(bytesnocopy_count_deallocator_).md>) — Creates a data buffer with memory content without copying the bytes.
- [init(capacity:)](<data/init(capacity_).md>) — Creates an empty data buffer of a specified size.
- [init(count:)](<data/init(count_).md>) — Creates a new data buffer with the specified count of zeroed bytes.

### Creating Data from Raw Memory

- [init(bytes:count:)](<data/init(bytes_count_).md>) — Creates data with copied memory content.
- [init(buffer:)](<data/init(buffer_)-75sng.md>) — Creates a data buffer with copied memory content using a buffer pointer.
- [init(buffer:)](<data/init(buffer_)-6xgv4.md>) — Creates a data buffer with copied memory content using a mutable buffer pointer.
- [init(bytesNoCopy:count:deallocator:)](<data/init(bytesnocopy_count_deallocator_).md>) — Creates a data buffer with memory content without copying the bytes.
- [Deallocator](data/deallocator.md) — A deallocator you use to customize how the backing store is deallocated for data created with the no-copy initializer.

### Reading and Writing Data

- [write(to:options:)](<data/write(to_options_).md>) — Writes the contents of the data buffer to a location.
- [ReadingOptions](data/readingoptions.md) — Options to control the reading of data from a URL.
- [WritingOptions](data/writingoptions.md) — Options to control the writing of data to a URL.

### Base-64 Encoding

- [base64EncodedData(options:)](<data/base64encodeddata(options_).md>) — Returns Base-64 encoded data.
- [base64EncodedString(options:)](<data/base64encodedstring(options_).md>) — Returns a Base-64 encoded string.
- [Base64DecodingOptions](data/base64decodingoptions.md) — Options to use when decoding data.
- [Base64EncodingOptions](data/base64encodingoptions.md) — Options to use when encoding data.

### Accessing Bytes

- [subscript(_:)](<data/subscript(__)-6lc96.md>) — Accesses the bytes at the specified range of indexes.
- [subscript(_:)](<data/subscript(__)-8kg64.md>) — Accesses the byte at the specified index.

### Accessing Underlying Memory

- [withUnsafeBytes(_:)](<data/withunsafebytes(__).md>) — Accesses the raw bytes in the data’s buffer.
- [withUnsafeMutableBytes(_:)](<data/withunsafemutablebytes(__)-7ac1g.md>) — Mutates the raw bytes in the data’s buffer.
- [copyBytes(to:count:)](<data/copybytes(to_count_).md>) — Copies the contents of the data to memory.
- [copyBytes(to:from:)](<data/copybytes(to_from_)-8qk4r.md>) — Copies a subset of the contents of the data to memory.
- [copyBytes(to:from:)](<data/copybytes(to_from_)-4o6zj.md>) — Copies the bytes in a range from the data into a buffer.

### Adding Bytes

- [append(_:)](<data/append(__)-vjwy.md>) — Appends the specified data to the end of this data.
- [append(_:)](<data/append(__)-xtlw.md>) — Append a buffer of bytes to the data.
- [append(_:count:)](<data/append(__count_).md>) — Appends the specified bytes from memory to the end of the data.
- [reserveCapacity(_:)](<data/reservecapacity(__).md>) — Prepares the collection to store the specified number of elements, when doing so is appropriate for the underlying type.

### Replacing a Range of Bytes

- [replaceSubrange(_:with:)](<data/replacesubrange(__with_)-9u7ry.md>) — Replaces a region of bytes in the data with new bytes from a collection.
- [replaceSubrange(_:with:)](<data/replacesubrange(__with_)-9nzh.md>) — Replaces a region of bytes in the data with new bytes from a buffer.
- [replaceSubrange(_:with:count:)](<data/replacesubrange(__with_count_).md>) — Replaces a region of bytes in the data with bytes from memory.

### Finding Bytes

- [range(of:options:in:)](<data/range(of_options_in_).md>) — Finds the range of the specified data as a subsequence of this data, if it exists.
- [SearchOptions](data/searchoptions.md) — Options that control a data search operation.

### Excluding Bytes

- [advanced(by:)](<data/advanced(by_).md>) — Returns a new data buffer created by removing the given number of bytes from the front of the original buffer.

### Iterating Over Bytes

- [makeIterator()](<data/makeiterator().md>) — Returns an iterator over the contents of the data.
- [Iterator](data/iterator.md) — An iterator that operates over the contents of data.
- [enumerateBytes(_:)](<data/enumeratebytes(__).md>) — Enumerates the contents of the data’s buffer.

### Splitting the Buffer

- [subdata(in:)](<data/subdata(in_).md>) — Returns a new copy of the data in a specified range.

### Comparing Data

- [==(_:_:)](<data/==(____).md>) — Returns `true` if the two `Data` arguments are equal.

### Manipulating Indexes

- [Index](data/index.md) — A type used to indicate a position in a data’s buffer.
- [startIndex](data/startindex.md) — The beginning index into the data.
- [endIndex](data/endindex.md) — The end index into the data.
- [index(after:)](<data/index(after_).md>) — Returns the index that immediately follows the specified index.
- [index(before:)](<data/index(before_).md>) — Returns the index that immediately precedes the specified index.

### Manipulating Index Ranges

- [Indices](data/indices.md) — A type used to indicate a range of positions in a data’s buffer.

### Describing Data

- [description](data/description.md) — A human-readable description for the data.
- [debugDescription](data/debugdescription.md) — A human-readable debug description for the data.

### Using Reference Types

- [NSData](nsdata.md) — A static byte buffer in memory.
- [NSMutableData](nsmutabledata.md) — An object representing a dynamic byte buffer in memory.

### Initializers

- [init(_:)](<data/init(__)-2r3sw.md>)
- [init(_:)](<data/init(__)-53ewf.md>)
- [init(base64Encoded:options:)](<data/init(base64encoded_options_)-1g88z.md>) — Initialize a `Data` from a Base-64, UTF-8 encoded `Data`.
- [init(base64Encoded:options:)](<data/init(base64encoded_options_)-654f.md>) — Initialize a `Data` from a Base-64 encoded String using the given options.
- [init(bytes:)](<data/init(bytes_)-5krj4.md>)
- [init(bytes:)](<data/init(bytes_)-5s0rs.md>)
- [init(bytes:)](<data/init(bytes_)-9othw.md>)
- [init(contentsOf:options:)](<data/init(contentsof_options_).md>) — Creates data by reading from the specified URL.
- [init(referencing:)](<data/init(referencing_).md>) — Initialize a `Data` by adopting a reference type.
- [init(repeating:count:)](<data/init(repeating_count_).md>) — Initialize a `Data` with a repeating byte pattern

### Instance Properties

- [bytes](data/bytes.md)
- [count](data/count.md) — The number of bytes in the data.
- [mutableBytes](data/mutablebytes.md)
- [mutableSpan](data/mutablespan.md)
- [span](data/span.md)

### Instance Methods

- [append(contentsOf:)](<data/append(contentsof_)-2ebzw.md>)
- [append(contentsOf:)](<data/append(contentsof_)-xeqk.md>) — Appends the bytes in the specified sequence to the end of the data.
- [replaceSubrange(_:with:)](<data/replacesubrange(__with_)-21ouz.md>) — Replaces a region of bytes in the data with new bytes from a collection.
- [withUnsafeMutableBytes(_:)](<data/withunsafemutablebytes(__)-79c12.md>)

### Subscripts

- [subscript(_:)](<data/subscript(__)-59z5z.md>) — Accesses the bytes at the specified range of indexes.

### Default Implementations

- [Attachable Implementations](data/attachable-implementations.md)
- [Collection Implementations](data/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](data/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](data/customstringconvertible-implementations.md)
- [Equatable Implementations](data/equatable-implementations.md)
- [Hashable Implementations](data/hashable-implementations.md)

## See Also

### Binary Data

- [DataProtocol](dataprotocol.md) — A protocol that provides consistent data access to the bytes underlying contiguous and noncontiguous data buffers.
- [MutableDataProtocol](mutabledataprotocol.md) — A protocol that provides consistent data access to the bytes underlying contiguous and noncontiguous mutable data buffers.
- [ContiguousBytes](contiguousbytes.md) — A protocol that declares the type offers direct access to the underlying raw bytes in a contiguous manner.
