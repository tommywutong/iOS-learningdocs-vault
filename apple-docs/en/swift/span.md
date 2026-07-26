---
title: Span
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/span
source_url: 'https://developer.apple.com/documentation/swift/span'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/span.json'
content_hash: 'sha256:f440615e1066da97'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Span

<sub>Structure</sub>

`Span<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Span<Element> where Element : ~Copyable
```

## Overview

A `Span` instance is a non-owning, non-escaping view into memory. When a `Span` is created, it inherits the lifetime of the container owning the contiguous memory, ensuring temporal safety and avoiding use-after-free errors. Operations on `Span` are bounds-checked, ensuring spatial safety and avoiding buffer overflow errors.

## Relationships

- **Conforms To**: [BitwiseCopyable](bitwisecopyable.md), [BorrowingSequence](borrowingsequence.md), [ContiguousBytes](../foundation/contiguousbytes.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Initializers

- [init()](<span/init().md>) — Create an empty span.
- [init(viewing:)](<span/init(viewing_)-18wsr.md>) — View initialized raw memory as a typed span.
- [init(viewing:)](<span/init(viewing_)-9d31g.md>) — View initialized raw memory as a span of bytes.

### Instance Properties

- [bytes](span/bytes-6qp42.md) — Construct a raw span over the memory represented by this span.
- [bytes](span/bytes-8rxg.md) — A raw span over the memory represented by this span.
- [count](span/count.md) — The number of elements in the span.
- [indices](span/indices.md) — The indices that are valid for subscripting the span, in ascending order.
- [isEmpty](span/isempty.md) — A Boolean value indicating whether the span is empty.

### Instance Methods

- [extracting(_:)](<span/extracting(__)-1c6e6.md>) — Constructs a new span over the items within the supplied range of indices within this span.
- [extracting(_:)](<span/extracting(__)-48neh.md>) — Constructs a new span over the items within the supplied range of indices within this span.
- [extracting(_:)](<span/extracting(__)-57peb.md>) — Constructs a new span over all the items of this span.
- [extracting(droppingFirst:)](<span/extracting(droppingfirst_).md>) — Returns a span over all but the given number of initial elements.
- [extracting(droppingLast:)](<span/extracting(droppinglast_).md>) — Returns a span over all but the given number of trailing elements.
- [extracting(first:)](<span/extracting(first_).md>) — Returns a span containing the initial elements of this span, up to the specified maximum length.
- [extracting(last:)](<span/extracting(last_).md>) — Returns a span containing the trailing elements of the span, up to the given maximum length.
- [extracting(unchecked:)](<span/extracting(unchecked_)-46y0h.md>) — Constructs a new span over the items within the supplied range of indices within this span.
- [extracting(unchecked:)](<span/extracting(unchecked_)-8hfj1.md>) — Constructs a new span over the items within the supplied range of indices within this span.
- [indices(of:)](<span/indices(of_).md>) — Returns the indices within this span where the memory represented by other is located, or nil if other is not located within this span.
- [isIdentical(to:)](<span/isidentical(to_).md>) — Returns a Boolean value indicating whether two instances refer to the same memory region.
- [isTriviallyIdentical(to:)](<span/istriviallyidentical(to_).md>) — Returns a Boolean value indicating whether two instances refer to the same memory region.
- [withUnsafeBufferPointer(_:)](<span/withunsafebufferpointer(__).md>) — Calls a closure with a pointer to the viewed contiguous storage.
- [withUnsafeBytes(_:)](<span/withunsafebytes(__).md>) — Calls the given closure with a pointer to the underlying bytes of the viewed contiguous storage.

### Subscripts

- [subscript(_:)](<span/subscript(__)-2g4jz.md>) — Accesses the element at the specified index in the `Span`.
- [subscript(_:)](<span/subscript(__)-3r1qm.md>) — Accesses the element at the specified index in the `Span`.
- [subscript(unchecked:)](<span/subscript(unchecked_)-2no6f.md>) — Accesses the element at the specified index in the `Span`.
- [subscript(unchecked:)](<span/subscript(unchecked_)-6gur1.md>) — Accesses the element at the specified index in the `Span`.

### Type Aliases

- [Index](span/index.md) — The representation for an index in `Span`.

### Default Implementations

- [BorrowingSequence Implementations](span/borrowingsequence-implementations.md)

## See Also

### Safe Memory Access

- [RawSpan](rawspan.md) — `RawSpan` represents a contiguous region of memory which contains initialized bytes.
- [OutputSpan](outputspan.md) — `OutputSpan` is a reference to a contiguous region of memory that starts with some number of initialized `Element` instances followed by uninitialized memory. It provides operations to access the items it stores, as well as to add new elements and to remove existing ones.
- [OutputRawSpan](outputrawspan.md) — `OutputRawSpan` is a reference to a contiguous region of memory which starts with some number of initialized bytes, followed by uninitialized memory. It provides operations to access the bytes it stores, as well as to append and to remove bytes.
- [UTF8Span](utf8span.md) — A borrowed view into contiguous memory that contains validly-encoded UTF-8 code units.
- [MutableSpan](mutablespan.md) — `MutableSpan<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.
- [MutableRawSpan](mutablerawspan.md) — `MutableRawSpan` represents a contiguous region of memory which contains initialized bytes.
- [SpanIterator](spaniterator.md) _(beta)_
