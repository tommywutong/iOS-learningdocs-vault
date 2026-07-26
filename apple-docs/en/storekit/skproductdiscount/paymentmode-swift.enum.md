---
title: SKProductDiscount.PaymentMode
framework: StoreKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.2+（18.0 起废弃）, iPadOS 11.2+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.13.2+（15.0 起废弃）, tvOS 11.2+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproductdiscount/paymentmode-swift.enum
source_url: 'https://developer.apple.com/documentation/storekit/skproductdiscount/paymentmode-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproductdiscount/paymentmode-swift.enum.json'
content_hash: 'sha256:5c77a047d4740fd3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKProductDiscount](../skproductdiscount.md)

# SKProductDiscount.PaymentMode

<sub>Enumeration</sub>

Values representing the payment modes for a product discount.

> [!warning] Deprecated
> Use Product.SubscriptionOffer.PaymentMode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum PaymentMode
```

## Overview

The payment mode indicates if the discount price is charged one time, multiple times, or if the discount is a free trial.

The payment mode may determine the wording you choose to phrase the offer in your app’s UI.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Discount Price Payment Modes

- [SKProductDiscountPaymentModePayAsYouGo](paymentmode-swift.enum/payasyougo.md) — A constant that indicates a product discount that applies over a single billing period or multiple billing periods. _(deprecated)_
- [SKProductDiscountPaymentModePayUpFront](paymentmode-swift.enum/payupfront.md) — A constant that indicates that the system applies the product discount up front. _(deprecated)_
- [SKProductDiscountPaymentModeFreeTrial](paymentmode-swift.enum/freetrial.md) — A constant that indicates that the payment mode is a free trial. _(deprecated)_

### Initializers

- [init(rawValue:)](<paymentmode-swift.enum/init(rawvalue_).md>) _(deprecated)_

## See Also

### Getting Price and Payment Mode

- [price](price.md) — The discount price of the product in the local currency. _(deprecated)_
- [priceLocale](pricelocale.md) — The locale used to format the discount price of the product. _(deprecated)_
- [paymentMode](paymentmode-swift.property.md) — The payment mode for this product discount. _(deprecated)_
