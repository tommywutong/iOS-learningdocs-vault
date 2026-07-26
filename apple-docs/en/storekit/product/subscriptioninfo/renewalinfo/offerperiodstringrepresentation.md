---
title: offerPeriodStringRepresentation
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+（18.4 起废弃）, iPadOS 15.0+（18.4 起废弃）, macOS 12.0+（15.4 起废弃）, tvOS 15.0+（18.4 起废弃）, visionOS 1.0+（2.4 起废弃）, watchOS 8.0+（11.4 起废弃）]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: true
doc_path: /documentation/storekit/product/subscriptioninfo/renewalinfo/offerperiodstringrepresentation
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/offerperiodstringrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalinfo/offerperiodstringrepresentation.json'
content_hash: 'sha256:ec0a8f5f6083e643'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionInfo](../../subscriptioninfo.md) · [RenewalInfo](../renewalinfo.md)

# offerPeriodStringRepresentation

<sub>Instance Property</sub>

The string representation of the subscription offer period applied to the next billing period.

> [!warning] Deprecated
> Use the [offer](offer.md) property instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 18.4, macOS 15.4, tvOS 18.4, watchOS 11.4, visionOS 2.4)
var offerPeriodStringRepresentation: String? { get }
```

## Discussion

This value is present only for subscriptions that include an offer.

> [!important] Important
> In rare cases, the property might return a sentinel `nil` value. One possible reason is using StoreKit Testing in Xcode; try testing on a device with a newer OS. Another reason could be a critical server error.

## See Also

### Deprecated

- [environmentStringRepresentation](environmentstringrepresentation.md) — The string representation of the server environment that signs the renewal information for an auto-renewable subscription. _(deprecated)_
- [offerID](offerid.md) — A string that identifies an offer that applies to the next subscription period. _(deprecated)_
- [offerType](offertype.md) — The subscription offer type for the next subscription period. _(deprecated)_
- [currencyCode](currencycode.md) — The three-letter ISO 4217 currency code for the price of the product. _(deprecated)_
- [offerPaymentModeStringRepresentation](offerpaymentmodestringrepresentation.md) _(deprecated)_
