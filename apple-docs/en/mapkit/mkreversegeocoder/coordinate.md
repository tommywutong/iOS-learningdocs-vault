---
title: coordinate
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（5.0 起废弃）, iPadOS 3.0+（5.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkreversegeocoder/coordinate
source_url: 'https://developer.apple.com/documentation/mapkit/mkreversegeocoder/coordinate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkreversegeocoder/coordinate.json'
content_hash: 'sha256:13010555d6191ab5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKReverseGeocoder](../mkreversegeocoder.md)

# coordinate

<sub>Instance Property</sub>

The coordinate whose placemark data you want to retrieve.

> [!warning] Deprecated
> Use the [CLGeocoder](../../corelocation/clgeocoder.md) class instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) CLLocationCoordinate2D coordinate;
```

## See Also

### Accessing Reverse Geocoder Attributes

- [delegate](delegate.md) — The reverse geocoder’s delegate object. _(deprecated)_
- [placemark](placemark.md) — The result of the reverse-geocoding operation. _(deprecated)_
