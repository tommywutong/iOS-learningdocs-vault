---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/StoreKit.html
archived_at: '2026-07-18T02:57:11.080306Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# StoreKit Changes for Swift

### StoreKit

Modified [SKDownload](https://developer.apple.com/documentation/storekit/skdownload)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SKDownloadState [enum]](https://developer.apple.com/documentation/storekit/skdownloadstate)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SKMutablePayment](https://developer.apple.com/documentation/storekit/skmutablepayment)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SKPayment](https://developer.apple.com/documentation/storekit/skpayment)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying, NSMutableCopying |
| To | NSCopying, NSMutableCopying |

Modified [SKPaymentQueue](https://developer.apple.com/documentation/storekit/skpaymentqueue)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SKPaymentTransaction](https://developer.apple.com/documentation/storekit/skpaymenttransaction)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SKPaymentTransactionState [enum]](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SKProduct](https://developer.apple.com/documentation/storekit/skproduct)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SKProductsRequest](https://developer.apple.com/documentation/storekit/skproductsrequest)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SKProductsRequestDelegate](https://developer.apple.com/documentation/storekit/skproductsrequestdelegate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol SKProductsRequestDelegate : SKRequestDelegate, NSObjectProtocol {     func productsRequest(_ request: SKProductsRequest, didReceiveResponse response: SKProductsResponse) } ``` | NSObjectProtocol, SKRequestDelegate |
| To | ``` protocol SKProductsRequestDelegate : SKRequestDelegate {     func productsRequest(_ request: SKProductsRequest, didReceiveResponse response: SKProductsResponse) } ``` | SKRequestDelegate |

Modified [SKProductsResponse](https://developer.apple.com/documentation/storekit/skproductsresponse)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SKReceiptRefreshRequest](https://developer.apple.com/documentation/storekit/skreceiptrefreshrequest)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SKRequest](https://developer.apple.com/documentation/storekit/skrequest)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SKStoreProductViewController](https://developer.apple.com/documentation/storekit/skstoreproductviewcontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

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
