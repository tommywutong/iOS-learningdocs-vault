---
title: image
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapsnapshotter/snapshot/image
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/snapshot/image'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapsnapshotter/snapshot/image.json'
content_hash: 'sha256:d445c005f9652041'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKMapSnapshotter](../../mkmapsnapshotter.md) · [Snapshot](../snapshot.md)

# image

<sub>Instance Property</sub>

The image of the map’s content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var image: UIImage { get }
```

<sub>macOS</sub>

```swift
var image: NSImage { get }
```

## Discussion

The image object contains representations appropriate for display on both Retina and standard displays.

## See Also

### Getting the snapshot image

- [appearance](appearance.md) — The visual style that MapKit uses when rendering the snapshot.
