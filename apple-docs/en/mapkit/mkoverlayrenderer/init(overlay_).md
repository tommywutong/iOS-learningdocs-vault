---
title: 'init(overlay:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkoverlayrenderer/init(overlay:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/init(overlay:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkoverlayrenderer/init%28overlay%3A%29.json'
content_hash: 'sha256:bde36f443cc5c431'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKOverlayRenderer](../mkoverlayrenderer.md)

# init(overlay:)

<sub>Initializer</sub>

Creates and returns the overlay renderer and associates it with the specified overlay object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(overlay: any MKOverlay)
```

## Parameters

- `overlay` — The overlay object to use when drawing the overlay content on the map. This object provides the data needed to draw the overlay’s shape. The overlay renderer stores a strong reference to this object.

## Return Value

An initialized overlay renderer object.

## Discussion

Initially, the overlay renderer assumes that the overlay is fully opaque and that it has a content scale factor of 1.0. You can change these values as needed using the [alpha](alpha.md) and [contentScaleFactor](contentscalefactor.md) properties.
