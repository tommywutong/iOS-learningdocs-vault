---
title: size
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapsnapshotter/options/size
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/size'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapsnapshotter/options/size.json'
content_hash: 'sha256:d356dea451dd998d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKMapSnapshotter](../../mkmapsnapshotter.md) · [Options](../options.md)

# size

<sub>Instance Property</sub>

The size of the image that you want to create.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var size: CGSize { get set }
```

<sub>macOS</sub>

```swift
var size: NSSize { get set }
```

## Discussion

The default value of this property is 256 by 256 points.

## See Also

### Configuring the image output

- [traitCollection](traitcollection.md) — Traits that determine the appearance of the map snapshot.
- [appearance](appearance.md) — The visual style (light or dark) to apply to the map when rendering the snapshot image.
- [scale](scale.md) — The scale factor to use when creating the image. _(deprecated)_
