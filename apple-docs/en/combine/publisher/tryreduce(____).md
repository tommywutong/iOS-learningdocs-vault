---
title: 'tryReduce(_:_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/tryreduce(_:_:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/tryreduce(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/tryreduce%28_%3A_%3A%29.json'
content_hash: 'sha256:d67f3ee1ed026130'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# tryReduce(_:_:)

<sub>Instance Method</sub>

Applies an error-throwing closure that collects each element of a stream and publishes a final result upon completion.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func tryReduce<T>(_ initialResult: T, _ nextPartialResult: @escaping (T, Self.Output) throws -> T) -> Publishers.TryReduce<Self, T>
```

## Parameters

- `initialResult` — The value that the closure receives the first time it’s called.

- `nextPartialResult` — An error-throwing closure that takes the previously-accumulated value and the next element from the upstream publisher to produce a new value.

## Return Value

A publisher that applies the closure to all received elements and produces an accumulated value when the upstream publisher finishes.

## Discussion

Use [tryReduce(_:_:)](<tryreduce(____).md>) to collect a stream of elements and produce an accumulated value based on an error-throwing closure you provide. If the closure throws an error, the publisher fails and passes the error to its subscriber.

In the example below, the publisher’s `0` element causes the `myDivide(_:_:)` function to throw an error and publish the [nan](../../swift/double/nan.md) result:

```swift
struct DivisionByZeroError: Error {}
func myDivide(_ dividend: Double, _ divisor: Double) throws -> Double {
    guard divisor != 0 else { throw DivisionByZeroError() }
    return dividend / divisor
}

var numbers: [Double] = [5, 4, 3, 2, 1, 0]
numbers.publisher
    .tryReduce(numbers.first!, { accum, next in try myDivide(accum, next) })
    .catch({ _ in Just(Double.nan) })
    .sink { print("\($0)") }
```

## See Also

### Reducing elements

- [collect()](<collect().md>) — Collects all received elements, and emits a single array of the collection when the upstream publisher finishes.
- [collect(_:)](<collect(__).md>) — Collects up to the specified number of elements, and then emits a single array of the collection.
- [collect(_:options:)](<collect(__options_).md>) — Collects elements by a given time-grouping strategy, and emits a single array of the collection.
- [TimeGroupingStrategy](../publishers/timegroupingstrategy.md) — A strategy for collecting received elements.
- [ignoreOutput()](<ignoreoutput().md>) — Ignores all upstream elements, but passes along the upstream publisher’s completion state (finished or failed).
- [reduce(_:_:)](<reduce(____).md>) — Applies a closure that collects each element of a stream and publishes a final result upon completion.
