---
title: reasonStringRepresentation
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+（17.0 起废弃）, iPadOS 15.0+（17.0 起废弃）, Mac Catalyst 15.0+（17.0 起废弃）, macOS 12.0+（14.0 起废弃）, tvOS 15.0+（17.0 起废弃）, watchOS 8.0+（10.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/storekit/transaction/reasonstringrepresentation
source_url: 'https://developer.apple.com/documentation/storekit/transaction/reasonstringrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/reasonstringrepresentation.json'
content_hash: 'sha256:68743fa5d18c0c98'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# reasonStringRepresentation

<sub>Instance Property</sub>

The string representation of the transaction reason.

> [!warning] Deprecated
> Use [reason](reason-swift.property.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0, macCatalyst 17.0)
var reasonStringRepresentation: String { get }
```

## Discussion

For more information, see [reason](reason-swift.property.md).

## See Also

### Deprecated

- [currencyCode](currencycode.md) — The three-letter ISO 4217 currency code for the price of the product. _(deprecated)_
- [environmentStringRepresentation](environmentstringrepresentation.md) — A string representation of the server environment. _(deprecated)_
- [offerID](offerid.md) — A string that identifies an offer applied to the current subscription. _(deprecated)_
- [offerPaymentModeStringRepresentation](offerpaymentmodestringrepresentation.md) — The string representation of the payment mode for a subscription offer. _(deprecated)_
- [offerType](offertype-swift.property.md) — The subscription offer type for the current subscription period. _(deprecated)_
- [storefrontCountryCode](storefrontcountrycode.md) — The three-letter code that represents the country or region associated with the App Store storefront of the purchase. _(deprecated)_
