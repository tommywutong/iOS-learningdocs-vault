---
title: freeTrial
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptionoffer/paymentmode-swift.struct/freetrial
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptionoffer/paymentmode-swift.struct/freetrial'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptionoffer/paymentmode-swift.struct/freetrial.json'
content_hash: 'sha256:cf5f8147484e5b0b'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionOffer](../../subscriptionoffer.md) · [PaymentMode](../paymentmode-swift.struct.md)

# freeTrial

<sub>Type Property</sub>

A payment mode of a product discount that indicates a free trial offer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let freeTrial: Product.SubscriptionOffer.PaymentMode
```

## Discussion

With a Free trial payment mode, customers pay nothing during the discount period.

![](../../../../../../attachments/31535a5905cc81be4d4fa37a8089ea5f/media-4311774@2x.png)

<sub>A timeline titled Free Trial that’s divided into three sections. The first section, which has a different timespan than the remaining sections, starts with the initial purchase and is the free trial period. The second section is labeled first renewal, and is at the regular price. The third section is labeled  second renewal, and is also at the regular price. Three dots at the end of the timeline indicate the pattern continues with renewals at the regular price.</sub>

## See Also

### Getting the payment modes

- [payAsYouGo](payasyougo.md) — A payment mode of a product discount that applies over a single billing period or multiple billing periods.
- [payUpFront](payupfront.md) — A payment mode of a product discount that applies the discount up front.
