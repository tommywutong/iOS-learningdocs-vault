---
title: mkCoordinateValue
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.2+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsvalue/mkcoordinatevalue
source_url: 'https://developer.apple.com/documentation/foundation/nsvalue/mkcoordinatevalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsvalue/mkcoordinatevalue.json'
content_hash: 'sha256:bb75ed514708b1ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSValue](../nsvalue.md)

# mkCoordinateValue

<sub>Instance Property</sub>

The CoreLocation geographic coordinate structure representation of the value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var mkCoordinateValue: CLLocationCoordinate2D { get }
```

## See Also

### Related Documentation

- [CLLocationCoordinate2D](../../corelocation/cllocationcoordinate2d.md) — The latitude and longitude associated with a location, specified using the WGS 84 reference frame.

### Working with Geographic Coordinate Values

- [+ valueWithMKCoordinate:](<init(mkcoordinate_).md>) — Creates a new value object containing the specified CoreLocation geographic coordinate structure.
- [+ valueWithMKCoordinateSpan:](<init(mkcoordinatespan_).md>) — Creates a new value object containing the specified MapKit coordinate span structure.
- [MKCoordinateSpanValue](mkcoordinatespanvalue.md) — The MapKit coordinate span structure representation of the value.
