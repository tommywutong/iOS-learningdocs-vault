---
title: oneTime
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.2+, iPadOS 17.2+, macOS 14.2+, tvOS 17.2+, visionOS 1.1+, watchOS 10.2+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/offer-swift.struct/paymentmode-swift.struct/onetime
source_url: 'https://developer.apple.com/documentation/storekit/transaction/offer-swift.struct/paymentmode-swift.struct/onetime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/offer-swift.struct/paymentmode-swift.struct/onetime.json'
content_hash: 'sha256:175104c185d02273'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Transaction](../../../transaction.md) · [Offer](../../offer-swift.struct.md) · [PaymentMode](../paymentmode-swift.struct.md)

# oneTime

<sub>Type Property</sub>

A payment mode for a consumable, non-consumable, or non-renewing subscription offer that indicates a one-time purchase.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 26.0, macOS 26.0, tvOS 26.0, watchOS 26.0, visionOS 26.0)
static var oneTime: Transaction.Offer.PaymentMode { get }
```

## See Also

### Getting payment modes

- [freeTrial](freetrial.md) — A payment mode of a product discount that indicates a free trial.
- [payAsYouGo](payasyougo.md) — A payment mode of a product discount that applies over a single billing period or multiple billing periods.
- [payUpFront](payupfront.md) — A payment mode of a product discount that applies the discount up front.
