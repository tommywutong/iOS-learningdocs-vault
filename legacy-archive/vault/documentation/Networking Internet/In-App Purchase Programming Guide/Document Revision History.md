---
title: In-App Purchase Programming Guide
apple_id: TP40008267
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: StoreKit
published: '2018-02-06'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/RevisionHistory.html
archived_at: '2026-07-27T06:57:07.419481Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [In-App Purchase Programming Guide](About%20In-App%20Purchase.md)


[Previous](Preparing%20for%20App%20Review.md)

# Document Revision History

This table describes the changes to _In-App Purchase Programming Guide_.

| __Date__ | __Notes__ |
| 2018-02-06 | Editorial corrections in [Working with Subscriptions](Working%20with%20Subscriptions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4denrxfvbuqnznknltm). |
| 2017-08-03 | Add link to Promotions chapter on main page and fix a link. |
| 2017-07-13 | Updated [Working with Subscriptions](Working%20with%20Subscriptions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4denrxfvbuqnznknltm). |
| 2017-07-11 | Added new section "Promoting In-App Purchases". |
| 2015-10-21 | Added information about retaining SKProductRequest instances. |
| 2013-10-22 | Expanded discussion of delivering products. Added a chapter on restoration. Minor changes throughout. |
|  | Added discussion of `applicationUsername` property in [Requesting Payment](Requesting%20Payment.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4denrxfvbuqnbnknlte). Expanded discussion of persisting purchases and downloading content in [Delivering Products](Delivering%20Products.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4denrxfvbuqnjnknltg). Added chapter [Restoring Purchased Products](Restoring%20Purchased%20Products.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4denrxfvbuqobnknlts). Added an implementation checklist in [Preparing for App Review](Preparing%20for%20App%20Review.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4denrxfvbuqmjqfvjvomi). |
| 2013-09-18 | Expanded and reorganized content throughout. |
|  | Moved information about validating receipts to _[Receipt Validation Programming Guide](../../../releasenotes/General/Receipt%20Validation%20Programming%20Guide/About%20Receipt%20Validation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknzt)_. |
| 2012-09-19 | Removed note that expires_date key was not present on restored transactions. |
|  | Best practice for restoring auto-renewable subscriptions is to simply respect the expires_date key on the restored transactions. Removed section on restoring auto-renewable subscriptions that indicated otherwise. |
| 2012-02-16 | Updated artwork throughout to reflect cross-platform availability. Updated code listing to remove deprecated method. |
|  | Replaced the deprecated [paymentWithProductIdentifier:](https://developer.apple.com/documentation/storekit/skpayment/1623907-paymentwithproductidentifier) method with the [paymentWithProduct:](https://developer.apple.com/documentation/storekit/skpayment/1506008-init) method in “Adding a Store to Your Application”. |
| 2012-01-09 | Minor updates for using this technology on OS X. |
| 2011-10-12 | Added information about a new type of purchase to the overview. |
| 2011-06-06 | First release of this document for OS X. |
| 2011-05-26 | Updated to reflect the latest server behavior for auto-renewable subscriptions. |
| 2011-03-08 | Corrected the list of keys in the renewable subscriptions chapter. |
| 2011-02-15 | Apps must always retrieve product information before submitting a purchase; this ensures that the item has been marked for sale. Information added about renewable subscriptions. |
| 2010-09-01 | Minor edits. |
| 2010-06-14 | Minor clarifications to SKRequest. |
| 2010-01-20 | Fixed a typo in the JSON receipt object. |
| 2009-11-12 | Receipt data must be base64 encoded before being passed to the validation server. Other minor updates. |
| 2009-09-09 | Revised introductory chapter. Clarified usage of receipt data. Recommended the iTunes Connect Developer Guide as the primary source of information about creating product metadata. Renamed from "Store Kit Programming Guide" to "In App Purchase Programming Guide". |
| 2009-06-12 | Revised to include discussion on retrieving price information from the Apple App Store as well as validating receipts with the store. |
| 2009-03-13 | New document that describes how to use the StoreKit API to implement a store with your application. |

[Previous](Preparing%20for%20App%20Review.md)
