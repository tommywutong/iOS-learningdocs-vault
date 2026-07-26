---
title: autoRenewPreference
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/renewalinfo/autorenewpreference
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/autorenewpreference'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalinfo/autorenewpreference.json'
content_hash: 'sha256:2d44820f647b6d17'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionInfo](../../subscriptioninfo.md) · [RenewalInfo](../renewalinfo.md)

# autoRenewPreference

<sub>Instance Property</sub>

The product ID of the auto-renewable subscription that will automatically renew.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let autoRenewPreference: String?
```

## Discussion

This value is the product ID of the auto-renewable subscription that will renew after the current period expires. The value may be:

- The same as [currentProductID](currentproductid.md) if the subscription will renew with the same product.
- Another product ID value if the subscription will renew to a different product.
- `nil` if the subscription won’t renew in the next period. This may occur for several reasons, including when the person disables auto-renew for the subscription, the subscription lapses due to a billing issue, or you increase the subscription price and the person doesn’t accept the increase.

## See Also

### Getting the renewal or expiration state

- [state](../status-swift.struct/state.md) — The renewal state of the auto-renewable subscription.
- [willAutoRenew](willautorenew.md) — A Boolean value that indicates whether the subscription automatically renews in the next period.
- [expirationReason](expirationreason-swift.property.md) — The reason the auto-renewable subscription expired.
- [ExpirationReason](expirationreason-swift.struct.md) — The reasons for auto-renewable subscription expirations.
