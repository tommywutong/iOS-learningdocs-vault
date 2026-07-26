---
title: 'MKMetersPerMapPointAtLatitude(_:)'
framework: MapKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmeterspermappointatlatitude(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmeterspermappointatlatitude(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmeterspermappointatlatitude%28_%3A%29.json'
content_hash: 'sha256:75d473f0a96f49e5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKMetersPerMapPointAtLatitude(_:)

<sub>Function</sub>

Returns the distance that one map point spans at the specified latitude.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func MKMetersPerMapPointAtLatitude(_ latitude: CLLocationDegrees) -> CLLocationDistance
```

## Parameters

- `latitude` — The latitude for which to return the value.

## Return Value

The distance (in meters) spanned by a single map point.

## Discussion

The distance between map points decreases as the latitude approaches the poles. This relationship parallels the relationship between longitudinal coordinates at different latitudes.

## See Also

### Getting the distance between points

- [MKMetersBetweenMapPoints](<mkmappoint/distance(to_).md>) — Returns the number of meters between two map points.
- [MKMapPointsPerMeterAtLatitude](<mkmappointspermeteratlatitude(__).md>) — Returns the number of map points that represent one meter at the specified latitude.
