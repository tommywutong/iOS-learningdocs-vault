---
title: MutableRawSpan
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/mutablerawspan
source_url: 'https://developer.apple.com/documentation/swift/mutablerawspan'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutablerawspan.json'
content_hash: 'sha256:26e63afd55427c70'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# MutableRawSpan

<sub>Structure</sub>

`MutableRawSpan` represents a contiguous region of memory which contains initialized bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct MutableRawSpan
```

## Relationships

- **Conforms To**: [BorrowingSequence](borrowingsequence.md), [ContiguousBytes](../foundation/contiguousbytes.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Initializers

- [init()](<mutablerawspan/init().md>) — Create an empty span.
- [init(elements:)](<mutablerawspan/init(elements_).md>) — Convert a typed span to a raw span.
- [init(mutating:)](<mutablerawspan/init(mutating_).md>) — Mutate the elements of a typed span as bytes.
- [init(unsafeElements:)](<mutablerawspan/init(unsafeelements_).md>) — Unsafely convert a typed span to a raw span.

### Instance Properties

- [byteCount](mutablerawspan/bytecount.md) — The number of bytes in the span.
- [byteOffsets](mutablerawspan/byteoffsets.md) — The valid byte offsets for accessing this span, in ascending order.
- [bytes](mutablerawspan/bytes.md) — Borrow the underlying initialized memory for read-only access.
- [isEmpty](mutablerawspan/isempty.md) — A Boolean value indicating whether the span is empty.

### Instance Methods

- [extracting(_:)](<mutablerawspan/extracting(__)-18k75.md>) — Constructs a new span over the bytes within the supplied range of positions within this span. _(deprecated)_
- [extracting(_:)](<mutablerawspan/extracting(__)-6fpo6.md>) — Constructs a new span over the bytes within the supplied range of positions within this span. _(deprecated)_
- [extracting(_:)](<mutablerawspan/extracting(__)-7d5f1.md>) — Constructs a new span over all the bytes of this span. _(deprecated)_
- [extracting(droppingFirst:)](<mutablerawspan/extracting(droppingfirst_).md>) — Returns a span over all but the given number of initial bytes. _(deprecated)_
- [extracting(droppingLast:)](<mutablerawspan/extracting(droppinglast_).md>) — Returns a span over all but the given number of trailing bytes. _(deprecated)_
- [extracting(first:)](<mutablerawspan/extracting(first_).md>) — Returns a span containing the initial bytes of this span, up to the specified maximum length. _(deprecated)_
- [extracting(last:)](<mutablerawspan/extracting(last_).md>) — Returns a span containing the trailing bytes of the span, up to the given maximum length. _(deprecated)_
- [extracting(unchecked:)](<mutablerawspan/extracting(unchecked_)-4b7xa.md>) — Constructs a new span over the bytes within the supplied range of positions within this span. _(deprecated)_
- [extracting(unchecked:)](<mutablerawspan/extracting(unchecked_)-7oy38.md>) — Constructs a new span over the bytes within the supplied range of positions within this span. _(deprecated)_
- [load(fromByteOffset:as:)](<mutablerawspan/load(frombyteoffset_as_).md>) — Returns a value constructed from the raw memory at the specified offset.
- [load(fromByteOffset:as:_:)](<mutablerawspan/load(frombyteoffset_as___).md>) — Returns a value constructed from the raw memory at the specified offset. _(beta)_
- [storeBytes(of:toByteOffset:as:)](<mutablerawspan/storebytes(of_tobyteoffset_as_)-1afju.md>) — Stores the given value’s bytes to the specified offset into the span’s memory.
- [storeBytes(of:toByteOffset:as:)](<mutablerawspan/storebytes(of_tobyteoffset_as_)-37pwo.md>) — Stores the given value’s bytes into the span’s raw memory at the specified byte offset.
- [storeBytes(of:toByteOffset:as:_:)](<mutablerawspan/storebytes(of_tobyteoffset_as___).md>) — Stores the given value’s bytes to the specified offset into the span’s memory. _(beta)_
- [storeBytes(of:toUncheckedByteOffset:as:)](<mutablerawspan/storebytes(of_touncheckedbyteoffset_as_).md>) — Stores the given value’s bytes into the span’s raw memory at the specified byte offset.
- [storeBytes(repeating:count:as:)](<mutablerawspan/storebytes(repeating_count_as_)-6822y.md>) — Stores the given value’s bytes repeatedly into this span’s memory.
- [storeBytes(repeating:count:as:)](<mutablerawspan/storebytes(repeating_count_as_)-7cd7p.md>) — Stores the given value’s bytes repeatedly into this span’s memory.
- [storeBytes(repeating:count:as:_:)](<mutablerawspan/storebytes(repeating_count_as___).md>) — Stores the given value’s bytes repeatedly into this span’s memory. _(beta)_
- [unsafeLoad(fromByteOffset:as:)](<mutablerawspan/unsafeload(frombyteoffset_as_).md>) — Returns a new instance of the given type, constructed from the raw memory at the specified offset.
- [unsafeLoad(fromUncheckedByteOffset:as:)](<mutablerawspan/unsafeload(fromuncheckedbyteoffset_as_).md>) — Returns a new instance of the given type, constructed from the raw memory at the specified offset.
- [unsafeLoadUnaligned(fromByteOffset:as:)](<mutablerawspan/unsafeloadunaligned(frombyteoffset_as_).md>) — Returns a new instance of the given type, constructed from the raw memory at the specified offset.
- [unsafeLoadUnaligned(fromUncheckedByteOffset:as:)](<mutablerawspan/unsafeloadunaligned(fromuncheckedbyteoffset_as_).md>) — Returns a new instance of the given type, constructed from the raw memory at the specified offset.
- [withUnsafeBytes(_:)](<mutablerawspan/withunsafebytes(__).md>) — Calls the given closure with a pointer to the underlying bytes of the viewed contiguous storage.
- [withUnsafeMutableBytes(_:)](<mutablerawspan/withunsafemutablebytes(__).md>) — Calls the given closure with a mutable pointer to the underlying bytes of the viewed contiguous storage.

### Subscripts

- [subscript(_:)](<mutablerawspan/subscript(__).md>) — Accesses the byte at the specified offset in the span.
- [subscript(unchecked:)](<mutablerawspan/subscript(unchecked_).md>) — Accesses the byte at the specified offset in the span.

### Default Implementations

- [BorrowingSequence Implementations](mutablerawspan/borrowingsequence-implementations.md)

## See Also

### Safe Memory Access

- [Span](span.md) — `Span<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.
- [RawSpan](rawspan.md) — `RawSpan` represents a contiguous region of memory which contains initialized bytes.
- [OutputSpan](outputspan.md) — `OutputSpan` is a reference to a contiguous region of memory that starts with some number of initialized `Element` instances followed by uninitialized memory. It provides operations to access the items it stores, as well as to add new elements and to remove existing ones.
- [OutputRawSpan](outputrawspan.md) — `OutputRawSpan` is a reference to a contiguous region of memory which starts with some number of initialized bytes, followed by uninitialized memory. It provides operations to access the bytes it stores, as well as to append and to remove bytes.
- [UTF8Span](utf8span.md) — A borrowed view into contiguous memory that contains validly-encoded UTF-8 code units.
- [MutableSpan](mutablespan.md) — `MutableSpan<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.
- [SpanIterator](spaniterator.md) _(beta)_
