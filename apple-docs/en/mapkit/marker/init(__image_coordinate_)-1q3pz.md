---
title: 'init(_:image:coordinate:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/marker/init(_:image:coordinate:)-1q3pz'
source_url: 'https://developer.apple.com/documentation/mapkit/marker/init(_:image:coordinate:)-1q3pz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/marker/init%28_%3Aimage%3Acoordinate%3A%29-1q3pz.json'
content_hash: 'sha256:fc59b59ab73987c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [Marker](../marker.md)

# init(_:image:coordinate:)

<sub>Initializer</sub>

Creates a marker at the given location with an image displayed as the balloon’s icon.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(_ titleResource: LocalizedStringResource, image: String, coordinate: CLLocationCoordinate2D) where Label == Label<Text, Image>
```

## Parameters

- `titleResource` — The localized string for the title.

- `image` — The name of the image resource to look up and use as the marker balloon’s glyph.

- `coordinate` — The coordinate to display the marker at.
