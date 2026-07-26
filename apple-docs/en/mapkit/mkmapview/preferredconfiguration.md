---
title: preferredConfiguration
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapview/preferredconfiguration
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/preferredconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/preferredconfiguration.json'
content_hash: 'sha256:b73eb6831d9f6696'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# preferredConfiguration

<sub>Instance Property</sub>

The characteristics of the map view, including the map type and features the map displays.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@NSCopying var preferredConfiguration: MKMapConfiguration { get set }
```

## See Also

### Configuring the map appearance

- [pitchButtonVisibility](pitchbuttonvisibility.md) — A value that indicates whether the map’s pitch button is visible.
- [showsUserTrackingButton](showsusertrackingbutton.md) — A Boolean value that indicates whether the map displays the user tracking button.
- [MKMapConfiguration](../mkmapconfiguration.md) — An abstract class that represents the shared elements of map configurations.
- [MKStandardMapConfiguration](../mkstandardmapconfiguration.md) — The class that represents the default map presentation, which is a street map that shows the position of all roads and some road names.
- [MKHybridMapConfiguration](../mkhybridmapconfiguration.md) — The class that represents a satellite image of the area with road and road name information layers on top.
- [MKImageryMapConfiguration](../mkimagerymapconfiguration.md) — The class that represents an imagery-based map presentation, such as one using satellite imagery.
