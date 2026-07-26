---
title: storefront
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+（18.0 起废弃）, iPadOS 13.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.15+（15.0 起废弃）, tvOS 13.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpaymentqueue/storefront
source_url: 'https://developer.apple.com/documentation/storekit/skpaymentqueue/storefront'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymentqueue/storefront.json'
content_hash: 'sha256:3704ed4e70f338b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentQueue](../skpaymentqueue.md)

# storefront

<sub>Instance Property</sub>

The App Store storefront of the device.

> [!warning] Deprecated
> Use Storefront.current.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var storefront: SKStorefront? { get }
```

## Discussion

The storefront information tells you the device’s App Store region. You can use this information to display products that your app makes available in specific regions. You maintain your own list of product identifiers and the storefronts in which you make them available.

If the storefront changes during a transaction, StoreKit notifies your app by calling the [- paymentQueueDidChangeStorefront:](<../skpaymenttransactionobserver/paymentqueuedidchangestorefront(__).md>) method of the [SKPaymentTransactionObserver](../skpaymenttransactionobserver.md) protocol. Implement [- paymentQueue:shouldContinueTransaction:inStorefront:](<../skpaymentqueuedelegate/paymentqueue(__shouldcontinue_in_).md>) to indicate whether the transaction should continue with the new storefront.

> [!important] Important
> [storefront](storefront.md) is a synchronous API that may take significant time to return. Don’t use [storefront](storefront.md) in a time-sensitive thread, such as during app launch. To get asynchronous behavior, dispatch it to a separate queue, or use the asynchronous [current](../storefront/current.md) property of [Storefront](../storefront.md) instead.
