---
title: 'nextSpan(maximumCount:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/spaniterator/nextspan(maximumcount:)'
source_url: 'https://developer.apple.com/documentation/swift/spaniterator/nextspan(maximumcount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/spaniterator/nextspan%28maximumcount%3A%29.json'
content_hash: 'sha256:0a2f1cddbfbc354e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SpanIterator](../spaniterator.md)

# nextSpan(maximumCount:)

<sub>Instance Method</sub>

Returns a span over the next group of elements that are ready to by visited, up to the specifed maximum.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func nextSpan(maximumCount: Int) -> Span<Element>
```

## Discussion

If the underlying type stores its elements in one or more blocks of contiguous memory, then the returned span typically directly addresses one of those buffers. On the other hand, if the underlying type materializes its elements on demand, then the returned span addresses a temporary buffer managed by the iterator itself. Consequently, the returned span is tied to this particular invocation of `nextSpan`, and it cannot survive beyond the next invocation of this method.

If the iterator has not yet reached the end of the underlying elements, then this method returns a non-empty span of at most `maximumCount` elements and updates the iterator’s current position to the element following the last item in the returned span. The `maximumCount` argument allows callers to avoid getting more items than they are able to process in one go, simplifying usage, and avoiding materializing more elements than needed.

If the iterator’s current position is at the end of the container, then this method returns an empty span without updating the position.

This method can be used to efficiently process the items of a container in bulk, by directly iterating over its piecewise contiguous pieces of storage:

```swift
var it = items.makeBorrowingIterator()
while true {
  let span = it.nextSpan(maximumCount: .max)
  if span.isEmpty { break }
  // Process items in `span`
}
```

The spans returned by this method are not guaranteed to be disjunct. Iterators that materialize elements on demand typically reuse the same buffer over and over again; and even some proper containers may link to a single storage chunk (or parts of a storage chunk) multiple times, for example to repeat their contents.
