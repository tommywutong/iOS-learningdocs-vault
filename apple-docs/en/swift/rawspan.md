---
title: RawSpan
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/rawspan
source_url: 'https://developer.apple.com/documentation/swift/rawspan'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rawspan.json'
content_hash: 'sha256:1e77ee8030e91d34'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# RawSpan

<sub>Structure</sub>

`RawSpan` represents a contiguous region of memory which contains initialized bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct RawSpan
```

## Overview

A `RawSpan` instance is a non-owning, non-escaping view into memory. When a `RawSpan` is created, it inherits the lifetime of the container owning the contiguous memory, ensuring temporal safety and avoiding use-after-free errors. Operations on `RawSpan` are bounds-checked, ensuring spatial safety and avoiding buffer overflow errors.

## Relationships

- **Conforms To**: [BitwiseCopyable](bitwisecopyable.md), [BorrowingSequence](borrowingsequence.md), [ContiguousBytes](../foundation/contiguousbytes.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Initializers

- [init()](<rawspan/init().md>) — Create an empty span.
- [init(elements:)](<rawspan/init(elements_).md>) — View a typed span as a raw span.
- [init(unsafeElements:)](<rawspan/init(unsafeelements_).md>) — Unsafely view a typed span as a raw span.

### Instance Properties

- [byteCount](rawspan/bytecount.md) — The number of bytes in the span.
- [byteOffsets](rawspan/byteoffsets.md) — The indices that are valid for subscripting the span, in ascending order.
- [isEmpty](rawspan/isempty.md) — A Boolean value indicating whether the span is empty.

### Instance Methods

- [byteOffsets(of:)](<rawspan/byteoffsets(of_).md>) — Returns the byte offsets within this span where the memory represented by other is located, or nil if other is not located within this span.
- [extracting(_:)](<rawspan/extracting(__)-2imhy.md>) — Constructs a new span over the bytes within the supplied range of positions within this span.
- [extracting(_:)](<rawspan/extracting(__)-3elv4.md>) — Constructs a new span over all the bytes of this span.
- [extracting(_:)](<rawspan/extracting(__)-8oy0e.md>) — Constructs a new span over the bytes within the supplied range of positions within this span.
- [extracting(droppingFirst:)](<rawspan/extracting(droppingfirst_).md>) — Returns a span over all but the given number of initial bytes.
- [extracting(droppingLast:)](<rawspan/extracting(droppinglast_).md>) — Returns a span over all but the given number of trailing bytes.
- [extracting(first:)](<rawspan/extracting(first_).md>) — Returns a span containing the initial bytes of this span, up to the specified maximum length.
- [extracting(last:)](<rawspan/extracting(last_).md>) — Returns a span containing the trailing bytes of the span, up to the given maximum length.
- [extracting(unchecked:)](<rawspan/extracting(unchecked_)-2hjqs.md>) — Constructs a new span over the bytes within the supplied range of positions within this span.
- [extracting(unchecked:)](<rawspan/extracting(unchecked_)-527ri.md>) — Constructs a new span over the bytes within the supplied range of positions within this span.
- [isIdentical(to:)](<rawspan/isidentical(to_).md>) — Returns a Boolean value indicating whether two instances refer to the same memory region.
- [isTriviallyIdentical(to:)](<rawspan/istriviallyidentical(to_).md>) — Returns a Boolean value indicating whether two instances refer to the same memory region.
- [load(fromByteOffset:as:)](<rawspan/load(frombyteoffset_as_).md>) — Returns a value constructed from the raw memory at the specified offset.
- [load(fromByteOffset:as:_:)](<rawspan/load(frombyteoffset_as___).md>) — Returns a value constructed from the raw memory at the specified offset. _(beta)_
- [unsafeLoad(fromByteOffset:as:)](<rawspan/unsafeload(frombyteoffset_as_).md>) — Returns a new instance of the given type, constructed from the raw memory at the specified offset.
- [unsafeLoad(fromUncheckedByteOffset:as:)](<rawspan/unsafeload(fromuncheckedbyteoffset_as_).md>) — Returns a new instance of the given type, constructed from the raw memory at the specified offset.
- [unsafeLoadUnaligned(fromByteOffset:as:)](<rawspan/unsafeloadunaligned(frombyteoffset_as_).md>) — Returns a new instance of the given type, constructed from the raw memory at the specified offset.
- [unsafeLoadUnaligned(fromUncheckedByteOffset:as:)](<rawspan/unsafeloadunaligned(fromuncheckedbyteoffset_as_).md>) — Returns a new instance of the given type, constructed from the raw memory at the specified offset.
- [withUnsafeBytes(_:)](<rawspan/withunsafebytes(__).md>) — Calls the given closure with a pointer to the underlying bytes of the viewed contiguous storage.

### Subscripts

- [subscript(_:)](<rawspan/subscript(__).md>) — Accesses the byte at the specified offset in the span.
- [subscript(unchecked:)](<rawspan/subscript(unchecked_).md>) — Accesses the byte at the specified offset in the span.

### Default Implementations

- [BorrowingSequence Implementations](rawspan/borrowingsequence-implementations.md)

## See Also

### Safe Memory Access

- [Span](span.md) — `Span<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.
- [OutputSpan](outputspan.md) — `OutputSpan` is a reference to a contiguous region of memory that starts with some number of initialized `Element` instances followed by uninitialized memory. It provides operations to access the items it stores, as well as to add new elements and to remove existing ones.
- [OutputRawSpan](outputrawspan.md) — `OutputRawSpan` is a reference to a contiguous region of memory which starts with some number of initialized bytes, followed by uninitialized memory. It provides operations to access the bytes it stores, as well as to append and to remove bytes.
- [UTF8Span](utf8span.md) — A borrowed view into contiguous memory that contains validly-encoded UTF-8 code units.
- [MutableSpan](mutablespan.md) — `MutableSpan<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.
- [MutableRawSpan](mutablerawspan.md) — `MutableRawSpan` represents a contiguous region of memory which contains initialized bytes.
- [SpanIterator](spaniterator.md) _(beta)_
