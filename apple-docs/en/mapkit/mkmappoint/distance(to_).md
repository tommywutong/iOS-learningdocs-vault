---
title: 'distance(to:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmappoint/distance(to:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmappoint/distance(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmappoint/distance%28to%3A%29.json'
content_hash: 'sha256:0f5c9155716a3ffb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapPoint](../mkmappoint.md)

# distance(to:)

<sub>Instance Method</sub>

Returns the number of meters between two map points.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func distance(to b: MKMapPoint) -> CLLocationDistance
```

## Parameters

- `b` — The second map point.

## Return Value

The number of meters between the specified map points.

## Discussion

This distance reflects the actual distance between the two points on the surface of the globe, taking into account the curvature of the Earth.

## See Also

### Getting the distance between points

- [MKMetersPerMapPointAtLatitude](<../mkmeterspermappointatlatitude(__).md>) — Returns the distance that one map point spans at the specified latitude.
- [MKMapPointsPerMeterAtLatitude](<../mkmappointspermeteratlatitude(__).md>) — Returns the number of map points that represent one meter at the specified latitude.
