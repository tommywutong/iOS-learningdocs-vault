---
title: pitchButtonVisibility
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapview/pitchbuttonvisibility
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/pitchbuttonvisibility'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/pitchbuttonvisibility.json'
content_hash: 'sha256:8ddd721f0402c48b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# pitchButtonVisibility

<sub>Instance Property</sub>

A value that indicates whether the map’s pitch button is visible.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var pitchButtonVisibility: MKFeatureVisibility { get set }
```

## Discussion

Use this button to display or hide a button that allows a person to set the map to a pleasing pitch or return the map to a flat appearance.

## See Also

### Configuring the map appearance

- [preferredConfiguration](preferredconfiguration.md) — The characteristics of the map view, including the map type and features the map displays.
- [showsUserTrackingButton](showsusertrackingbutton.md) — A Boolean value that indicates whether the map displays the user tracking button.
- [MKMapConfiguration](../mkmapconfiguration.md) — An abstract class that represents the shared elements of map configurations.
- [MKStandardMapConfiguration](../mkstandardmapconfiguration.md) — The class that represents the default map presentation, which is a street map that shows the position of all roads and some road names.
- [MKHybridMapConfiguration](../mkhybridmapconfiguration.md) — The class that represents a satellite image of the area with road and road name information layers on top.
- [MKImageryMapConfiguration](../mkimagerymapconfiguration.md) — The class that represents an imagery-based map presentation, such as one using satellite imagery.
