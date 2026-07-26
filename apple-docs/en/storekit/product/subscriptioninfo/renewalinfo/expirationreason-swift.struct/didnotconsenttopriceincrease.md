---
title: didNotConsentToPriceIncrease
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/renewalinfo/expirationreason-swift.struct/didnotconsenttopriceincrease
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/expirationreason-swift.struct/didnotconsenttopriceincrease'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalinfo/expirationreason-swift.struct/didnotconsenttopriceincrease.json'
content_hash: 'sha256:5392426ac0c85c82'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [StoreKit](../../../../../storekit.md) · [Product](../../../../product.md) · [SubscriptionInfo](../../../subscriptioninfo.md) · [RenewalInfo](../../renewalinfo.md) · [ExpirationReason](../expirationreason-swift.struct.md)

# didNotConsentToPriceIncrease

<sub>Type Property</sub>

The subscription expired because the customer didn’t consent to a price increase that requires customer consent.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let didNotConsentToPriceIncrease: Product.SubscriptionInfo.RenewalInfo.ExpirationReason
```

## Discussion

The customer didn’t consent to an auto-renewable subscription price increase that requires their consent, or to a subscription offer conversion that requires their consent, so the subscription expired.

For more information about subscription price increases that require customer consent, see [Auto-renewable subscription price increase thresholds](https://developer.apple.com/help/app-store-connect/reference/auto-renewable-subscription-price-increase-thresholds). For more information about offer conversions that require customer consent, see [Consent for subscription offer conversions](https://developer.apple.com/help/app-store-connect/reference/consent-for-subscription-offer-conversions).

## See Also

### Getting the expiration reason

- [autoRenewDisabled](autorenewdisabled.md) — The auto-renewable subscription expired because the customer voluntarily canceled their subscription.
- [billingError](billingerror.md) — The auto-renewable subscription expired because of a billing error.
- [productUnavailable](productunavailable.md) — The auto-renewable subscription expired because the product was unavailable for purchase at the time of the renewal.
- [unknown](unknown.md) — The auto-renewable subscription expired for an unknown reason.
