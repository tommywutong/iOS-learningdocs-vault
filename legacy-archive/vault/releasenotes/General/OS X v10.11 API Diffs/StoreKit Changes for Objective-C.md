---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/StoreKit.html
archived_at: '2026-07-18T02:53:14.267607Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# StoreKit Changes for Objective-C

### StoreKit

#### SKDownload.h

Added [SKDownload.transaction](https://developer.apple.com/documentation/storekit/skdownload/1458949-transaction)Modified [SKDownload.contentIdentifier](https://developer.apple.com/documentation/storekit/skdownload/1458941-contentidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *contentIdentifier ``` |
| To | ``` @property(readonly, nonnull) NSString *contentIdentifier ``` |

Modified [SKDownload.contentLength](https://developer.apple.com/documentation/storekit/skdownload/1458932-contentlength)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, readonly) NSNumber *contentLength ``` |
| To | ``` @property(copy, readonly, nonnull) NSNumber *contentLength ``` |

Modified [SKDownload.contentURL](https://developer.apple.com/documentation/storekit/skdownload/1458930-contenturl)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, readonly) NSURL *contentURL ``` |
| To | ``` @property(copy, readonly, nullable) NSURL *contentURL ``` |

Modified [+[SKDownload contentURLForProductID:]](https://developer.apple.com/documentation/storekit/skdownload/1458924-contenturlforproductid)

|  | Declaration |
| --- | --- |
| From | ``` + (NSURL *)contentURLForProductID:(NSString *)productID ``` |
| To | ``` + (NSURL * _Nullable)contentURLForProductID:(NSString * _Nonnull)productID ``` |

Modified [SKDownload.contentVersion](https://developer.apple.com/documentation/storekit/skdownload/1458916-contentversion)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, readonly) NSString *contentVersion ``` |
| To | ``` @property(copy, readonly, nullable) NSString *contentVersion ``` |

Modified [+[SKDownload deleteContentForProductID:]](https://developer.apple.com/documentation/storekit/skdownload/1458926-deletecontent)

|  | Declaration |
| --- | --- |
| From | ``` + (void)deleteContentForProductID:(NSString *)productID ``` |
| To | ``` + (void)deleteContentForProductID:(NSString * _Nonnull)productID ``` |

Modified [SKDownload.error](https://developer.apple.com/documentation/storekit/skdownload/1458914-error)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, readonly) NSError *error ``` |
| To | ``` @property(copy, readonly, nullable) NSError *error ``` |

#### SKPayment.h

Modified [SKMutablePayment.applicationUsername](https://developer.apple.com/documentation/storekit/skmutablepayment/1506088-applicationusername)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy, readwrite) NSString *applicationUsername ``` |
| To | ``` @property(nonatomic, copy, readwrite, nullable) NSString *applicationUsername ``` |

Modified [SKMutablePayment.productIdentifier](https://developer.apple.com/documentation/storekit/skmutablepayment/1505983-productidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, readwrite) NSString *productIdentifier ``` |
| To | ``` @property(copy, readwrite, nonnull) NSString *productIdentifier ``` |

Modified [SKMutablePayment.requestData](https://developer.apple.com/documentation/storekit/skmutablepayment/1505974-requestdata)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, readwrite) NSData *requestData ``` |
| To | ``` @property(copy, readwrite, nullable) NSData *requestData ``` |

Modified [SKPayment.applicationUsername](https://developer.apple.com/documentation/storekit/skpayment/1506116-applicationusername)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy, readonly) NSString *applicationUsername ``` |
| To | ``` @property(nonatomic, copy, readonly, nullable) NSString *applicationUsername ``` |

Modified [+[SKPayment paymentWithProduct:]](https://developer.apple.com/documentation/storekit/skpayment/1506008-init)

|  | Declaration |
| --- | --- |
| From | ``` + (id)paymentWithProduct:(SKProduct *)product ``` |
| To | ``` + (id _Nonnull)paymentWithProduct:(SKProduct * _Nonnull)product ``` |

Modified [SKPayment.productIdentifier](https://developer.apple.com/documentation/storekit/skpayment/1506155-productidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, readonly) NSString *productIdentifier ``` |
| To | ``` @property(copy, readonly, nonnull) NSString *productIdentifier ``` |

Modified [SKPayment.requestData](https://developer.apple.com/documentation/storekit/skpayment/1506159-requestdata)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, readonly) NSData *requestData ``` |
| To | ``` @property(copy, readonly, nullable) NSData *requestData ``` |

#### SKPaymentQueue.h

Modified [-[SKPaymentQueue addPayment:]](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506036-add)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addPayment:(SKPayment *)payment ``` |
| To | ``` - (void)addPayment:(SKPayment * _Nonnull)payment ``` |

Modified [-[SKPaymentQueue addTransactionObserver:]](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506042-add)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addTransactionObserver:(id<SKPaymentTransactionObserver>)observer ``` |
| To | ``` - (void)addTransactionObserver:(id<SKPaymentTransactionObserver> _Nonnull)observer ``` |

Modified [-[SKPaymentQueue cancelDownloads:]](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506092-cancel)

|  | Declaration |
| --- | --- |
| From | ``` - (void)cancelDownloads:(NSArray *)downloads ``` |
| To | ``` - (void)cancelDownloads:(NSArray<SKDownload *> * _Nonnull)downloads ``` |

Modified [+[SKPaymentQueue defaultQueue]](https://developer.apple.com/documentation/storekit/skpaymentqueue/1505990-default)

|  | Declaration |
| --- | --- |
| From | ``` + (SKPaymentQueue *)defaultQueue ``` |
| To | ``` + (SKPaymentQueue * _Nonnull)defaultQueue ``` |

Modified [-[SKPaymentQueue finishTransaction:]](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506003-finishtransaction)

|  | Declaration |
| --- | --- |
| From | ``` - (void)finishTransaction:(SKPaymentTransaction *)transaction ``` |
| To | ``` - (void)finishTransaction:(SKPaymentTransaction * _Nonnull)transaction ``` |

Modified [-[SKPaymentQueue pauseDownloads:]](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506053-pause)

|  | Declaration |
| --- | --- |
| From | ``` - (void)pauseDownloads:(NSArray *)downloads ``` |
| To | ``` - (void)pauseDownloads:(NSArray<SKDownload *> * _Nonnull)downloads ``` |

Modified [-[SKPaymentQueue removeTransactionObserver:]](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506165-removetransactionobserver)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeTransactionObserver:(id<SKPaymentTransactionObserver>)observer ``` |
| To | ``` - (void)removeTransactionObserver:(id<SKPaymentTransactionObserver> _Nonnull)observer ``` |

Modified [-[SKPaymentQueue restoreCompletedTransactionsWithApplicationUsername:]](https://developer.apple.com/documentation/storekit/skpaymentqueue/1505992-restorecompletedtransactions)

|  | Declaration |
| --- | --- |
| From | ``` - (void)restoreCompletedTransactionsWithApplicationUsername:(NSString *)username ``` |
| To | ``` - (void)restoreCompletedTransactionsWithApplicationUsername:(NSString * _Nullable)username ``` |

Modified [-[SKPaymentQueue resumeDownloads:]](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506096-resume)

|  | Declaration |
| --- | --- |
| From | ``` - (void)resumeDownloads:(NSArray *)downloads ``` |
| To | ``` - (void)resumeDownloads:(NSArray<SKDownload *> * _Nonnull)downloads ``` |

Modified [-[SKPaymentQueue startDownloads:]](https://developer.apple.com/documentation/storekit/skpaymentqueue/1505998-start)

|  | Declaration |
| --- | --- |
| From | ``` - (void)startDownloads:(NSArray *)downloads ``` |
| To | ``` - (void)startDownloads:(NSArray<SKDownload *> * _Nonnull)downloads ``` |

Modified [SKPaymentQueue.transactions](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506026-transactions)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *transactions ``` |
| To | ``` @property(readonly, nullable) NSArray<SKPaymentTransaction *> *transactions ``` |

Modified [-[SKPaymentTransactionObserver paymentQueue:removedTransactions:]](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/1505994-paymentqueue)

|  | Declaration |
| --- | --- |
| From | ``` - (void)paymentQueue:(SKPaymentQueue *)queue removedTransactions:(NSArray *)transactions ``` |
| To | ``` - (void)paymentQueue:(SKPaymentQueue * _Nonnull)queue removedTransactions:(NSArray<SKPaymentTransaction *> * _Nonnull)transactions ``` |

Modified [-[SKPaymentTransactionObserver paymentQueue:restoreCompletedTransactionsFailedWithError:]](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/1506063-paymentqueue)

|  | Declaration |
| --- | --- |
| From | ``` - (void)paymentQueue:(SKPaymentQueue *)queue restoreCompletedTransactionsFailedWithError:(NSError *)error ``` |
| To | ``` - (void)paymentQueue:(SKPaymentQueue * _Nonnull)queue restoreCompletedTransactionsFailedWithError:(NSError * _Nonnull)error ``` |

Modified [-[SKPaymentTransactionObserver paymentQueue:updatedDownloads:]](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/1506073-paymentqueue)

|  | Declaration |
| --- | --- |
| From | ``` - (void)paymentQueue:(SKPaymentQueue *)queue updatedDownloads:(NSArray *)downloads ``` |
| To | ``` - (void)paymentQueue:(SKPaymentQueue * _Nonnull)queue updatedDownloads:(NSArray<SKDownload *> * _Nonnull)downloads ``` |

Modified [-[SKPaymentTransactionObserver paymentQueue:updatedTransactions:]](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/1506107-paymentqueue)

|  | Declaration |
| --- | --- |
| From | ``` - (void)paymentQueue:(SKPaymentQueue *)queue updatedTransactions:(NSArray *)transactions ``` |
| To | ``` - (void)paymentQueue:(SKPaymentQueue * _Nonnull)queue updatedTransactions:(NSArray<SKPaymentTransaction *> * _Nonnull)transactions ``` |

Modified [-[SKPaymentTransactionObserver paymentQueueRestoreCompletedTransactionsFinished:]](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/1506101-paymentqueuerestorecompletedtran)

|  | Declaration |
| --- | --- |
| From | ``` - (void)paymentQueueRestoreCompletedTransactionsFinished:(SKPaymentQueue *)queue ``` |
| To | ``` - (void)paymentQueueRestoreCompletedTransactionsFinished:(SKPaymentQueue * _Nonnull)queue ``` |

#### SKPaymentTransaction.h

Modified [SKPaymentTransaction.downloads](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411282-downloads)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *downloads ``` |
| To | ``` @property(readonly, nullable) NSArray *downloads ``` |

Modified [SKPaymentTransaction.error](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411269-error)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSError *error ``` |
| To | ``` @property(readonly, nullable) NSError *error ``` |

Modified [SKPaymentTransaction.originalTransaction](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411284-originaltransaction)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) SKPaymentTransaction *originalTransaction ``` |
| To | ``` @property(readonly, nullable) SKPaymentTransaction *originalTransaction ``` |

Modified [SKPaymentTransaction.payment](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411286-payment)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) SKPayment *payment ``` |
| To | ``` @property(readonly, nonnull) SKPayment *payment ``` |

Modified [SKPaymentTransaction.transactionDate](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411273-transactiondate)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSDate *transactionDate ``` |
| To | ``` @property(readonly, nullable) NSDate *transactionDate ``` |

Modified [SKPaymentTransaction.transactionIdentifier](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411288-transactionidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *transactionIdentifier ``` |
| To | ``` @property(readonly, nullable) NSString *transactionIdentifier ``` |

#### SKProduct.h

Modified [SKProduct.contentLengths](https://developer.apple.com/documentation/storekit/skproduct/1506157-contentlengths)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *contentLengths ``` |
| To | ``` @property(readonly, nullable) NSArray<NSNumber *> *contentLengths ``` |

Modified [SKProduct.contentVersion](https://developer.apple.com/documentation/storekit/skproduct/1505996-contentversion)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *contentVersion ``` |
| To | ``` @property(readonly, nullable) NSString *contentVersion ``` |

Modified [SKProduct.localizedDescription](https://developer.apple.com/documentation/storekit/skproduct/1506040-localizeddescription)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *localizedDescription ``` |
| To | ``` @property(readonly, nullable) NSString *localizedDescription ``` |

Modified [SKProduct.localizedTitle](https://developer.apple.com/documentation/storekit/skproduct/1506001-localizedtitle)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *localizedTitle ``` |
| To | ``` @property(readonly, nullable) NSString *localizedTitle ``` |

Modified [SKProduct.price](https://developer.apple.com/documentation/storekit/skproduct/1506094-price)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSDecimalNumber *price ``` |
| To | ``` @property(readonly, nullable) NSDecimalNumber *price ``` |

Modified [SKProduct.priceLocale](https://developer.apple.com/documentation/storekit/skproduct/1506145-pricelocale)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSLocale *priceLocale ``` |
| To | ``` @property(readonly, nullable) NSLocale *priceLocale ``` |

Modified [SKProduct.productIdentifier](https://developer.apple.com/documentation/storekit/skproduct/1506080-productidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *productIdentifier ``` |
| To | ``` @property(readonly, nullable) NSString *productIdentifier ``` |

#### SKProductsRequest.h

Modified [SKProductsRequest.delegate](https://developer.apple.com/documentation/storekit/skproductsrequest/1506142-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id<SKProductsRequestDelegate> delegate ``` |
| To | ``` @property(assign, nullable) id<SKProductsRequestDelegate> delegate ``` |

Modified [-[SKProductsRequest initWithProductIdentifiers:]](https://developer.apple.com/documentation/storekit/skproductsrequest/1506172-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithProductIdentifiers:(NSSet *)productIdentifiers ``` |
| To | ``` - (id _Nonnull)initWithProductIdentifiers:(NSSet * _Nonnull)productIdentifiers ``` |

Modified [-[SKProductsRequestDelegate productsRequest:didReceiveResponse:]](https://developer.apple.com/documentation/storekit/skproductsrequestdelegate/1506070-productsrequest)

|  | Declaration |
| --- | --- |
| From | ``` - (void)productsRequest:(SKProductsRequest *)request didReceiveResponse:(SKProductsResponse *)response ``` |
| To | ``` - (void)productsRequest:(SKProductsRequest * _Nonnull)request didReceiveResponse:(SKProductsResponse * _Nonnull)response ``` |

Modified [SKProductsResponse.invalidProductIdentifiers](https://developer.apple.com/documentation/storekit/skproductsresponse/1505985-invalidproductidentifiers)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *invalidProductIdentifiers ``` |
| To | ``` @property(readonly, nullable) NSArray<NSString *> *invalidProductIdentifiers ``` |

Modified [SKProductsResponse.products](https://developer.apple.com/documentation/storekit/skproductsresponse/1506047-products)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *products ``` |
| To | ``` @property(readonly, nullable) NSArray<SKProduct *> *products ``` |

#### SKReceiptRefreshRequest.h

Modified [-[SKReceiptRefreshRequest initWithReceiptProperties:]](https://developer.apple.com/documentation/storekit/skreceiptrefreshrequest/1506038-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithReceiptProperties:(NSDictionary *)properties ``` |
| To | ``` - (id _Nullable)initWithReceiptProperties:(NSDictionary<NSString *,id> * _Nonnull)properties ``` |

Modified [SKReceiptRefreshRequest.receiptProperties](https://developer.apple.com/documentation/storekit/skreceiptrefreshrequest/1506029-receiptproperties)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSDictionary *receiptProperties ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSDictionary<NSString *,id> *receiptProperties ``` |

#### SKRequest.h

Modified [SKRequest.delegate](https://developer.apple.com/documentation/storekit/skrequest/1385530-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id<SKRequestDelegate> delegate ``` |
| To | ``` @property(assign, nullable) id<SKRequestDelegate> delegate ``` |

Modified [-[SKRequestDelegate request:didFailWithError:]](https://developer.apple.com/documentation/storekit/skrequestdelegate/1385536-request)

|  | Declaration |
| --- | --- |
| From | ``` - (void)request:(SKRequest *)request didFailWithError:(NSError *)error ``` |
| To | ``` - (void)request:(SKRequest * _Nonnull)request didFailWithError:(NSError * _Nullable)error ``` |

Modified [-[SKRequestDelegate requestDidFinish:]](https://developer.apple.com/documentation/storekit/skrequestdelegate/1385532-requestdidfinish)

|  | Declaration |
| --- | --- |
| From | ``` - (void)requestDidFinish:(SKRequest *)request ``` |
| To | ``` - (void)requestDidFinish:(SKRequest * _Nonnull)request ``` |

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
