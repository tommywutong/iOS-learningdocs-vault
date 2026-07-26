---
title: 'init(mapView:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkusertrackingbutton/init(mapview:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkusertrackingbutton/init(mapview:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkusertrackingbutton/init%28mapview%3A%29.json'
content_hash: 'sha256:9d596a3a55c9b1e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKUserTrackingButton](../mkusertrackingbutton.md)

# init(mapView:)

<sub>Initializer</sub>

Initializes the button with the map view that it should control.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
convenience init(mapView: MKMapView?)
```

## Parameters

- `mapView` — The mapView to associate with the button. Taps on the button change the appearance of this map view.

## Return Value

An initialized [MKUserTrackingButton](../mkusertrackingbutton.md) object.
