---
title: 'reverseGeocoder:didFailWithError:'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（5.0 起废弃）, iPadOS 3.0+（5.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/mapkit/mkreversegeocoderdelegate/reversegeocoder:didfailwitherror:'
source_url: 'https://developer.apple.com/documentation/mapkit/mkreversegeocoderdelegate/reversegeocoder:didfailwitherror:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkreversegeocoderdelegate/reversegeocoder%3Adidfailwitherror%3A.json'
content_hash: 'sha256:3cb049f46765e2b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKReverseGeocoderDelegate](../mkreversegeocoderdelegate.md)

# reverseGeocoder:didFailWithError:

<sub>Instance Method</sub>

Tells the delegate that the specified reverse geocoder failed to obtain information about its coordinate.

> [!warning] Deprecated
> Use the [CLGeocoder](../../corelocation/clgeocoder.md) class instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) reverseGeocoder:(MKReverseGeocoder *) geocoder didFailWithError:(NSError *) error;
```

## Parameters

- `geocoder` — The reverse geocoder object that was unable to complete its request.

- `error` — An error object indicating the reason the request did not succeed.

## See Also

### Processing placemark searches

- [reverseGeocoder:didFindPlacemark:](reversegeocoder_didfindplacemark_.md) — Tells the delegate that a reverse geocoder successfully obtained placemark information for its coordinate. _(deprecated)_
