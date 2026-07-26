---
title: isGeocoding
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+（26.0 起废弃）, iPadOS 5.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.8+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）, watchOS 2.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/clgeocoder/isgeocoding
source_url: 'https://developer.apple.com/documentation/corelocation/clgeocoder/isgeocoding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clgeocoder/isgeocoding.json'
content_hash: 'sha256:925b7f899f364381'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLGeocoder](../clgeocoder.md)

# isGeocoding

<sub>Instance Property</sub>

A Boolean value indicating whether the receiver is in the middle of geocoding its value.

> [!warning] Deprecated
> Use MapKit

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isGeocoding: Bool { get }
```

## Discussion

This property contains the value [true](../../swift/true.md) if the process is ongoing or [false](../../swift/false.md) if the process is done or has not yet been initiated.

## See Also

### Managing geocoding requests

- [- cancelGeocode](<cancelgeocode().md>) — Cancels a pending geocoding request. _(deprecated)_
