---
title: unknown
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/renewalinfo/expirationreason-swift.struct/unknown
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/expirationreason-swift.struct/unknown'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalinfo/expirationreason-swift.struct/unknown.json'
content_hash: 'sha256:8742bcf6b62b8d2c'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [StoreKit](../../../../../storekit.md) · [Product](../../../../product.md) · [SubscriptionInfo](../../../subscriptioninfo.md) · [RenewalInfo](../../renewalinfo.md) · [ExpirationReason](../expirationreason-swift.struct.md)

# unknown

<sub>Type Property</sub>

The auto-renewable subscription expired for an unknown reason.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let unknown: Product.SubscriptionInfo.RenewalInfo.ExpirationReason
```

## See Also

### Getting the expiration reason

- [autoRenewDisabled](autorenewdisabled.md) — The auto-renewable subscription expired because the customer voluntarily canceled their subscription.
- [billingError](billingerror.md) — The auto-renewable subscription expired because of a billing error.
- [didNotConsentToPriceIncrease](didnotconsenttopriceincrease.md) — The subscription expired because the customer didn’t consent to a price increase that requires customer consent.
- [productUnavailable](productunavailable.md) — The auto-renewable subscription expired because the product was unavailable for purchase at the time of the renewal.
