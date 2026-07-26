---
title: 'reduce(_:_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/reduce(_:_:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/reduce(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/reduce%28_%3A_%3A%29.json'
content_hash: 'sha256:aa6845ef6bdee38c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# reduce(_:_:)

<sub>Instance Method</sub>

Applies a closure that collects each element of a stream and publishes a final result upon completion.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func reduce<T>(_ initialResult: T, _ nextPartialResult: @escaping (T, Self.Output) -> T) -> Publishers.Reduce<Self, T>
```

## Parameters

- `initialResult` — The value that the closure receives the first time it’s called.

- `nextPartialResult` — A closure that produces a new value by taking the previously-accumulated value and the next element it receives from the upstream publisher.

## Return Value

A publisher that applies the closure to all received elements and produces an accumulated value when the upstream publisher finishes. If [reduce(_:_:)](<reduce(____).md>) receives an error from the upstream publisher, the operator delivers it to the downstream subscriber, the publisher terminates and publishes no value.

## Discussion

Use [reduce(_:_:)](<reduce(____).md>) to collect a stream of elements and produce an accumulated value based on a closure you provide.

In the following example, the [reduce(_:_:)](<reduce(____).md>) operator collects all the integer values it receives from its upstream publisher:

```swift
let numbers = (0...10)
cancellable = numbers.publisher
    .reduce(0, { accum, next in accum + next })
    .sink { print("\($0)") }

// Prints: "55"
```

## See Also

### Reducing elements

- [collect()](<collect().md>) — Collects all received elements, and emits a single array of the collection when the upstream publisher finishes.
- [collect(_:)](<collect(__).md>) — Collects up to the specified number of elements, and then emits a single array of the collection.
- [collect(_:options:)](<collect(__options_).md>) — Collects elements by a given time-grouping strategy, and emits a single array of the collection.
- [TimeGroupingStrategy](../publishers/timegroupingstrategy.md) — A strategy for collecting received elements.
- [ignoreOutput()](<ignoreoutput().md>) — Ignores all upstream elements, but passes along the upstream publisher’s completion state (finished or failed).
- [tryReduce(_:_:)](<tryreduce(____).md>) — Applies an error-throwing closure that collects each element of a stream and publishes a final result upon completion.
