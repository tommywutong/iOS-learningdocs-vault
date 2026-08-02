---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/StoreKit.html
archived_at: '2026-07-18T02:52:41.290870Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# StoreKit Changes

## StoreKit

Modified SKDownload

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SKDownload.contentLength

|  | Declaration |
| --- | --- |
| From | ``` var contentLength: NSNumber! { get } ``` |
| To | ``` @NSCopying var contentLength: NSNumber! { get } ``` |

Modified SKDownload.contentURL

|  | Declaration |
| --- | --- |
| From | ``` var contentURL: NSURL! { get } ``` |
| To | ``` @NSCopying var contentURL: NSURL! { get } ``` |

Modified SKDownload.error

|  | Declaration |
| --- | --- |
| From | ``` var error: NSError! { get } ``` |
| To | ``` @NSCopying var error: NSError! { get } ``` |

Modified SKMutablePayment

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified SKMutablePayment.requestData

|  | Declaration |
| --- | --- |
| From | ``` var requestData: NSData! ``` |
| To | ``` @NSCopying var requestData: NSData! ``` |

Modified SKPayment

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified SKPayment.requestData

|  | Declaration |
| --- | --- |
| From | ``` var requestData: NSData! { get } ``` |
| To | ``` @NSCopying var requestData: NSData! { get } ``` |

Modified SKPaymentQueue

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified SKPaymentTransaction

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified SKPaymentTransactionObserver.paymentQueue(SKPaymentQueue!, removedTransactions:[AnyObject]!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified SKPaymentTransactionObserver.paymentQueue(SKPaymentQueue!, restoreCompletedTransactionsFailedWithError: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified SKPaymentTransactionObserver.paymentQueue(SKPaymentQueue!, updatedDownloads:[AnyObject]!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified SKPaymentTransactionObserver.paymentQueueRestoreCompletedTransactionsFinished(SKPaymentQueue!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified SKProduct

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified SKProductsRequest

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified SKProductsRequest.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: SKProductsRequestDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: SKProductsRequestDelegate! ``` |

Modified SKProductsRequest.init(productIdentifiers: Set<NSObject>!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(productIdentifiers productIdentifiers: NSSet!) ``` | OS X 10.10 |
| To | ``` init!(productIdentifiers productIdentifiers: Set<NSObject>!) ``` | OS X 10.10.3 |

Modified SKProductsResponse

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified SKReceiptRefreshRequest

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified SKReceiptRefreshRequest.init(receiptProperties: [NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(receiptProperties properties: [NSObject : AnyObject]!) ``` |
| To | ``` init!(receiptProperties properties: [NSObject : AnyObject]!) ``` |

Modified SKRequest

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified SKRequest.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: SKRequestDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: SKRequestDelegate! ``` |

Modified SKRequestDelegate.request(SKRequest!, didFailWithError: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified SKRequestDelegate.requestDidFinish(SKRequest!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified SKErrorDomain

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let SKErrorDomain: NSString! ``` | OS X 10.10 |
| To | ``` let SKErrorDomain: String ``` | OS X 10.7 |

Modified SKReceiptPropertyIsExpired

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let SKReceiptPropertyIsExpired: NSString! ``` | OS X 10.10 |
| To | ``` let SKReceiptPropertyIsExpired: String ``` | OS X 10.7 |

Modified SKReceiptPropertyIsRevoked

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let SKReceiptPropertyIsRevoked: NSString! ``` | OS X 10.10 |
| To | ``` let SKReceiptPropertyIsRevoked: String ``` | OS X 10.7 |

Modified SKReceiptPropertyIsVolumePurchase

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let SKReceiptPropertyIsVolumePurchase: NSString! ``` | OS X 10.10 |
| To | ``` let SKReceiptPropertyIsVolumePurchase: String ``` | OS X 10.7 |

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
