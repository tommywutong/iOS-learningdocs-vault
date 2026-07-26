---
title: 'init(polygon:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkpolygonrenderer/init(polygon:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkpolygonrenderer/init(polygon:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkpolygonrenderer/init%28polygon%3A%29.json'
content_hash: 'sha256:90df8dd94002b5b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKPolygonRenderer](../mkpolygonrenderer.md)

# init(polygon:)

<sub>Initializer</sub>

Creates a new renderer that handles drawing for the specified polygon overlay object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(polygon: MKPolygon)
```

## Parameters

- `polygon` — The polygon overlay containing information about the area the polygon renderer draws. This object requires at least three points defining the polygon to draw. This parameter can’t be `nil`.

## Return Value

An initialized polygon renderer object.
