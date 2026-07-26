---
title: 'tag(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapcontent/tag(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapcontent/tag(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcontent/tag%28_%3A%29.json'
content_hash: 'sha256:0a9fbd2c0cbc4477'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapContent](../mapcontent.md)

# tag(_:)

<sub>Instance Method</sub>

Sets the unique tag value of this piece of map content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func tag<V>(_ tag: V) -> some MapContent where V : Hashable

```

## Parameters

- `tag` — A [Hashable](../../swift/hashable.md) value to use as the map content’s tag.

## Return Value

Map content with the specified tag set.

## Discussion

Use this modifier to differentiate between selectable content in the map. When the map’s selection binding has the same value as the tag applied to a piece of map content, that content is considered selected.

A `ForEach` automatically applies a default tag to each enumerated view using the `id` parameter of the corresponding element. If the element’s `id` parameter and the the map’s selection input have the same type, you can omit the explicit tag modifier.
