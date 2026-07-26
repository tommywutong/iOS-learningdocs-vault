---
title: placemark
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+（5.0 起废弃）, iPadOS 3.2+（5.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkreversegeocoder/placemark
source_url: 'https://developer.apple.com/documentation/mapkit/mkreversegeocoder/placemark'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkreversegeocoder/placemark.json'
content_hash: 'sha256:abbbf87c90d73e7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKReverseGeocoder](../mkreversegeocoder.md)

# placemark

<sub>Instance Property</sub>

The result of the reverse-geocoding operation.

> [!warning] Deprecated
> Use the [CLGeocoder](../../corelocation/clgeocoder.md) class instead. Note that placemarks in [CLGeocoder](../../corelocation/clgeocoder.md) always come back to the coordinate of the place, not the requested coordinate.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) MKPlacemark * placemark;
```

## Discussion

The value of this property is `nil` by default. After a successful reverse-geocoding operation, it is set to the placemark object that was generated.

## See Also

### Accessing Reverse Geocoder Attributes

- [delegate](delegate.md) — The reverse geocoder’s delegate object. _(deprecated)_
- [coordinate](coordinate.md) — The coordinate whose placemark data you want to retrieve. _(deprecated)_
