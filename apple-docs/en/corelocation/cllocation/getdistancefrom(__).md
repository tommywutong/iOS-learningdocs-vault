---
title: 'getDistanceFrom(_:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corelocation/cllocation/getdistancefrom(_:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocation/getdistancefrom(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocation/getdistancefrom%28_%3A%29.json'
content_hash: 'sha256:7421d55eec914b04'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocation](../cllocation.md)

# getDistanceFrom(_:)

<sub>Instance Method</sub>

Returns the distance (measured in meters) from the current object’s location to the specified location.

> [!warning] Deprecated
> Use the [- distanceFromLocation:](<distance(from_).md>) method instead.

<sub>macOS</sub>

```swift
func getDistanceFrom(_ location: CLLocation) -> CLLocationDistance
```

## Parameters

- `location` — The other location.

## Return Value

The distance (in meters) between the two locations.

## Discussion

This method measures the distance between the location in the current object and the value in the `location` parameter. The distance is calculated by tracing a line between the two points that follows the curvature of the Earth, and measuring the length of the resulting arc. The arc is a smooth curve that does not take into account altitude changes between the two locations.

## See Also

### Measuring the distance between coordinates

- [- distanceFromLocation:](<distance(from_).md>) — Returns the distance (measured in meters) from the current object’s location to the specified location.
