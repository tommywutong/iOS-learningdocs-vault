---
title: 'combineLatest(_:_:_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/combinelatest(_:_:_:)-6ekpz'
source_url: 'https://developer.apple.com/documentation/combine/publisher/combinelatest(_:_:_:)-6ekpz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/combinelatest%28_%3A_%3A_%3A%29-6ekpz.json'
content_hash: 'sha256:a68fd4d0670f3cef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# combineLatest(_:_:_:)

<sub>Instance Method</sub>

Subscribes to two additional publishers and invokes a closure upon receiving output from any of the publishers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func combineLatest<P, Q, T>(_ publisher1: P, _ publisher2: Q, _ transform: @escaping (Self.Output, P.Output, Q.Output) -> T) -> Publishers.Map<Publishers.CombineLatest3<Self, P, Q>, T> where P : Publisher, Q : Publisher, Self.Failure == P.Failure, P.Failure == Q.Failure
```

## Parameters

- `publisher1` — A second publisher to combine with the first publisher.

- `publisher2` — A third publisher to combine with the first publisher.

- `transform` — A closure that receives the most-recent value from each publisher and returns a new value to publish.

## Return Value

A publisher that receives and combines elements from this publisher and two other publishers.

## Discussion

Use `combineLatest<P, Q>(_:,_:)` to combine the current and two additional publishers and transform them using a closure you specify to publish a new value to the downstream.

> [!tip] Tip
> The combined publisher doesn’t produce elements until each of its upstream publishers publishes at least one element.

The combined publisher passes through any requests to _all_ upstream publishers. However, it still obeys the demand-fulfilling rule of only sending the request amount downstream. If the demand isn’t `.unlimited`, it drops values from upstream publishers. It implements this by using a buffer size of 1 for each upstream, and holds the most-recent value in each buffer. All upstream publishers need to finish for this publisher to finish. If an upstream publisher never publishes a value, this publisher never finishes. If any of the combined publishers terminates with a failure, this publisher also fails.

In the example below, `combineLatest()` receives the most-recent values published by three publishers, multiplies them together, and republishes the result:

```swift
let pub = PassthroughSubject<Int, Never>()
let pub2 = PassthroughSubject<Int, Never>()
let pub3 = PassthroughSubject<Int, Never>()

cancellable = pub
    .combineLatest(pub2, pub3) { firstValue, secondValue, thirdValue in
        return firstValue * secondValue * thirdValue
    }
    .sink { print("Result: \($0).") }

pub.send(1)
pub.send(2)
pub2.send(2)
pub3.send(10)

pub.send(9)
pub3.send(4)
pub2.send(12)

// Prints:
//  Result: 40.     // pub = 2, pub2 = 2, pub3 = 10
//  Result: 180.    // pub = 9, pub2 = 2, pub3 = 10
//  Result: 72.     // pub = 9, pub2 = 2, pub3 = 4
//  Result: 432.    // pub = 9, pub2 = 12, pub3 = 4
```

## See Also

### Collecting and republishing the latest elements from multiple publishers

- [combineLatest(_:_:)](<combinelatest(____)-1n30g.md>) — Subscribes to an additional publisher and invokes a closure upon receiving output from either publisher.
- [combineLatest(_:)](<combinelatest(__).md>) — Subscribes to an additional publisher and publishes a tuple upon receiving output from either publisher.
- [combineLatest(_:_:)](<combinelatest(____)-5crqg.md>) — Subscribes to two additional publishers and publishes a tuple upon receiving output from any of the publishers.
- [combineLatest(_:_:_:_:)](<combinelatest(________).md>) — Subscribes to three additional publishers and invokes a closure upon receiving output from any of the publishers.
- [combineLatest(_:_:_:)](<combinelatest(______)-48buc.md>) — Subscribes to three additional publishers and publishes a tuple upon receiving output from any of the publishers.
