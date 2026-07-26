---
title: SKPaymentTransactionObserver
framework: StoreKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS 9.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skpaymenttransactionobserver
source_url: 'https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skpaymenttransactionobserver.json'
content_hash: 'sha256:d22a450a9b6e2037'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKPaymentTransactionObserver

<sub>Protocol</sub>

A set of methods that process transactions, unlock purchased functionality, and continue promoted In-App Purchases.

> [!warning] Deprecated
> Use StoreKit 2 Transaction APIs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol SKPaymentTransactionObserver : NSObjectProtocol
```

## Overview

Observers of [SKPaymentQueue](skpaymentqueue.md) objects implement the methods of this protocol.

The system calls an observer when the queue updates or removes transactions. An observer needs to process all successful transactions, unlock the functionality the user purchases, and then finish the transaction by calling the payment queue’s [- finishTransaction:](<skpaymentqueue/finishtransaction(__).md>) method.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Handling transactions

- [- paymentQueue:updatedTransactions:](<skpaymenttransactionobserver/paymentqueue(__updatedtransactions_).md>) — Tells an observer that one or more transactions have been updated. _(deprecated)_
- [- paymentQueue:removedTransactions:](<skpaymenttransactionobserver/paymentqueue(__removedtransactions_).md>) — Tells an observer that one or more transactions have been removed from the queue. _(deprecated)_

### Restoring transactions

- [- paymentQueue:restoreCompletedTransactionsFailedWithError:](<skpaymenttransactionobserver/paymentqueue(__restorecompletedtransactionsfailedwitherror_).md>) — Tells the observer that an error occurred while restoring transactions. _(deprecated)_
- [- paymentQueueRestoreCompletedTransactionsFinished:](<skpaymenttransactionobserver/paymentqueuerestorecompletedtransactionsfinished(__).md>) — Tells the observer that the payment queue has finished sending restored transactions. _(deprecated)_

### Handling promoted in-app purchases

- [Promoting In-App Purchases](promoting-in-app-purchases.md) — Show promoted In-App Purchases on your product page and handle purchases that customers initiate on the App Store.
- [- paymentQueue:shouldAddStorePayment:forProduct:](<skpaymenttransactionobserver/paymentqueue(__shouldaddstorepayment_for_).md>) — Tells the observer when a user initiates an in-app purchase from the App Store. _(deprecated)_

### Revoking entitlements

- [- paymentQueue:didRevokeEntitlementsForProductIdentifiers:](<skpaymenttransactionobserver/paymentqueue(__didrevokeentitlementsforproductidentifiers_).md>) — Tells an observer that the customer is no longer entitled to one or more Family Sharing purchases. _(deprecated)_

### Changing the storefront

- [- paymentQueueDidChangeStorefront:](<skpaymenttransactionobserver/paymentqueuedidchangestorefront(__).md>) — Tells the observer that the storefront for the payment queue has changed. _(deprecated)_

### Handling download actions

- [- paymentQueue:updatedDownloads:](<skpaymenttransactionobserver/paymentqueue(__updateddownloads_).md>) — Tells the observer that the payment queue has updated one or more download objects. _(deprecated)_

## See Also

### Essentials

- [Setting up the transaction observer for the payment queue](setting-up-the-transaction-observer-for-the-payment-queue.md) — Enable your app to receive and handle transactions by adding an observer.
- [Offering, completing, and restoring in-app purchases](offering-completing-and-restoring-in-app-purchases.md) — Fetch, display, purchase, validate, and finish transactions in your app.
- [SKPaymentQueue](skpaymentqueue.md) — A queue of payment transactions for the App Store to process. _(deprecated)_
- [SKPaymentQueueDelegate](skpaymentqueuedelegate.md) — The protocol that provides information needed to complete transactions. _(deprecated)_
- [SKRequest](skrequest.md) — An abstract class that represents a request to the App Store. _(deprecated)_
