---
title: freeTrial
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.2+, iPadOS 17.2+, macOS 14.2+, tvOS 17.2+, visionOS 1.1+, watchOS 10.2+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/offer-swift.struct/paymentmode-swift.struct/freetrial
source_url: 'https://developer.apple.com/documentation/storekit/transaction/offer-swift.struct/paymentmode-swift.struct/freetrial'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/offer-swift.struct/paymentmode-swift.struct/freetrial.json'
content_hash: 'sha256:ed31f1c308d6b656'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Transaction](../../../transaction.md) · [Offer](../../offer-swift.struct.md) · [PaymentMode](../paymentmode-swift.struct.md)

# freeTrial

<sub>Type Property</sub>

A payment mode of a product discount that indicates a free trial.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let freeTrial: Transaction.Offer.PaymentMode
```

## Discussion

With a Free trial payment mode, customers pay nothing during the discount period.

![](../../../../../../attachments/31535a5905cc81be4d4fa37a8089ea5f/media-4311726@2x.png)

<sub>A timeline titled Free Trial that’s divided into three sections. The first section, which has a different timespan than the remaining sections, starts with the initial purchase and is the free trial period. The second section is labeled first renewal, and is at the regular price. The third section is labeled  second renewal, and is also at the regular price. Three dots at the end of the timeline indicate the pattern continues with renewals at the regular price.</sub>

## See Also

### Getting payment modes

- [payAsYouGo](payasyougo.md) — A payment mode of a product discount that applies over a single billing period or multiple billing periods.
- [payUpFront](payupfront.md) — A payment mode of a product discount that applies the discount up front.
- [oneTime](onetime.md) — A payment mode for a consumable, non-consumable, or non-renewing subscription offer that indicates a one-time purchase.
