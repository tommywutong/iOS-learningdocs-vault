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
doc_path: '/documentation/combine/publisher/zip(_:_:_:)-9yqi1'
source_url: 'https://developer.apple.com/documentation/combine/publisher/zip(_:_:_:)-9yqi1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/zip%28_%3A_%3A_%3A%29-9yqi1.json'
content_hash: 'sha256:50554cdac6a4c093'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# zip(_:_:_:)

<sub>Instance Method</sub>

Combines elements from two other publishers and delivers a transformed output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func zip<P, Q, T>(_ publisher1: P, _ publisher2: Q, _ transform: @escaping (Self.Output, P.Output, Q.Output) -> T) -> Publishers.Map<Publishers.Zip3<Self, P, Q>, T> where P : Publisher, Q : Publisher, Self.Failure == P.Failure, P.Failure == Q.Failure
```

## Parameters

- `publisher1` — A second publisher.

- `publisher2` — A third publisher.

- `transform` — A closure that receives the most-recent value from each publisher and returns a new value to publish.

## Return Value

A publisher that uses the `transform` closure to emit new elements, produced by combining the most recent value from three upstream publishers.

## Discussion

Use [zip(_:_:_:)](<zip(______)-9yqi1.md>) to return a new publisher that combines the elements from two other publishers using a transformation you specify to publish a new value to the downstream subscriber. The returned publisher waits until all three publishers have emitted an event, then delivers the oldest unconsumed event from each publisher together that the operator uses in the transformation.

In this example, `numbersPub`, `lettersPub` and `emojiPub` are each a [PassthroughSubject](../passthroughsubject.md) that emit values; [zip(_:_:_:)](<zip(______)-9yqi1.md>) receives the oldest value from each publisher and uses the `Int` from `numbersPub` and publishes a string that repeats the [String](../../swift/string.md) from `lettersPub` and `emojiPub` that many times.

```swift
let numbersPub = PassthroughSubject<Int, Never>()
let lettersPub = PassthroughSubject<String, Never>()
let emojiPub = PassthroughSubject<String, Never>()

cancellable = numbersPub
    .zip(letters, emoji) { anInt, aLetter, anEmoji in
        ("\(String(repeating: anEmoji, count: anInt)) \(String(repeating: aLetter, count: anInt))")
    }
    .sink { print("\($0)") }

numbersPub.send(1)     // numbersPub: 1      lettersPub:        emojiPub:            zip output: <none>
numbersPub.send(2)     // numbersPub: 1,2    lettersPub:        emojiPub:            zip output: <none>
numbersPub.send(3)     // numbersPub: 1,2,3  lettersPub:        emojiPub:            zip output: <none>
lettersPub.send("A")   // numbersPub: 1,2,3  lettersPub: "A"    emojiPub:            zip output: <none>
emojiPub.send("😀")    // numbersPub: 2,3    lettersPub: "A"    emojiPub:"😀"        zip output: "😀 A"
lettersPub.send("B")   // numbersPub: 2,3    lettersPub: "B"    emojiPub:            zip output: <none>
emojiPub.send("🥰")    // numbersPub: 3      lettersPub:        emojiPub:"😀", "🥰"  zip output: "🥰🥰 BB"

// Prints:
// 😀 A
// 🥰🥰 BB
```

If any upstream publisher finishes successfully or fails with an error, so too does the zipped publisher.

## See Also

### Collecting and republishing the oldest unconsumed elements from multiple publishers

- [zip(_:)](<zip(__).md>) — Combines elements from another publisher and deliver pairs of elements as tuples.
- [zip(_:_:)](<zip(____)-4xn21.md>) — Combines elements from another publisher and delivers a transformed output.
- [zip(_:_:)](<zip(____)-8d7k7.md>) — Combines elements from two other publishers and delivers groups of elements as tuples.
- [zip(_:_:_:)](<zip(______)-16rcy.md>) — Combines elements from three other publishers and delivers groups of elements as tuples.
- [zip(_:_:_:_:)](<zip(________).md>) — Combines elements from three other publishers and delivers a transformed output.
