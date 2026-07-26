---
title: offerID
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+（18.0 起废弃）, iPadOS 15.0+（18.0 起废弃）, macOS 12.0+（15.0 起废弃）, tvOS 15.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 8.0+（11.0 起废弃）]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: true
doc_path: /documentation/storekit/product/subscriptioninfo/renewalinfo/offerid
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/offerid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalinfo/offerid.json'
content_hash: 'sha256:b6e48d14f59e62a7'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionInfo](../../subscriptioninfo.md) · [RenewalInfo](../renewalinfo.md)

# offerID

<sub>Instance Property</sub>

A string that identifies an offer that applies to the next subscription period.

> [!warning] Deprecated
> Use the offer property instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var offerID: String? { get }
```

## Discussion

This value is `nil` if there isn’t an offer, or if the offer type is [introductory](../../../transaction/offertype-swift.struct/introductory.md).

If the offer type is [promotional](../../../transaction/offertype-swift.struct/promotional.md), this value contains the promotional offer identifier you set up in App Store Connect. For more information about promotional offers, see [Set up promotional offers for auto-renewable subscriptions](https://help.apple.com/app-store-connect/#/dev16dfca448).

If the offer type is [code](../../../transaction/offertype-swift.struct/code.md), this value contains the reference name of the offer code you set up in App Store Connect. For more information about offer codes, see [Set up offer codes](https://help.apple.com/app-store-connect/#/dev6a098e4b1).

## See Also

### Deprecated

- [environmentStringRepresentation](environmentstringrepresentation.md) — The string representation of the server environment that signs the renewal information for an auto-renewable subscription. _(deprecated)_
- [offerType](offertype.md) — The subscription offer type for the next subscription period. _(deprecated)_
- [currencyCode](currencycode.md) — The three-letter ISO 4217 currency code for the price of the product. _(deprecated)_
- [offerPaymentModeStringRepresentation](offerpaymentmodestringrepresentation.md) _(deprecated)_
- [offerPeriodStringRepresentation](offerperiodstringrepresentation.md) — The string representation of the subscription offer period applied to the next billing period. _(deprecated)_
