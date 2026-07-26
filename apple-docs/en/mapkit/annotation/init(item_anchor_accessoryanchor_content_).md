---
title: 'init(item:anchor:accessoryAnchor:content:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/annotation/init(item:anchor:accessoryanchor:content:)'
source_url: 'https://developer.apple.com/documentation/mapkit/annotation/init(item:anchor:accessoryanchor:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/annotation/init%28item%3Aanchor%3Aaccessoryanchor%3Acontent%3A%29.json'
content_hash: 'sha256:8565c347c10c7728'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [Annotation](../annotation.md)

# init(item:anchor:accessoryAnchor:content:)

<sub>Initializer</sub>

Creates an annotation that displays a view at a coordinate on the map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(item: MKMapItem, anchor: UnitPoint = .center, accessoryAnchor: UnitPoint = .center, @ViewBuilder content: () -> Content) where Label == Text
```

## Parameters

- `item` — A map item that provides a label and coordinate for the annotation.

- `anchor` — A [UnitPoint](../../swiftui/unitpoint.md) value that indicates how to position the content around the provided coordinate.

- `accessoryAnchor` — A [UnitPoint](../../swiftui/unitpoint.md) value that indicates how to place accessories around the provided content.

- `content` — The view to place on the map.

## See Also

### Creating annotations

- [init(_:coordinate:anchor:accessoryAnchor:content:)](<init(__coordinate_anchor_accessoryanchor_content_)-6rxmn.md>) — Creates an annotation that displays a view at a coordinate on the map.
- [init(_:coordinate:anchor:accessoryAnchor:content:)](<init(__coordinate_anchor_accessoryanchor_content_)-14m3t.md>) — Creates an annotation that displays a view at a coordinate on the map.
- [init(coordinate:anchor:accessoryAnchor:content:label:)](<init(coordinate_anchor_accessoryanchor_content_label_).md>) — Creates an annotation that displays a view at a coordinate on the map.
- [init(_:coordinate:anchor:content:)](<init(__coordinate_anchor_content_)-2w242.md>) — Creates an annotation that displays a view at a coordinate on the map.
- [init(_:coordinate:anchor:content:)](<init(__coordinate_anchor_content_)-6wnoh.md>) — Creates an annotation that displays a view at a coordinate on the map using a title key, coordinate, anchor location, and view you provide.
- [init(coordinate:anchor:content:label:)](<init(coordinate_anchor_content_label_).md>) — Creates an annotation that displays a view on the map using coordinates, anchor location, view, and label you provide.
