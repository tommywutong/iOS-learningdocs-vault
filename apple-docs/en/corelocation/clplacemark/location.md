---
title: location
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.8+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/clplacemark/location
source_url: 'https://developer.apple.com/documentation/corelocation/clplacemark/location'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clplacemark/location.json'
content_hash: 'sha256:3865da5b8be32a78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLPlacemark](../clplacemark.md)

# location

<sub>Instance Property</sub>

The location object containing latitude and longitude information.

> [!warning] Deprecated
> Use either GeoToolbox.PlaceDescriptor or MapKit

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var location: CLLocation? { get }
```

## Discussion

Use this object to initialize the placemark object.

## See Also

### Getting the placemark’s location

- [region](region.md) — The geographic region associated with the placemark. _(deprecated)_
