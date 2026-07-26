---
title: ignoreOutput()
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publisher/ignoreoutput()
source_url: 'https://developer.apple.com/documentation/combine/publisher/ignoreoutput()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/ignoreoutput%28%29.json'
content_hash: 'sha256:c55c5f3f7e757940'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# ignoreOutput()

<sub>Instance Method</sub>

Ignores all upstream elements, but passes along the upstream publisher’s completion state (finished or failed).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func ignoreOutput() -> Publishers.IgnoreOutput<Self>
```

## Return Value

A publisher that ignores all upstream elements.

## Discussion

Use the [ignoreOutput()](<ignoreoutput().md>) operator to determine if a publisher is able to complete successfully or would fail.

In the example below, the array publisher (`numbers`) delivers the first five of its elements successfully, as indicated by the [ignoreOutput()](<ignoreoutput().md>) operator. The operator consumes, but doesn’t republish the elements downstream. However, the sixth element, `0`, causes the error throwing closure to catch a `NoZeroValuesAllowedError` that terminates the stream.

```swift
struct NoZeroValuesAllowedError: Error {}
let numbers = [1, 2, 3, 4, 5, 0, 6, 7, 8, 9]
cancellable = numbers.publisher
    .tryFilter({ anInt in
        guard anInt != 0 else { throw NoZeroValuesAllowedError() }
        return anInt < 20
    })
    .ignoreOutput()
    .sink(receiveCompletion: {print("completion: \($0)")},
          receiveValue: {print("value \($0)")})

// Prints: "completion: failure(NoZeroValuesAllowedError())"
```

The output type of this publisher is [Never](../../swift/never.md).

## See Also

### Reducing elements

- [collect()](<collect().md>) — Collects all received elements, and emits a single array of the collection when the upstream publisher finishes.
- [collect(_:)](<collect(__).md>) — Collects up to the specified number of elements, and then emits a single array of the collection.
- [collect(_:options:)](<collect(__options_).md>) — Collects elements by a given time-grouping strategy, and emits a single array of the collection.
- [TimeGroupingStrategy](../publishers/timegroupingstrategy.md) — A strategy for collecting received elements.
- [reduce(_:_:)](<reduce(____).md>) — Applies a closure that collects each element of a stream and publishes a final result upon completion.
- [tryReduce(_:_:)](<tryreduce(____).md>) — Applies an error-throwing closure that collects each element of a stream and publishes a final result upon completion.
