---
title: 'paymentQueue(_:shouldAddStorePayment:for:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+（18.0 起废弃）, iPadOS 11.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, macOS 11.0+（15.0 起废弃）, tvOS 11.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skpaymenttransactionobserver/paymentqueue(_:shouldaddstorepayment:for:)'
source_url: 'https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/paymentqueue(_:shouldaddstorepayment:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymenttransactionobserver/paymentqueue%28_%3Ashouldaddstorepayment%3Afor%3A%29.json'
content_hash: 'sha256:4164b4fc76218c92'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentTransactionObserver](../skpaymenttransactionobserver.md)

# paymentQueue(_:shouldAddStorePayment:for:)

<sub>Instance Method</sub>

Tells the observer when a user initiates an in-app purchase from the App Store.

> [!warning] Deprecated
> Use PurchaseIntent.intents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func paymentQueue(_ queue: SKPaymentQueue, shouldAddStorePayment payment: SKPayment, for product: SKProduct) -> Bool
```

## Parameters

- `queue` — The payment queue the app uses to make the payment request.

- `payment` — The payment request.

- `product` — The in-app purchase product.

## Return Value

Return `true` to continue the transaction in your app.

## Discussion

Return `false` to defer or cancel the transaction.

If you return `false`, you can continue the transaction later by manually adding the [SKPayment](../skpayment.md) `payment` to the [SKPaymentQueue](../skpaymentqueue.md) `queue`.

## Discussion

The system calls this delegate method when the user starts an in-app purchase in the App Store, and the transaction continues in your app. Specifically, if your app is already installed, StoreKit calls this method automatically.

If your app isn’t installed when the user starts the in-app purchase in the App Store, the user receives a notification when the app installation is complete. StoreKit calls this method when the user taps the notification. Otherwise, if the user opens the app manually, StoreKit calls this method only if they open the app soon after they initiate the purchase.

> [!important] Important
> To enable promoted in-app purchases, your app needs to use either [PurchaseIntent](../purchaseintent.md) (starting in iOS 16.4) or [- paymentQueue:shouldAddStorePayment:forProduct:](<paymentqueue(__shouldaddstorepayment_for_).md>) (starting in iOS 11). Don’t use both at the same time. If necessary, use conditional compilation to identify the OS version the app is running in. For more information, see [Running code on a specific platform or OS version](../../xcode/running-code-on-a-specific-version.md).

For more information, see [Promoting In-App Purchases](../promoting-in-app-purchases.md).

## See Also

### Handling promoted in-app purchases

- [Promoting In-App Purchases](../promoting-in-app-purchases.md) — Show promoted In-App Purchases on your product page and handle purchases that customers initiate on the App Store.
