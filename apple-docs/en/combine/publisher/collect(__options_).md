---
title: 'collect(_:options:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/collect(_:options:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/collect(_:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/collect%28_%3Aoptions%3A%29.json'
content_hash: 'sha256:63f2cda28bc59662'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# collect(_:options:)

<sub>Instance Method</sub>

Collects elements by a given time-grouping strategy, and emits a single array of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func collect<S>(_ strategy: Publishers.TimeGroupingStrategy<S>, options: S.SchedulerOptions? = nil) -> Publishers.CollectByTime<Self, S> where S : Scheduler
```

## Parameters

- `strategy` — The timing group strategy used by the operator to collect and publish elements.

- `options` — Scheduler options to use for the strategy.

## Return Value

A publisher that collects elements by a given strategy, and emits a single array of the collection.

## Discussion

Use [collect(_:options:)](<collect(__options_).md>) to emit arrays of elements on a schedule specified by a [Scheduler](../scheduler.md) and `Stride` that you provide. At the end of each scheduled interval, the publisher sends an array that contains the items it collected. If the upstream publisher finishes before filling the buffer, the publisher sends an array that contains items it received. This may be fewer than the number of elements specified in the requested `Stride`.

If the upstream publisher fails with an error, this publisher forwards the error to the downstream receiver instead of sending its output.

The example above collects timestamps generated on a one-second [Timer](../../foundation/timer.md) in groups (`Stride`) of five.

```swift
let sub = Timer.publish(every: 1, on: .main, in: .default)
    .autoconnect()
    .collect(.byTime(RunLoop.main, .seconds(5)))
    .sink { print("\($0)", terminator: "\n\n") }

// Prints: "[2020-01-24 00:54:46 +0000, 2020-01-24 00:54:47 +0000,
//          2020-01-24 00:54:48 +0000, 2020-01-24 00:54:49 +0000,
//          2020-01-24 00:54:50 +0000]"
```

> [!note] Note
> When this publisher receives a request for `.max(n)` elements, it requests `.max(count * n)` from the upstream publisher.

## See Also

### Reducing elements

- [collect()](<collect().md>) — Collects all received elements, and emits a single array of the collection when the upstream publisher finishes.
- [collect(_:)](<collect(__).md>) — Collects up to the specified number of elements, and then emits a single array of the collection.
- [TimeGroupingStrategy](../publishers/timegroupingstrategy.md) — A strategy for collecting received elements.
- [ignoreOutput()](<ignoreoutput().md>) — Ignores all upstream elements, but passes along the upstream publisher’s completion state (finished or failed).
- [reduce(_:_:)](<reduce(____).md>) — Applies a closure that collects each element of a stream and publishes a final result upon completion.
- [tryReduce(_:_:)](<tryreduce(____).md>) — Applies an error-throwing closure that collects each element of a stream and publishes a final result upon completion.
