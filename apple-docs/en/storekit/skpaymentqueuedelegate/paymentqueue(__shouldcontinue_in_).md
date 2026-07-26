---
title: 'paymentQueue(_:shouldContinue:in:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（18.0 起废弃）, iPadOS 13.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.15+（15.0 起废弃）, tvOS 13.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skpaymentqueuedelegate/paymentqueue(_:shouldcontinue:in:)'
source_url: 'https://developer.apple.com/documentation/storekit/skpaymentqueuedelegate/paymentqueue(_:shouldcontinue:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymentqueuedelegate/paymentqueue%28_%3Ashouldcontinue%3Ain%3A%29.json'
content_hash: 'sha256:0845044256d512a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentQueueDelegate](../skpaymentqueuedelegate.md)

# paymentQueue(_:shouldContinue:in:)

<sub>Instance Method</sub>

Asks the delegate whether to continue the transaction if the device’s App Store storefront changes during a transaction.

> [!warning] Deprecated
> Pass Product.PurchaseOption.onStorefrontChange(shouldContinuePurchase:) to product.purchase(options:).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func paymentQueue(_ paymentQueue: SKPaymentQueue, shouldContinue transaction: SKPaymentTransaction, in newStorefront: SKStorefront) -> Bool
```

## Discussion

StoreKit calls this delegate method if the storefront changes while processing a transaction.

- Return `true` if you wish to continue the transaction within the updated storefront.
- Return `false` to stop the transaction. The transaction will fail with the error [SKErrorStoreProductNotAvailable](../skerror/code/storeproductnotavailable.md). In this case, consider displaying a message to the user indicating that the product isn’t available in the current storefront.

If the delegate isn’t implemented, [- paymentQueue:shouldContinueTransaction:inStorefront:](<paymentqueue(__shouldcontinue_in_).md>) defaults to `true`.

This call times out after approximately one second, defaulting to `false` and causing the transaction to fail. The delegate should return as quickly as possible. Don’t perform any networking calls in this method. Your app should cache product availability information locally before starting a transaction.

See [SKStorefront](../skstorefront.md) for more information.
