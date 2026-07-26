---
title: Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus
framework: StoreKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/renewalinfo/priceincreasestatus-swift.enum
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/priceincreasestatus-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalinfo/priceincreasestatus-swift.enum.json'
content_hash: 'sha256:727a16e84fc52827'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionInfo](../../subscriptioninfo.md) · [RenewalInfo](../renewalinfo.md)

# Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus

<sub>Enumeration</sub>

Status values that indicate whether an auto-renewable subscription is subject to a price increase.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum PriceIncreaseStatus
```

## Overview

For more information, see [Managing Price Increases for Auto-Renewable Subscriptions](../../../managing-price-increases-for-auto-renewable-subscriptions.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../../../../swift/bitwisecopyable.md), [Copyable](../../../../swift/copyable.md), [Equatable](../../../../swift/equatable.md), [Hashable](../../../../swift/hashable.md), [Sendable](../../../../swift/sendable.md), [SendableMetatype](../../../../swift/sendablemetatype.md)

## Topics

### Getting Price Increase Status

- [Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.noIncreasePending](priceincreasestatus-swift.enum/noincreasepending.md) — There’s no pending price increase for the auto-renewable subscription.
- [Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.agreed](priceincreasestatus-swift.enum/agreed.md) — The auto-renewable subscription is subject to a price increase.
- [Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.pending](priceincreasestatus-swift.enum/pending.md) — The customer hasn’t yet responded to an auto-renewable subscription price increase that requires customer consent.

### Getting a Localized Description

- [localizedDescription](priceincreasestatus-swift.enum/localizeddescription.md) — A string containing the localized description of the price increase status.

## See Also

### Getting the price increase status

- [Managing Price Increases for Auto-Renewable Subscriptions](../../../managing-price-increases-for-auto-renewable-subscriptions.md) — Identify the price increase status for auto-renewable subscriptions in your app and on your server.
- [priceIncreaseStatus](priceincreasestatus-swift.property.md) — The status that indicates whether the auto-renewable subscription is subject to a price increase.
