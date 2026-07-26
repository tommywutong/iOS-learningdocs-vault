---
title: switchToLatest()
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publisher/switchtolatest()-1c51y
source_url: 'https://developer.apple.com/documentation/combine/publisher/switchtolatest()-1c51y'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/switchtolatest%28%29-1c51y.json'
content_hash: 'sha256:c08b0c3f2fb0c40f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# switchToLatest()

<sub>Instance Method</sub>

Republishes elements sent by the most recently received publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func switchToLatest() -> Publishers.SwitchToLatest<Self.Output, Publishers.SetFailureType<Self, Self.Output.Failure>>
```

## Discussion

This operator works with an upstream publisher of publishers, flattening the stream of elements to appear as if they were coming from a single stream of elements. It switches the inner publisher as new ones arrive but keeps the outer publisher constant for downstream subscribers.

When this operator receives a new publisher from the upstream publisher, it cancels its previous subscription. Use this feature to prevent earlier publishers from performing unnecessary work, such as creating network request publishers from frequently updating user interface publishers.

## See Also

### Republishing elements by subscribing to new publishers

- [flatMap(maxPublishers:_:)](<flatmap(maxpublishers___)-3k7z5.md>) — Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [flatMap(maxPublishers:_:)](<flatmap(maxpublishers___)-qxf.md>) — Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [flatMap(maxPublishers:_:)](<flatmap(maxpublishers___)-hyb0.md>) — Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [flatMap(maxPublishers:_:)](<flatmap(maxpublishers___)-4of8w.md>) — Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [switchToLatest()](<switchtolatest()-453ht.md>) — Republishes elements sent by the most recently received publisher.
- [switchToLatest()](<switchtolatest()-20v3t.md>) — Republishes elements sent by the most recently received publisher.
- [switchToLatest()](<switchtolatest()-9eb3r.md>) — Republishes elements sent by the most recently received publisher.
