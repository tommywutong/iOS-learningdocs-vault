---
title: SKPaymentQueue
framework: StoreKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS 9.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpaymentqueue
source_url: 'https://developer.apple.com/documentation/storekit/skpaymentqueue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymentqueue.json'
content_hash: 'sha256:b1ca7510fcdc6912'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKPaymentQueue

<sub>Class</sub>

A queue of payment transactions for the App Store to process.

> [!warning] Deprecated
> No longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class SKPaymentQueue
```

## Overview

The payment queue communicates with the App Store and presents a user interface so that the user can authorize payment. The contents of the queue are persistent between launches of your app.

To process a payment, first add at least one observer object ([SKPaymentTransactionObserver](skpaymenttransactionobserver.md)) to the queue (see [- addTransactionObserver:](<skpaymentqueue/add(__)-5ciz2.md>)). Then, add a payment object ([SKPayment](skpayment.md)) for the item the user wants to purchase. Each time you add a payment object, the queue creates a transaction object ([SKPaymentTransaction](skpaymenttransaction.md)) to process that payment and enqueues it to be processed. After payment is fulfilled, the queue updates the transaction object and then calls any observer objects to provide them the updated transaction. Your observer should process the transaction and then remove it from the queue.

The exact mechanism you use to process a processed transaction depends on the design of your app and the product being purchased. Here are a few common examples:

- If the product is a feature already built into your app, your app enables the feature to process the transaction.
- If the product includes downloadable content provided by the App Store, your app retrieves the [SKDownload](skdownload.md) objects from the transaction and ask the payment queue to download them. You provide the actual content files to be served by the App Store to App Store Connect when you create the product information.
- If the product represents downloadable content provided by your own server, your app might open a network connection to your server and download the content from there.

For more information on designing the payment processing portion of your app, see [In-App Purchase Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html#//apple_ref/doc/uid/TP40008267).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Determining Whether the User Can Make Payments

- [+ canMakePayments](<skpaymentqueue/canmakepayments().md>) — A method that indicates whether the person can make purchases. _(deprecated)_

### Determining Store Content

- [storefront](skpaymentqueue/storefront.md) — The App Store storefront of the device. _(deprecated)_

### Getting the Queue

- [+ defaultQueue](<skpaymentqueue/default().md>) — Returns the default payment queue instance. _(deprecated)_

### Adding, Getting, and Removing Observers

- [- addTransactionObserver:](<skpaymentqueue/add(__)-5ciz2.md>) — Adds an observer to the payment queue. _(deprecated)_
- [transactionObservers](skpaymentqueue/transactionobservers.md) — An array of all active payment queue observers. _(deprecated)_
- [- removeTransactionObserver:](<skpaymentqueue/remove(__).md>) — Removes an observer from the payment queue. _(deprecated)_

### Managing Transactions

- [delegate](skpaymentqueue/delegate.md) — A delegate that provides information needed to complete transactions. _(deprecated)_
- [transactions](skpaymentqueue/transactions.md) — Returns an array of pending transactions. _(deprecated)_
- [- addPayment:](<skpaymentqueue/add(__)-4vct1.md>) — Adds a payment request to the queue. _(deprecated)_
- [- finishTransaction:](<skpaymentqueue/finishtransaction(__).md>) — Notifies the App Store that the app finished processing the transaction. _(deprecated)_

### Restoring Purchases

- [- restoreCompletedTransactions](<skpaymentqueue/restorecompletedtransactions().md>) — Asks the payment queue to restore previously completed purchases. _(deprecated)_
- [- restoreCompletedTransactionsWithApplicationUsername:](<skpaymentqueue/restorecompletedtransactions(withapplicationusername_).md>) — Asks the payment queue to restore previously completed purchases, providing an opaque identifier for the user’s account. _(deprecated)_

### Showing Price Consent

- [- showPriceConsentIfNeeded](<skpaymentqueue/showpriceconsentifneeded().md>) — Asks the system to display the price consent sheet if the user hasn’t yet responded to a subscription price increase. _(deprecated)_

### Redeeming Codes

- [- presentCodeRedemptionSheet](<skpaymentqueue/presentcoderedemptionsheet().md>) — Displays a sheet that enables customers to redeem offer codes that you configure in App Store Connect. _(deprecated)_

### Downloading Content

- [- startDownloads:](<skpaymentqueue/start(__).md>) — Adds a set of downloads to the download list. _(deprecated)_
- [- cancelDownloads:](<skpaymentqueue/cancel(__).md>) — Removes a set of downloads from the download list. _(deprecated)_
- [- pauseDownloads:](<skpaymentqueue/pause(__).md>) — Pauses a set of downloads. _(deprecated)_
- [- resumeDownloads:](<skpaymentqueue/resume(__).md>) — Resumes a set of downloads. _(deprecated)_

## See Also

### Essentials

- [Setting up the transaction observer for the payment queue](setting-up-the-transaction-observer-for-the-payment-queue.md) — Enable your app to receive and handle transactions by adding an observer.
- [Offering, completing, and restoring in-app purchases](offering-completing-and-restoring-in-app-purchases.md) — Fetch, display, purchase, validate, and finish transactions in your app.
- [SKPaymentTransactionObserver](skpaymenttransactionobserver.md) — A set of methods that process transactions, unlock purchased functionality, and continue promoted In-App Purchases. _(deprecated)_
- [SKPaymentQueueDelegate](skpaymentqueuedelegate.md) — The protocol that provides information needed to complete transactions. _(deprecated)_
- [SKRequest](skrequest.md) — An abstract class that represents a request to the App Store. _(deprecated)_
