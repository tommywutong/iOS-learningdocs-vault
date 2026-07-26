---
title: 'zip(_:_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/zip(_:_:)-4xn21'
source_url: 'https://developer.apple.com/documentation/combine/publisher/zip(_:_:)-4xn21'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/zip%28_%3A_%3A%29-4xn21.json'
content_hash: 'sha256:537d06c762431e21'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# zip(_:_:)

<sub>Instance Method</sub>

Combines elements from another publisher and delivers a transformed output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func zip<P, T>(_ other: P, _ transform: @escaping (Self.Output, P.Output) -> T) -> Publishers.Map<Publishers.Zip<Self, P>, T> where P : Publisher, Self.Failure == P.Failure
```

## Parameters

- `other` — Another publisher.

- `transform` — A closure that receives the most-recent value from each publisher and returns a new value to publish.

## Return Value

A publisher that uses the `transform` closure to emit new elements, produced by combining the most recent value from two upstream publishers.

## Discussion

Use [zip(_:_:)](<zip(____)-4xn21.md>) to return a new publisher that combines the elements from two publishers using a transformation you specify to publish a new value to the downstream.  The returned publisher waits until both publishers have emitted an event, then delivers the oldest unconsumed event from each publisher together that the operator uses in the transformation.

In this example, [PassthroughSubject](../passthroughsubject.md) instances `numbersPub` and `lettersPub` emit values; [zip(_:_:)](<zip(____)-4xn21.md>) receives the oldest value from each publisher, uses the `Int` from `numbersPub` and publishes a string that repeats the [String](../../swift/string.md) from `lettersPub` that many times.

```swift
let numbersPub = PassthroughSubject<Int, Never>()
let lettersPub = PassthroughSubject<String, Never>()
cancellable = numbersPub
    .zip(lettersPub) { anInt, aLetter in
        String(repeating: aLetter, count: anInt)
    }
    .sink { print("\($0)") }
numbersPub.send(1)     // numbersPub: 1      lettersPub:       zip output: <none>
numbersPub.send(2)     // numbersPub: 1,2    lettersPub:       zip output: <none>
numbersPub.send(3)     // numbersPub: 1,2,3  lettersPub:       zip output: <none>
lettersPub.send("A")   // numbersPub: 1,2,3  lettersPub: "A"   zip output: "A"
lettersPub.send("B")   // numbersPub: 2,3    lettersPub: "B"   zip output: "BB"
// Prints:
//  A
//  BB
```

If either upstream publisher finishes successfully or fails with an error, the zipped publisher does the same.

## See Also

### Collecting and republishing the oldest unconsumed elements from multiple publishers

- [zip(_:)](<zip(__).md>) — Combines elements from another publisher and deliver pairs of elements as tuples.
- [zip(_:_:)](<zip(____)-8d7k7.md>) — Combines elements from two other publishers and delivers groups of elements as tuples.
- [zip(_:_:_:)](<zip(______)-9yqi1.md>) — Combines elements from two other publishers and delivers a transformed output.
- [zip(_:_:_:)](<zip(______)-16rcy.md>) — Combines elements from three other publishers and delivers groups of elements as tuples.
- [zip(_:_:_:_:)](<zip(________).md>) — Combines elements from three other publishers and delivers a transformed output.
