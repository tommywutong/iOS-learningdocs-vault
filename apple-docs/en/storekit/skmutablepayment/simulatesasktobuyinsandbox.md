---
title: simulatesAskToBuyInSandbox
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.3+（18.0 起废弃）, iPadOS 8.3+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.14+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skmutablepayment/simulatesasktobuyinsandbox
source_url: 'https://developer.apple.com/documentation/storekit/skmutablepayment/simulatesasktobuyinsandbox'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skmutablepayment/simulatesasktobuyinsandbox.json'
content_hash: 'sha256:8aaaa2c7cbb37e46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKMutablePayment](../skmutablepayment.md)

# simulatesAskToBuyInSandbox

<sub>Instance Property</sub>

A Boolean value that produces an “ask to buy” flow for this payment in the sandbox.

> [!warning] Deprecated
> Create a Product.PurchaseOption.simulatesAskToBuyInSandbox to use in Product.purchase(confirmIn:options:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var simulatesAskToBuyInSandbox: Bool { get set }
```
