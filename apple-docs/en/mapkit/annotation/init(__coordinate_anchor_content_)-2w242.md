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
doc_path: '/documentation/mapkit/annotation/init(_:coordinate:anchor:content:)-2w242'
source_url: 'https://developer.apple.com/documentation/mapkit/annotation/init(_:coordinate:anchor:content:)-2w242'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/annotation/init%28_%3Acoordinate%3Aanchor%3Acontent%3A%29-2w242.json'
content_hash: 'sha256:7059be8308c55a9a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [Annotation](../annotation.md)

# init(_:coordinate:anchor:content:)

<sub>Initializer</sub>

Creates an annotation that displays a view at a coordinate on the map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(_ titleKey: LocalizedStringKey, coordinate: CLLocationCoordinate2D, anchor: UnitPoint = .center, @ViewBuilder content: () -> Content) where Label == Text
```

## Parameters

- `titleKey` — The localized string key to use to look up the title.

- `coordinate` — The coordinate position of the annotation.

- `anchor` — A [UnitPoint](../../swiftui/unitpoint.md) value that indicates how to position the content around the provided coordinate.

- `content` — The view to place on the map.

## See Also

### Creating annotations

- [init(_:coordinate:anchor:accessoryAnchor:content:)](<init(__coordinate_anchor_accessoryanchor_content_)-6rxmn.md>) — Creates an annotation that displays a view at a coordinate on the map.
- [init(_:coordinate:anchor:accessoryAnchor:content:)](<init(__coordinate_anchor_accessoryanchor_content_)-14m3t.md>) — Creates an annotation that displays a view at a coordinate on the map.
- [init(coordinate:anchor:accessoryAnchor:content:label:)](<init(coordinate_anchor_accessoryanchor_content_label_).md>) — Creates an annotation that displays a view at a coordinate on the map.
- [init(item:anchor:accessoryAnchor:content:)](<init(item_anchor_accessoryanchor_content_).md>) — Creates an annotation that displays a view at a coordinate on the map.
- [init(_:coordinate:anchor:content:)](<init(__coordinate_anchor_content_)-6wnoh.md>) — Creates an annotation that displays a view at a coordinate on the map using a title key, coordinate, anchor location, and view you provide.
- [init(coordinate:anchor:content:label:)](<init(coordinate_anchor_content_label_).md>) — Creates an annotation that displays a view on the map using coordinates, anchor location, view, and label you provide.
