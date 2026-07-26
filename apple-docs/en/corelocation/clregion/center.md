---
title: center
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.7+（10.10 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/clregion/center
source_url: 'https://developer.apple.com/documentation/corelocation/clregion/center'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clregion/center.json'
content_hash: 'sha256:a238ab09efe98e45'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLRegion](../clregion.md)

# center

<sub>Instance Property</sub>

The center point of the region.

> [!warning] Deprecated
> Use [center](../clcircularregion/center.md) in [CLCircularRegion](../clcircularregion.md) instead.

<sub>macOS, watchOS</sub>

```swift
var center: CLLocationCoordinate2D { get }
```

## Discussion

In iOS, use a [CLCircularRegion](../clcircularregion.md) object to manage geographic regions.

## See Also

### Deprecated

- [- initCircularRegionWithCenter:radius:identifier:](<init(circularregionwithcenter_radius_identifier_).md>) — Initializes and returns a region object defining a circular area. _(deprecated)_
- [- containsCoordinate:](<contains(__).md>) — Returns a Boolean value indicating whether the region contains the specified coordinate. _(deprecated)_
- [radius](radius.md) — The radius (measured in meters) that defines the region’s outer boundary. _(deprecated)_
