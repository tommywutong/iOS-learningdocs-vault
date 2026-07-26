---
title: 'MKMapPointsPerMeterAtLatitude(_:)'
framework: MapKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmappointspermeteratlatitude(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmappointspermeteratlatitude(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmappointspermeteratlatitude%28_%3A%29.json'
content_hash: 'sha256:8e9dae48c49de75a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKMapPointsPerMeterAtLatitude(_:)

<sub>Function</sub>

Returns the number of map points that represent one meter at the specified latitude.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func MKMapPointsPerMeterAtLatitude(_ latitude: CLLocationDegrees) -> Double
```

## Parameters

- `latitude` — The latitude for which to return the value.

## Return Value

The number of map points that span one meter.

## Discussion

The number of map points per meter increases as the latitude approaches the poles.

## See Also

### Getting the distance between points

- [MKMetersBetweenMapPoints](<mkmappoint/distance(to_).md>) — Returns the number of meters between two map points.
- [MKMetersPerMapPointAtLatitude](<mkmeterspermappointatlatitude(__).md>) — Returns the distance that one map point spans at the specified latitude.
