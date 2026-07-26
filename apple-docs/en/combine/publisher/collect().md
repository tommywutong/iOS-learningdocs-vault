---
title: collect()
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publisher/collect()
source_url: 'https://developer.apple.com/documentation/combine/publisher/collect()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/collect%28%29.json'
content_hash: 'sha256:f9f7089be064a43e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# collect()

<sub>Instance Method</sub>

Collects all received elements, and emits a single array of the collection when the upstream publisher finishes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func collect() -> Publishers.Collect<Self>
```

## Return Value

A publisher that collects all received items and returns them as an array upon completion.

## Discussion

Use [collect()](<collect().md>) to gather elements into an array that the operator emits after the upstream publisher finishes.

If the upstream publisher fails with an error, this publisher forwards the error to the downstream receiver instead of sending its output.

This publisher requests an unlimited number of elements from the upstream publisher and uses an unbounded amount of memory to store the received values. The publisher may exert memory pressure on the system for very large sets of elements.

The [collect()](<collect().md>) operator only sends the collected array to its downstream receiver after a request whose demand is greater than 0 items. Otherwise, [collect()](<collect().md>) waits until it receives a non-zero request.

In the example below, an Integer range is a publisher that emits an array of integers:

```swift
let numbers = (0...10)
cancellable = numbers.publisher
    .collect()
    .sink { print("\($0)") }

// Prints: "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
```

## See Also

### Reducing elements

- [collect(_:)](<collect(__).md>) — Collects up to the specified number of elements, and then emits a single array of the collection.
- [collect(_:options:)](<collect(__options_).md>) — Collects elements by a given time-grouping strategy, and emits a single array of the collection.
- [TimeGroupingStrategy](../publishers/timegroupingstrategy.md) — A strategy for collecting received elements.
- [ignoreOutput()](<ignoreoutput().md>) — Ignores all upstream elements, but passes along the upstream publisher’s completion state (finished or failed).
- [reduce(_:_:)](<reduce(____).md>) — Applies a closure that collects each element of a stream and publishes a final result upon completion.
- [tryReduce(_:_:)](<tryreduce(____).md>) — Applies an error-throwing closure that collects each element of a stream and publishes a final result upon completion.
