---
title: '"Payment requests are restricted to products returned as valid via Store Kit''s
  didReceiveResponse method." when testing In App Purchase in the Sandbox environment'
apple_id: DTS40010381
resource_type: QA
platform: iOS
topic: null
technology: StoreKit
published: '2010-10-05'
source_url: https://developer.apple.com/library/archive/qa/qa1691/_index.html
archived_at: '2026-07-18T02:34:10.940395Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1691

# "Payment requests are restricted to products returned as valid via Store Kit's didReceiveResponse method." when testing In App Purchase in the Sandbox environment

## Q:  Why am I getting the "Payment requests are restricted to products returned as valid via Store Kit's didReceiveResponse method." error message when testing In App Purchase in the Sandbox environment?

A: Applications implementing In App Purchase must populate their user interface with products that were returned by the App Store. Your application must first send a products request to the App Store before deciding what products to display for purchase in its user interface. This is done by initializing an `SKProductsRequest` object with a set of potentially valid product identifiers. Store Kit sends your set to the App Store, then calls the

`-(void)productsRequest:(SKProductsRequest *)request didReceiveResponse:(SKProductsResponse *)response`

method returning your request and an  `SKProductsResponse` object. The  `SKProductsResponse` object contains your list of potentially valid products broken into two arrays: `products` that contains an array of products, as `SKProduct` objects, which Store Kit considers valid and `invalidProductIdentifiers` that contains an array of product identifiers strings, which Store Kit believes to be invalid.

See the [Frequently Asked Questions](https://developer.apple.com/library/ios/#technotes/tn2009/tn2259.html) section of the Adding In App Purchase to your iPhone Applications technote for reasons for which your product identifier may be returned as invalid by the App Store.

It is important to build the list of items you display and offer to your customers from the list of valid products. Requesting payment for products not returned as valid will fail during development with the following dialog:

__Figure 1__  Invalid Payment Request

!

- `[SKPayment paymentWithProductIdentifier:PRODUCT_ID]`
- `[SKPayment paymentWithProduct:YOUR_SKPRODUCT_OBJECT]`

Apple recommends that you use `[SKPayment paymentWithProduct:YOUR_SKPRODUCT_OBJECT]` when requesting a payment. Using this method ensures that you're always requesting payment for products considered valid and products that your customers will be able to buy.

So, be sure to only present products that were returned by the App Store in your application. For more information on presenting products for purchase from within your application, see the [Feature Delivery](https://developer.apple.com/iphone/library/documentation/NetworkingInternet/Conceptual/StoreKitGuide/APIOverview/OverviewoftheStoreKitAPI.html) section of the In App Purchase Programming Guide.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-10-05 | New document that describes how to resolve the "Payment requests are restricted to products returned as valid via Store Kit's didReceiveResponse method." error message. |

