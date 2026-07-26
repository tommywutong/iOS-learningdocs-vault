---
title: DispatchData
framework: Dispatch
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchdata
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchdata.json'
content_hash: 'sha256:3feaa3da30f2733d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DispatchData

<sub>Structure</sub>

An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DispatchData
```

## Overview

The memory buffer managed by this object may be a single contiguous block of memory, or it may consist of multiple discontiguous blocks. For the discontiguous case, the dispatch data object makes it appear as if the memory is contiguous.

## Relationships

- **Conforms To**: [BidirectionalCollection](../swift/bidirectionalcollection.md), [Collection](../swift/collection.md), [Copyable](../swift/copyable.md), [DataProtocol](../foundation/dataprotocol.md), [Escapable](../swift/escapable.md), [RandomAccessCollection](../swift/randomaccesscollection.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Sequence](../swift/sequence.md)

## Topics

### Creating a Dispatch Data Structure

- [init(bytes:)](<dispatchdata/init(bytes_)-9lrd.md>) — Creates a new dispatch data object from the specified memory buffer.
- [init(bytesNoCopy:deallocator:)](<dispatchdata/init(bytesnocopy_deallocator_)-vfoe.md>) — Creates a new dispatch data object using the specified memory buffer and deallocator.
- [withUnsafeBytes(body:)](<dispatchdata/withunsafebytes(body_).md>)
- [Deallocator](dispatchdata/deallocator.md) — Memory deallocators for dispatch data objects.
- [empty](dispatchdata/empty.md) — A dispatch data object representing a zero-length memory region.

### Appending Data to the Buffer

- [append(_:)](<dispatchdata/append(__)-3bvdr.md>)
- [append(_:)](<dispatchdata/append(__)-9sgkq.md>)
- [append(_:)](<dispatchdata/append(__)-1m94x.md>)

### Copying Bytes

- [copyBytes(to:count:)](<dispatchdata/copybytes(to_count_)-3j0qx.md>)
- [copyBytes(to:from:)](<dispatchdata/copybytes(to_from_)-7zz4y.md>)
- [copyBytes(to:from:)](<dispatchdata/copybytes(to_from_)-60yai.md>)

### Accessing Buffer Data

- [subscript(_:)](<dispatchdata/subscript(__).md>)
- [region(location:)](<dispatchdata/region(location_).md>)
- [Region](dispatchdata/region.md)

### Iterating Over the Buffer Contents

- [makeIterator()](<dispatchdata/makeiterator().md>)
- [enumerateBytes(_:)](<dispatchdata/enumeratebytes(__).md>)

### Retrieving Buffer Subsequences

- [subdata(in:)](<dispatchdata/subdata(in_).md>)

### Combining Sequence Elements

- [append(_:)](<dispatchdata/append(__)-3bvdr.md>)
- [append(_:)](<dispatchdata/append(__)-9sgkq.md>)
- [append(_:)](<dispatchdata/append(__)-1m94x.md>)
- [append(_:count:)](<dispatchdata/append(__count_).md>)
- [copyBytes(to:count:)](<dispatchdata/copybytes(to_count_)-4ffyj.md>)
- [copyBytes(to:count:)](<dispatchdata/copybytes(to_count_)-3j0qx.md>)
- [copyBytes(to:from:)](<dispatchdata/copybytes(to_from_)-7zz4y.md>)
- [copyBytes(to:from:)](<dispatchdata/copybytes(to_from_)-6ztcb.md>)
- [copyBytes(to:from:)](<dispatchdata/copybytes(to_from_)-60yai.md>)
- [enumerateBytes(_:)](<dispatchdata/enumeratebytes(__).md>)
- [makeIterator()](<dispatchdata/makeiterator().md>)
- [region(location:)](<dispatchdata/region(location_).md>)
- [subdata(in:)](<dispatchdata/subdata(in_).md>)
- [withUnsafeBytes(body:)](<dispatchdata/withunsafebytes(body_).md>)

### Deprecated

- [init(bytes:)](<dispatchdata/init(bytes_)-mkbp.md>) — Initialize a data object with copied memory content.
- [init(bytesNoCopy:deallocator:)](<dispatchdata/init(bytesnocopy_deallocator_)-7h08w.md>) — Initialize a data object without copying the bytes.
- [append(_:count:)](<dispatchdata/append(__count_).md>)
- [copyBytes(to:count:)](<dispatchdata/copybytes(to_count_)-4ffyj.md>)
- [copyBytes(to:from:)](<dispatchdata/copybytes(to_from_)-6ztcb.md>)

### Instance Methods

- [enumerateBytes(block:)](<dispatchdata/enumeratebytes(block_).md>)

## See Also

### System Event Monitoring

- [DispatchSource](dispatchsource.md) — An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- [Dispatch Source](dispatch-source.md) — An object that coordinates the processing of specific low-level system events, such as file-system events, timers, and UNIX signals.
- [DispatchIO](dispatchio.md) — An object that manages operations on a file descriptor using either stream-based or random-access semantics.
- [DispatchDataIterator](dispatchdataiterator.md) — A byte-by-byte iterator over the contents of a dispatch data object.
- [Dispatch I/O](dispatch-i-o.md) — An object that manages operations on a file descriptor using either stream-based or random-access semantics.
- [Dispatch Data](dispatch-data.md) — An object that manages a memory-based data buffer and exposes it as a contiguous block of memory.
- [DispatchSourceProtocol](dispatchsourceprotocol.md) — Defines a common set of properties and methods that are shared with all dispatch source types.
