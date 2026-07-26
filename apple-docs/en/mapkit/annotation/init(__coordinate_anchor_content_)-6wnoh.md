---
title: 'init(_:coordinate:anchor:content:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/annotation/init(_:coordinate:anchor:content:)-6wnoh'
source_url: 'https://developer.apple.com/documentation/mapkit/annotation/init(_:coordinate:anchor:content:)-6wnoh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/annotation/init%28_%3Acoordinate%3Aanchor%3Acontent%3A%29-6wnoh.json'
content_hash: 'sha256:616b53f099afc3c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [Annotation](../annotation.md)

# init(_:coordinate:anchor:content:)

<sub>Initializer</sub>

Creates an annotation that displays a view at a coordinate on the map using a title key, coordinate, anchor location, and view you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init<S>(_ title: S, coordinate: CLLocationCoordinate2D, anchor: UnitPoint = .center, @ViewBuilder content: () -> Content) where Label == Text, S : StringProtocol
```

## Parameters

- `title` — The title of the annotation.

- `coordinate` — The coordinate position of the annotation.

- `anchor` — A [UnitPoint](../../swiftui/unitpoint.md) value that indicates how to position the content around the provided coordinate.

- `content` — The view to place on the map.

## See Also

### Creating annotations

- [init(_:coordinate:anchor:accessoryAnchor:content:)](<init(__coordinate_anchor_accessoryanchor_content_)-6rxmn.md>) — Creates an annotation that displays a view at a coordinate on the map.
- [init(_:coordinate:anchor:accessoryAnchor:content:)](<init(__coordinate_anchor_accessoryanchor_content_)-14m3t.md>) — Creates an annotation that displays a view at a coordinate on the map.
- [init(coordinate:anchor:accessoryAnchor:content:label:)](<init(coordinate_anchor_accessoryanchor_content_label_).md>) — Creates an annotation that displays a view at a coordinate on the map.
- [init(item:anchor:accessoryAnchor:content:)](<init(item_anchor_accessoryanchor_content_).md>) — Creates an annotation that displays a view at a coordinate on the map.
- [init(_:coordinate:anchor:content:)](<init(__coordinate_anchor_content_)-2w242.md>) — Creates an annotation that displays a view at a coordinate on the map.
- [init(coordinate:anchor:content:label:)](<init(coordinate_anchor_content_label_).md>) — Creates an annotation that displays a view on the map using coordinates, anchor location, view, and label you provide.
