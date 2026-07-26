---
title: 'getCoordinates(_:range:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmultipoint/getcoordinates(_:range:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmultipoint/getcoordinates(_:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmultipoint/getcoordinates%28_%3Arange%3A%29.json'
content_hash: 'sha256:f8c369fbdf110b24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMultiPoint](../mkmultipoint.md)

# getCoordinates(_:range:)

<sub>Instance Method</sub>

Retrieves one or more points associated with the shape and converts them to coordinate values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getCoordinates(_ coords: UnsafeMutablePointer<CLLocationCoordinate2D>, range: NSRange)
```

## Parameters

- `coords` — On input, provide a C array of structures large enough to hold the desired number of coordinates. On output, this structure contains the requested coordinate data.

- `range` — The range of points you want. The `location` field indicates the first point you’re requesting, with `0` being the first point, `1` being the second point, and so on. The `length` field indicates the number of points you want. The array in `coords` needs to be large enough to accommodate the number of requested coordinates.

## Discussion

This method converts the map points into coordinates before returning them to you. If you want to specify the value of each point as a map point, you can access the values directly using the [- points](<points().md>) method.
