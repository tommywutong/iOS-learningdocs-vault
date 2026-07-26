---
title: MutableSpan
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/mutablespan
source_url: 'https://developer.apple.com/documentation/swift/mutablespan'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutablespan.json'
content_hash: 'sha256:cced75afafea5983'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# MutableSpan

<sub>Structure</sub>

`MutableSpan<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct MutableSpan<Element> where Element : ~Copyable
```

## Relationships

- **Conforms To**: [BorrowingSequence](borrowingsequence.md), [ContiguousBytes](../foundation/contiguousbytes.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Initializers

- [init()](<mutablespan/init().md>) — Create an empty span.
- [init(mutableBytes:)](<mutablespan/init(mutablebytes_).md>) — Convert a raw span to a typed span.
- [init(mutating:)](<mutablespan/init(mutating_).md>) — Mutate untyped memory as a typed span.

### Instance Properties

- [bytes](mutablespan/bytes-478ye.md) — A raw span over the memory represented by this span.
- [bytes](mutablespan/bytes-61tq.md) — Construct a raw span over the memory represented by this span.
- [count](mutablespan/count.md) — The number of elements in the span.
- [indices](mutablespan/indices.md) — The range of valid indices for subscripting the span.
- [isEmpty](mutablespan/isempty.md) — A Boolean value indicating whether the span is empty.
- [mutableBytes](mutablespan/mutablebytes-7cwoq.md) — Construct a mutable raw span over the memory represented by this span.
- [mutableBytes](mutablespan/mutablebytes-9ha97.md) — A mutable raw span over the memory represented by this span.
- [span](mutablespan/span.md) — Borrow the underlying initialized memory for read-only access.

### Instance Methods

- [extracting(_:)](<mutablespan/extracting(__)-2g8w3.md>) — Constructs a new span over the items within the supplied range of indices within this span. _(deprecated)_
- [extracting(_:)](<mutablespan/extracting(__)-80srp.md>) — Constructs a new span over all the items of this span. _(deprecated)_
- [extracting(_:)](<mutablespan/extracting(__)-bphj.md>) — Constructs a new span over the items within the supplied range of indices within this span. _(deprecated)_
- [extracting(droppingFirst:)](<mutablespan/extracting(droppingfirst_).md>) — Returns a span over all but the given number of initial elements. _(deprecated)_
- [extracting(droppingLast:)](<mutablespan/extracting(droppinglast_).md>) — Returns a span over all but the given number of trailing elements. _(deprecated)_
- [extracting(first:)](<mutablespan/extracting(first_).md>) — Returns a span containing the initial elements of this span, up to the specified maximum length. _(deprecated)_
- [extracting(last:)](<mutablespan/extracting(last_).md>) — Returns a span containing the trailing elements of the span, up to the given maximum length. _(deprecated)_
- [extracting(unchecked:)](<mutablespan/extracting(unchecked_)-23qq.md>) — Constructs a new span over the items within the supplied range of indices within this span. _(deprecated)_
- [extracting(unchecked:)](<mutablespan/extracting(unchecked_)-4y8oj.md>) — Constructs a new span over the items within the supplied range of indices within this span. _(deprecated)_
- [swapAt(_:_:)](<mutablespan/swapat(____).md>) — Exchange the elements at the two given indices.
- [swapAt(unchecked:unchecked:)](<mutablespan/swapat(unchecked_unchecked_).md>) — Exchange the elements at the two given indices.
- [update(repeating:)](<mutablespan/update(repeating_).md>) — Update every element of this span to the given value.
- [withUnsafeBufferPointer(_:)](<mutablespan/withunsafebufferpointer(__).md>) — Call a closure with a pointer to the viewed contiguous storage.
- [withUnsafeBytes(_:)](<mutablespan/withunsafebytes(__).md>) — Calls the given closure with a pointer to the underlying bytes of the viewed contiguous storage.
- [withUnsafeMutableBufferPointer(_:)](<mutablespan/withunsafemutablebufferpointer(__).md>) — Call a closure with a pointer to the viewed mutable contiguous storage.
- [withUnsafeMutableBytes(_:)](<mutablespan/withunsafemutablebytes(__).md>) — Calls the given closure with a mutable pointer to the underlying bytes of the viewed contiguous storage.

### Subscripts

- [subscript(_:)](<mutablespan/subscript(__).md>) — Accesses the element at the specified index in the `MutableSpan`.
- [subscript(unchecked:)](<mutablespan/subscript(unchecked_).md>) — Accesses the element at the specified index in the `MutableSpan`.

### Type Aliases

- [Index](mutablespan/index.md) — The type that represents an index in a `MutableSpan`.

### Default Implementations

- [BorrowingSequence Implementations](mutablespan/borrowingsequence-implementations.md)

## See Also

### Safe Memory Access

- [Span](span.md) — `Span<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.
- [RawSpan](rawspan.md) — `RawSpan` represents a contiguous region of memory which contains initialized bytes.
- [OutputSpan](outputspan.md) — `OutputSpan` is a reference to a contiguous region of memory that starts with some number of initialized `Element` instances followed by uninitialized memory. It provides operations to access the items it stores, as well as to add new elements and to remove existing ones.
- [OutputRawSpan](outputrawspan.md) — `OutputRawSpan` is a reference to a contiguous region of memory which starts with some number of initialized bytes, followed by uninitialized memory. It provides operations to access the bytes it stores, as well as to append and to remove bytes.
- [UTF8Span](utf8span.md) — A borrowed view into contiguous memory that contains validly-encoded UTF-8 code units.
- [MutableRawSpan](mutablerawspan.md) — `MutableRawSpan` represents a contiguous region of memory which contains initialized bytes.
- [SpanIterator](spaniterator.md) _(beta)_
