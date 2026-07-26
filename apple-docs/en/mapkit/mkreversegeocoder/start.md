---
title: start
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（5.0 起废弃）, iPadOS 3.0+（5.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkreversegeocoder/start
source_url: 'https://developer.apple.com/documentation/mapkit/mkreversegeocoder/start'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkreversegeocoder/start.json'
content_hash: 'sha256:38595d2e390ef44b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKReverseGeocoder](../mkreversegeocoder.md)

# start

<sub>Instance Method</sub>

Starts the reverse-geocoding process asynchronously.

> [!warning] Deprecated
> Use the [CLGeocoder](../../corelocation/clgeocoder.md) class instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) start;
```

## Discussion

You should call this method only once to begin the reverse-geocoding process. This method submits the coordinate value to the map server asynchronously and returns. Once the process is complete, the results are delivered to the associated delegate object.

## See Also

### Managing the Search

- [querying](querying.md) — A Boolean value indicating whether the receiver is in the middle of reverse-geocoding its coordinate. _(deprecated)_
- [cancel](cancel.md) — Cancels a pending reverse-geocoding request. _(deprecated)_
