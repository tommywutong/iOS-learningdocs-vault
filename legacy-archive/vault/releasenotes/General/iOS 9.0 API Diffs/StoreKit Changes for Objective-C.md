---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/StoreKit.html
archived_at: '2026-07-18T02:56:36.815013Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# StoreKit Changes for Objective-C

### StoreKit

#### SKPaymentQueue.h

Modified [-[SKPaymentQueue cancelDownloads:]](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506092-cancel)

|  | Declaration |
| --- | --- |
| From | ``` - (void)cancelDownloads:(NSArray *)downloads ``` |
| To | ``` - (void)cancelDownloads:(NSArray<SKDownload *> * _Nonnull)downloads ``` |

Modified [-[SKPaymentQueue pauseDownloads:]](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506053-pause)

|  | Declaration |
| --- | --- |
| From | ``` - (void)pauseDownloads:(NSArray *)downloads ``` |
| To | ``` - (void)pauseDownloads:(NSArray<SKDownload *> * _Nonnull)downloads ``` |

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
| From | ``` @property(nonatomic, readonly) NSArray *transactions ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<SKPaymentTransaction *> *transactions ``` |

Modified [-[SKPaymentTransactionObserver paymentQueue:removedTransactions:]](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/1505994-paymentqueue)

|  | Declaration |
| --- | --- |
| From | ``` - (void)paymentQueue:(SKPaymentQueue *)queue removedTransactions:(NSArray *)transactions ``` |
| To | ``` - (void)paymentQueue:(SKPaymentQueue * _Nonnull)queue removedTransactions:(NSArray<SKPaymentTransaction *> * _Nonnull)transactions ``` |

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

#### SKPaymentTransaction.h

Modified [SKPaymentTransaction.downloads](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411282-downloads)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *downloads ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<SKDownload *> *downloads ``` |

#### SKProduct.h

Modified [SKProduct.downloadContentLengths](https://developer.apple.com/documentation/storekit/skproduct/1615752-downloadcontentlengths)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *downloadContentLengths ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSNumber *> *downloadContentLengths ``` |

#### SKProductsRequest.h

Modified [-[SKProductsRequest initWithProductIdentifiers:]](https://developer.apple.com/documentation/storekit/skproductsrequest/1506172-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithProductIdentifiers:(NSSet *)productIdentifiers ``` |
| To | ``` - (instancetype _Nonnull)initWithProductIdentifiers:(NSSet<NSString *> * _Nonnull)productIdentifiers ``` |

Modified [SKProductsResponse.invalidProductIdentifiers](https://developer.apple.com/documentation/storekit/skproductsresponse/1505985-invalidproductidentifiers)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *invalidProductIdentifiers ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSString *> *invalidProductIdentifiers ``` |

Modified [SKProductsResponse.products](https://developer.apple.com/documentation/storekit/skproductsresponse/1506047-products)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *products ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<SKProduct *> *products ``` |

#### SKReceiptRefreshRequest.h

Modified [-[SKReceiptRefreshRequest initWithReceiptProperties:]](https://developer.apple.com/documentation/storekit/skreceiptrefreshrequest/1506038-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithReceiptProperties:(NSDictionary *)properties ``` |
| To | ``` - (instancetype _Nonnull)initWithReceiptProperties:(NSDictionary<NSString *,id> * _Nullable)properties ``` |

Modified [SKReceiptRefreshRequest.receiptProperties](https://developer.apple.com/documentation/storekit/skreceiptrefreshrequest/1506029-receiptproperties)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSDictionary *receiptProperties ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSDictionary<NSString *,id> *receiptProperties ``` |

#### SKStoreProductViewController.h

Modified [-[SKStoreProductViewController loadProductWithParameters:completionBlock:]](https://developer.apple.com/documentation/storekit/skstoreproductviewcontroller/1620632-loadproductwithparameters)

|  | Declaration |
| --- | --- |
| From | ``` - (void)loadProductWithParameters:(NSDictionary *)parameters completionBlock:(void (^)(BOOL result, NSError *error))block ``` |
| To | ``` - (void)loadProductWithParameters:(NSDictionary<NSString *,id> * _Nonnull)parameters completionBlock:(void (^ _Nullable)(BOOL result, NSError * _Nullable error))block ``` |

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
