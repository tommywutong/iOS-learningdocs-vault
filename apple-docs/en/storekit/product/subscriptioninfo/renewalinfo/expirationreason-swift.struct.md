---
title: Product.SubscriptionInfo.RenewalInfo.ExpirationReason
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/renewalinfo/expirationreason-swift.struct
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/expirationreason-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalinfo/expirationreason-swift.struct.json'
content_hash: 'sha256:4ed2affa97018257'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionInfo](../../subscriptioninfo.md) · [RenewalInfo](../renewalinfo.md)

# Product.SubscriptionInfo.RenewalInfo.ExpirationReason

<sub>Structure</sub>

The reasons for auto-renewable subscription expirations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ExpirationReason
```

## Relationships

- **Conforms To**: [Equatable](../../../../swift/equatable.md), [Hashable](../../../../swift/hashable.md), [RawRepresentable](../../../../swift/rawrepresentable.md), [Sendable](../../../../swift/sendable.md), [SendableMetatype](../../../../swift/sendablemetatype.md)

## Topics

### Getting the expiration reason

- [autoRenewDisabled](expirationreason-swift.struct/autorenewdisabled.md) — The auto-renewable subscription expired because the customer voluntarily canceled their subscription.
- [billingError](expirationreason-swift.struct/billingerror.md) — The auto-renewable subscription expired because of a billing error.
- [didNotConsentToPriceIncrease](expirationreason-swift.struct/didnotconsenttopriceincrease.md) — The subscription expired because the customer didn’t consent to a price increase that requires customer consent.
- [productUnavailable](expirationreason-swift.struct/productunavailable.md) — The auto-renewable subscription expired because the product was unavailable for purchase at the time of the renewal.
- [unknown](expirationreason-swift.struct/unknown.md) — The auto-renewable subscription expired for an unknown reason.

### Getting a localized description

- [localizedDescription](expirationreason-swift.struct/localizeddescription.md) — The localized text that describes the expiration reason.

### Type Properties

- [unbundled](expirationreason-swift.struct/unbundled.md) — The subscription expired because the customer left the Subscription Bundle.

## See Also

### Getting the renewal or expiration state

- [state](../status-swift.struct/state.md) — The renewal state of the auto-renewable subscription.
- [autoRenewPreference](autorenewpreference.md) — The product ID of the auto-renewable subscription that will automatically renew.
- [willAutoRenew](willautorenew.md) — A Boolean value that indicates whether the subscription automatically renews in the next period.
- [expirationReason](expirationreason-swift.property.md) — The reason the auto-renewable subscription expired.
