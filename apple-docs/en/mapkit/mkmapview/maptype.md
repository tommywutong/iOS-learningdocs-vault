---
title: mapType
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（27.0 起废弃）, iPadOS 3.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.9+（27.0 起废弃）, tvOS 9.2+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkmapview/maptype
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapview/maptype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapview/maptype.json'
content_hash: 'sha256:f2c2783db338cd28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapView](../mkmapview.md)

# mapType

<sub>Instance Property</sub>

The type of data the map view displays.

> [!warning] Deprecated
> Use the map view’s [preferredConfiguration](preferredconfiguration.md) property with an [MKMapConfiguration](../mkmapconfiguration.md) subclass to specify how the framework presents the map instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var mapType: MKMapType { get set }
```

## Discussion

Changing the value in this property may cause the receiver to begin loading new map content. For example, changing from [MKMapTypeStandard](../mkmaptype/standard.md) to [MKMapTypeSatellite](../mkmaptype/satellite.md) might cause it to begin loading the satellite imagery for the map. If the map needs new data, however, it loads asynchronously and MapKit sends appropriate messages to the receiver’s delegate indicating the status of the operation.

## See Also

### Related Documentation

- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)

### Accessing map properties

- [MKMapType](../mkmaptype.md) — The type of map to display. _(deprecated)_
- [zoomEnabled](iszoomenabled.md) — A Boolean value that determines whether the user may use pinch gestures to zoom in and out of the map.
- [scrollEnabled](isscrollenabled.md) — A Boolean value that determines whether the user may scroll around the map.
- [pitchEnabled](ispitchenabled.md) — A Boolean value that indicates whether the map uses the camera’s pitch information.
- [rotateEnabled](isrotateenabled.md) — A Boolean value that indicates whether the map uses the camera’s heading information.
