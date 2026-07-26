---
title: SKProductDiscount
framework: StoreKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.2+（18.0 起废弃）, iPadOS 11.2+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.13.2+（15.0 起废弃）, tvOS 11.2+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproductdiscount
source_url: 'https://developer.apple.com/documentation/storekit/skproductdiscount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproductdiscount.json'
content_hash: 'sha256:cf2cc5c48b61401e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKProductDiscount

<sub>Class</sub>

The details of an introductory offer or a promotional offer for an auto-renewable subscription.

> [!warning] Deprecated
> Use Product.SubscriptionOffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class SKProductDiscount
```

## Overview

You set up introductory and promotional offers in App Store Connect. [SKProductDiscount](skproductdiscount.md) contains the offer information as retrieved from the App Store.

For more information about setting up offers, see [Set an introductory offer for an auto-renewable subscription](https://help.apple.com/app-store-connect/#/deve1d49254f) and [Set up promotional offers for auto-renewable subscriptions](https://help.apple.com/app-store-connect/#/dev16dfca448).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Identifying the Discount

- [identifier](skproductdiscount/identifier.md) — A string used to uniquely identify a discount offer for a product. _(deprecated)_
- [type](skproductdiscount/type-swift.property.md) — The type of discount offer. _(deprecated)_
- [Type](skproductdiscount/type-swift.enum.md) — Values representing the types of discount offers an app can present. _(deprecated)_

### Getting Price and Payment Mode

- [price](skproductdiscount/price.md) — The discount price of the product in the local currency. _(deprecated)_
- [priceLocale](skproductdiscount/pricelocale.md) — The locale used to format the discount price of the product. _(deprecated)_
- [paymentMode](skproductdiscount/paymentmode-swift.property.md) — The payment mode for this product discount. _(deprecated)_
- [PaymentMode](skproductdiscount/paymentmode-swift.enum.md) — Values representing the payment modes for a product discount. _(deprecated)_

### Getting the Discount Duration

- [numberOfPeriods](skproductdiscount/numberofperiods.md) — An integer that indicates the number of periods the product discount is available. _(deprecated)_
- [subscriptionPeriod](skproductdiscount/subscriptionperiod.md) — An object that defines the period for the product discount. _(deprecated)_

## See Also

### Getting Pricing Information

- [price](skproduct/price.md) — The cost of the product in the local currency. _(deprecated)_
- [priceLocale](skproduct/pricelocale.md) — The locale used to format the price of the product. _(deprecated)_
- [introductoryPrice](skproduct/introductoryprice.md) — The object containing introductory price information for the product. _(deprecated)_
- [discounts](skproduct/discounts.md) — An array of subscription offers available for the auto-renewable subscription. _(deprecated)_
