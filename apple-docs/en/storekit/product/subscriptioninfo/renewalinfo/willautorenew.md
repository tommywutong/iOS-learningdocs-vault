---
title: willAutoRenew
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/renewalinfo/willautorenew
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/willautorenew'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalinfo/willautorenew.json'
content_hash: 'sha256:2f8f8d1ac3372c85'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionInfo](../../subscriptioninfo.md) · [RenewalInfo](../renewalinfo.md)

# willAutoRenew

<sub>Instance Property</sub>

A Boolean value that indicates whether the subscription automatically renews in the next period.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let willAutoRenew: Bool
```

## See Also

### Getting the renewal or expiration state

- [state](../status-swift.struct/state.md) — The renewal state of the auto-renewable subscription.
- [autoRenewPreference](autorenewpreference.md) — The product ID of the auto-renewable subscription that will automatically renew.
- [expirationReason](expirationreason-swift.property.md) — The reason the auto-renewable subscription expired.
- [ExpirationReason](expirationreason-swift.struct.md) — The reasons for auto-renewable subscription expirations.
