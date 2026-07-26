---
title: 'init(_:coordinate:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/marker/init(_:coordinate:)-3bjj6'
source_url: 'https://developer.apple.com/documentation/mapkit/marker/init(_:coordinate:)-3bjj6'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/marker/init%28_%3Acoordinate%3A%29-3bjj6.json'
content_hash: 'sha256:d53780dcff9bcdcb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [Marker](../marker.md)

# init(_:coordinate:)

<sub>Initializer</sub>

Creates a marker at the given location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(_ titleResource: LocalizedStringResource, coordinate: CLLocationCoordinate2D) where Label == Text
```

## Parameters

- `titleResource` — The localized string for the title.

- `coordinate` — The coordinate to display the marker at.
