---
title: In-App Purchase Programming Guide
apple_id: TP40008267
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: StoreKit
published: '2018-02-06'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Chapters/DeliverProduct.html
archived_at: '2026-07-27T06:57:07.371532Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [In-App Purchase Programming Guide](About%20In-App%20Purchase.md)


[Next](Working%20with%20Subscriptions.md)[Previous](Promoting%20In-App%20Purchases.md)

# Delivering Products

In the final part of the purchase process, your app waits for the App Store to process the payment request, stores information about the purchase for future launches, downloads the purchased content, and then marks the transaction as finished, as shown in Figure 5-1.

__Figure 5-1__  Stages of the purchase process—delivering products

（原归档配图获取待重试：`delivering_products_2x.png`）

## Waiting for the App Store to Process Transactions

The _transaction queue_ plays a central role in letting your app communicate with the App Store through the StoreKit framework. You add work to the queue that the App Store needs to act on, such as a payment request that needs to be processed. When the transaction’s state changes—for example, when a payment request succeeds—StoreKit calls the app’s _transaction queue observer_. It’s your decision which class acts as the observer. In very small apps, you could handle all the StoreKit logic in the app delegate, including observing the transaction queue. In most apps, you create a separate class that handles this observer logic along with the rest of your app’s store logic. The observer must conform to the [SKPaymentTransactionObserver](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver) protocol.

Using an observer means your app doesn’t constantly poll the status of its active transactions. In addition to using the transaction queue for payment requests, your app also uses the transaction queue to download Apple-hosted content and to find out that subscriptions have been renewed.

Register a transaction queue observer when your app is launched, as shown in Listing 5-1. Make sure that the observer is ready to handle a transaction at any time, not just after you add a transaction to the queue. For example, consider the case of a user buying something in your app right before going into a tunnel. Your app isn’t able to deliver the purchased content because there’s no network connection. The next time your app is launched, StoreKit calls your transaction queue observer again and delivers the purchased content at that time. Similarly, if your app fails to mark a transaction as finished, StoreKit calls the observer every time your app is launched until the transaction is properly finished.

__Listing 5-1__  Registering the transaction queue observer

```objc
- (BOOL)application:(UIApplication *)application
 didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
    /* ... */

    [[SKPaymentQueue defaultQueue] addTransactionObserver:observer];
}
```

Implement the [paymentQueue:updatedTransactions:](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/1506107-paymentqueue) method on your transaction queue observer. StoreKit calls this method when the status of a transaction changes—for example, when a payment request has been processed. The transaction status tells you what action your app needs to perform, as shown in Table 5-1 and Listing 5-2. Transactions in the queue can change state in any order. Your app needs to be ready to work on any active transaction at any time.

__Table 5-1__  Transaction statuses and corresponding actions

| Status | Action to take in your app |
| [SKPaymentTransactionStatePurchasing](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/purchasing) | Update your UI to reflect the in-progress status, and wait to be called again. |
| [SKPaymentTransactionStateDeferred](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/deferred) | Update your UI to reflect the deferred status, and wait to be called again. |
| [SKPaymentTransactionStateFailed](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/skpaymenttransactionstatefailed) | Use the value of the `error` property to present a message to the user. For a list of error constants, see [SKErrorDomain](https://developer.apple.com/documentation/storekit/skerrordomain). |
| [SKPaymentTransactionStatePurchased](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/purchased) | Provide the purchased functionality. |
| [SKPaymentTransactionStateRestored](https://developer.apple.com/documentation/storekit/skpaymenttransactionstate/skpaymenttransactionstaterestored) | Restore the previously purchased functionality. |

__Listing 5-2__  Responding to transaction statuses

```objc
- (void)paymentQueue:(SKPaymentQueue *)queue
 updatedTransactions:(NSArray *)transactions
{
    for (SKPaymentTransaction *transaction in transactions) {
        switch (transaction.transactionState) {
            // Call the appropriate custom method for the transaction state.
            case SKPaymentTransactionStatePurchasing:
                [self showTransactionAsInProgress:transaction deferred:NO];
                break;
            case SKPaymentTransactionStateDeferred:
                [self showTransactionAsInProgress:transaction deferred:YES];
                break;
            case SKPaymentTransactionStateFailed:
                [self failedTransaction:transaction];
                break;
            case SKPaymentTransactionStatePurchased:
                [self completeTransaction:transaction];
                break;
            case SKPaymentTransactionStateRestored:
                [self restoreTransaction:transaction];
                break;
            default:
                // For debugging
                NSLog(@"Unexpected transaction state %@", @(transaction.transactionState));
                break;
        }
    }
}
```

To keep your user interface up to date while waiting, the transaction queue observer can implement optional methods from the [SKPaymentTransactionObserver](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver) protocol as follows. The [paymentQueue:removedTransactions:](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/1505994-paymentqueue) method is called when transactions are removed from the queue—in your implementation of this method, remove the corresponding items from your app’s UI. The [paymentQueueRestoreCompletedTransactionsFinished:](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/1506101-paymentqueuerestorecompletedtran) or [paymentQueue:restoreCompletedTransactionsFailedWithError:](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/1506063-paymentqueue) method is called when StoreKit finishes restoring transactions, depending on whether there was an error. In your implementation of these methods, update your app’s UI to reflect the success or error.

## Persisting the Purchase

After making the product available, your app needs to make a persistent record of the purchase. Your app uses that persistent record on launch to continue to make the product available. It also uses that record to restore purchases, as described in [Restoring Purchased Products](Restoring%20Purchased%20Products.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4denrxfvbuqobnknlts). Your app’s persistence strategy depends the type of products you sell and the versions of iOS.

- For non-consumable products and auto-renewable subscriptions in iOS 7 and later, use the app receipt as your persistent record.
- For non-consumable products and auto-renewable subscriptions in versions of iOS earlier than iOS 7, use the User Defaults system or iCloud to keep a persistent record.
- For non-renewing subscriptions, use iCloud or your own server to keep a persistent record.
- For consumable products, your app updates its internal state to reflect the purchase, but there’s no need to keep a persistent record because consumable products aren’t restored or synced across devices. Ensure that the updated state is part of an object that supports state preservation (in iOS) or that you manually preserve the state across app launches (in iOS or macOS). For information about state preservation, see State Preservation and Restoration.

When using the User Defaults system or iCloud, your app can store a value, such as a number or a Boolean, or a copy of the transaction receipt. In macOS, the user can edit the User Defaults system using the `defaults` command. Storing a receipt requires more application logic, but prevents the persistent record from being tampered with.

When persisting via iCloud, note that your app’s persistent record is synced across devices, but your app is responsible for downloading any associated content on other devices.

### Persisting Using the App Receipt

The app receipt contains a record of the user’s purchases, cryptographically signed by Apple. For more information, see _[Receipt Validation Programming Guide](../../../releasenotes/General/Receipt%20Validation%20Programming%20Guide/About%20Receipt%20Validation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknzt)_.

Information about consumable products is added to the receipt when they’re paid for and remains in the receipt until you finish the transaction. After you finish the transaction, this information is removed the next time the receipt is updated—for example, the next time the user makes a purchase.

Information about all other kinds of purchases is added to the receipt when they’re paid for and remains in the receipt indefinitely.

### Persisting a Value in User Defaults or iCloud

To store information in User Defaults or iCloud, set the value for a key.

```
#if USE_ICLOUD_STORAGE
NSUbiquitousKeyValueStore *storage = [NSUbiquitousKeyValueStore defaultStore];
#else
NSUserDefaults *storage = [NSUserDefaults standardUserDefaults];
#endif

[storage setBool:YES forKey:@"enable_rocket_car"];
[storage setObject:@15 forKey:@"highest_unlocked_level"];

[storage synchronize];
```

### Persisting Using Your Own Server

Send a copy of the receipt to your server along with some kind of credentials or identifier so you can keep track of which receipts belong to a particular user. For example, let users identify themselves to your server with an email or user name, plus a password. Don’t use the `identifierForVendor` property of `UIDevice`—you can’t use it to identify and restore purchases made by the same user on a different device, because different devices have different values for this property.

## Unlocking App Functionality

If the product enables app functionality, set a Boolean value to enable the code path and update your user interface as needed. To determine what functionality to unlock, consult the persistent record that your app made when the transaction occurred. Your app needs to update this Boolean value whenever a purchase is completed and at app launch.

For example, using the app receipt, your code might look like the following:

```
NSURL *receiptURL = [[NSBundle mainBundle] appStoreReceiptURL];
NSData *receiptData = [NSData dataWithContentsOfURL:receiptURL];

// Custom method to work with receipts
BOOL rocketCarEnabled = [self receipt:receiptData
        includesProductID:@"com.example.rocketCar"];
```

Or, using the User Defaults system:

```
NSUserDefaults *defaults = [NSUserDefaults standardUserDefaults];
BOOL rocketCarEnabled = [defaults boolForKey:@"enable_rocket_car"];
```

Then use that information to enable the appropriate code paths in your app.

```
if (rocketCarEnabled) {
    // Use the rocket car.
} else {
    // Use the regular car.
}
```

## Delivering Associated Content

If the product has associated content, your app needs to deliver that content to the user. For example, purchasing a level in a game requires delivering the files that define that level, and purchasing additional instruments in a music app requires delivering the sound files needed to let the user play those instruments.

You can embed that content in your app’s bundle or you can download it as needed—each approach has its advantages and disadvantages. If you include too little content in your app bundle, the user must wait for even small purchases to be downloaded. If you include too much in your app bundle, the initial download of the app takes too long, and the space is wasted for users who don’t purchase the corresponding products. Additionally, if your app is too large, users won’t be able to download it over cellular networks.

__Embed smaller files (up to a few megabytes) in your app, especially if you expect most users to buy that product.__ Content in your app bundle can be made available immediately when the user purchases it. However, to add or update content in your app bundle, you have to submit an updated version of your app.

__Download larger files when needed.__ Separating content from your app bundle keeps your app’s initial download small. For example, a game can include the first level in its app bundle and let users download the rest of the levels when they’re purchased. Assuming your app fetches its list of product identifiers from your server, and not hard-coded in the app bundle, you don’t need to resubmit your app to add or update content that is downloaded by your app.

In iOS 6 and later, most apps should use Apple-hosted content for downloaded files. You create an Apple-hosted content bundle using the In-App Purchase Content target in Xcode and submit it to App Store Connect. When you host content on Apple’s servers you don’t need to provide any servers—your app’s content is stored by Apple using the same infrastructure that supports other large-scale operations, such as the App Store. Additionally, Apple-hosted content automatically downloads in the background even if your app isn’t running.

You might choose to host your own content if you already have server infrastructure, if you need to support older versions of iOS, or if you share your server infrastructure across multiple platforms.

__Note:__  You can’t patch your app binary or download executable code. Your app must contain all executable code needed to support all of its functionality when you submit it. If a new product requires code changes, submit an updated version of your app.

### Loading Local Content

Load local content using the [NSBundle](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/cl/NSBundle) class, just as you load other resources from your app bundle.

```
NSURL *url = [[NSBundle mainBundle] URLForResource:@"rocketCar"
                                     withExtension:@"plist"];
[self loadVehicleAtURL:url];
```

### Downloading Hosted Content from Apple’s Server

When the user purchases a product that has associated Apple-hosted content, the transaction passed to your transaction queue observer also includes an instance of [SKDownload](https://developer.apple.com/documentation/storekit/skdownload) that lets you download the associated content.

To download the content, add the download objects from the transaction’s [downloads](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411282-downloads) property to the transaction queue by calling the [startDownloads:](https://developer.apple.com/documentation/storekit/skpaymentqueue/1505998-start) method of [SKPaymentQueue](https://developer.apple.com/documentation/storekit/skpaymentqueue). If the value of the `downloads` property is `nil`, there’s no Apple-hosted content for that transaction. Unlike downloading apps, downloading content doesn’t automatically require a Wi-Fi connection for content larger than a certain size. Avoid using cellular networks to download large files without an explicit action from the user.

Implement the [paymentQueue:updatedDownloads:](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/1506073-paymentqueue) method on the transaction queue observer to respond to changes in a download’s state—for example, by updating progress in your UI. If a download fails, use the information in its [error](https://developer.apple.com/documentation/storekit/skdownload/1458914-error) property to present the error to the user.

Ensure that your app handles errors gracefully. For example, if the device runs out of disk space during a download, give the user the option to discard the partial download or to resume the download later when space becomes available.

Update your user interface while the content is downloading using the values of the `progress` and `timeRemaining` properties. You can use the [pauseDownloads:](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506053-pause), [resumeDownloads:](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506096-resume), and [cancelDownloads:](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506092-cancel) methods of [SKPaymentQueue](https://developer.apple.com/documentation/storekit/skpaymentqueue) from your UI to let the user control in-progress downloads. Use the [downloadState](https://developer.apple.com/documentation/storekit/skdownload/1620412-downloadstate) property to determine whether the download has completed. Don’t use the [progress](https://developer.apple.com/documentation/storekit/skdownload/1458945-progress) or [timeRemaining](https://developer.apple.com/documentation/storekit/skdownload/1458943-timeremaining) property of the download object to check its status—these properties are for updating your UI.

__Note:__ Download all Apple-hosted content before finishing the transaction. After a transaction is complete, its download objects can no longer be used.

In iOS, your app can manage the downloaded files. The files are saved for you by the StoreKit framework in the `Caches` directory with the backup flag unset. After the download completes, your app is responsible for moving it to the appropriate location. For content that can be deleted if the device runs out of disk space (and later re-downloaded by your app), leave the files in the `Caches` directory. Otherwise, move the files to the `Documents` folder and set the flag to exclude them from user backups.

__Listing 5-3__  Excluding downloaded content from backups

```
NSError *error;
BOOL success = [URL setResourceValue:[NSNumber numberWithBool:YES]
                              forKey:NSURLIsExcludedFromBackupKey
                               error:&error];
if (!success) { /* Handle error... */ }
```

In macOS, the downloaded files are managed by the system; your app can’t move or delete them directly. To locate the content after downloading it, use the [contentURL](https://developer.apple.com/documentation/storekit/skdownload/1458930-contenturl) property of the download object. To locate the file on subsequent launches, use the [contentURLForProductID:](https://developer.apple.com/documentation/storekit/skdownload/1458924-contenturlforproductid) class method of [SKDownload](https://developer.apple.com/documentation/storekit/skdownload). To delete a file, use the [deleteContentForProductID:](https://developer.apple.com/documentation/storekit/skdownload/1458926-deletecontent) class method. For information about reading the product identifiers from your app’s receipt, see _[Receipt Validation Programming Guide](../../../releasenotes/General/Receipt%20Validation%20Programming%20Guide/About%20Receipt%20Validation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknzt)_.

### Downloading Content from Your Own Server

As with all other interactions between your app and your server, the details and mechanics of the process of downloading content from your own server are your responsibility. The communication consists of, at a minimum, the following steps:

1. Your app sends the receipt to your server and requests the content.
2. Your server validates the receipt to establish that the content has been purchased, as described in _[Receipt Validation Programming Guide](../../../releasenotes/General/Receipt%20Validation%20Programming%20Guide/About%20Receipt%20Validation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknzt)_.
3. Assuming the receipt is valid, your server responds to your app with the content.

Ensure that your app handles errors gracefully. For example, if the device runs out of disk space during a download, give the user the option to discard the partial download or to resume the download later when space becomes available.

Consider the security implications of how you host your content and of how your app communicates with your server. For more information, see _[Security Overview](../../Security/Security%20Overview/About%20Software%20Security.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzw)_.

## Finishing the Transaction

Finishing a transaction tells StoreKit that you’ve completed everything needed for the purchase. Unfinished transactions remain in the queue until they’re finished, and the transaction queue observer is called every time your app is launched so your app can finish the transactions. Your app needs to finish every transaction, regardless of whether the transaction succeeded or failed.

Complete all of the following actions before you finish the transaction:

- Persist the purchase.
- Download associated content.
- Update your app’s UI to let the user access the product.

To finish a transaction, call the `finishTransaction:` method on the payment queue.

```
SKPaymentTransaction *transaction = <# The current payment #>;
[[SKPaymentQueue defaultQueue] finishTransaction:transaction];
```

After you finish a transaction, don’t take any actions on that transaction or do any work to deliver the product. If any work remains, your app isn’t ready to finish the transaction yet.

__Note:__ Don’t try to call the `finishTransaction:` method before the transaction is actually completed, attempting to use some other mechanism in your app to track the transaction as unfinished. StoreKit isn’t designed to be used this way. Doing so prevents your app from downloading Apple-hosted content and can lead to other issues.

## Suggested Testing Steps

Test each part of your code to verify that you’ve implemented it correctly.

### Test a Payment Request

Create an instance of `SKPayment` using a valid product identifier that you’ve already tested. Set a breakpoint and inspect the payment request. Add the payment request to the transaction queue, and set a breakpoint to confirm that the `paymentQueue:updatedTransactions:` method of your observer is called.

During testing, it’s OK to finish the transaction immediately without providing the content. However, even during testing, failing to finish the transaction can cause problems: unfinished transactions remain in the queue indefinitely, which could interfere with later testing.

### Verify Your Observer Code

Review the transaction observer’s implementation of the `SKPaymentTransactionObserver` protocol. Verify that it can handle transactions even if you aren’t currently displaying your app’s store UI and even if you didn’t recently initiate a purchase.

Locate the call to the `addTransactionObserver:` method of `SKPaymentQueue` in your code. Verify that your app calls this method at app launch.

### Test a Successful Transaction

Sign in to the App Store with a test user account, and make a purchase in your app. Set a breakpoint in your implementation of the transaction queue observer’s `paymentQueue:updatedTransactions:` method, and inspect the transaction to verify that its status is `SKPaymentTransactionStatePurchased`.

Set a breakpoint at the point in your code that persists the purchase, and confirm that this code is called in response to a successful purchase. Inspect the User Defaults or iCloud key-value store, and confirm that the correct information has been recorded.

### Test an Interrupted Transaction

Set a breakpoint in your transaction queue observer’s `paymentQueue:updatedTransactions:` method so you can control whether it delivers the product. Then make a purchase as usual in the test environment, and use the breakpoint to temporarily ignore the transaction—for example, by returning from the method immediately using the `thread return` command in LLDB.

Terminate and relaunch your app. StoreKit calls the `paymentQueue:updatedTransactions:` method again shortly after launch; this time, let your app respond normally. Verify that your app correctly delivers the product and completes the transaction.

### Verify That Transactions Are Finished

Locate where your app calls the `finishTransaction:` method. Verify that all work related to the transaction has been completed before the method is called and that the method is called for every transaction, whether it succeeded or failed.

[Next](Working%20with%20Subscriptions.md)[Previous](Promoting%20In-App%20Purchases.md)
