---
title: 'init(circularRegionWithCenter:radius:identifier:)'
framework: Core Location
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.7+（10.10 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corelocation/clregion/init(circularregionwithcenter:radius:identifier:)'
source_url: 'https://developer.apple.com/documentation/corelocation/clregion/init(circularregionwithcenter:radius:identifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clregion/init%28circularregionwithcenter%3Aradius%3Aidentifier%3A%29.json'
content_hash: 'sha256:269e5ed542ebe61f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLRegion](../clregion.md)

# init(circularRegionWithCenter:radius:identifier:)

<sub>Initializer</sub>

Initializes and returns a region object defining a circular area.

> [!warning] Deprecated
> Use [- initWithCenter:radius:identifier:](<../clcircularregion/init(center_radius_identifier_).md>) in [CLCircularRegion](../clcircularregion.md) instead.

<sub>macOS, watchOS</sub>

```swift
init(circularRegionWithCenter center: CLLocationCoordinate2D, radius: CLLocationDistance, identifier: String)
```

## Parameters

- `center` — The center point of the region.

- `radius` — The distance (measured in meters) from the center point that marks the boundary of the region.

- `identifier` — A unique identifier to associate with the region object. You use this identifier to differentiate regions within your application. This value must not be `nil`.

## Return Value

An initialized region object.

## Discussion

In iOS, use a [CLCircularRegion](../clcircularregion.md) object to manage geographic regions.

## See Also

### Deprecated

- [- containsCoordinate:](<contains(__).md>) — Returns a Boolean value indicating whether the region contains the specified coordinate. _(deprecated)_
- [center](center.md) — The center point of the region. _(deprecated)_
- [radius](radius.md) — The radius (measured in meters) that defines the region’s outer boundary. _(deprecated)_
