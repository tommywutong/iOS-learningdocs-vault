---
title: Product.SubscriptionOffer.PaymentMode
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptionoffer/paymentmode-swift.struct
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptionoffer/paymentmode-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptionoffer/paymentmode-swift.struct.json'
content_hash: 'sha256:f5ab30e5f745d329'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [SubscriptionOffer](../subscriptionoffer.md)

# Product.SubscriptionOffer.PaymentMode

<sub>Structure</sub>

The payment modes for subscription offers that apply to a transaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PaymentMode
```

## Overview

A payment mode describes how a subscription offer charges its discounted price — whether it charges one time, charges multiple times, or charges nothing because it’s a free trial.

## Relationships

- **Conforms To**: [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [RawRepresentable](../../../swift/rawrepresentable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Getting the payment modes

- [freeTrial](paymentmode-swift.struct/freetrial.md) — A payment mode of a product discount that indicates a free trial offer.
- [payAsYouGo](paymentmode-swift.struct/payasyougo.md) — A payment mode of a product discount that applies over a single billing period or multiple billing periods.
- [payUpFront](paymentmode-swift.struct/payupfront.md) — A payment mode of a product discount that applies the discount up front.

### Getting a localized description

- [localizedDescription](paymentmode-swift.struct/localizeddescription.md) — The localized text that describes the payment mode.

## See Also

### Getting price information

- [displayPrice](displayprice.md) — The localized string representation of the discounted price of the subscription offer.
- [price](price.md) — The decimal representation of the discounted price of the subscription offer.
- [paymentMode](paymentmode-swift.property.md) — The offer’s payment mode.
