---
title: 'MKRoadWidthAtZoomScale(_:)'
framework: MapKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkroadwidthatzoomscale(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkroadwidthatzoomscale(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkroadwidthatzoomscale%28_%3A%29.json'
content_hash: 'sha256:9733b4887c2a6c57'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKRoadWidthAtZoomScale(_:)

<sub>Function</sub>

Returns the width (in screen points) of roads on a map at the specified zoom level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func MKRoadWidthAtZoomScale(_ zoomScale: MKZoomScale) -> CGFloat
```

## Parameters

- `zoomScale` — The scale factor currently applied to the map view.

## Return Value

The width of roads, measured in screen points. You can use the returned value to set the width of lines in drawing code that traces the path of a road.

## See Also

### Types

- [MKZoomScale](mkzoomscale.md) — A scale factor to use in conjunction with a map.
