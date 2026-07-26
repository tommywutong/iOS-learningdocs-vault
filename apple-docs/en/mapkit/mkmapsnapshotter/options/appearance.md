---
title: appearance
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.14+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapsnapshotter/options/appearance
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/appearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapsnapshotter/options/appearance.json'
content_hash: 'sha256:a62a38bf7e6ec9e5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKMapSnapshotter](../../mkmapsnapshotter.md) · [Options](../options.md)

# appearance

<sub>Instance Property</sub>

The visual style (light or dark) to apply to the map when rendering the snapshot image.

<sub>macOS</sub>

```swift
var appearance: NSAppearance? { get set }
```

## Discussion

Use this property to specify a light or dark appearance for the map in the resulting snapshot image. When the value of this property is `nil` (the default), the snapshotter derives the appropriate appearance based on the following logic:

- If the user specifically disables Dark Mode for map content in the Maps app, the snapshot uses a light appearance.
- The snapshot uses your app’s appearance.
- The snapshot uses the system appearance.

## See Also

### Configuring the image output

- [traitCollection](traitcollection.md) — Traits that determine the appearance of the map snapshot.
- [size](size.md) — The size of the image that you want to create.
- [scale](scale.md) — The scale factor to use when creating the image. _(deprecated)_
