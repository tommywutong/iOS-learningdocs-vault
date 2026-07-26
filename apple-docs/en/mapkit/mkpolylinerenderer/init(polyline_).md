---
title: 'init(polyline:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkpolylinerenderer/init(polyline:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkpolylinerenderer/init(polyline:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkpolylinerenderer/init%28polyline%3A%29.json'
content_hash: 'sha256:09f2d9cb8393f393'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKPolylineRenderer](../mkpolylinerenderer.md)

# init(polyline:)

<sub>Initializer</sub>

Creates a new overlay view using the specified polyline overlay object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(polyline: MKPolyline)
```

## Parameters

- `polyline` — The polyline overlay containing information about the area the renderer draws. This object requires at least two points defining the line segment to draw. This parameter can’t be `nil`.

## Return Value

An initialized polyline renderer object.
