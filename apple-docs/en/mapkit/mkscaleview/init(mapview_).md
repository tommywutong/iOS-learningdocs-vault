---
title: 'init(mapView:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkscaleview/init(mapview:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkscaleview/init(mapview:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkscaleview/init%28mapview%3A%29.json'
content_hash: 'sha256:14d5749b2c26a968'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKScaleView](../mkscaleview.md)

# init(mapView:)

<sub>Initializer</sub>

Creates a scale view and associates it with the specified map view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(mapView: MKMapView?)
```

## Parameters

- `mapView` — The map to associate with the scale view. The scale view automatically updates to reflect the scale of this map.

## Return Value

An initialized scale view.
