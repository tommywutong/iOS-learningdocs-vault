---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/StoreKit.html
archived_at: '2026-07-18T02:56:16.576017Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# StoreKit Changes

## StoreKit

Modified SKDownload

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified SKDownload.contentIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified SKDownload.contentLength

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified SKDownload.contentURL

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified SKDownload.contentVersion

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified SKDownload.downloadState

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified SKDownload.error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified SKDownload.progress

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified SKDownload.timeRemaining

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified SKDownload.transaction

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified SKDownloadState [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified SKMutablePayment

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKMutablePayment.applicationUsername

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified SKMutablePayment.productIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKMutablePayment.quantity

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKMutablePayment.requestData

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKPayment

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKPayment.applicationUsername

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified SKPayment.init(product: SKProduct!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(product product: SKProduct!) ``` |
| To | ``` convenience init!(product product: SKProduct!) ``` |

Modified SKPayment.productIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKPayment.quantity

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKPayment.requestData

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKPaymentQueue

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKPaymentQueue.addPayment(SKPayment!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKPaymentQueue.addTransactionObserver(SKPaymentTransactionObserver!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKPaymentQueue.canMakePayments() -> Bool [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKPaymentQueue.cancelDownloads([AnyObject]!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified SKPaymentQueue.defaultQueue() -> Self! [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKPaymentQueue.finishTransaction(SKPaymentTransaction!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKPaymentQueue.pauseDownloads([AnyObject]!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified SKPaymentQueue.removeTransactionObserver(SKPaymentTransactionObserver!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKPaymentQueue.restoreCompletedTransactions()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKPaymentQueue.restoreCompletedTransactionsWithApplicationUsername(String!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified SKPaymentQueue.resumeDownloads([AnyObject]!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified SKPaymentQueue.startDownloads([AnyObject]!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified SKPaymentQueue.transactions

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKPaymentTransaction

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKPaymentTransaction.downloads

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified SKPaymentTransaction.error

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKPaymentTransaction.originalTransaction

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKPaymentTransaction.payment

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKPaymentTransaction.transactionDate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKPaymentTransaction.transactionIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKPaymentTransaction.transactionState

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKPaymentTransactionObserver.paymentQueue(SKPaymentQueue!, removedTransactions:[AnyObject]!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKPaymentTransactionObserver.paymentQueue(SKPaymentQueue!, restoreCompletedTransactionsFailedWithError: NSError!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKPaymentTransactionObserver.paymentQueue(SKPaymentQueue!, updatedDownloads:[AnyObject]!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified SKPaymentTransactionObserver.paymentQueue(SKPaymentQueue!, updatedTransactions:[AnyObject]!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKPaymentTransactionObserver.paymentQueueRestoreCompletedTransactionsFinished(SKPaymentQueue!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKPaymentTransactionState [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKProduct

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKProduct.downloadContentLengths

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified SKProduct.downloadContentVersion

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified SKProduct.downloadable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified SKProduct.localizedDescription

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKProduct.localizedTitle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKProduct.price

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKProduct.priceLocale

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKProduct.productIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKProductsRequest

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKProductsRequest.delegate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKProductsRequest.init(productIdentifiers: NSSet!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(productIdentifiers productIdentifiers: NSSet!) ``` | iOS 8.0 |
| To | ``` init!(productIdentifiers productIdentifiers: NSSet!) ``` | iOS 3.0 |

Modified SKProductsRequestDelegate.productsRequest(SKProductsRequest!, didReceiveResponse: SKProductsResponse!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKProductsResponse

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKProductsResponse.invalidProductIdentifiers

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKProductsResponse.products

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKReceiptRefreshRequest

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified SKReceiptRefreshRequest.receiptProperties

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified SKReceiptRefreshRequest.init(receiptProperties: [NSObject: AnyObject]!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(receiptProperties properties: [NSObject : AnyObject]!) ``` | iOS 8.0 |
| To | ``` init!(receiptProperties properties: [NSObject : AnyObject]!) ``` | iOS 7.0 |

Modified SKRequest

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKRequest.cancel()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKRequest.delegate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKRequest.start()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKRequestDelegate.request(SKRequest!, didFailWithError: NSError!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKRequestDelegate.requestDidFinish(SKRequest!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKStoreProductViewController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified SKStoreProductViewController.delegate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified SKStoreProductViewController.loadProductWithParameters([NSObject: AnyObject]!, completionBlock:((Bool, NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified SKStoreProductViewControllerDelegate.productViewControllerDidFinish(SKStoreProductViewController!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified SKDownloadTimeRemainingUnknown

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified SKErrorDomain

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKReceiptPropertyIsExpired

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified SKReceiptPropertyIsRevoked

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified SKReceiptPropertyIsVolumePurchase

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified SKStoreProductParameterITunesItemIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified SKTerminateForInvalidReceipt()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

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
