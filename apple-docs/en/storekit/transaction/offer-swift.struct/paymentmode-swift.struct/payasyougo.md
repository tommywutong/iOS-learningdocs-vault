---
title: payAsYouGo
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.2+, iPadOS 17.2+, macOS 14.2+, tvOS 17.2+, visionOS 1.1+, watchOS 10.2+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/offer-swift.struct/paymentmode-swift.struct/payasyougo
source_url: 'https://developer.apple.com/documentation/storekit/transaction/offer-swift.struct/paymentmode-swift.struct/payasyougo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/offer-swift.struct/paymentmode-swift.struct/payasyougo.json'
content_hash: 'sha256:30cfc414a6a0774f'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Transaction](../../../transaction.md) · [Offer](../../offer-swift.struct.md) · [PaymentMode](../paymentmode-swift.struct.md)

# payAsYouGo

<sub>Type Property</sub>

A payment mode of a product discount that applies over a single billing period or multiple billing periods.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let payAsYouGo: Transaction.Offer.PaymentMode
```

## Discussion

With a Pay As You Go payment mode, subscribers pay a discounted price for each billing period for the duration of the discount.

![](../../../../../../attachments/a6962b6c59fca2500367c1d792f2ec46/media-4311727@2x.png)

<sub>A timeline titled Pay As You Go that’s divided into four sections. The first three sections, labeled Introductory price, each have an equal timespan, and the fourth section, labeled Regular price has a different timespan. The first three sections represent the initial purchase, first renewal, and second renewal, respectively.  The fourth section is the third renewal, at the regular price. Three dots at the end of the timeline indicate the pattern continues with renewals at the regular price.</sub>

## See Also

### Getting payment modes

- [freeTrial](freetrial.md) — A payment mode of a product discount that indicates a free trial.
- [payUpFront](payupfront.md) — A payment mode of a product discount that applies the discount up front.
- [oneTime](onetime.md) — A payment mode for a consumable, non-consumable, or non-renewing subscription offer that indicates a one-time purchase.
