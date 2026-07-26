---
title: 'init(_:monogram:coordinate:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/marker/init(_:monogram:coordinate:)-77k4r'
source_url: 'https://developer.apple.com/documentation/mapkit/marker/init(_:monogram:coordinate:)-77k4r'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/marker/init%28_%3Amonogram%3Acoordinate%3A%29-77k4r.json'
content_hash: 'sha256:6bece459d9a9e6e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [Marker](../marker.md)

# init(_:monogram:coordinate:)

<sub>Initializer</sub>

Creates a marker at the given location with a monogram displayed as the balloon’s icon.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(_ titleResource: LocalizedStringResource, monogram: Text, coordinate: CLLocationCoordinate2D) where Label == Label<Text, Text>
```

## Parameters

- `titleResource` — The localized string for the title.

- `monogram` — Up to three characters to display on the marker’s balloon.

- `coordinate` — The coordinate to display the marker at.
