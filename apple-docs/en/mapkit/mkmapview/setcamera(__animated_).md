---
title: 'setCamera(_:animated:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapview/setcamera(_:animated:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/setcamera(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/setcamera%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:b5afcf394adb1493'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# setCamera(_:animated:)

<sub>Instance Method</sub>

Changes the camera to use for determining the map’s viewing parameters, and optionally animates the change.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setCamera(_ camera: MKMapCamera, animated: Bool)
```

## Parameters

- `camera` — The camera object containing the viewing angle information. This parameter can’t be `nil`.

- `animated` — Specify [true](../../swift/true.md) if you want the map view to animate the change in viewing angle, or [false](../../swift/false.md) if you want the map to reflect the changes without animations.

## See Also

### Configuring the map display

- [camera](camera.md) — The camera to use for determining the appearance of the map.
- [showsCompass](showscompass.md) — A Boolean value that indicates whether the map displays a compass control.
- [showsPitchControl](showspitchcontrol.md) — A Boolean value that indicates whether the map displays the pitch control.
- [showsScale](showsscale.md) — A Boolean value that indicates whether the map shows scale information.
- [showsZoomControls](showszoomcontrols.md) — A Boolean value that indicates whether the map displays zoom controls.
- [showsBuildings](showsbuildings.md) — A Boolean value that indicates whether the map displays extruded building information on supported map types. _(deprecated)_
- [showsPointsOfInterest](showspointsofinterest.md) — A Boolean value that indicates whether the map displays point-of-interest information. _(deprecated)_
- [pointOfInterestFilter](pointofinterestfilter.md) — The filter to use for determining the points of interest that appear on the map. _(deprecated)_
- [showsTraffic](showstraffic.md) — A Boolean value that indicates whether the map displays traffic information. _(deprecated)_
