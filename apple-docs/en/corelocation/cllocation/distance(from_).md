---
title: 'distance(from:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocation/distance(from:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocation/distance(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocation/distance%28from%3A%29.json'
content_hash: 'sha256:4daf53e461712d84'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocation](../cllocation.md)

# distance(from:)

<sub>Instance Method</sub>

Returns the distance (measured in meters) from the current object’s location to the specified location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func distance(from location: CLLocation) -> CLLocationDistance
```

## Parameters

- `location` — The destination location.

## Return Value

The distance (in meters) between the two locations.

## Discussion

This method measures the distance between the location in the current object and the value in the `location` parameter. The distance is calculated by tracing a line between the two points that follows the curvature of the Earth, and measuring the length of the resulting arc. The arc is a smooth curve that doesn’t take into account altitude changes between the two locations.

## See Also

### Measuring the distance between coordinates

- [- getDistanceFrom:](<getdistancefrom(__).md>) — Returns the distance (measured in meters) from the current object’s location to the specified location. _(deprecated)_
