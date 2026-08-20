---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Objective-C/StoreKit.html
archived_at: '2026-07-18T02:50:45.496600Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# StoreKit Changes for Objective-C

### StoreKit

#### SKDownload.h

Modified [SKDownload.contentIdentifier](https://developer.apple.com/documentation/storekit/skdownload/1458941-contentidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *contentIdentifier ``` |
| To | ``` @property(nonatomic, readonly) NSString *contentIdentifier ``` |

Modified [SKDownload.contentLength](https://developer.apple.com/documentation/storekit/skdownload/1458932-contentlength)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, readonly) NSNumber *contentLength ``` |
| To | ``` @property(nonatomic, copy, readonly) NSNumber *contentLength ``` |

Modified [SKDownload.contentURL](https://developer.apple.com/documentation/storekit/skdownload/1458930-contenturl)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, readonly) NSURL *contentURL ``` |
| To | ``` @property(nonatomic, readonly) NSURL *contentURL ``` |

Modified [SKDownload.contentVersion](https://developer.apple.com/documentation/storekit/skdownload/1458916-contentversion)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, readonly) NSString *contentVersion ``` |
| To | ``` @property(nonatomic, copy, readonly) NSString *contentVersion ``` |

Modified [SKDownload.error](https://developer.apple.com/documentation/storekit/skdownload/1458914-error)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, readonly) NSError *error ``` |
| To | ``` @property(nonatomic, copy, readonly) NSError *error ``` |

Modified [SKDownload.progress](https://developer.apple.com/documentation/storekit/skdownload/1458945-progress)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) float progress ``` |
| To | ``` @property(nonatomic, readonly) float progress ``` |

Modified [SKDownload.state](https://developer.apple.com/documentation/storekit/skdownload/1458937-state)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) SKDownloadState state ``` |
| To | ``` @property(nonatomic, readonly) SKDownloadState state ``` |

Modified [SKDownload.timeRemaining](https://developer.apple.com/documentation/storekit/skdownload/1458943-timeremaining)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSTimeInterval timeRemaining ``` |
| To | ``` @property(nonatomic, readonly) NSTimeInterval timeRemaining ``` |

#### SKError.h

Added [SKErrorCode](https://developer.apple.com/documentation/storekit/skerror/code)

#### SKPayment.h

Modified [SKMutablePayment.applicationUsername](https://developer.apple.com/documentation/storekit/skmutablepayment/1506088-applicationusername)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy, readwrite) NSString *applicationUsername ``` |
| To | ``` @property(nonatomic, copy) NSString *applicationUsername ``` |

Modified [SKMutablePayment.productIdentifier](https://developer.apple.com/documentation/storekit/skmutablepayment/1505983-productidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, readwrite) NSString *productIdentifier ``` |
| To | ``` @property(nonatomic, copy) NSString *productIdentifier ``` |

Modified [SKMutablePayment.quantity](https://developer.apple.com/documentation/storekit/skmutablepayment/1506170-quantity)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite) NSInteger quantity ``` |
| To | ``` @property(nonatomic) NSInteger quantity ``` |

Modified [SKMutablePayment.requestData](https://developer.apple.com/documentation/storekit/skmutablepayment/1505974-requestdata)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, readwrite) NSData *requestData ``` |
| To | ``` @property(nonatomic, copy) NSData *requestData ``` |

Modified [+[SKPayment paymentWithProduct:]](https://developer.apple.com/documentation/storekit/skpayment/1506008-init)

|  | Declaration |
| --- | --- |
| From | ``` + (id)paymentWithProduct:(SKProduct *)product ``` |
| To | ``` + (instancetype)paymentWithProduct:(SKProduct *)product ``` |

Modified [SKPayment.productIdentifier](https://developer.apple.com/documentation/storekit/skpayment/1506155-productidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, readonly) NSString *productIdentifier ``` |
| To | ``` @property(nonatomic, copy, readonly) NSString *productIdentifier ``` |

Modified [SKPayment.quantity](https://developer.apple.com/documentation/storekit/skpayment/1506077-quantity)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSInteger quantity ``` |
| To | ``` @property(nonatomic, readonly) NSInteger quantity ``` |

Modified [SKPayment.requestData](https://developer.apple.com/documentation/storekit/skpayment/1506159-requestdata)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, readonly) NSData *requestData ``` |
| To | ``` @property(nonatomic, copy, readonly) NSData *requestData ``` |

#### SKPaymentQueue.h

Modified [+[SKPaymentQueue defaultQueue]](https://developer.apple.com/documentation/storekit/skpaymentqueue/1505990-default)

|  | Declaration |
| --- | --- |
| From | ``` + (SKPaymentQueue *)defaultQueue ``` |
| To | ``` + (instancetype)defaultQueue ``` |

Modified [SKPaymentQueue.transactions](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506026-transactions)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray<SKPaymentTransaction *> *transactions ``` |
| To | ``` @property(nonatomic, readonly) NSArray<SKPaymentTransaction *> *transactions ``` |

#### SKPaymentTransaction.h

Modified [SKPaymentTransaction.downloads](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411282-downloads)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *downloads ``` |
| To | ``` @property(nonatomic, readonly) NSArray<SKDownload *> *downloads ``` |

Modified [SKPaymentTransaction.error](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411269-error)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSError *error ``` |
| To | ``` @property(nonatomic, readonly) NSError *error ``` |

Modified [SKPaymentTransaction.originalTransaction](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411284-originaltransaction)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) SKPaymentTransaction *originalTransaction ``` |
| To | ``` @property(nonatomic, readonly) SKPaymentTransaction *originalTransaction ``` |

Modified [SKPaymentTransaction.payment](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411286-payment)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) SKPayment *payment ``` |
| To | ``` @property(nonatomic, readonly) SKPayment *payment ``` |

Modified [SKPaymentTransaction.transactionDate](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411273-transactiondate)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSDate *transactionDate ``` |
| To | ``` @property(nonatomic, readonly) NSDate *transactionDate ``` |

Modified [SKPaymentTransaction.transactionIdentifier](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411288-transactionidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *transactionIdentifier ``` |
| To | ``` @property(nonatomic, readonly) NSString *transactionIdentifier ``` |

Modified [SKPaymentTransaction.transactionState](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411275-transactionstate)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) SKPaymentTransactionState transactionState ``` |
| To | ``` @property(nonatomic, readonly) SKPaymentTransactionState transactionState ``` |

#### SKProduct.h

Modified [SKProduct.contentLengths](https://developer.apple.com/documentation/storekit/skproduct/1506157-contentlengths)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray<NSNumber *> *contentLengths ``` |
| To | ``` @property(nonatomic, readonly) NSArray<NSNumber *> *contentLengths ``` |

Modified [SKProduct.contentVersion](https://developer.apple.com/documentation/storekit/skproduct/1505996-contentversion)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *contentVersion ``` |
| To | ``` @property(nonatomic, readonly) NSString *contentVersion ``` |

Modified [SKProduct.downloadable](https://developer.apple.com/documentation/storekit/skproduct/1506161-downloadable)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) BOOL downloadable ``` |
| To | ``` @property(nonatomic, readonly) BOOL downloadable ``` |

Modified [SKProduct.localizedDescription](https://developer.apple.com/documentation/storekit/skproduct/1506040-localizeddescription)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *localizedDescription ``` |
| To | ``` @property(nonatomic, readonly) NSString *localizedDescription ``` |

Modified [SKProduct.localizedTitle](https://developer.apple.com/documentation/storekit/skproduct/1506001-localizedtitle)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *localizedTitle ``` |
| To | ``` @property(nonatomic, readonly) NSString *localizedTitle ``` |

Modified [SKProduct.price](https://developer.apple.com/documentation/storekit/skproduct/1506094-price)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSDecimalNumber *price ``` |
| To | ``` @property(nonatomic, readonly) NSDecimalNumber *price ``` |

Modified [SKProduct.priceLocale](https://developer.apple.com/documentation/storekit/skproduct/1506145-pricelocale)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSLocale *priceLocale ``` |
| To | ``` @property(nonatomic, readonly) NSLocale *priceLocale ``` |

Modified [SKProduct.productIdentifier](https://developer.apple.com/documentation/storekit/skproduct/1506080-productidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *productIdentifier ``` |
| To | ``` @property(nonatomic, readonly) NSString *productIdentifier ``` |

#### SKProductsRequest.h

Modified [SKProductsRequest.delegate](https://developer.apple.com/documentation/storekit/skproductsrequest/1506142-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id<SKProductsRequestDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak) id<SKProductsRequestDelegate> delegate ``` |

Modified [-[SKProductsRequest initWithProductIdentifiers:]](https://developer.apple.com/documentation/storekit/skproductsrequest/1506172-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithProductIdentifiers:(NSSet *)productIdentifiers ``` |
| To | ``` - (instancetype)initWithProductIdentifiers:(NSSet<NSString *> *)productIdentifiers ``` |

Modified [SKProductsResponse.invalidProductIdentifiers](https://developer.apple.com/documentation/storekit/skproductsresponse/1505985-invalidproductidentifiers)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray<NSString *> *invalidProductIdentifiers ``` |
| To | ``` @property(nonatomic, readonly) NSArray<NSString *> *invalidProductIdentifiers ``` |

Modified [SKProductsResponse.products](https://developer.apple.com/documentation/storekit/skproductsresponse/1506047-products)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray<SKProduct *> *products ``` |
| To | ``` @property(nonatomic, readonly) NSArray<SKProduct *> *products ``` |

#### SKReceiptRefreshRequest.h

Modified [-[SKReceiptRefreshRequest initWithReceiptProperties:]](https://developer.apple.com/documentation/storekit/skreceiptrefreshrequest/1506038-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithReceiptProperties:(NSDictionary<NSString *,id> *)properties ``` |
| To | ``` - (instancetype)initWithReceiptProperties:(NSDictionary<NSString *,id> *)properties ``` |

#### SKRequest.h

Modified [SKRequest.delegate](https://developer.apple.com/documentation/storekit/skrequest/1385530-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id<SKRequestDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak) id<SKRequestDelegate> delegate ``` |

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
