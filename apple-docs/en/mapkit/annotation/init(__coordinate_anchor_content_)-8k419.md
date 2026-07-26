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
doc_path: '/documentation/mapkit/annotation/init(_:coordinate:anchor:content:)-8k419'
source_url: 'https://developer.apple.com/documentation/mapkit/annotation/init(_:coordinate:anchor:content:)-8k419'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/annotation/init%28_%3Acoordinate%3Aanchor%3Acontent%3A%29-8k419.json'
content_hash: 'sha256:c955b9b7b2c8b12d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [Annotation](../annotation.md)

# init(_:coordinate:anchor:content:)

<sub>Initializer</sub>

Creates an annotation that displays a view at a coordinate on the map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(_ titleResource: LocalizedStringResource, coordinate: CLLocationCoordinate2D, anchor: UnitPoint = .center, @ViewBuilder content: () -> Content) where Label == Text
```

## Parameters

- `titleResource` — The localized string for the title.

- `coordinate` — The coordinate to display the annotation at.

- `anchor` — How to place the content around the provided coordinate.

- `content` — The view to place on the map.

## Discussion

Uses `.center` for `accessoryAnchor`. For greater control of selection accessory positioning, please use an initializer with an `accessoryAnchor` parameter.
