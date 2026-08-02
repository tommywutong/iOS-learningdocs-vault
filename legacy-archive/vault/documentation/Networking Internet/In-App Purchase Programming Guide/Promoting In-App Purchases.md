---
title: In-App Purchase Programming Guide
apple_id: TP40008267
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: StoreKit
published: '2018-02-06'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/PromotingIn-AppPurchases/PromotingIn-AppPurchases.html
archived_at: '2026-07-27T06:57:07.349696Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [In-App Purchase Programming Guide](About%20In-App%20Purchase.md)


[Next](Delivering%20Products.md)[Previous](Requesting%20Payment.md)

# Promoting In-App Purchases

Starting in iOS 11, you can promote in-app purchases on the App Store. Promoted in-app purchases appear on your product page, can be displayed in search results, and may be featured on an appropriate tab on the App Store. Users can start an in-app purchase on the App Store and be taken into your app to continue the transaction. If your app is not yet installed, they are prompted to download it.

## Promoting Your In-App Purchases

Promoting in-app purchases requires two steps:

1. Set up in-app purchases in App Store Connect by uploading promotional images for the in-app purchases you’d like to promote. Then use the App Store Promotions tool in App Store Connect to manage their order and visibility on the App Store.
2. Implement the delegate method in the [SKPaymentTransactionObserver](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver) protocol that handles purchases.

To further customize each user’s view, you can optionally override the visibility of in-app purchases, and the order in which they appear, using methods in [SKProductStorePromotionController](https://developer.apple.com/documentation/storekit/skproductstorepromotioncontroller).

For marketing guidance on this feature, see [Promoting Your In-App Purchases](https://developer.apple.com/app-store/promoting-in-app-purchases/).

## Completing a Purchase

When a user taps or clicks Buy on an in-app purchase on the App Store, StoreKit automatically opens your app and sends the transaction information to your app through the delegate method in the [SKPaymentTransactionObserver](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver) protocol. Your app must complete the purchase transaction and any related actions that are specific to your app.

In the delegate method you return `true` to continue the transaction, or `false` to defer or cancel the transaction.

If your app is not installed when the user taps or clicks Buy, the App Store automatically downloads the app or prompts the user to buy it. If the installed version of your app is an older version that doesn’t support in-app purchase promotions, the App Store prompts the user to upgrade the app.

### Continuing a Transaction

To continue an in-app purchase transaction, implement the delegate method in the [SKPaymentTransactionObserver](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver) protocol and return `true`. StoreKit then displays the payment sheet, and the user can complete the transaction.

```swift
//Continuing a Transaction from the App Store

//MARK: - SKPaymentTransactionObserver

func paymentQueue(_ queue: SKPaymentQueue, shouldAddStorePayment payment: SKPayment,
        forProduct product: SKProduct) -> Bool {
    // Check to see if you can complete the transaction.
    // Return true if you can.
    return true
}
```

### Deferring or Canceling a Transaction

If your app needs to defer or cancel a transaction, you return `false`. For example, you may need to defer a transaction if the user is in the middle of onboarding, and continue it after onboarding is completed. Or, you may need to cancel a transaction if the user has already unlocked the product they are trying to buy.

To defer a transaction:

1. Save the `payment` to use when the app is ready. The payment already contains information about the product. _Do not create a new SKPayment with the same product._
2. Return `false`.
3. After the user is finished with onboarding or other actions that required a deferral, send the saved payment to the payment queue, the same way you would with a normal in-app purchase.

To cancel a transaction:

1. Return `false`.
2. (Optional) Provide feedback to the user. Otherwise, the app’s lack of action after the user taps or clicks Buy in the App Store may seem like a bug.

```swift
//Handling a Transaction from the App Store

//MARK: - SKPaymentTransactionObserver

func paymentQueue(_ queue: SKPaymentQueue, shouldAddStorePayment payment: SKPayment,
        forProduct product: SKProduct) -> Bool {

    // ... Add code here to check if your app must defer the transaction.
    let shouldDeferPayment = ...
    // If you must defer until onboarding is completed, then save the payment and return false.
    if shouldDeferPayment {
        self.savedPayment = payment
    return false
    }

    // ... Add code here to check if your app must cancel the transaction.
    let shouldCancelPayment = ...
    // If you must cancel the transaction, then return false:
    if shouldCancelPayment {
    return false
    }
}

// (If you canceled the transaction, provide feedback to the user.)

// Continuing a previously deferred payment
SKPaymentQueue.default().add(savedPayment)

)
```

## Advanced Features for Promoted Products

To customize the list of promoted in-app purchases for your user, you can use [SKProductStorePromotionController](https://developer.apple.com/documentation/storekit/skproductstorepromotioncontroller) to set the visibility of in-app purchases and the order in which they appear. The default order and visibility of in-app purchases are set in App Store Connect. Your overrides are per device, and are not synced to an iCloud account. Note that this feature relies on local device storage, and the API can only run after the app has launched on a device at least once.

Implementing these advanced features is optional. They are not required for your in-app purchases to appear on the App Store.

### Reading Visibility Settings

To read the visibility setting for a product, call the [fetchStorePromotionVisibility(for:completionHandler:)](https://developer.apple.com/documentation/storekit/skproductstorepromotioncontroller/2915867-fetchstorepromotionvisibility) method, providing it the product information.

```
// Reading Visibility Override of a Promoted In-App Purchase

// Fetch Product Info for "Hidden Beaches pack"

let storePromotionController = SKProductStorePromotionController.default()
storePromotionController.fetchStorePromotionVisibility(forProduct: hiddenBeaches,
    completionHandler: { visibility: SKProductSTorePromotionVisiblity, error: Error?) in
        // visibility == .default
```

### Overriding Visibility Settings

You can decide whether to make in-app purchases visible or hidden, per device. For example, you may want to hide in-app purchases the customer has already made, and show only the products they can still buy.

For example, to hide the product “Pro Subscription” after a user has purchased it, fetch the product info and update the default store promotion controller with the `.hide` setting, as shown below. The Pro Subscription in-app purchase will no longer appear on the given device.

```
// Updating Visibility Override of a Promoted In-App Purchase
// Fetch Product Info for "Pro Subscription"

let storePromotionController = SKProductStorePromotionController.default()
storePromotionController.update(storePromotionVisibility: .hide, forProduct: proSubscription,
    completionHandler: { (error: Error?) in
        // Complete
    })
```

In this example, visibility is set to `.default` because no overrides have been set yet. The product is hidden or shown based on what you set as the default in App Store Connect.

### Overriding Promotion Order

You can set the order of promoted in-app purchases on the App Store product page, per device. For example, you can promote an in-app purchase product that unlocks a specific level in your game when a user reaches the level immediately before the specified level.

To override the default product order for in-app purchases, put the product information for the subset of products you want to reorder into an array, in the order you want them to appear in. Pass the array to the [updateStorePromotionOrder:completionHandler:](https://developer.apple.com/documentation/storekit/skproductstorepromotioncontroller/2915874-updatestorepromotionorder) method. The products in the array are shown at the beginning of the list, followed by the remaining in-app purchase products, which are listed in the same relative order that you set in App Store Connect.

```
// Updating Order Override of Promoted In-App Purchases

// Fetch Product Info for three products: Pro Subscription, Fishing Hot Spots, and Hidden Beaches

let storePromotionController = SKProductStorePromotionController.default()
let newProductsOrder = [hiddenBeaches, proSubscription, fishingHotSpots]
storePromotionController.updateStorePromotionOrder(newProductsOrder,
    completionHandler: { (error: Error?) in
        // Complete
    })
```

### Canceling Order Overrides

To cancel order overrides, send an empty product array to the [updateStorePromotionOrder:completionHandler:](https://developer.apple.com/documentation/storekit/skproductstorepromotioncontroller/2915874-updatestorepromotionorder) method. The in-app purchase products are displayed in the default order.

### Reading Order Overrides

To read a product order override as it will appear on a given device, call the [fetchStorePromotionOrder(completionHandler:)](https://developer.apple.com/documentation/storekit/skproductstorepromotioncontroller/2915873-fetchstorepromotionorderwithcomp) method. You should receive an array of products whose order is overridden. If you get an empty array, you have not set any overrides and the products are in the default order.

```
// Reading Order Override of Promoted In-App Purchases

let storePromotionController = SKProductStorePromotionController.default()
storePromotionController.fetchStorePromotionOrder(completionHander: {
    (products: [SKProduct], error: Error?) in
        // products == [hiddenBeaches, proSubscription, fishingHotSpots
    })
```

## Testing Promoted In-App Purchases

To test your promoted in-app purchases before your app is available in the App Store, Apple provides a system URL that triggers your app using the `itms-services://` protocol.

__Table 4-1__  System URL for Testing Promoted In-App Purchases

| Protocol | `itms-services://` |
| Parameter `action` | `purchaseIntent` |
| Parameter `bundleId` | The bundle Id for your app, for example:  `com.example.app` |
| Parameter `productIdentifier` | The in-app purchase product name you want to test, for example:  `product_name` |

The resulting URL looks like this:

`itms-services://?action=purchaseIntent&bundleId=com.example.app&productIdentifier=product_name`

Send this URL to yourself in an email or iMessage and open it from your device. You will know the test is running when your app opens automatically. You can then test your promoted in-app purchase.

[Next](Delivering%20Products.md)[Previous](Requesting%20Payment.md)
