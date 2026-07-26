---
title: offerPaymentModeStringRepresentation
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+（18.0 起废弃）, iPadOS 15.0+（18.0 起废弃）, macOS 12.0+（15.0 起废弃）, tvOS 15.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 8.0+（11.0 起废弃）]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: true
doc_path: /documentation/storekit/product/subscriptioninfo/renewalinfo/offerpaymentmodestringrepresentation
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/offerpaymentmodestringrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalinfo/offerpaymentmodestringrepresentation.json'
content_hash: 'sha256:8fc0e5441b473eed'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionInfo](../../subscriptioninfo.md) · [RenewalInfo](../renewalinfo.md)

# offerPaymentModeStringRepresentation

<sub>Instance Property</sub>

> [!warning] Deprecated
> Use the offer property instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 18.0, macOS 15.0, tvOS 18.0, watchOS 11.0, visionOS 2.0)
var offerPaymentModeStringRepresentation: String? { get }
```

## See Also

### Deprecated

- [environmentStringRepresentation](environmentstringrepresentation.md) — The string representation of the server environment that signs the renewal information for an auto-renewable subscription. _(deprecated)_
- [offerID](offerid.md) — A string that identifies an offer that applies to the next subscription period. _(deprecated)_
- [offerType](offertype.md) — The subscription offer type for the next subscription period. _(deprecated)_
- [currencyCode](currencycode.md) — The three-letter ISO 4217 currency code for the price of the product. _(deprecated)_
- [offerPeriodStringRepresentation](offerperiodstringrepresentation.md) — The string representation of the subscription offer period applied to the next billing period. _(deprecated)_
