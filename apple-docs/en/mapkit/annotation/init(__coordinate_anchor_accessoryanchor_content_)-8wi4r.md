---
title: 'init(_:coordinate:anchor:accessoryAnchor:content:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/annotation/init(_:coordinate:anchor:accessoryanchor:content:)-8wi4r'
source_url: 'https://developer.apple.com/documentation/mapkit/annotation/init(_:coordinate:anchor:accessoryanchor:content:)-8wi4r'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/annotation/init%28_%3Acoordinate%3Aanchor%3Aaccessoryanchor%3Acontent%3A%29-8wi4r.json'
content_hash: 'sha256:c145fc87be3c9bcc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [Annotation](../annotation.md)

# init(_:coordinate:anchor:accessoryAnchor:content:)

<sub>Initializer</sub>

Creates an annotation that displays a view at a coordinate on the map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(_ titleResource: LocalizedStringResource, coordinate: CLLocationCoordinate2D, anchor: UnitPoint = .center, accessoryAnchor: UnitPoint, @ViewBuilder content: () -> Content) where Label == Text
```

## Parameters

- `titleResource` — The localized string for the title.

- `coordinate` — The coordinate to display the annotation at.

- `anchor` — How to place the content around the provided coordinate.

- `accessoryAnchor` — How to place accessories around the provided content.

- `content` — The view to place on the map.
