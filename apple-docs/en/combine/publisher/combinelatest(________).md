---
title: 'combineLatest(_:_:_:_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/combinelatest(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/combinelatest(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/combinelatest%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:3cdc4b88a6a58dad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# combineLatest(_:_:_:_:)

<sub>Instance Method</sub>

Subscribes to three additional publishers and invokes a closure upon receiving output from any of the publishers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func combineLatest<P, Q, R, T>(_ publisher1: P, _ publisher2: Q, _ publisher3: R, _ transform: @escaping (Self.Output, P.Output, Q.Output, R.Output) -> T) -> Publishers.Map<Publishers.CombineLatest4<Self, P, Q, R>, T> where P : Publisher, Q : Publisher, R : Publisher, Self.Failure == P.Failure, P.Failure == Q.Failure, Q.Failure == R.Failure
```

## Parameters

- `publisher1` — A second publisher to combine with the first publisher.

- `publisher2` — A third publisher to combine with the first publisher.

- `publisher3` — A fourth publisher to combine with the first publisher.

- `transform` — A closure that receives the most-recent value from each publisher and returns a new value to publish.

## Return Value

A publisher that receives and combines elements from this publisher and three other publishers.

## Discussion

Use [combineLatest(_:_:_:_:)](<combinelatest(________).md>) when you need to combine the current and 3 additional publishers and transform the values using a closure in which you specify the published elements, to publish a new element.

> [!tip] Tip
> The combined publisher doesn’t produce elements until each of its upstream publishers publishes at least one element.

The combined publisher passes through any requests to _all_ upstream publishers. However, it still obeys the demand-fulfilling rule of only sending the request amount downstream. If the demand isn’t [unlimited](../subscribers/demand/unlimited.md), it drops values from upstream publishers. It implements this by using a buffer size of 1 for each upstream, and holds the most-recent value in each buffer.

All upstream publishers need to finish for this publisher to finish. If an upstream publisher never publishes a value, this publisher never finishes.

In the example below, as [combineLatest(_:_:_:_:)](<combinelatest(________).md>) receives the most-recent values published by four publishers, multiplies them together, and republishes the result:

```swift
let pub = PassthroughSubject<Int, Never>()
let pub2 = PassthroughSubject<Int, Never>()
let pub3 = PassthroughSubject<Int, Never>()
let pub4 = PassthroughSubject<Int, Never>()

cancellable = pub
    .combineLatest(pub2, pub3, pub4) { firstValue, secondValue, thirdValue, fourthValue in
        return firstValue * secondValue * thirdValue * fourthValue
    }
    .sink { print("Result: \($0).") }

pub.send(1)
pub.send(2)
pub2.send(2)
pub3.send(9)
pub4.send(1)

pub.send(3)
pub2.send(12)
pub.send(13)
pub3.send(19)

// Prints:
//  Result: 36.     // pub = 2,  pub2 = 2,   pub3 = 9,  pub4 = 1
//  Result: 54.     // pub = 3,  pub2 = 2,   pub3 = 9,  pub4 = 1
//  Result: 324.    // pub = 3,  pub2 = 12,  pub3 = 9,  pub4 = 1
//  Result: 1404.   // pub = 13, pub2 = 12,  pub3 = 9,  pub4 = 1
//  Result: 2964.   // pub = 13, pub2 = 12,  pub3 = 19, pub4 = 1
```

## See Also

### Collecting and republishing the latest elements from multiple publishers

- [combineLatest(_:_:)](<combinelatest(____)-1n30g.md>) — Subscribes to an additional publisher and invokes a closure upon receiving output from either publisher.
- [combineLatest(_:)](<combinelatest(__).md>) — Subscribes to an additional publisher and publishes a tuple upon receiving output from either publisher.
- [combineLatest(_:_:_:)](<combinelatest(______)-6ekpz.md>) — Subscribes to two additional publishers and invokes a closure upon receiving output from any of the publishers.
- [combineLatest(_:_:)](<combinelatest(____)-5crqg.md>) — Subscribes to two additional publishers and publishes a tuple upon receiving output from any of the publishers.
- [combineLatest(_:_:_:)](<combinelatest(______)-48buc.md>) — Subscribes to three additional publishers and publishes a tuple upon receiving output from any of the publishers.
