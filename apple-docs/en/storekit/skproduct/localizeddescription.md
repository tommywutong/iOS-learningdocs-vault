---
title: localizedDescription
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproduct/localizeddescription
source_url: 'https://developer.apple.com/documentation/storekit/skproduct/localizeddescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproduct/localizeddescription.json'
content_hash: 'sha256:b5f5571a9c644594'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProduct](../skproduct.md)

# localizedDescription

<sub>Instance Property</sub>

A description of the product.

> [!warning] Deprecated
> Use Product.description.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var localizedDescription: String { get }
```

## Discussion

The description’s language is determined by the storefront that the user’s device is connected to, not the preferred language set on the device.

## See Also

### Related Documentation

- [SKStorefront](../skstorefront.md) — An object containing the location and unique identifier of an Apple App Store storefront. _(deprecated)_

### Getting Product Attributes

- [localizedTitle](localizedtitle.md) — The name of the product. _(deprecated)_
- [contentVersion](contentversion.md) — A string that identifies the version of the content. _(deprecated)_
- [isFamilyShareable](isfamilyshareable.md) — A Boolean value that indicates whether the product is available for Family Sharing in App Store Connect. _(deprecated)_
- [contentLengths](contentlengths.md) — The total size of the content, in bytes. _(deprecated)_
