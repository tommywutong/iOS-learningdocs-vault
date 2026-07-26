---
title: delegate
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（5.0 起废弃）, iPadOS 3.0+（5.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkreversegeocoder/delegate
source_url: 'https://developer.apple.com/documentation/mapkit/mkreversegeocoder/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkreversegeocoder/delegate.json'
content_hash: 'sha256:19bec1d5cd2c9c1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKReverseGeocoder](../mkreversegeocoder.md)

# delegate

<sub>Instance Property</sub>

The reverse geocoder’s delegate object.

> [!warning] Deprecated
> Use the [CLGeocoder](../../corelocation/clgeocoder.md) class instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, weak) id<MKReverseGeocoderDelegate> delegate;
```

## Discussion

A reverse-geocoder object sends messages to its delegate regarding the successful (or unsuccessful) acquisition of placemark data. You must provide a delegate object to receive this data.

For more information about the [MKReverseGeocoderDelegate](../mkreversegeocoderdelegate.md) protocol, see [MKReverseGeocoderDelegate](../mkreversegeocoderdelegate.md).

## See Also

### Accessing Reverse Geocoder Attributes

- [coordinate](coordinate.md) — The coordinate whose placemark data you want to retrieve. _(deprecated)_
- [placemark](placemark.md) — The result of the reverse-geocoding operation. _(deprecated)_
