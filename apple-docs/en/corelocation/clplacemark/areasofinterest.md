---
title: areasOfInterest
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.8+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/clplacemark/areasofinterest
source_url: 'https://developer.apple.com/documentation/corelocation/clplacemark/areasofinterest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clplacemark/areasofinterest.json'
content_hash: 'sha256:fc6170b82e6e715d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLPlacemark](../clplacemark.md)

# areasOfInterest

<sub>Instance Property</sub>

The relevant areas of interest associated with the placemark.

> [!warning] Deprecated
> Use either GeoToolbox.PlaceDescriptor or MapKit

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var areasOfInterest: [String]? { get }
```

## Discussion

Examples of an area of interest are the name of a military base, large national park, or an attraction such as the Eiffel Tower, Disneyland, or Golden Gate Park.
