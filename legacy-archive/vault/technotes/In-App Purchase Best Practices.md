---
title: In-App Purchase Best Practices
apple_id: DTS40014795
resource_type: Technical Note
platform: iOS|macOS
topic: null
technology: StoreKit
published: '2017-05-02'
source_url: https://developer.apple.com/library/archive/technotes/tn2387/_index.html
archived_at: '2026-07-27T06:57:05.389478Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2387

# In-App Purchase Best Practices

This document describes best practices for implementing in-app purchase in iOS, macOS, and tvOS applications.

[Best Practices](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytinzzguwugsbrfvbeku2ul5ifeqkdkreugrkt)[Add a transaction queue observer at application launch](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytinzzguwugsbrfvbeku2ul5ifeqkdkreugrktfvauirc7ifpviusbjzjucq2ujfhu4x2rkvcvkrk7j5bfgrkskzcvex2bkrpucucqjreugqkujfhu4x2mifku4q2i)[Query the App Store for product information before presenting your app’s store UI](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytinzzguwugsbrfvbeku2ul5ifeqkdkreugrktfvivkrkslfpviscfl5avauc7knke6usfl5de6us7kbje6rcvinkf6skoizhvetkbkreu6ts7ijcumt2sivpvausfkncu4vcjjzdv6wkpkvjf6qkqkbpv6x2tl5jvit2sivpvksi)[Provide a UI for restoring products](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytinzzguwugsbrfvbeku2ul5ifeqkdkreugrktfvifet2wjfcekx2bl5kusx2gj5jf6usfknke6usjjzdv6ucsj5cfkq2ukm)[Process the transaction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytinzzguwugsbrfvbeku2ul5ifeqkdkreugrktfvifet2divjvgx2ujbcv6vcsifhfgqkdkreu6tq)[Provide the paid content](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytinzzguwugsbrfvbeku2ul5ifeqkdkreugrktfvifet2wjfcekx2ujbcv6ucbjfcf6q2pjzkektsu)[Finish the transaction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytinzzguwugsbrfvbeku2ul5ifeqkdkreugrktfvdestsjknef6vciivpviusbjzjucq2ujfhu4)[Test your implementation of In-App Purchase](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytinzzguwugsbrfvbeku2ul5ifeqkdkreugrktfvkeku2ul5mu6vksl5eu2ucmivguktsuifkest2ol5humx2jjzpucucql5ifkusdjbavgri)[Always verify your receipt with the production URL first](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytinzzguwugsbrfvbeku2ul5ifeqkdkreugrktfvauyv2blfjv6vsfkjeumwk7lfhvkus7kjcugrkjkbkf6v2jkref6vciivpvauspirkugvcjj5hf6vksjrpumsksknka)[Additional Resources](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytinzzguwugsbrfvauircjkreu6tsbjrpverktj5kveq2fkm)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytinzzguwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Best Practices

Below is a list of best practices that developers should follow when implementing in-app purchase.

### Add a transaction queue observer at application launch

StoreKit attaches your observer to the payment queue when your app calls

```
SKPaymentQueue.default().add(your_observer)
```

StoreKit automatically notifies your observer when the content of the payment queue changes upon resuming or while running your app. Adding your app's observer at launch ensures that it will persist during all launches of your app, thus allowing your app to receive all the payment queue notifications.

Consider the case of an app whose `DetailViewController` class creates an observer right before adding a payment request to the queue as seen in Listing 1. This observer exists as long as the instance of `DetailViewController`, which created it, exists. In the advent of interruptions such as a network failure, the app does not complete the purchase process, and the associated transaction stays in the payment queue. When the app resumes, it has no observers as the above observer was deallocated when your app was sent to the background. As a result, your app would not get notified about the transaction in the queue.

__Listing 1__  Does not follow best practices for implementing a transaction observer: App adds an observer to the payment queue when the customer attempts to purchase a product.

```swift
import UIKit
import StoreKit

class DetailViewController: UIViewController, SKPaymentTransactionObserver {
                            ....
    // Called when a customer attempts to purchase a product.
    @IBAction func purchase(_ sender: UIButton) {
        // Register an observer to the payment queue.
        SKPaymentQueue.default().add(your_observer)

        // Create a payment request.
        let payment = SKMutablePayment(product: product)

        // Submit the payment request to the payment queue.
        SKPaymentQueue.default().add(payment)
    }
                           ....
}
```

See Listing 2 for an example that correctly registers a transaction queue observer.

__Listing 2__  Follows best practices for registering a transaction observer.

```swift
import UIKit
import StoreKit

class AppDelegate: UIResponder, UIApplicationDelegate {
                           ....
    // Attach an observer to the payment queue.
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
        // Attach an observer to the payment queue.
        SKPaymentQueue.default().add(your_observer)
        return true
    }

    // Called when the application is about to terminate.
    func applicationWillTerminate(_ application: UIApplication) {
       // Remove the observer.
       SKPaymentQueue.default().remove(your_observer)
    }
                           ....
}
```

StoreKit removes an observer from the payment queue when your app calls

```
 SKPaymentQueue.default().remove(your_observer)
```

As such, StoreKit may attempt to notify the above observer if it was not removed from the payment queue, thus causing your app to crash, as the observer no longer exists.

__Important:__ Apps should avoid initializing the SKPaymentQueue prior to the call to [UIApplicationMain(_:_:_:_:)](https://developer.apple.com/reference/uikit/1622933-uiapplicationmain). Doing so may result in unexpected behavior. Therefore, be sure to initialize the SKPaymentQueue in your app's delegate [application(_:didFinishLaunchingWithOptions:)](https://developer.apple.com/reference/uikit/uiapplicationdelegate/1622921-application) method as shown in Listing 2.

### Query the App Store for product information before presenting your app’s store UI

Your app must first send a product request to the App Store before deciding what products to display for purchase in its user interface. Sending a product request allows you to determine whether your products are available for sale in the App Store, thus preventing you from displaying products that cannot be purchased in your app. See [Retrieving Product Information](https://developer.apple.com/library/ios/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Chapters/ShowUI.html#//apple_ref/doc/uid/TP40008267-CH3-SW9) to learn how to create a product request. The App Store responds to your product request with an `SKResponse` object. Use its `products` property to update your UI, thus ensuring that your customers will only be presented with products available for sale in the App Store.

__Listing 3__  Does not follow best practices for presenting In-App Purchase products: App queries the App Store for product information after presenting it for sale.

```swift
import UIKit
import StoreKit

class DetailViewController: UIViewController, SKProductsRequestDelegate, SKPaymentTransactionObserver {
    var productRequest: SKProductsRequest!
                            ....
    // App first displays a product for sale, then queries the App Store about it when
   //  a customer attempts to purchase it.
   @IBAction func purchase(_ sender: UIButton) {
        // Create a set for your product identifier.
        let identifiers = Set(your_product_identifier)

        // Initialize the product request with the above set.
        productRequest = SKProductsRequest(productIdentifiers: identifiers)
        productRequest.delegate = self

        // Send the request to the App Store.
        productRequest.start()
    }

    // Get the App Store's response.
    func productsRequest(_ request: SKProductsRequest, didReceive response: SKProductsResponse) {
        // Let's sell the first available product.
        let product = response.products.first!
        let payment = SKMutablePayment(product: product)
        SKPaymentQueue.default().add(payment)
    }
}
```

See Listing 4 for an example that follows best practices for presenting in-app purchase products.

__Listing 4__  Follows best practices for presenting In-App Purchase products.

```swift
import UIKit
import StoreKit

class DetailViewController: UIViewController, SKProductsRequestDelegate, SKPaymentTransactionObserver {
    var productRequest: SKProductsRequest!

    // Fetch information about your products from the App Store.
    func fetchProducts(matchingIdentifiers identifiers: [String]) {
        // Create a set for your product identifiers.
        let productIdentifiers = Set(identifiers)
        // Initialize the product request with the above set.
        productRequest = SKProductsRequest(productIdentifiers: productIdentifiers)
        productRequest.delegate = self

        // Send the request to the App Store.
        productRequest.start()
    }

    // Get the App Store's response
    func productsRequest(_ request: SKProductsRequest, didReceive response: SKProductsResponse) {
         // No purchase will take place if there are no products available for sale.
        // As a result, StoreKit won't prompt your customer to authenticate their purchase.
        if response.products.count > 0 {
            // Use availableProducts to populate your UI.
            let availableProducts = response.products
        }
    }
}
```

### Provide a UI for restoring products

If your app sells non-consumable, auto-renewable subscription, or non-renewing subscription products, then you must provide a UI that allows them to be restored. See [Differences Between Product Types](https://developer.apple.com/library/ios/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Chapters/Products.html#//apple_ref/doc/uid/TP40008267-CH2-SW5) and [Restoring Purchased Products](https://developer.apple.com/library/ios/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Chapters/Restoring.html#//apple_ref/doc/uid/TP40008267-CH8-SW9) for more information.

### Process the transaction

StoreKit adds a payment request to the payment queue when your app calls

```
SKPaymentQueue.default().add(your_payment)
```

The queue creates a transaction object to process this request. StoreKit notifies your observer by calling its `paymentQueue(_:updatedTransactions:)` method when the state of this transaction changes. Every transaction has five possible states as shown in [In-App Purchase Programming Guide> Delivering Products> Table 4-1 Transaction statuses and corresponding actions](https://developer.apple.com/library/ios/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Chapters/DeliverProduct.html#//apple_ref/doc/uid/TP40008267-CH5-SW4). Make sure that your observer's `paymentQueue(_:updatedTransactions:)` can respond to any of these states at any time. Implement the `paymentQueue(_:updatedDownloads:)` method on your observer, if your app provides products hosted by Apple.

### Provide the paid content

Deliver the content or unlock your app's functionality when your app receives a transaction whose state is `purchased` or `restored`. These states indicate that a payment was received for the product being sold. As such, your customer expects to be provided with the paid content. If your purchased product includes hosted content from the App Store, be sure to call SKPaymentQueue's `start(_:)` to download the content. See [Unlocking App Functionality](https://developer.apple.com/library/ios/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Chapters/DeliverProduct.html#//apple_ref/doc/uid/TP40008267-CH5-SW20) and [Delivering Associated Content](https://developer.apple.com/library/ios/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Chapters/DeliverProduct.html#//apple_ref/doc/uid/TP40008267-CH5-SW9) for more information.

### Finish the transaction

Transactions stay in the payment queue until they are removed. StoreKit will call your observer’s `paymentQueue(_:updatedTransactions:)` every time that your app launches or resumes from background until they are removed. To that effect, your customers may be repeatedly asked to authenticate their purchases or be prevented from purchasing your products.

Call `finishTransaction(_:)` on your transaction to remove it from the queue. Finished transactions are not recoverable. Therefore, be sure to provide your content, to download all Apple-hosted content of a product, or complete your purchase process before finishing your transaction. See [Finishing the Transaction](https://developer.apple.com/library/ios/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Chapters/DeliverProduct.html#//apple_ref/doc/uid/TP40008267-CH5-SW10) for more information.

### Test your implementation of In-App Purchase

Be sure to thoroughly test your implementation of in-app purchase before submitting your app for review. See [Suggested Testing Steps](https://developer.apple.com/library/ios/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Chapters/DeliverProduct.html#//apple_ref/doc/uid/TP40008267-CH5-SW12) for various scenarios for testing your implementation and [TN2413: In-App Purchase FAQ](https://developer.apple.com/library/content/technotes/tn2413) to troubleshoot your issues.

### Always verify your receipt with the production URL first

If you are doing receipt validation, be sure to verify your receipt with the production URL (`https://buy.itunes.apple.com/verifyReceipt`) first. This applies even in the case where your app is used in the sandbox environment. App Review will review the production version of your app in the sandbox. When your app processes the receipt, it must be capable of detecting the 21007 receipt status code and sending the receipt to the sandbox receipt validation server (`https://sandbox.itunes.apple.com/verifyReceipt`). Once your app is approved and running in the production environment, sending the receipt to the production server first is the correct action. See [What url should I use to verify my receipt?](https://developer.apple.com/library/ios/technotes/tn2413/_index.html#//apple_ref/doc/uid/DTS40016228-CH1-RECEIPTURL) for more information.

[Back to Top](#)

## Additional Resources

- [TN2413: In-App Purchase FAQ](https://developer.apple.com/library/ios/technotes/tn2413/_index.html#//apple_ref/doc/uid/DTS40016228)
- [In-App Purchase Programming Guide](https://developer.apple.com/library/ios/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction.html)
- [Receipt Validation Programming Guide](https://developer.apple.com/library/ios/releasenotes/General/ValidateAppStoreReceipt/Introduction.html#//apple_ref/doc/uid/TP40010573)
- [WWDC 2014: Optimizing In-App Purchases](https://developer.apple.com/videos/play/wwdc2014/303)
- [WWDC 2012: Selling Products with Store Kit](https://developer.apple.com/videos/wwdc/2012/?id=302)
- [WWDC 2013: Using Store Kit for In-App Purchases](https://developer.apple.com/videos/wwdc/2013/?id=305)
- [WWDC 2012: Managing Subscriptions with In-App Purchase](https://developer.apple.com/videos/wwdc/2012/?id=308)
- [TN2259: Adding In-App Purchase to Your Applications](https://developer.apple.com/library/ios/technotes/tn2259/_index.html)

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-05-02 | Fixed typos. |
| 2016-11-09 | Editorial update. |
| 2015-12-07 | Added the "Always verify your receipt with the production URL first" section. |
| 2014-12-16 | Updated the "Add a transaction queue observer at application launch" section. |
| 2014-08-05 | New document that provides best practices for implementing in-app purchase in iOS, macOS, and tvOS applications. |
