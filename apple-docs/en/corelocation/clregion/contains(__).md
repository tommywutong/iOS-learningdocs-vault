---
title: 'contains(_:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.7+（10.10 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corelocation/clregion/contains(_:)'
source_url: 'https://developer.apple.com/documentation/corelocation/clregion/contains(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clregion/contains%28_%3A%29.json'
content_hash: 'sha256:5d468a462b43168d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLRegion](../clregion.md)

# contains(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the region contains the specified coordinate.

> [!warning] Deprecated
> Use [- containsCoordinate:](<../clcircularregion/contains(__).md>) in [CLCircularRegion](../clcircularregion.md) instead.

<sub>macOS, watchOS</sub>

```swift
func contains(_ coordinate: CLLocationCoordinate2D) -> Bool
```

## Parameters

- `coordinate` — The coordinate to test against the region.

## Return Value

[true](../../swift/true.md) if the coordinate lies within the region’s boundaries or [false](../../swift/false.md) if it does not.

## Discussion

In iOS, use a [CLCircularRegion](../clcircularregion.md) object to manage geographic regions.

## See Also

### Deprecated

- [- initCircularRegionWithCenter:radius:identifier:](<init(circularregionwithcenter_radius_identifier_).md>) — Initializes and returns a region object defining a circular area. _(deprecated)_
- [center](center.md) — The center point of the region. _(deprecated)_
- [radius](radius.md) — The radius (measured in meters) that defines the region’s outer boundary. _(deprecated)_
