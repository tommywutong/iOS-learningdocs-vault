---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/StoreKit.html
archived_at: '2026-07-18T02:56:27.954618Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# StoreKit Changes

## StoreKit

Added SKMutablePayment.simulatesAskToBuyInSandboxAdded SKPayment.simulatesAskToBuyInSandboxAdded SKStoreProductParameterProviderTokenModified SKPayment.init(product: SKProduct!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified SKProductsRequest.init(productIdentifiers: Set<NSObject>!)

|  | Declaration |
| --- | --- |
| From | ``` init!(productIdentifiers productIdentifiers: NSSet!) ``` |
| To | ``` init!(productIdentifiers productIdentifiers: Set<NSObject>!) ``` |

Modified SKErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let SKErrorDomain: NSString! ``` |
| To | ``` let SKErrorDomain: String ``` |

Modified SKReceiptPropertyIsExpired

|  | Declaration |
| --- | --- |
| From | ``` let SKReceiptPropertyIsExpired: NSString! ``` |
| To | ``` let SKReceiptPropertyIsExpired: String ``` |

Modified SKReceiptPropertyIsRevoked

|  | Declaration |
| --- | --- |
| From | ``` let SKReceiptPropertyIsRevoked: NSString! ``` |
| To | ``` let SKReceiptPropertyIsRevoked: String ``` |

Modified SKReceiptPropertyIsVolumePurchase

|  | Declaration |
| --- | --- |
| From | ``` let SKReceiptPropertyIsVolumePurchase: NSString! ``` |
| To | ``` let SKReceiptPropertyIsVolumePurchase: String ``` |

Modified SKStoreProductParameterAffiliateToken

|  | Declaration |
| --- | --- |
| From | ``` let SKStoreProductParameterAffiliateToken: NSString! ``` |
| To | ``` let SKStoreProductParameterAffiliateToken: String ``` |

Modified SKStoreProductParameterCampaignToken

|  | Declaration |
| --- | --- |
| From | ``` let SKStoreProductParameterCampaignToken: NSString! ``` |
| To | ``` let SKStoreProductParameterCampaignToken: String ``` |

Modified SKStoreProductParameterITunesItemIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let SKStoreProductParameterITunesItemIdentifier: NSString! ``` |
| To | ``` let SKStoreProductParameterITunesItemIdentifier: String ``` |

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
