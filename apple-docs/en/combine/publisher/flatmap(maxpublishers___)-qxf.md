---
title: 'flatMap(maxPublishers:_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/flatmap(maxpublishers:_:)-qxf'
source_url: 'https://developer.apple.com/documentation/combine/publisher/flatmap(maxpublishers:_:)-qxf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/flatmap%28maxpublishers%3A_%3A%29-qxf.json'
content_hash: 'sha256:0d46e41d36d3ced7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# flatMap(maxPublishers:_:)

<sub>Instance Method</sub>

Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func flatMap<P>(maxPublishers: Subscribers.Demand = .unlimited, _ transform: @escaping (Self.Output) -> P) -> Publishers.FlatMap<P, Publishers.SetFailureType<Self, P.Failure>> where P : Publisher
```

## Parameters

- `maxPublishers` — Specifies the maximum number of concurrent publisher subscriptions, or [unlimited](../subscribers/demand/unlimited.md) if unspecified.

- `transform` — A closure that takes an element as a parameter and returns a publisher that produces elements of that type.

## Return Value

A publisher that transforms elements from an upstream  publisher into a publisher of that element’s type.

## See Also

### Republishing elements by subscribing to new publishers

- [flatMap(maxPublishers:_:)](<flatmap(maxpublishers___)-3k7z5.md>) — Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [flatMap(maxPublishers:_:)](<flatmap(maxpublishers___)-hyb0.md>) — Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [flatMap(maxPublishers:_:)](<flatmap(maxpublishers___)-4of8w.md>) — Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [switchToLatest()](<switchtolatest()-453ht.md>) — Republishes elements sent by the most recently received publisher.
- [switchToLatest()](<switchtolatest()-1c51y.md>) — Republishes elements sent by the most recently received publisher.
- [switchToLatest()](<switchtolatest()-20v3t.md>) — Republishes elements sent by the most recently received publisher.
- [switchToLatest()](<switchtolatest()-9eb3r.md>) — Republishes elements sent by the most recently received publisher.
