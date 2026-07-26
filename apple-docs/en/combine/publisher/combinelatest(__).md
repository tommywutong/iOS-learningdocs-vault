---
title: 'combineLatest(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/combinelatest(_:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/combinelatest(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/combinelatest%28_%3A%29.json'
content_hash: 'sha256:abfa4421fb644230'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# combineLatest(_:)

<sub>Instance Method</sub>

Subscribes to an additional publisher and publishes a tuple upon receiving output from either publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func combineLatest<P>(_ other: P) -> Publishers.CombineLatest<Self, P> where P : Publisher, Self.Failure == P.Failure
```

## Parameters

- `other` — Another publisher to combine with this one.

## Return Value

A publisher that receives and combines elements from this and another publisher.

## Discussion

Use [combineLatest(_:)](<combinelatest(__).md>) when you want the downstream subscriber to receive a tuple of the most-recent element from multiple publishers when any of them emit a value. To pair elements from multiple publishers, use [zip(_:)](<zip(__).md>) instead. To receive just the most-recent element from multiple publishers rather than tuples, use [merge(with:)](<merge(with_)-7qt71.md>).

> [!tip] Tip
> The combined publisher doesn’t produce elements until each of its upstream publishers publishes at least one element.

The combined publisher passes through any requests to _all_ upstream publishers. However, it still obeys the demand-fulfilling rule of only sending the request amount downstream. If the demand isn’t [unlimited](../subscribers/demand/unlimited.md), it drops values from upstream publishers. It implements this by using a buffer size of 1 for each upstream, and holds the most-recent value in each buffer.

In this example, [PassthroughSubject](../passthroughsubject.md) `pub1` and also `pub2` emit values; as [combineLatest(_:)](<combinelatest(__).md>) receives input from either upstream publisher, it combines the latest value from each publisher into a tuple and publishes it.

```swift
let pub1 = PassthroughSubject<Int, Never>()
let pub2 = PassthroughSubject<Int, Never>()

cancellable = pub1
    .combineLatest(pub2)
    .sink { print("Result: \($0).") }

pub1.send(1)
pub1.send(2)
pub2.send(2)
pub1.send(3)
pub1.send(45)
pub2.send(22)

// Prints:
//    Result: (2, 2).    // pub1 latest = 2, pub2 latest = 2
//    Result: (3, 2).    // pub1 latest = 3, pub2 latest = 2
//    Result: (45, 2).   // pub1 latest = 45, pub2 latest = 2
//    Result: (45, 22).  // pub1 latest = 45, pub2 latest = 22
```

When all upstream publishers finish, this publisher finishes. If an upstream publisher never publishes a value, this publisher never finishes.

## See Also

### Collecting and republishing the latest elements from multiple publishers

- [combineLatest(_:_:)](<combinelatest(____)-1n30g.md>) — Subscribes to an additional publisher and invokes a closure upon receiving output from either publisher.
- [combineLatest(_:_:_:)](<combinelatest(______)-6ekpz.md>) — Subscribes to two additional publishers and invokes a closure upon receiving output from any of the publishers.
- [combineLatest(_:_:)](<combinelatest(____)-5crqg.md>) — Subscribes to two additional publishers and publishes a tuple upon receiving output from any of the publishers.
- [combineLatest(_:_:_:_:)](<combinelatest(________).md>) — Subscribes to three additional publishers and invokes a closure upon receiving output from any of the publishers.
- [combineLatest(_:_:_:)](<combinelatest(______)-48buc.md>) — Subscribes to three additional publishers and publishes a tuple upon receiving output from any of the publishers.
