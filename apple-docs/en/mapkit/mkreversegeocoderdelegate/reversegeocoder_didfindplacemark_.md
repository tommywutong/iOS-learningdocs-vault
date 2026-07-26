---
title: 'reverseGeocoder:didFindPlacemark:'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（5.0 起废弃）, iPadOS 3.0+（5.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/mapkit/mkreversegeocoderdelegate/reversegeocoder:didfindplacemark:'
source_url: 'https://developer.apple.com/documentation/mapkit/mkreversegeocoderdelegate/reversegeocoder:didfindplacemark:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkreversegeocoderdelegate/reversegeocoder%3Adidfindplacemark%3A.json'
content_hash: 'sha256:39d5dd1096000096'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKReverseGeocoderDelegate](../mkreversegeocoderdelegate.md)

# reverseGeocoder:didFindPlacemark:

<sub>Instance Method</sub>

Tells the delegate that a reverse geocoder successfully obtained placemark information for its coordinate.

> [!warning] Deprecated
> Use the [CLGeocoder](../../corelocation/clgeocoder.md) class instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) reverseGeocoder:(MKReverseGeocoder *) geocoder didFindPlacemark:(MKPlacemark *) placemark;
```

## Parameters

- `geocoder` — The reverse geocoder object that completed its request successfully.

- `placemark` — The object containing the placemark data.

## Discussion

You can get the map coordinate for the associated request from either the reverse geocoder object or from the placemark object, which itself supports the [MKAnnotation](../mkannotation.md) protocol.

## See Also

### Related Documentation

- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)

### Processing placemark searches

- [reverseGeocoder:didFailWithError:](reversegeocoder_didfailwitherror_.md) — Tells the delegate that the specified reverse geocoder failed to obtain information about its coordinate. _(deprecated)_
