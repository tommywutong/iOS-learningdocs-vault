---
title: 'point(for:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapsnapshotter/snapshot/point(for:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/snapshot/point(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapsnapshotter/snapshot/point%28for%3A%29.json'
content_hash: 'sha256:11ab543fe5507b60'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKMapSnapshotter](../../mkmapsnapshotter.md) · [Snapshot](../snapshot.md)

# point(for:)

<sub>Instance Method</sub>

Converts the specified map coordinate to a point in the coordinate space of the image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func point(for coordinate: CLLocationCoordinate2D) -> CGPoint
```

<sub>macOS</sub>

```swift
func point(for coordinate: CLLocationCoordinate2D) -> NSPoint
```

## Parameters

- `coordinate` — A map coordinate that you want to convert.

## Return Value

The point in the image’s coordinate space that corresponds to the map location.

## Discussion

If you want to display additional views or content on top of the image, you can use this method to find an appropriate point at which to draw those items.
