---
title: Choosing a receipt validation technique
framework: StoreKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/choosing-a-receipt-validation-technique
source_url: 'https://developer.apple.com/documentation/storekit/choosing-a-receipt-validation-technique'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/choosing-a-receipt-validation-technique.json'
content_hash: 'sha256:0c69ba7059a8ca9a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md) · [In-App Purchase](in-app-purchase.md) · [Original API for In-App Purchase](original-api-for-in-app-purchase.md)

# Choosing a receipt validation technique

<sub>Article</sub>

Select the type of receipt validation, on the device or on your server, that works for your app.

## Overview

> [!note] Note
> The receipt isn’t necessary if you use [AppTransaction](apptransaction.md) to validate the app download, or [Transaction](transaction.md) to validate in-app purchases. Only use the receipt if your app uses the [Original API for In-App Purchase](original-api-for-in-app-purchase.md), or needs the receipt to validate the app download because it can’t use [AppTransaction](apptransaction.md).

An App Store receipt provides a record of the sale of an app and any purchases the person makes within the app. You can authenticate purchased content by adding receipt validation code to your app or server. Receipt validation requires an understanding of secure coding techniques to employ a solution that’s secure and unique to your app.

### Choose a validation technique

There are two ways to verify a receipt’s authenticity:

- Locally, on the device. Validating receipts locally requires code that reads and validates a binary file that Apple encodes and signs as a PKCS #7 container. For more information, see [Validating receipts on the device](../appstorereceipts/validating-receipts-on-the-device.md).
- On your server with the App Store. Validating receipts with the App Store requires secure connections between your app and your server, and between your server and the App Store. For more information, see [Validating receipts with the App Store](validating-receipts-with-the-app-store.md).

Compare the approaches and determine the method that best fits your app and your infrastructure. You can also choose to implement both approaches. For managing auto-renewable subscriptions, see the following table for the key advantages that server-side receipt validation provides over on-device receipt validation:

| Capability | On-device validation | Server-side validation |
|---|---|---|
| Validates authenticity of receipt | Yes | Yes |
| Includes subscription renewal transactions | Yes | Yes |
| Includes additional subscription information | No | Yes |
| Resistant to device clock change | No | Yes |

Receipts contain non-consumable in-app purchases, auto-renewable subscriptions, and non-renewing subscriptions indefinitely. Consumable in-app purchases remain in the receipt until you call [- finishTransaction:](<skpaymentqueue/finishtransaction(__).md>). You may choose to maintain and manage records of consumable in-app purchases on your server.

### Get the latest receipt

The App Store updates receipts immediately after completed purchases. When you call [verifyReceipt](../appstorereceipts/verify-receipt.md) from your server, the App Store returns the latest transaction information, regardless of the contents of the receipt you send in the request.

On the device, the system updates the receipt immediately when it has an internet connection, and any of the following occur:

- The customer completes an in-app purchase.
- The app launches its transaction observer ([SKPaymentTransactionObserver](skpaymenttransactionobserver.md)) and has unfinished transactions or subscription renewals.
- The app calls [- restoreCompletedTransactions](<skpaymentqueue/restorecompletedtransactions().md>) or [- restoreCompletedTransactionsWithApplicationUsername:](<skpaymentqueue/restorecompletedtransactions(withapplicationusername_).md>) to restore transactions.
- The app sends a request to [SKReceiptRefreshRequest](skreceiptrefreshrequest.md) to get a receipt if the receipt is invalid or missing.

Transactions can also occur at times when the app isn’t running. When necessary, call [- restoreCompletedTransactions](<skpaymentqueue/restorecompletedtransactions().md>) to ensure the receipt you’re working with is up-to-date. For example, if a customer purchases an auto-renewable subscription on another device, call this method to get those transactions and update the receipt.

To ensure that your app receives all transactions, add the transaction observer, [- addTransactionObserver:](<skpaymentqueue/add(__)-5ciz2.md>), at app launch time. For more information, see [Setting up the transaction observer for the payment queue](setting-up-the-transaction-observer-for-the-payment-queue.md).

> [!note] Related Sessions from WWDC 2018
> Session 705: [Engineering Subscriptions](https://developer.apple.com/videos/play/wwdc2018/705/)

## See Also

### Purchase validation

- [Validating receipts with the App Store](validating-receipts-with-the-app-store.md) — Verify transactions with the App Store on a secure server.
- [appStoreReceiptURL](../foundation/bundle/appstorereceipturl.md) — The file URL for the bundle’s App Store receipt. _(deprecated)_
- [SKReceiptRefreshRequest](skreceiptrefreshrequest.md) — A request to the App Store to get the app receipt, which represents the customer’s transactions with your app. _(deprecated)_
