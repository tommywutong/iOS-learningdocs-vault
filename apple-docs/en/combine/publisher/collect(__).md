---
title: 'collect(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/collect(_:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/collect(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/collect%28_%3A%29.json'
content_hash: 'sha256:317ce654f570531e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# collect(_:)

<sub>Instance Method</sub>

Collects up to the specified number of elements, and then emits a single array of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func collect(_ count: Int) -> Publishers.CollectByCount<Self>
```

## Parameters

- `count` — The maximum number of received elements to buffer before publishing.

## Return Value

A publisher that collects up to the specified number of elements, and then publishes them as an array.

## Discussion

Use [collect(_:)](<collect(__).md>) to emit arrays of at most `count` elements from an upstream publisher. If the upstream publisher finishes before collecting the specified number of elements, the publisher sends an array of only the items it received. This may be fewer than `count` elements.

If the upstream publisher fails with an error, this publisher forwards the error to the downstream receiver instead of sending its output.

In the example below, the [collect(_:)](<collect(__).md>) operator emits one partial and two full arrays based on the requested collection size of `5`:

```swift
let numbers = (0...10)
cancellable = numbers.publisher
    .collect(5)
    .sink { print("\($0), terminator: " "") }

// Prints "[0, 1, 2, 3, 4] [5, 6, 7, 8, 9] [10] "
```

> [!note] Note
> When this publisher receives a request for `.max(n)` elements, it requests `.max(count * n)` from the upstream publisher.

## See Also

### Reducing elements

- [collect()](<collect().md>) — Collects all received elements, and emits a single array of the collection when the upstream publisher finishes.
- [collect(_:options:)](<collect(__options_).md>) — Collects elements by a given time-grouping strategy, and emits a single array of the collection.
- [TimeGroupingStrategy](../publishers/timegroupingstrategy.md) — A strategy for collecting received elements.
- [ignoreOutput()](<ignoreoutput().md>) — Ignores all upstream elements, but passes along the upstream publisher’s completion state (finished or failed).
- [reduce(_:_:)](<reduce(____).md>) — Applies a closure that collects each element of a stream and publishes a final result upon completion.
- [tryReduce(_:_:)](<tryreduce(____).md>) — Applies an error-throwing closure that collects each element of a stream and publishes a final result upon completion.
