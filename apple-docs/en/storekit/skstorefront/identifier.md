---
title: identifier
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+（18.0 起废弃）, iPadOS 13.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.15+（15.0 起废弃）, tvOS 13.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skstorefront/identifier
source_url: 'https://developer.apple.com/documentation/storekit/skstorefront/identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skstorefront/identifier.json'
content_hash: 'sha256:a7c67728e6da62e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKStorefront](../skstorefront.md)

# identifier

<sub>Instance Property</sub>

A value defined by Apple that uniquely identifies an App Store storefront.

> [!warning] Deprecated
> Use 'Storefront.id'.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var identifier: String { get }
```

## See Also

### Identifying the Storefront

- [countryCode](countrycode.md) — The three-letter code representing the country or region associated with the App Store storefront. _(deprecated)_
