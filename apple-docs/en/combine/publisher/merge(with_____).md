---
title: 'merge(with:_:_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/merge(with:_:_:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/merge(with:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/merge%28with%3A_%3A_%3A%29.json'
content_hash: 'sha256:318e2d1b45c6d02f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# merge(with:_:_:)

<sub>Instance Method</sub>

Combines elements from this publisher with those from three other publishers, delivering an interleaved sequence of elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func merge<B, C, D>(with b: B, _ c: C, _ d: D) -> Publishers.Merge4<Self, B, C, D> where B : Publisher, C : Publisher, D : Publisher, Self.Failure == B.Failure, Self.Output == B.Output, B.Failure == C.Failure, B.Output == C.Output, C.Failure == D.Failure, C.Output == D.Output
```

## Parameters

- `b` — A second publisher.

- `c` — A third publisher.

- `d` — A fourth publisher.

## Return Value

A publisher that emits an event when any upstream publisher emits an event.

## Discussion

Use [merge(with:_:_:)](<merge(with_____).md>) when you want to receive a new element whenever any of the upstream publishers emits an element. To receive tuples of the most-recent value from all the upstream publishers whenever any of them emit a value, use [combineLatest(_:_:_:)](<combinelatest(______)-48buc.md>). To combine elements from multiple upstream publishers, use [zip(_:_:_:)](<zip(______)-16rcy.md>).

In this example, as [merge(with:_:_:)](<merge(with_____).md>) receives input from the upstream publishers, it republishes the interleaved elements to the downstream:

```swift
let pubA = PassthroughSubject<Int, Never>()
let pubB = PassthroughSubject<Int, Never>()
let pubC = PassthroughSubject<Int, Never>()
let pubD = PassthroughSubject<Int, Never>()

cancellable = pubA
    .merge(with: pubB, pubC, pubD)
    .sink { print("\($0)", terminator: " " )}

pubA.send(1)
pubB.send(40)
pubC.send(90)
pubD.send(-1)
pubA.send(2)
pubB.send(50)
pubC.send(100)
pubD.send(-2)

// Prints: "1 40 90 -1 2 50 100 -2 "
```

The merged publisher continues to emit elements until all upstream publishers finish. If an upstream publisher produces an error, the merged publisher fails with that error.

## See Also

### Republishing elements from multiple publishers as an interleaved stream

- [merge(with:)](<merge(with_)-7fk3a.md>) — Combines elements from this publisher with those from another publisher of the same type, delivering an interleaved sequence of elements.
- [merge(with:)](<merge(with_)-7qt71.md>) — Combines elements from this publisher with those from another publisher, delivering an interleaved sequence of elements.
- [merge(with:_:)](<merge(with___).md>) — Combines elements from this publisher with those from two other publishers, delivering an interleaved sequence of elements.
- [merge(with:_:_:_:)](<merge(with_______).md>) — Combines elements from this publisher with those from four other publishers, delivering an interleaved sequence of elements.
- [merge(with:_:_:_:_:)](<merge(with_________).md>) — Combines elements from this publisher with those from five other publishers, delivering an interleaved sequence of elements.
- [merge(with:_:_:_:_:_:)](<merge(with___________).md>) — Combines elements from this publisher with those from six other publishers, delivering an interleaved sequence of elements.
- [merge(with:_:_:_:_:_:_:)](<merge(with_____________).md>) — Combines elements from this publisher with those from seven other publishers, delivering an interleaved sequence of elements.
