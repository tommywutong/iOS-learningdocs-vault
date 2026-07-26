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
doc_path: '/documentation/combine/publisher/zip(_:_:)-8d7k7'
source_url: 'https://developer.apple.com/documentation/combine/publisher/zip(_:_:)-8d7k7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/zip%28_%3A_%3A%29-8d7k7.json'
content_hash: 'sha256:8c475f275bb6614b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# zip(_:_:)

<sub>Instance Method</sub>

Combines elements from two other publishers and delivers groups of elements as tuples.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func zip<P, Q>(_ publisher1: P, _ publisher2: Q) -> Publishers.Zip3<Self, P, Q> where P : Publisher, Q : Publisher, Self.Failure == P.Failure, P.Failure == Q.Failure
```

## Parameters

- `publisher1` — A second publisher.

- `publisher2` — A third publisher.

## Return Value

A publisher that emits groups of elements from the upstream publishers as tuples.

## Discussion

Use [zip(_:_:)](<zip(____)-8d7k7.md>) to return a new publisher that combines the elements from two additional publishers to publish a tuple to the downstream. The returned publisher waits until all three publishers have emitted an event, then delivers the oldest unconsumed event from each publisher as a tuple to the subscriber.

In this example, `numbersPub`, `lettersPub` and `emojiPub` are each a [PassthroughSubject](../passthroughsubject.md); [zip(_:_:)](<zip(____)-8d7k7.md>) receives the oldest unconsumed value from each publisher and combines them into a tuple that it republishes to the downstream:

```swift
let numbersPub = PassthroughSubject<Int, Never>()
let lettersPub = PassthroughSubject<String, Never>()
let emojiPub = PassthroughSubject<String, Never>()

cancellable = numbersPub
    .zip(lettersPub, emojiPub)
    .sink { print("\($0)") }
numbersPub.send(1)     // numbersPub: 1      lettersPub:          emojiPub:        zip output: <none>
numbersPub.send(2)     // numbersPub: 1,2    lettersPub:          emojiPub:        zip output: <none>
numbersPub.send(3)     // numbersPub: 1,2,3  lettersPub:          emojiPub:        zip output: <none>
lettersPub.send("A")   // numbersPub: 1,2,3  lettersPub: "A"      emojiPub:        zip output: <none>
emojiPub.send("😀")    // numbersPub: 2,3    lettersPub: "A"      emojiPub: "😀"   zip output: (1, "A", "😀")
lettersPub.send("B")   // numbersPub: 2,3    lettersPub: "B"      emojiPub:        zip output: <none>
emojiPub.send("🥰")    // numbersPub: 3      lettersPub:          emojiPub:        zip output: (2, "B", "🥰")

// Prints:
//  (1, "A", "😀")
//  (2, "B", "🥰")
```

If any upstream publisher finishes successfully or fails with an error, so too does the zipped publisher.

## See Also

### Collecting and republishing the oldest unconsumed elements from multiple publishers

- [zip(_:)](<zip(__).md>) — Combines elements from another publisher and deliver pairs of elements as tuples.
- [zip(_:_:)](<zip(____)-4xn21.md>) — Combines elements from another publisher and delivers a transformed output.
- [zip(_:_:_:)](<zip(______)-9yqi1.md>) — Combines elements from two other publishers and delivers a transformed output.
- [zip(_:_:_:)](<zip(______)-16rcy.md>) — Combines elements from three other publishers and delivers groups of elements as tuples.
- [zip(_:_:_:_:)](<zip(________).md>) — Combines elements from three other publishers and delivers a transformed output.
