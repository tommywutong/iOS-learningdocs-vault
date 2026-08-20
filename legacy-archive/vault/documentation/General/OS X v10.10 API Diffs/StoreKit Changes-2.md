---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/modules/StoreKit.html
archived_at: '2026-07-15T07:34:57.527063Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# StoreKit Changes

## StoreKit (Added)

Added SKDownloadAdded SKDownload.contentIdentifierAdded SKDownload.contentLengthAdded SKDownload.contentURLAdded SKDownload.contentURLForProductID(String!) -> NSURL! [class]Added SKDownload.contentVersionAdded SKDownload.deleteContentForProductID(String!) [class]Added SKDownload.errorAdded SKDownload.progressAdded SKDownload.stateAdded SKDownload.timeRemainingAdded SKDownloadState [struct]Added SKDownloadState.init(_: Int)Added SKDownloadState.valueAdded SKMutablePaymentAdded SKMutablePayment.applicationUsernameAdded SKMutablePayment.productIdentifierAdded SKMutablePayment.quantityAdded SKMutablePayment.requestDataAdded SKPaymentAdded SKPayment.applicationUsernameAdded SKPayment.paymentWithProduct(SKProduct!) -> AnyObject! [class]Added SKPayment.productIdentifierAdded SKPayment.quantityAdded SKPayment.requestDataAdded SKPaymentQueueAdded SKPaymentQueue.addPayment(SKPayment!)Added SKPaymentQueue.addTransactionObserver(SKPaymentTransactionObserver!)Added SKPaymentQueue.canMakePayments() -> Bool [class]Added SKPaymentQueue.cancelDownloads([AnyObject]!)Added SKPaymentQueue.defaultQueue() -> SKPaymentQueue! [class]Added SKPaymentQueue.finishTransaction(SKPaymentTransaction!)Added SKPaymentQueue.pauseDownloads([AnyObject]!)Added SKPaymentQueue.removeTransactionObserver(SKPaymentTransactionObserver!)Added SKPaymentQueue.restoreCompletedTransactions()Added SKPaymentQueue.restoreCompletedTransactionsWithApplicationUsername(String!)Added SKPaymentQueue.resumeDownloads([AnyObject]!)Added SKPaymentQueue.startDownloads([AnyObject]!)Added SKPaymentQueue.transactionsAdded SKPaymentTransactionAdded SKPaymentTransaction.downloadsAdded SKPaymentTransaction.errorAdded SKPaymentTransaction.originalTransactionAdded SKPaymentTransaction.paymentAdded SKPaymentTransaction.transactionDateAdded SKPaymentTransaction.transactionIdentifierAdded SKPaymentTransaction.transactionStateAdded SKPaymentTransactionObserverAdded SKPaymentTransactionObserver.paymentQueue(SKPaymentQueue!, removedTransactions:[AnyObject]!)Added SKPaymentTransactionObserver.paymentQueue(SKPaymentQueue!, restoreCompletedTransactionsFailedWithError: NSError!)Added SKPaymentTransactionObserver.paymentQueue(SKPaymentQueue!, updatedDownloads:[AnyObject]!)Added SKPaymentTransactionObserver.paymentQueue(SKPaymentQueue!, updatedTransactions:[AnyObject]!)Added SKPaymentTransactionObserver.paymentQueueRestoreCompletedTransactionsFinished(SKPaymentQueue!)Added SKProductAdded SKProduct.contentLengthsAdded SKProduct.contentVersionAdded SKProduct.downloadableAdded SKProduct.localizedDescriptionAdded SKProduct.localizedTitleAdded SKProduct.priceAdded SKProduct.priceLocaleAdded SKProduct.productIdentifierAdded SKProductsRequestAdded SKProductsRequest.delegateAdded SKProductsRequest.init(productIdentifiers: NSSet!)Added SKProductsRequestDelegateAdded SKProductsRequestDelegate.productsRequest(SKProductsRequest!, didReceiveResponse: SKProductsResponse!)Added SKProductsResponseAdded SKProductsResponse.invalidProductIdentifiersAdded SKProductsResponse.productsAdded SKReceiptRefreshRequestAdded SKReceiptRefreshRequest.receiptPropertiesAdded SKReceiptRefreshRequest.init(receiptProperties: [NSObject: AnyObject]!)Added SKRequestAdded SKRequest.cancel()Added SKRequest.delegateAdded SKRequest.start()Added SKRequestDelegateAdded SKRequestDelegate.request(SKRequest!, didFailWithError: NSError!)Added SKRequestDelegate.requestDidFinish(SKRequest!)Added SKDownloadStateActiveAdded SKDownloadStateCancelledAdded SKDownloadStateFailedAdded SKDownloadStateFinishedAdded SKDownloadStatePausedAdded SKDownloadStateWaitingAdded SKErrorClientInvalidAdded SKErrorDomainAdded SKErrorPaymentCancelledAdded SKErrorPaymentInvalidAdded SKErrorPaymentNotAllowedAdded SKErrorUnknownAdded SKPaymentTransactionStateAdded SKPaymentTransactionStateDeferredAdded SKPaymentTransactionStateFailedAdded SKPaymentTransactionStatePurchasedAdded SKPaymentTransactionStatePurchasingAdded SKPaymentTransactionStateRestoredAdded SKReceiptPropertyIsExpiredAdded SKReceiptPropertyIsRevokedAdded SKReceiptPropertyIsVolumePurchase

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
