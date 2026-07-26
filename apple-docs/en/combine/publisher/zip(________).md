---
title: 'zip(_:_:_:_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/zip(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/zip(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/zip%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:86683a869432b332'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# zip(_:_:_:_:)

<sub>Instance Method</sub>

Combines elements from three other publishers and delivers a transformed output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func zip<P, Q, R, T>(_ publisher1: P, _ publisher2: Q, _ publisher3: R, _ transform: @escaping (Self.Output, P.Output, Q.Output, R.Output) -> T) -> Publishers.Map<Publishers.Zip4<Self, P, Q, R>, T> where P : Publisher, Q : Publisher, R : Publisher, Self.Failure == P.Failure, P.Failure == Q.Failure, Q.Failure == R.Failure
```

## Parameters

- `publisher1` — A second publisher.

- `publisher2` — A third publisher.

- `publisher3` — A fourth publisher.

- `transform` — A closure that receives the most-recent value from each publisher and returns a new value to publish.

## Return Value

A publisher that uses the `transform` closure to emit new elements, produced by combining the most recent value from four upstream publishers.

## Discussion

Use [zip(_:_:_:_:)](<zip(________).md>) to return a new publisher that combines the elements from three other publishers using a transformation you specify to publish a new value to the downstream subscriber. The returned publisher waits until all four publishers have emitted an event, then delivers the oldest unconsumed event from each publisher together that the operator uses in the transformation.

In this example, the [PassthroughSubject](../passthroughsubject.md) publishers, `numbersPub`, `fractionsPub`, `lettersPub`, and `emojiPub` emit values. The [zip(_:_:_:_:)](<zip(________).md>) operator receives the oldest value from each publisher and uses the `Int` from `numbersPub` and publishes a string that repeats the [String](../../swift/string.md) from `lettersPub` and `emojiPub` that many times and prints out the value in `fractionsPub`.

```swift
let numbersPub = PassthroughSubject<Int, Never>()      // first publisher
let lettersPub = PassthroughSubject<String, Never>()   // second
let emojiPub = PassthroughSubject<String, Never>()     // third
let fractionsPub  = PassthroughSubject<Double, Never>()// fourth

cancellable = numbersPub
    .zip(lettersPub, emojiPub, fractionsPub) { anInt, aLetter, anEmoji, aFraction  in
        ("\(String(repeating: anEmoji, count: anInt)) \(String(repeating: aLetter, count: anInt)) \(aFraction)")
    }
    .sink { print("\($0)") }

numbersPub.send(1)         // numbersPub: 1       lettersPub:          emojiPub:          zip output: <none>
numbersPub.send(2)         // numbersPub: 1,2     lettersPub:          emojiPub:          zip output: <none>
numbersPub.send(3)         // numbersPub: 1,2,3   lettersPub:          emojiPub:          zip output: <none>
fractionsPub.send(0.1)     // numbersPub: 1,2,3   lettersPub: "A"      emojiPub:          zip output: <none>
lettersPub.send("A")       // numbersPub: 1,2,3   lettersPub: "A"      emojiPub:          zip output: <none>
emojiPub.send("😀")        // numbersPub: 1,2,3   lettersPub: "A"      emojiPub:"😀"      zip output: "😀 A"
lettersPub.send("B")       // numbersPub: 2,3     lettersPub: "B"      emojiPub:          zip output: <none>
fractionsPub.send(0.8)     // numbersPub: 2,3     lettersPub: "A"      emojiPub:          zip output: <none>
emojiPub.send("🥰")        // numbersPub: 3       lettersPub: "B"      emojiPub:          zip output: "🥰🥰 BB"
// Prints:
//1 😀 A 0.1
//2 🥰🥰 BB 0.8
```

If any upstream publisher finishes successfully or fails with an error, so too does the zipped publisher.

## See Also

### Collecting and republishing the oldest unconsumed elements from multiple publishers

- [zip(_:)](<zip(__).md>) — Combines elements from another publisher and deliver pairs of elements as tuples.
- [zip(_:_:)](<zip(____)-4xn21.md>) — Combines elements from another publisher and delivers a transformed output.
- [zip(_:_:)](<zip(____)-8d7k7.md>) — Combines elements from two other publishers and delivers groups of elements as tuples.
- [zip(_:_:_:)](<zip(______)-9yqi1.md>) — Combines elements from two other publishers and delivers a transformed output.
- [zip(_:_:_:)](<zip(______)-16rcy.md>) — Combines elements from three other publishers and delivers groups of elements as tuples.
