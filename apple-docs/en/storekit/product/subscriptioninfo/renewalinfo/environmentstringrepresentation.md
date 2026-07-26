---
title: environmentStringRepresentation
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+（16.0 起废弃）, iPadOS 15.0+（16.0 起废弃）, Mac Catalyst 15.0+（16.0 起废弃）, macOS 12.0+（13.0 起废弃）, tvOS 15.0+（16.0 起废弃）, watchOS 8.0+（9.0 起废弃）]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: true
doc_path: /documentation/storekit/product/subscriptioninfo/renewalinfo/environmentstringrepresentation
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/environmentstringrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalinfo/environmentstringrepresentation.json'
content_hash: 'sha256:522a594edb00bd6b'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionInfo](../../subscriptioninfo.md) · [RenewalInfo](../renewalinfo.md)

# environmentStringRepresentation

<sub>Instance Property</sub>

The string representation of the server environment that signs the renewal information for an auto-renewable subscription.

> [!warning] Deprecated
> Use the environment property instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
@backDeployed(before: iOS 16.0, macOS 13.0, tvOS 16.0, watchOS 9.0, macCatalyst 16.0)
var environmentStringRepresentation: String { get }
```

## See Also

### Deprecated

- [offerID](offerid.md) — A string that identifies an offer that applies to the next subscription period. _(deprecated)_
- [offerType](offertype.md) — The subscription offer type for the next subscription period. _(deprecated)_
- [currencyCode](currencycode.md) — The three-letter ISO 4217 currency code for the price of the product. _(deprecated)_
- [offerPaymentModeStringRepresentation](offerpaymentmodestringrepresentation.md) _(deprecated)_
- [offerPeriodStringRepresentation](offerperiodstringrepresentation.md) — The string representation of the subscription offer period applied to the next billing period. _(deprecated)_
