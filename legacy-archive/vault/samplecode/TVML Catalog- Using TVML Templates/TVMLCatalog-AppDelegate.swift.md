---
title: 'TVML Catalog: Using TVML Templates'
apple_id: TP40016505
resource_type: Sample Code
platform: tvOS
topic: User Experience
technology: TVMLKit
published: '2017-06-06'
source_url: https://developer.apple.com/library/archive/samplecode/TVMLCatalog/Listings/TVMLCatalog_AppDelegate_swift.html
archived_at: '2026-07-18T03:26:06.696481Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TVML Catalog: Using TVML Templates](TVML%20Catalog-%20Using%20TVML%20Templates.md)


[Next](LICENSE.txt.md)[Previous](README.md.md)

# TVMLCatalog/AppDelegate.swift

```swift
/*
See LICENSE.txt for this sample’s licensing information.

Abstract:
The application delegate class that starts TVML.
*/

import UIKit
import TVMLKit

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate, TVApplicationControllerDelegate {
    // MARK: Properties

    var window: UIWindow?

    var appController: TVApplicationController?

    /// - Tag: tvBaseURL
    static let tvBaseURL = "http://127.0.0.1:9001/"

    static let tvBootURL = "\(AppDelegate.tvBaseURL)js/application.js"

    // MARK: UIApplication Overrides

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey : Any]? = [:]) -> Bool {
        // Override point for customization after application launch.
        window = UIWindow(frame: UIScreen.main.bounds)

        /*
            Create the TVApplicationControllerContext for this application
            and set the properties that will be passed to the `App.onLaunch` function
            in JavaScript.
        */
        let appControllerContext = TVApplicationControllerContext()

        /*
            The JavaScript URL is used to create the JavaScript context for your
            TVMLKit application. Although it is possible to separate your JavaScript
            into separate files, to help reduce the launch time of your application
            we recommend creating minified and compressed version of this resource.
            This will allow for the resource to be retrieved and UI presented to
            the user quickly.
        */
        if let javaScriptURL = URL(string: AppDelegate.tvBootURL) {
            appControllerContext.javaScriptApplicationURL = javaScriptURL
        }

        appControllerContext.launchOptions = ["baseURL": AppDelegate.tvBaseURL]

        for (key, value) in launchOptions ?? [:] {
            appControllerContext.launchOptions[key.rawValue] = value
        }

        appController = TVApplicationController(context: appControllerContext, window: window, delegate: self)

        return true
    }

    // MARK: TVApplicationControllerDelegate

    func appController(_ appController: TVApplicationController, didFail error: Error) {
        print("\(#function) invoked with error: \(error)")

        let title = "Error Launching Application"
        let message = error.localizedDescription
        let alertController = UIAlertController(title: title, message: message, preferredStyle: .alert)

        self.appController?.navigationController.present(alertController, animated: true, completion: nil)
    }

}
```

[Next](LICENSE.txt.md)[Previous](README.md.md)

