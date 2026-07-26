---
title: productUnavailable
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/renewalinfo/expirationreason-swift.struct/productunavailable
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/expirationreason-swift.struct/productunavailable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalinfo/expirationreason-swift.struct/productunavailable.json'
content_hash: 'sha256:e8ef978080d787c9'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [StoreKit](../../../../../storekit.md) · [Product](../../../../product.md) · [SubscriptionInfo](../../../subscriptioninfo.md) · [RenewalInfo](../../renewalinfo.md) · [ExpirationReason](../expirationreason-swift.struct.md)

# productUnavailable

<sub>Type Property</sub>

The auto-renewable subscription expired because the product was unavailable for purchase at the time of the renewal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let productUnavailable: Product.SubscriptionInfo.RenewalInfo.ExpirationReason
```

## See Also

### Getting the expiration reason

- [autoRenewDisabled](autorenewdisabled.md) — The auto-renewable subscription expired because the customer voluntarily canceled their subscription.
- [billingError](billingerror.md) — The auto-renewable subscription expired because of a billing error.
- [didNotConsentToPriceIncrease](didnotconsenttopriceincrease.md) — The subscription expired because the customer didn’t consent to a price increase that requires customer consent.
- [unknown](unknown.md) — The auto-renewable subscription expired for an unknown reason.
