---
title: cancel
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（5.0 起废弃）, iPadOS 3.0+（5.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkreversegeocoder/cancel
source_url: 'https://developer.apple.com/documentation/mapkit/mkreversegeocoder/cancel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkreversegeocoder/cancel.json'
content_hash: 'sha256:f25ab874fd8da0e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKReverseGeocoder](../mkreversegeocoder.md)

# cancel

<sub>Instance Method</sub>

Cancels a pending reverse-geocoding request.

> [!warning] Deprecated
> Use the [CLGeocoder](../../corelocation/clgeocoder.md) class instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) cancel;
```

## Discussion

You can use this method to cancel a pending request and free up the resources associated with that request. If the request has already returned or has not yet begun, calling this method has no effect.

## See Also

### Managing the Search

- [start](start.md) — Starts the reverse-geocoding process asynchronously. _(deprecated)_
- [querying](querying.md) — A Boolean value indicating whether the receiver is in the middle of reverse-geocoding its coordinate. _(deprecated)_
