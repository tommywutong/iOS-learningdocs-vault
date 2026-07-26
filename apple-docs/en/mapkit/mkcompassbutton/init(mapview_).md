---
title: 'init(mapView:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkcompassbutton/init(mapview:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkcompassbutton/init(mapview:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkcompassbutton/init%28mapview%3A%29.json'
content_hash: 'sha256:fa966d80ed90b17a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKCompassButton](../mkcompassbutton.md)

# init(mapView:)

<sub>Initializer</sub>

Creates a compass button and associates it with the specified map view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
convenience init(mapView: MKMapView?)
```

## Parameters

- `mapView` — The map to associate with the compass button. The compass button reflects the orientation of this map, and tapping the button reorients the map appropriately.

## Return Value

An initialized compass button.
