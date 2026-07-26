---
title: expirationReason
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/renewalinfo/expirationreason-swift.property
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/expirationreason-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalinfo/expirationreason-swift.property.json'
content_hash: 'sha256:65a49485356b4314'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionInfo](../../subscriptioninfo.md) · [RenewalInfo](../renewalinfo.md)

# expirationReason

<sub>Instance Property</sub>

The reason the auto-renewable subscription expired.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let expirationReason: Product.SubscriptionInfo.RenewalInfo.ExpirationReason?
```

## Discussion

This optional value is `nil` if the auto-renewable subscription is active and hasn’t expired.

## See Also

### Getting the renewal or expiration state

- [state](../status-swift.struct/state.md) — The renewal state of the auto-renewable subscription.
- [autoRenewPreference](autorenewpreference.md) — The product ID of the auto-renewable subscription that will automatically renew.
- [willAutoRenew](willautorenew.md) — A Boolean value that indicates whether the subscription automatically renews in the next period.
- [ExpirationReason](expirationreason-swift.struct.md) — The reasons for auto-renewable subscription expirations.
