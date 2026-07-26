---
title: payAsYouGo
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptionoffer/paymentmode-swift.struct/payasyougo
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptionoffer/paymentmode-swift.struct/payasyougo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptionoffer/paymentmode-swift.struct/payasyougo.json'
content_hash: 'sha256:821b86328fd6b056'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionOffer](../../subscriptionoffer.md) · [PaymentMode](../paymentmode-swift.struct.md)

# payAsYouGo

<sub>Type Property</sub>

A payment mode of a product discount that applies over a single billing period or multiple billing periods.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let payAsYouGo: Product.SubscriptionOffer.PaymentMode
```

## Discussion

With a Pay As You Go payment mode, subscribers pay a discounted price for each billing period for the duration of the discount.

![](../../../../../../attachments/a6962b6c59fca2500367c1d792f2ec46/media-4311775@2x.png)

<sub>A timeline titled Pay As You Go that’s divided into four sections. The first three sections, labeled Introductory price, each have an equal timespan, and the fourth section, labeled Regular price has a different timespan. The first three sections represent the initial purchase, first renewal, and second renewal, respectively.  The fourth section is the third renewal, at the regular price. Three dots at the end of the timeline indicate the pattern continues with renewals at the regular price.</sub>

## See Also

### Getting the payment modes

- [freeTrial](freetrial.md) — A payment mode of a product discount that indicates a free trial offer.
- [payUpFront](payupfront.md) — A payment mode of a product discount that applies the discount up front.
