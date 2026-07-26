---
title: OutputRawSpan
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/outputrawspan
source_url: 'https://developer.apple.com/documentation/swift/outputrawspan'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/outputrawspan.json'
content_hash: 'sha256:6cdb8af0eae719e6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# OutputRawSpan

<sub>Structure</sub>

`OutputRawSpan` is a reference to a contiguous region of memory which starts with some number of initialized bytes, followed by uninitialized memory. It provides operations to access the bytes it stores, as well as to append and to remove bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct OutputRawSpan
```

## Relationships

- **Conforms To**: [ContiguousBytes](../foundation/contiguousbytes.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Initializers

- [init()](<outputrawspan/init().md>) — Create an OutputRawSpan with zero capacity.
- [init(buffer:initializedCount:)](<outputrawspan/init(buffer_initializedcount_)-1vcj6.md>) — Unsafely create an OutputRawSpan over partly-initialized memory.
- [init(buffer:initializedCount:)](<outputrawspan/init(buffer_initializedcount_)-5sduz.md>) — Unsafely create an OutputRawSpan over partly-initialized memory.

### Instance Properties

- [byteCount](outputrawspan/bytecount.md) — The number of initialized bytes in this span.
- [byteOffsets](outputrawspan/byteoffsets.md) — The indices that are valid for subscripting the span, in ascending order.
- [bytes](outputrawspan/bytes.md) — Borrow the underlying initialized memory for read-only access.
- [capacity](outputrawspan/capacity.md) — The total number of bytes that this output span can contain.
- [freeCapacity](outputrawspan/freecapacity.md) — The number of additional bytes that can be appended to this span.
- [isEmpty](outputrawspan/isempty.md) — A Boolean value indicating whether the span is empty.
- [isFull](outputrawspan/isfull.md) — A Boolean value indicating whether the span is full.
- [mutableBytes](outputrawspan/mutablebytes.md) — Exclusively borrow the underlying initialized memory for mutation.

### Instance Methods

- [append(_:)](<outputrawspan/append(__).md>) — Append a single byte to this span.
- [append(_:as:)](<outputrawspan/append(__as_)-63w17.md>) — Appends the given value’s bytes to this span’s bytes.
- [append(_:as:)](<outputrawspan/append(__as_)-89j87.md>) — Appends the given value’s bytes to this span’s bytes.
- [append(_:as:_:)](<outputrawspan/append(__as___).md>) — Appends the given value’s bytes to this span’s bytes. _(beta)_
- [append(repeating:count:as:)](<outputrawspan/append(repeating_count_as_)-1h8m1.md>) — Appends the given value’s bytes repeatedly to this span’s bytes.
- [append(repeating:count:as:)](<outputrawspan/append(repeating_count_as_)-3z0bf.md>) — Appends the given value’s bytes repeatedly to this span’s bytes.
- [append(repeating:count:as:_:)](<outputrawspan/append(repeating_count_as___).md>) — Appends the given value’s bytes repeatedly to this span’s bytes. _(beta)_
- [finalize(for:)](<outputrawspan/finalize(for_)-4su35.md>) — Consume the output span and return the number of initialized bytes.
- [finalize(for:)](<outputrawspan/finalize(for_)-8oz61.md>) — Consume the output span and return the number of initialized bytes.
- [removeAll()](<outputrawspan/removeall().md>) — Remove all this span’s bytes and return its memory to the uninitialized state.
- [removeLast()](<outputrawspan/removelast().md>) — Remove the last byte from this span.
- [removeLast(_:)](<outputrawspan/removelast(__).md>) — Remove the last n bytes from this span, returning the memory they occupy to the uninitialized state.
- [withUnsafeMutableBytes(_:)](<outputrawspan/withunsafemutablebytes(__).md>) — Call the given closure with the unsafe buffer pointer addressed by this OutputRawSpan and a mutable reference to its count of initialized bytes.

### Subscripts

- [subscript(_:)](<outputrawspan/subscript(__).md>) — Accesses the byte at the specified offset in the span.
- [subscript(unchecked:)](<outputrawspan/subscript(unchecked_).md>) — Accesses the byte at the specified offset in the span.

## See Also

### Safe Memory Access

- [Span](span.md) — `Span<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.
- [RawSpan](rawspan.md) — `RawSpan` represents a contiguous region of memory which contains initialized bytes.
- [OutputSpan](outputspan.md) — `OutputSpan` is a reference to a contiguous region of memory that starts with some number of initialized `Element` instances followed by uninitialized memory. It provides operations to access the items it stores, as well as to add new elements and to remove existing ones.
- [UTF8Span](utf8span.md) — A borrowed view into contiguous memory that contains validly-encoded UTF-8 code units.
- [MutableSpan](mutablespan.md) — `MutableSpan<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.
- [MutableRawSpan](mutablerawspan.md) — `MutableRawSpan` represents a contiguous region of memory which contains initialized bytes.
- [SpanIterator](spaniterator.md) _(beta)_
