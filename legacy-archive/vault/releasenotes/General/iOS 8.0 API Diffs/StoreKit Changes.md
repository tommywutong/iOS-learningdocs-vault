---
title: iOS 8.0 API Diffs
apple_id: TP40014455
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS80APIDiffs/frameworks/StoreKit.html
archived_at: '2026-07-18T02:56:01.200935Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.0 API Diffs](iOS%207.1%20to%20iOS%208.0%20API%20Differences.md)


# StoreKit Changes

## StoreKit

SKPayment.hModified [+[SKPayment paymentWithProduct:]](https://developer.apple.com/documentation/storekit/skpayment/1506008-init)

|  | Declaration |
| --- | --- |
| From | ``` + (id)paymentWithProduct:(SKProduct *)product ``` |
| To | ``` + (instancetype)paymentWithProduct:(SKProduct *)product ``` |

SKPaymentQueue.hModified [+[SKPaymentQueue defaultQueue]](https://developer.apple.com/documentation/storekit/skpaymentqueue/1505990-default)

|  | Declaration |
| --- | --- |
| From | ``` + (SKPaymentQueue *)defaultQueue ``` |
| To | ``` + (instancetype)defaultQueue ``` |

Modified [-[SKPaymentTransactionObserver paymentQueue:removedTransactions:]](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/1505994-paymentqueue)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[SKPaymentTransactionObserver paymentQueue:restoreCompletedTransactionsFailedWithError:]](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/1506063-paymentqueue)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[SKPaymentTransactionObserver paymentQueue:updatedDownloads:]](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/1506073-paymentqueue)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[SKPaymentTransactionObserver paymentQueueRestoreCompletedTransactionsFinished:]](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/1506101-paymentqueuerestorecompletedtran)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

SKPaymentTransaction.hAdded [SKPaymentTransactionStateDeferred](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/deferred)SKProductsRequest.hModified [-[SKProductsRequest initWithProductIdentifiers:]](https://developer.apple.com/documentation/storekit/skproductsrequest/1506172-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithProductIdentifiers:(NSSet *)productIdentifiers ``` |
| To | ``` - (instancetype)initWithProductIdentifiers:(NSSet *)productIdentifiers ``` |

SKReceiptRefreshRequest.hModified [-[SKReceiptRefreshRequest initWithReceiptProperties:]](https://developer.apple.com/documentation/storekit/skreceiptrefreshrequest/1506038-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithReceiptProperties:(NSDictionary *)properties ``` |
| To | ``` - (instancetype)initWithReceiptProperties:(NSDictionary *)properties ``` |

SKRequest.hModified [-[SKRequestDelegate request:didFailWithError:]](https://developer.apple.com/documentation/storekit/skrequestdelegate/1385536-request)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[SKRequestDelegate requestDidFinish:]](https://developer.apple.com/documentation/storekit/skrequestdelegate/1385532-requestdidfinish)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

SKStoreProductViewController.hAdded [SKStoreProductParameterAffiliateToken](https://developer.apple.com/documentation/storekit/skstoreproductparameteraffiliatetoken)Added [SKStoreProductParameterCampaignToken](https://developer.apple.com/documentation/storekit/skstoreproductparametercampaigntoken)Modified [-[SKStoreProductViewControllerDelegate productViewControllerDidFinish:]](https://developer.apple.com/documentation/storekit/skstoreproductviewcontrollerdelegate/1620620-productviewcontrollerdidfinish)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

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
