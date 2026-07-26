---
title: state
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/status-swift.struct/state
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/status-swift.struct/state'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/status-swift.struct/state.json'
content_hash: 'sha256:fbe5a0c9571e8b8e'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionInfo](../../subscriptioninfo.md) · [Status](../status-swift.struct.md)

# state

<sub>Instance Property</sub>

The renewal state of the auto-renewable subscription.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let state: Product.SubscriptionInfo.RenewalState
```

## See Also

### Getting the renewal or expiration state

- [autoRenewPreference](../renewalinfo/autorenewpreference.md) — The product ID of the auto-renewable subscription that will automatically renew.
- [willAutoRenew](../renewalinfo/willautorenew.md) — A Boolean value that indicates whether the subscription automatically renews in the next period.
- [expirationReason](../renewalinfo/expirationreason-swift.property.md) — The reason the auto-renewable subscription expired.
- [ExpirationReason](../renewalinfo/expirationreason-swift.struct.md) — The reasons for auto-renewable subscription expirations.
