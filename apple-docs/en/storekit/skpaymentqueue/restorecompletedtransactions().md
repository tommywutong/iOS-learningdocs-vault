---
title: restoreCompletedTransactions()
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS 9.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpaymentqueue/restorecompletedtransactions()
source_url: 'https://developer.apple.com/documentation/storekit/skpaymentqueue/restorecompletedtransactions()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymentqueue/restorecompletedtransactions%28%29.json'
content_hash: 'sha256:b81a81a13ffa3d65'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKPaymentQueue](../skpaymentqueue.md)

# restoreCompletedTransactions()

<sub>Instance Method</sub>

Asks the payment queue to restore previously completed purchases.

> [!warning] Deprecated
> Use AppStore.sync().

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func restoreCompletedTransactions()
```

## Discussion

Use this method to restore finished transactions—that is, transactions for which you have already called [- finishTransaction:](<finishtransaction(__).md>). You call this method in one of the following situations:

- To install purchases on additional devices
- To restore purchases for an application that the user deleted and reinstalled

When you create a new product to be sold in your store, you choose whether that product can be restored or not. See the [In-App Purchase Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267) for more information.

The payment queue delivers a new transaction for each previously completed transaction that can be restored. Each transaction includes a copy of the original transaction.

After the transactions are delivered, the payment queue calls the observer’s [- paymentQueueRestoreCompletedTransactionsFinished:](<../skpaymenttransactionobserver/paymentqueuerestorecompletedtransactionsfinished(__).md>) method. If an error occurred while restoring transactions, the observer will be notified through its [- paymentQueue:restoreCompletedTransactionsFailedWithError:](<../skpaymenttransactionobserver/paymentqueue(__restorecompletedtransactionsfailedwitherror_).md>) method.

This method has no effect in the following situations:

- All transactions are unfinished.
- The user did not purchase anything that is restorable.
- You tried to restore items that are not restorable, such as a non-renewing subscription or a consumable product.
- Your app’s build version does not meet the guidelines for the `CFBundleVersion` key.

> [!important] Important
> If you are using the [In-App Purchase](../in-app-purchase.md) API and managing transactions using the [Transaction](../transaction.md) API, use [currentEntitlements](../transaction/currententitlements.md) to determine which in-app purchases the customer is currently entitled to. The [- restoreCompletedTransactions](<restorecompletedtransactions().md>) function doesn’t affect transactions in the [Transaction](../transaction.md) API. In rare cases when a user suspects the app isn’t showing all the transactions, call [sync()](<../appstore/sync().md>) in response to an explicit user action, like tapping a button.

## See Also

### Restoring Purchases

- [- restoreCompletedTransactionsWithApplicationUsername:](<restorecompletedtransactions(withapplicationusername_).md>) — Asks the payment queue to restore previously completed purchases, providing an opaque identifier for the user’s account. _(deprecated)_
