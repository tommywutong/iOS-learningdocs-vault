---
title: OutputSpan
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/outputspan
source_url: 'https://developer.apple.com/documentation/swift/outputspan'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/outputspan.json'
content_hash: 'sha256:bcbf642d02688108'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# OutputSpan

<sub>Structure</sub>

`OutputSpan` is a reference to a contiguous region of memory that starts with some number of initialized `Element` instances followed by uninitialized memory. It provides operations to access the items it stores, as well as to add new elements and to remove existing ones.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct OutputSpan<Element> where Element : ~Copyable
```

## Relationships

- **Conforms To**: [ContiguousBytes](../foundation/contiguousbytes.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Initializers

- [init()](<outputspan/init().md>) — Create an OutputSpan with zero capacity.
- [init(buffer:initializedCount:)](<outputspan/init(buffer_initializedcount_)-3tbg3.md>) — Unsafely create an OutputSpan over partly-initialized memory.
- [init(buffer:initializedCount:)](<outputspan/init(buffer_initializedcount_)-vie3.md>) — Unsafely create an OutputSpan over partly-initialized memory.

### Instance Properties

- [capacity](outputspan/capacity.md) — The total number of elements that this output span can contain.
- [count](outputspan/count.md) — The number of initialized elements in this span.
- [freeCapacity](outputspan/freecapacity.md) — The number of additional elements that can be added to this span.
- [indices](outputspan/indices.md) — The range of initialized indices for this `OutputSpan`.
- [isEmpty](outputspan/isempty.md) — A Boolean value indicating whether the span is empty.
- [isFull](outputspan/isfull.md) — A Boolean value indicating whether the span is full.
- [mutableSpan](outputspan/mutablespan.md) — Exclusively borrow the underlying initialized memory for mutation.
- [span](outputspan/span.md) — Borrow the underlying initialized memory for read-only access.

### Instance Methods

- [append(_:)](<outputspan/append(__).md>) — Append a single element to this span.
- [append(repeating:count:)](<outputspan/append(repeating_count_).md>) — Repeatedly append an element to this span.
- [finalize(for:)](<outputspan/finalize(for_)-5utkq.md>) — Consume the output span and return the number of initialized elements.
- [finalize(for:)](<outputspan/finalize(for_)-83pw0.md>) — Consume the output span and return the number of initialized elements.
- [removeAll()](<outputspan/removeall().md>) — Remove all this span’s elements and return its memory to the uninitialized state.
- [removeLast()](<outputspan/removelast().md>) — Remove the last initialized element from this span.
- [removeLast(_:)](<outputspan/removelast(__).md>) — Remove the last n elements of this span, returning the memory they occupy to the uninitialized state.
- [swapAt(_:_:)](<outputspan/swapat(____).md>) — Exchange the elements at the two given indices.
- [swapAt(unchecked:unchecked:)](<outputspan/swapat(unchecked_unchecked_).md>) — Exchange the elements at the two given indices.
- [withUnsafeMutableBufferPointer(_:)](<outputspan/withunsafemutablebufferpointer(__).md>) — Call the given closure with the unsafe buffer pointer addressed by this OutputSpan and a mutable reference to its count of initialized elements.

### Subscripts

- [subscript(_:)](<outputspan/subscript(__).md>) — Accesses the element at the specified index.
- [subscript(unchecked:)](<outputspan/subscript(unchecked_).md>) — Accesses the element at the specified index.

### Type Aliases

- [Index](outputspan/index.md) — The type that represents an initialized index in an `OutputSpan`.

## See Also

### Safe Memory Access

- [Span](span.md) — `Span<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.
- [RawSpan](rawspan.md) — `RawSpan` represents a contiguous region of memory which contains initialized bytes.
- [OutputRawSpan](outputrawspan.md) — `OutputRawSpan` is a reference to a contiguous region of memory which starts with some number of initialized bytes, followed by uninitialized memory. It provides operations to access the bytes it stores, as well as to append and to remove bytes.
- [UTF8Span](utf8span.md) — A borrowed view into contiguous memory that contains validly-encoded UTF-8 code units.
- [MutableSpan](mutablespan.md) — `MutableSpan<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.
- [MutableRawSpan](mutablerawspan.md) — `MutableRawSpan` represents a contiguous region of memory which contains initialized bytes.
- [SpanIterator](spaniterator.md) _(beta)_
