---
title: 'zip(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/zip(_:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/zip(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/zip%28_%3A%29.json'
content_hash: 'sha256:ddebf46ae03a222f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# zip(_:)

<sub>Instance Method</sub>

Combines elements from another publisher and deliver pairs of elements as tuples.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func zip<P>(_ other: P) -> Publishers.Zip<Self, P> where P : Publisher, Self.Failure == P.Failure
```

## Parameters

- `other` — Another publisher.

## Return Value

A publisher that emits pairs of elements from the upstream publishers as tuples.

## Discussion

Use [zip(_:)](<zip(__).md>) to combine the latest elements from two publishers and emit a tuple to the downstream. The returned publisher waits until both publishers have emitted an event, then delivers the oldest unconsumed event from each publisher together as a tuple to the subscriber.

Much like a zipper or zip fastener on a piece of clothing pulls together rows of teeth to link the two sides, [zip(_:)](<zip(__).md>) combines streams from two different publishers by linking pairs of elements from each side.

In this example, `numbers` and `letters` are [PassthroughSubject](../passthroughsubject.md)s that emit values; once [zip(_:)](<zip(__).md>) receives one value from each, it publishes the pair as a tuple to the downstream subscriber. It then waits for the next pair of values.

```swift
 let numbersPub = PassthroughSubject<Int, Never>()
 let lettersPub = PassthroughSubject<String, Never>()

 cancellable = numbersPub
     .zip(lettersPub)
     .sink { print("\($0)") }
 numbersPub.send(1)    // numbersPub: 1      lettersPub:        zip output: <none>
 numbersPub.send(2)    // numbersPub: 1,2    lettersPub:        zip output: <none>
 letters.send("A")     // numbers: 1,2       letters:"A"        zip output: <none>
 numbers.send(3)       // numbers: 1,2,3     letters:           zip output: (1,"A")
 letters.send("B")     // numbers: 1,2,3     letters: "B"       zip output: (2,"B")

 // Prints:
 //  (1, "A")
 //  (2, "B")
```

If either upstream publisher finishes successfully or fails with an error, the zipped publisher does the same.

## See Also

### Collecting and republishing the oldest unconsumed elements from multiple publishers

- [zip(_:_:)](<zip(____)-4xn21.md>) — Combines elements from another publisher and delivers a transformed output.
- [zip(_:_:)](<zip(____)-8d7k7.md>) — Combines elements from two other publishers and delivers groups of elements as tuples.
- [zip(_:_:_:)](<zip(______)-9yqi1.md>) — Combines elements from two other publishers and delivers a transformed output.
- [zip(_:_:_:)](<zip(______)-16rcy.md>) — Combines elements from three other publishers and delivers groups of elements as tuples.
- [zip(_:_:_:_:)](<zip(________).md>) — Combines elements from three other publishers and delivers a transformed output.
