---
title: legendAlignment
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkscaleview/legendalignment
source_url: 'https://developer.apple.com/documentation/mapkit/mkscaleview/legendalignment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkscaleview/legendalignment.json'
content_hash: 'sha256:f2f8b1363062cdeb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKScaleView](../mkscaleview.md)

# legendAlignment

<sub>Instance Property</sub>

The alignment of the distance information in the scale view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var legendAlignment: MKScaleView.Alignment { get set }
```

## Discussion

This property determines whether measurements start at the leading or trailing edge of the view. The default value of this property is [MKScaleViewAlignmentLeading](alignment/leading.md).

## See Also

### Getting the scale view attributes

- [mapView](mapview.md) — The map view that provides the scale information to the scale view.
- [scaleVisibility](scalevisibility.md) — The visibility of the scale view.
- [Alignment](alignment.md) — Constants that indicate how the framework should align measurements.
