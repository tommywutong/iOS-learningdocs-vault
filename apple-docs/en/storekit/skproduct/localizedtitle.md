---
title: localizedTitle
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproduct/localizedtitle
source_url: 'https://developer.apple.com/documentation/storekit/skproduct/localizedtitle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproduct/localizedtitle.json'
content_hash: 'sha256:7cb650e87c277893'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProduct](../skproduct.md)

# localizedTitle

<sub>Instance Property</sub>

The name of the product.

> [!warning] Deprecated
> Use Product.displayName.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var localizedTitle: String { get }
```

## Discussion

The title’s language is determined by the storefront that the user’s device is connected to, not the preferred language set on the device.

## See Also

### Related Documentation

- [SKStorefront](../skstorefront.md) — An object containing the location and unique identifier of an Apple App Store storefront. _(deprecated)_

### Getting Product Attributes

- [localizedDescription](localizeddescription.md) — A description of the product. _(deprecated)_
- [contentVersion](contentversion.md) — A string that identifies the version of the content. _(deprecated)_
- [isFamilyShareable](isfamilyshareable.md) — A Boolean value that indicates whether the product is available for Family Sharing in App Store Connect. _(deprecated)_
- [contentLengths](contentlengths.md) — The total size of the content, in bytes. _(deprecated)_
