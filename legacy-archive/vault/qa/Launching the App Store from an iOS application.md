---
title: Launching the App Store from an iOS application
apple_id: DTS40008173
resource_type: QA
platform: iOS
topic: General
technology: null
published: '2017-06-14'
source_url: https://developer.apple.com/library/archive/qa/qa1629/_index.html
archived_at: '2026-07-18T02:33:02.461435Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1629

# Launching the App Store from an iOS application

## Q:  How do I launch the App Store from my iOS app? Also, how do I link to my application on the store?

A: You can launch the App Store from your app by using either the UIApplication class or the SKStoreProductViewController class.

UIApplication's [open(_:options:completionHandler:)](https://developer.apple.com/reference/uikit/uiapplication/1648685-open) method handles links to applications and media by launching the appropriate store application passed in the [URL](https://developer.apple.com/reference/foundation/url) object. Follow the steps below to obtain a link to an app, music, movie, or any other item sold on Apple's online stores (iTunes, App Store, and iBooks) and link to it from your iOS app:

1. Launch iTunes on your computer.
2. Search for the item you want to link to.
3. Right-click or control-click on the item's name in iTunes, then choose "Copy Link" from the pop-up menu.
4. In your application, create an `URL` object with the copied iTunes URL, then pass this object to `UIApplication`' s `open(_:options:completionHandler:)` method to open your item in a store.

See Listing 1 for an example that launches the App Store app using `UIApplication`.

__Listing 1__  Launching the App Store using UIApplication.

```
 // App Store URL.
 let appStoreLink = "https://itunes.apple.com/us/app/apple-store/id375380948?mt=8"

 /* First create a URL, then check whether there is an installed app that can
    open it on the device. */
if let url = URL(string: appStoreLink), UIApplication.shared.canOpenURL(url) {
   // Attempt to open the URL.
   UIApplication.shared.open(url, options: [:], completionHandler: {(success: Bool) in
      if success {
          print("Launching \(url) was successful")
   }})
}
```


The [SKStoreProductViewController](https://developer.apple.com/reference/storekit/skstoreproductviewcontroller) class allows you to present an Apple store (iTunes, App Store, and iBooks) from within your app. See Listing 2 that demonstrates how to launch the App Store from an app.

__Listing 2__  Launching the App Store using SKStoreProductViewController.

```swift
import StoreKit
class ViewController: UIViewController, SKStoreProductViewControllerDelegate {
    // Create a store product view controller.
    var storeProductViewController = SKStoreProductViewController()

    override func viewDidLoad() {
        super.viewDidLoad()
        storeProductViewController.delegate = self
    }

    // Launches the store product view controller.
    @IBAction func launchStoreProductViewController(_ sender: UIButton) {
        // Create a product dictionary using the App Store's iTunes identifer.
        let parametersDict = [SKStoreProductParameterITunesItemIdentifier: 375380948]

        /* Attempt to load it, present the store product view controller if success
            and print an error message, otherwise. */
        storeProductViewController.loadProduct(withParameters: parametersDict, completionBlock: { (status: Bool, error: Error?) -> Void in
            if status {
               self.present(self.storeProductViewController, animated: true, completion: nil)
            }
            else {
               if let error = error {
               print("Error: \(error.localizedDescription)")
          }}})
    }

    // Let's dismiss the presented store product view controller.
    func productViewControllerDidFinish(_ viewController: SKStoreProductViewController) {
       viewController.presentingViewController?.dismiss(animated: true, completion: nil)
   }
}
```


---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-06-14 | Editorial update. |
| 2014-03-13 | Removed reference to catching and processing redirect iTunes links; iTunes no longer supports redirect-style hosts. |
| 2012-02-07 | Updated code listings. |
| 2010-01-09 | Removed reference to phobos.apple.com URLs, which are no longer needed for direct linking to the App Store. |
| 2009-10-27 | Fixed typo. |
| 2009-01-27 | New document that describes how to launch the App Store from native iOS apps. |

