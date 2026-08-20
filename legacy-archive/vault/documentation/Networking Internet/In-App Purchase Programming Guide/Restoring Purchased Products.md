---
title: In-App Purchase Programming Guide
apple_id: TP40008267
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: StoreKit
published: '2018-02-06'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Chapters/Restoring.html
archived_at: '2026-07-27T06:57:07.403912Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [In-App Purchase Programming Guide](About%20In-App%20Purchase.md)


[Next](Preparing%20for%20App%20Review.md)[Previous](Working%20with%20Subscriptions.md)

# Restoring Purchased Products

Users restore transactions to maintain access to content they’ve already purchased. For example, when they upgrade to a new phone, they don’t lose all of the items they purchased on the old phone. Include some mechanism in your app to let the user restore their purchases, such as a Restore Purchases button. Restoring purchases prompts for the user’s App Store credentials, which interrupts the flow of your app: because of this, don’t automatically restore purchases, especially not every time your app is launched.

In most cases, all your app needs to do is refresh its receipt and deliver the products in its receipt. The refreshed receipt contains a record of the user’s purchases in this app, on this device or any other device. However, some apps need to take an alternate approach for one of the following reasons:

- If you use Apple-hosted content, restoring completed transactions gives your app the transaction objects it uses to download the content.
- If you need to support versions of iOS earlier than iOS 7, where the app receipt isn’t available, restore completed transactions instead.
- If your app uses non-renewing subscriptions, your app is responsible for the restoration process.

Refreshing the receipt asks the App Store for the latest copy of the receipt. Refreshing a receipt does not create any new transactions. Although you should avoid refreshing multiple times in a row, this action would have same result as refreshing it just once.

Restoring completed transactions creates a new transaction for every completed transaction the user made, essentially replaying history for your transaction queue observer. While transactions are being restored, your app maintains its own state to keep track of why it’s restoring completed transactions and how it needs to handle them. Restoring multiple times creates multiple restored transactions for each completed transaction.

__Note:__ If the user attempts to purchase a product that’s already been purchased, rather than using your app’s restoration interface, the App Store creates a regular transaction instead of a restore transaction. The user isn’t charged again for the product. Treat these transactions the exact same way you treated the original transactions.

Give the user an appropriate level of control over what content is redownloaded. For example, don’t download three years worth of daily newspapers or hundreds of megabytes worth of game levels all at once.

## Refreshing the App Receipt

Create a receipt refresh request, set a delegate, and start the request. The request supports optional properties for obtaining receipts in various states during testing such as expired receipts—for details, see the values for the [initWithReceiptProperties:](https://developer.apple.com/documentation/storekit/skreceiptrefreshrequest/1506038-init) method of [SKReceiptRefreshRequest](https://developer.apple.com/documentation/storekit/skreceiptrefreshrequest).

```
request = [[SKReceiptRefreshRequest alloc] init];
request.delegate = self;
[request start];
```

After the receipt is refreshed, examine it and deliver any products that were added.

## Restoring Completed Transactions

Your app starts the process by calling the [restoreCompletedTransactions](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506123-restorecompletedtransactions) method of [SKPaymentQueue](https://developer.apple.com/documentation/storekit/skpaymentqueue). This sends a request to the App Store to restore all of your app’s completed transactions. If your app sets a value for the `applicationUsername` property of its payment requests, as described in [Detecting Irregular Activity](Requesting%20Payment.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4denrxfvbuqnbnknltm), use the [restoreCompletedTransactionsWithApplicationUsername:](https://developer.apple.com/documentation/storekit/skpaymentqueue/1505992-restorecompletedtransactions) method to provide the same information when restoring transactions.

The App Store generates a new transaction for each transaction that was previously completed. The restored transaction has a reference to the original transaction: instances of [SKPaymentTransaction](https://developer.apple.com/documentation/storekit/skpaymenttransaction) have a [originalTransaction](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411284-originaltransaction) property, and the entries in the receipt have an Original Transaction Identifier field.

__Note:__ The date fields have slightly different meanings for restored purchases. For details, see the Purchase Date and Original Purchase Date fields in _[Receipt Validation Programming Guide](../../../releasenotes/General/Receipt%20Validation%20Programming%20Guide/About%20Receipt%20Validation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknzt)_.

Your transaction queue observer is called with a status of [SKPaymentTransactionStateRestored](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/skpaymenttransactionstaterestored) for each restored transaction, as described in [Waiting for the App Store to Process Transactions](Delivering%20Products.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4denrxfvbuqnjnknlti). The action you take at this point depends on the design of your app.

- If your app uses the app receipt and doesn’t have Apple-hosted content, this code isn’t needed because your app doesn’t restore completed transactions. Finish any restored transactions immediately.
- If your app uses the app receipt and has Apple-hosted content, let the user select which products to restore before starting the restoration process. During restoration, re-download the user-selected content and finish any other transactions immediately.

  ```
  NSMutableArray *productIDsToRestore = <# From the user #>;
  SKPaymentTransaction *transaction = <# Current transaction #>;

  if ([productIDsToRestore containsObject:transaction.transactionIdentifier]) {
      // Re-download the Apple-hosted content, then finish the transaction
      // and remove the product identifier from the array of product IDs.
  } else {
      [[SKPaymentQueue defaultQueue] finishTransaction:transaction];
  }
  ```
- If your app doesn’t use the app receipt, it examines all completed transactions as they’re restored. It uses a similar code path to the original purchase logic to make the product available and then finishes the transaction.

  Apps with more than a few products, especially products with associated content, let the user select which products to restore instead of restoring everything all at once. These apps keep track of which completed transactions need to be processed as they’re restored and which transactions can be ignored by finishing them immediately.

[Next](Preparing%20for%20App%20Review.md)[Previous](Working%20with%20Subscriptions.md)
