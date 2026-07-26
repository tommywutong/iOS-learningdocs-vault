---
title: 'paymentQueueDidChangeStorefront(_:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（18.0 起废弃）, iPadOS 13.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.15+（15.0 起废弃）, tvOS 13.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skpaymenttransactionobserver/paymentqueuedidchangestorefront(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/paymentqueuedidchangestorefront(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymenttransactionobserver/paymentqueuedidchangestorefront%28_%3A%29.json'
content_hash: 'sha256:9ed77db86f63672f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentTransactionObserver](../skpaymenttransactionobserver.md)

# paymentQueueDidChangeStorefront(_:)

<sub>Instance Method</sub>

Tells the observer that the storefront for the payment queue has changed.

> [!warning] Deprecated
> Use Storefront.updates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func paymentQueueDidChangeStorefront(_ queue: SKPaymentQueue)
```

## Discussion

See [SKStorefront](../skstorefront.md) for more information.
