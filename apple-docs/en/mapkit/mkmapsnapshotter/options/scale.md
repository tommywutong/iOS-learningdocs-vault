---
title: scale
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（27.0 起废弃）, iPadOS 7.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS 9.2+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkmapsnapshotter/options/scale
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/scale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapsnapshotter/options/scale.json'
content_hash: 'sha256:47f25c818c06c981'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKMapSnapshotter](../../mkmapsnapshotter.md) · [Options](../options.md)

# scale

<sub>Instance Property</sub>

The scale factor to use when creating the image.

> [!warning] Deprecated
> Use [traitCollection](../snapshot/traitcollection.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var scale: CGFloat { get set }
```

## Discussion

The value of this property is either `1.0` or `2.0`, depending on whether the device has a standard or Retina display. Set the value to `1.0` if you want to display the resulting image on a standard resolution display. Set the value to 2.0 if you want to display the image on a Retina display or want to use the image for printing.

This snapshotter sets this property to a default value that corresponds to the resolution of the current device’s display. You can change the value as needed to generate an image suitable for display on a different device.

## See Also

### Configuring the image output

- [traitCollection](traitcollection.md) — Traits that determine the appearance of the map snapshot.
- [size](size.md) — The size of the image that you want to create.
- [appearance](appearance.md) — The visual style (light or dark) to apply to the map when rendering the snapshot image.
