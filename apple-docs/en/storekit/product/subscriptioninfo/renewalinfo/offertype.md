---
title: offerType
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+（18.0 起废弃）, iPadOS 15.0+（18.0 起废弃）, macOS 12.0+（15.0 起废弃）, tvOS 15.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 8.0+（11.0 起废弃）]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: true
doc_path: /documentation/storekit/product/subscriptioninfo/renewalinfo/offertype
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/offertype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalinfo/offertype.json'
content_hash: 'sha256:83f449a1787ce1fe'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionInfo](../../subscriptioninfo.md) · [RenewalInfo](../renewalinfo.md)

# offerType

<sub>Instance Property</sub>

The subscription offer type for the next subscription period.

> [!warning] Deprecated
> Use the offer property instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var offerType: Transaction.OfferType? { get }
```

## Discussion

If this value is `nil`, there’s no offer applied.

## See Also

### Deprecated

- [environmentStringRepresentation](environmentstringrepresentation.md) — The string representation of the server environment that signs the renewal information for an auto-renewable subscription. _(deprecated)_
- [offerID](offerid.md) — A string that identifies an offer that applies to the next subscription period. _(deprecated)_
- [currencyCode](currencycode.md) — The three-letter ISO 4217 currency code for the price of the product. _(deprecated)_
- [offerPaymentModeStringRepresentation](offerpaymentmodestringrepresentation.md) _(deprecated)_
- [offerPeriodStringRepresentation](offerperiodstringrepresentation.md) — The string representation of the subscription offer period applied to the next billing period. _(deprecated)_
