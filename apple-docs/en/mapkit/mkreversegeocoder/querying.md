---
title: querying
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（5.0 起废弃）, iPadOS 3.0+（5.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkreversegeocoder/querying
source_url: 'https://developer.apple.com/documentation/mapkit/mkreversegeocoder/querying'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkreversegeocoder/querying.json'
content_hash: 'sha256:a89d804684c4def8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKReverseGeocoder](../mkreversegeocoder.md)

# querying

<sub>Instance Property</sub>

A Boolean value indicating whether the receiver is in the middle of reverse-geocoding its coordinate.

> [!warning] Deprecated
> Use the [CLGeocoder](../../corelocation/clgeocoder.md) class instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly, getter=isQuerying) BOOL querying;
```

## Discussion

This property contains YES if the process is ongoing or NO if the process is done or has not yet been initiated.

## See Also

### Managing the Search

- [start](start.md) — Starts the reverse-geocoding process asynchronously. _(deprecated)_
- [cancel](cancel.md) — Cancels a pending reverse-geocoding request. _(deprecated)_
