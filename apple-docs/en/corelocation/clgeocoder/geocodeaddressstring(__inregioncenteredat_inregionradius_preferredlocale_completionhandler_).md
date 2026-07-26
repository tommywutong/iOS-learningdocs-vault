---
title: 'geocodeAddressString(_:inRegionCenteredAt:inRegionRadius:preferredLocale:completionHandler:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 1.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corelocation/clgeocoder/geocodeaddressstring(_:inregioncenteredat:inregionradius:preferredlocale:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/corelocation/clgeocoder/geocodeaddressstring(_:inregioncenteredat:inregionradius:preferredlocale:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clgeocoder/geocodeaddressstring%28_%3Ainregioncenteredat%3Ainregionradius%3Apreferredlocale%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:63e0630cba5e0382'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLGeocoder](../clgeocoder.md)

# geocodeAddressString(_:inRegionCenteredAt:inRegionRadius:preferredLocale:completionHandler:)

<sub>Instance Method</sub>

> [!warning] Deprecated
> Use MKGeocodingRequest

<sub>visionOS</sub>

```swift
func geocodeAddressString(_ addressString: String, inRegionCenteredAt centroid: CLLocationCoordinate2D, inRegionRadius radius: CLLocationDistance, preferredLocale locale: Locale?, completionHandler: @escaping @Sendable ([CLPlacemark]?, (any Error)?) -> Void)
```

<sub>visionOS</sub>

```swift
func geocodeAddressString(_ addressString: String, inRegionCenteredAt centroid: CLLocationCoordinate2D, inRegionRadius radius: CLLocationDistance, preferredLocale locale: Locale?) async throws -> [CLPlacemark]
```
