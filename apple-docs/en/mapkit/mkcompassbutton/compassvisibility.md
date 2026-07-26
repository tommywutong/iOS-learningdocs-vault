---
title: compassVisibility
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkcompassbutton/compassvisibility
source_url: 'https://developer.apple.com/documentation/mapkit/mkcompassbutton/compassvisibility'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkcompassbutton/compassvisibility.json'
content_hash: 'sha256:4478932f296879d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKCompassButton](../mkcompassbutton.md)

# compassVisibility

<sub>Instance Property</sub>

The visibility of the compass button.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var compassVisibility: MKFeatureVisibility { get set }
```

## Discussion

You can configure a compass button to be visible all the time or only when the compass heading changes.

## See Also

### Getting the compass attributes

- [mapView](mapview.md) — The map view that provides the heading information for the compass button.
- [MKFeatureVisibility](../mkfeaturevisibility.md) — Constants that indicate the visibility of different map features.
