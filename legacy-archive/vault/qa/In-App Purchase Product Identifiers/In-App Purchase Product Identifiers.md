---
title: In-App Purchase Product Identifiers
apple_id: DTS40009463
resource_type: QA
platform: iOS
topic: General
technology: StoreKit
published: '2018-05-02'
source_url: https://developer.apple.com/library/archive/qa/qa1329/_index.html
archived_at: '2026-07-18T02:30:24.493621Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1329

# In-App Purchase Product Identifiers

## Q:  I am implementing in-app purchase and must register my product identifiers. What are product identifiers and how do I create and use them in my application?

A: A product identifier is a string used to uniquely identify every product you wish to sell from your application. The App Store uses it to retrieve information about a product. It is a string identifier that can only contain alphanumeric (A-Z, a-z, 0-9), underscore (_), and period (.) characters. You can use any sequence of these characters for your identifier. However, we recommend that you use the reverse domain name style (for example, `com.companyname.application.productid`) when creating your identifier.

See [Create an in-app purchase](https://help.apple.com/itunes-connect/developer/#/devae49fb316) for more information on how to create a product identifier.

Figure 1 displays the `com.samplecode.planners.plates.round.7days`, `com.samplecode.planners.coins.100`, `com.samplecode.planners.tutorial.1`, and `com.samplecode.planners.maps.7days` product identifiers for the `Planners` app.

__Figure 1__  In-App Purchase items in iTunes Connect.

!!

You create an `SKProductsRequest` object, then pass your list of product identifiers to its [init(productIdentifiers:)](https://developer.apple.com/reference/storekit/skproductsrequest/1506172-init) method to retrieve information about your products. See Listing 1 for an example that requests information about the products associated with the product identifiers shown in Figure 1.

__Listing 1__  Retrieving product information.

```swift
// Keep a strong reference to the product request.
var productRequest: SKProductsRequest!

func retrieveProductInformation() {
    let identifiers = Set(["com.samplecode.planners.plates.round.7days",
                           "com.samplecode.planners.coins.100",
                           "com.samplecode.planners.tutorial.1",
                           "com.samplecode.planners.maps.7days"])

    // Initialize the product request object with the above list.
    productRequest = SKProductsRequest(productIdentifiers: identifiers)

    //Attach the request to your delegate.
    productRequest.delegate = self

    // Send the request to the App Store.
    productRequest.start()
}
```


- [In-App Purchase](https://developer.apple.com/in-app-purchase/)
- [iTunes Connect Developer Help](http://help.apple.com/itunes-connect/developer/)
- [In-App Purchase Programming Guide](https://developer.apple.com/library/ios/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html)
- [Receipt Validation Programming Guide](https://developer.apple.com/library/mac/releasenotes/General/ValidateAppStoreReceipt/Introduction.html)
- [TN2387: In-App Purchase Best Practices](https://developer.apple.com/library/ios/technotes/tn2387/_index.html)
- [WWDC 2014: Optimizing In-App Purchases](https://developer.apple.com/videos/play/wwdc2014/303)
- [WWDC 2012: Selling Products with Store Kit](https://developer.apple.com/videos/wwdc/2012/?id=302)
- [WWDC 2013: Using Store Kit for In-App Purchases](https://developer.apple.com/videos/wwdc/2013/?id=305)
- [TN2259: Adding In-App Purchase to your Applications](https://developer.apple.com/library/ios/technotes/tn2259/_index.html)
- [WWDC 2012: Managing Subscriptions with In-App Purchase](https://developer.apple.com/videos/wwdc/2012/?id=308)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2018-05-02 | Updated screenshot and broken links. |
| 2018-05-01 | Updated screenshot and broken links. |
|  | Updated screenshot and broken links. |
| 2017-04-28 | Editorial update. |
| 2015-11-10 | Editorial Update. |
| 2012-01-25 | Updated the "How do I create a product identifier?" section. |
| 2011-07-18 | Updated screenshot. |
| 2010-01-18 | New document that describes how to create and use product identifiers for in-app purchase. |

