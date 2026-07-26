---
title: 'zip(_:_:_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/zip(_:_:_:)-16rcy'
source_url: 'https://developer.apple.com/documentation/combine/publisher/zip(_:_:_:)-16rcy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/zip%28_%3A_%3A_%3A%29-16rcy.json'
content_hash: 'sha256:7ff2cfe12b63edfe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# zip(_:_:_:)

<sub>Instance Method</sub>

Combines elements from three other publishers and delivers groups of elements as tuples.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func zip<P, Q, R>(_ publisher1: P, _ publisher2: Q, _ publisher3: R) -> Publishers.Zip4<Self, P, Q, R> where P : Publisher, Q : Publisher, R : Publisher, Self.Failure == P.Failure, P.Failure == Q.Failure, Q.Failure == R.Failure
```

## Parameters

- `publisher1` — A second publisher.

- `publisher2` — A third publisher.

- `publisher3` — A fourth publisher.

## Return Value

A publisher that emits groups of elements from the upstream publishers as tuples.

## Discussion

Use [zip(_:_:_:)](<zip(______)-16rcy.md>) to return a new publisher that combines the elements from three other publishers to publish a tuple to the downstream subscriber. The returned publisher waits until all four publishers have emitted an event, then delivers the oldest unconsumed event from each publisher as a tuple to the subscriber.

In this example, several [PassthroughSubject](../passthroughsubject.md) instances emit values; [zip(_:_:_:)](<zip(______)-16rcy.md>) receives the oldest unconsumed value from each publisher and combines them into a tuple that it republishes to the downstream:

```swift
let numbersPub = PassthroughSubject<Int, Never>()
let lettersPub = PassthroughSubject<String, Never>()
let emojiPub = PassthroughSubject<String, Never>()
let fractionsPub  = PassthroughSubject<Double, Never>()

cancellable = numbersPub
    .zip(lettersPub, emojiPub, fractionsPub)
    .sink { print("\($0)") }
numbersPub.send(1)         // numbersPub: 1       lettersPub:        emojiPub:       fractionsPub:         zip output: <none>
numbersPub.send(2)         // numbersPub: 1,2     lettersPub:        emojiPub:       fractionsPub:         zip output: <none>
numbersPub.send(3)         // numbersPub: 1,2,3   lettersPub:        emojiPub:       fractionsPub:         zip output: <none>
fractionsPub.send(0.1)     // numbersPub: 1,2,3   lettersPub: "A"    emojiPub:       fractionsPub: 0.1     zip output: <none>
lettersPub.send("A")       // numbersPub: 1,2,3   lettersPub: "A"    emojiPub:       fractionsPub: 0.1     zip output: <none>
emojiPub.send("😀")        // numbersPub: 2,3     lettersPub: "A"    emojiPub: "😀"  fractionsPub: 0.1     zip output: (1, "A", "😀", 0.1)
lettersPub.send("B")       // numbersPub: 2,3     lettersPub: "B"    emojiPub:       fractionsPub:         zip output: <none>
fractionsPub.send(0.8)     // numbersPub: 2,3     lettersPub: "B"    emojiPub:       fractionsPub: 0.8     zip output: <none>
emojiPub.send("🥰")        // numbersPub: 3       lettersPub: "B"    emojiPub:       fractionsPub: 0.8     zip output: (2, "B", "🥰", 0.8)
// Prints:
//  (1, "A", "😀", 0.1)
//  (2, "B", "🥰", 0.8)
```

If any upstream publisher finishes successfully or fails with an error, so too does the zipped publisher.

## See Also

### Collecting and republishing the oldest unconsumed elements from multiple publishers

- [zip(_:)](<zip(__).md>) — Combines elements from another publisher and deliver pairs of elements as tuples.
- [zip(_:_:)](<zip(____)-4xn21.md>) — Combines elements from another publisher and delivers a transformed output.
- [zip(_:_:)](<zip(____)-8d7k7.md>) — Combines elements from two other publishers and delivers groups of elements as tuples.
- [zip(_:_:_:)](<zip(______)-9yqi1.md>) — Combines elements from two other publishers and delivers a transformed output.
- [zip(_:_:_:_:)](<zip(________).md>) — Combines elements from three other publishers and delivers a transformed output.
