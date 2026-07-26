---
title: 'init(mapItem:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapitemannotation/init(mapitem:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapitemannotation/init(mapitem:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapitemannotation/init%28mapitem%3A%29.json'
content_hash: 'sha256:6e9c32c94f3d5458'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapItemAnnotation](../mkmapitemannotation.md)

# init(mapItem:)

<sub>Initializer</sub>

Creates a map item annotation

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init?(mapItem: MKMapItem)
```

## Parameters

- `mapItem` — The map item this annotation will represent

## Discussion

If the map item does not have valid coordinate data, the result will be nil.
