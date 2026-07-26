---
title: 'init(MKCoordinate:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.2+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsvalue/init(mkcoordinate:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsvalue/init(mkcoordinate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvalue/init%28mkcoordinate%3A%29.json'
content_hash: 'sha256:b921b0590d142160'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValue](../nsvalue.md)

# init(MKCoordinate:)

<sub>Initializer</sub>

Creates a new value object containing the specified CoreLocation geographic coordinate structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(MKCoordinate coordinate: CLLocationCoordinate2D)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(mkCoordinate coordinate: CLLocationCoordinate2D)
```

## Parameters

- `coordinate` — The value for the new object.

## Return Value

A new value object that contains the geographic coordinate information.

## See Also

### Related Documentation

- [CLLocationCoordinate2D](../../corelocation/cllocationcoordinate2d.md) — The latitude and longitude associated with a location, specified using the WGS 84 reference frame.

### Working with Geographic Coordinate Values

- [+ valueWithMKCoordinateSpan:](<init(mkcoordinatespan_).md>) — Creates a new value object containing the specified MapKit coordinate span structure.
- [MKCoordinateValue](mkcoordinatevalue.md) — The CoreLocation geographic coordinate structure representation of the value.
- [MKCoordinateSpanValue](mkcoordinatespanvalue.md) — The MapKit coordinate span structure representation of the value.
