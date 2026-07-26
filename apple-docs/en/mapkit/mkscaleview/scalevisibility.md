---
title: scaleVisibility
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkscaleview/scalevisibility
source_url: 'https://developer.apple.com/documentation/mapkit/mkscaleview/scalevisibility'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkscaleview/scalevisibility.json'
content_hash: 'sha256:fd49ab8173a090e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKScaleView](../mkscaleview.md)

# scaleVisibility

<sub>Instance Property</sub>

The visibility of the scale view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var scaleVisibility: MKFeatureVisibility { get set }
```

## Discussion

You can configure a scale view to be visible all the time or only when the scale of the map changes.

## See Also

### Getting the scale view attributes

- [mapView](mapview.md) — The map view that provides the scale information to the scale view.
- [legendAlignment](legendalignment.md) — The alignment of the distance information in the scale view.
- [Alignment](alignment.md) — Constants that indicate how the framework should align measurements.
