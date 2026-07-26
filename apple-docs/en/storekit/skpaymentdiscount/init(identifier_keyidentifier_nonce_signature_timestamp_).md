---
title: 'init(identifier:keyIdentifier:nonce:signature:timestamp:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.2+（18.0 起废弃）, iPadOS 12.2+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.14.4+（15.0 起废弃）, tvOS 12.2+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skpaymentdiscount/init(identifier:keyidentifier:nonce:signature:timestamp:)'
source_url: 'https://developer.apple.com/documentation/storekit/skpaymentdiscount/init(identifier:keyidentifier:nonce:signature:timestamp:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymentdiscount/init%28identifier%3Akeyidentifier%3Anonce%3Asignature%3Atimestamp%3A%29.json'
content_hash: 'sha256:5e3078bbbfa14c74'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentDiscount](../skpaymentdiscount.md)

# init(identifier:keyIdentifier:nonce:signature:timestamp:)

<sub>Initializer</sub>

Initializes the payment discount with a signature and the parameters used by the signature.

> [!warning] Deprecated
> Create a Product.PurchaseOption.promotionalOffer to use in Product.purchase(confirmIn:options:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(identifier: String, keyIdentifier: String, nonce: UUID, signature: String, timestamp: NSNumber)
```
