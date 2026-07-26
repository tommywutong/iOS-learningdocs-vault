---
title: postalAddress
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.13+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 4.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/clplacemark/postaladdress
source_url: 'https://developer.apple.com/documentation/corelocation/clplacemark/postaladdress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clplacemark/postaladdress.json'
content_hash: 'sha256:3e57e8b663a480fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLPlacemark](../clplacemark.md)

# postalAddress

<sub>Instance Property</sub>

The postal address associated with the location, formatted for use with the Contacts framework.

> [!warning] Deprecated
> Use either GeoToolbox.PlaceDescriptor or MapKit

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var postalAddress: CNPostalAddress? { get }
```

## See Also

### Getting the associated contact details

- [addressDictionary](addressdictionary.md) — A dictionary containing the Address Book keys and values for the placemark. _(deprecated)_
