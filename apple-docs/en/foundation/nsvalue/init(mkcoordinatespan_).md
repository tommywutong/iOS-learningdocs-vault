---
title: 'init(MKCoordinateSpan:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.2+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsvalue/init(mkcoordinatespan:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsvalue/init(mkcoordinatespan:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvalue/init%28mkcoordinatespan%3A%29.json'
content_hash: 'sha256:3d1c5eecd8d0aba2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValue](../nsvalue.md)

# init(MKCoordinateSpan:)

<sub>Initializer</sub>

Creates a new value object containing the specified MapKit coordinate span structure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(MKCoordinateSpan span: MKCoordinateSpan)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(mkCoordinateSpan span: MKCoordinateSpan)
```

## Parameters

- `span` — The value for the new object.

## Return Value

A new value object that contains the coordinate span information.

## See Also

### Related Documentation

- [MKCoordinateSpan](../../mapkit/mkcoordinatespan.md) — The width and height of a map region.

### Working with Geographic Coordinate Values

- [+ valueWithMKCoordinate:](<init(mkcoordinate_).md>) — Creates a new value object containing the specified CoreLocation geographic coordinate structure.
- [MKCoordinateValue](mkcoordinatevalue.md) — The CoreLocation geographic coordinate structure representation of the value.
- [MKCoordinateSpanValue](mkcoordinatespanvalue.md) — The MapKit coordinate span structure representation of the value.
