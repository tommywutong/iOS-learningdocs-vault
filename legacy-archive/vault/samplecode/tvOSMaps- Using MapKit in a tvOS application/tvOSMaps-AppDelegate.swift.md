---
title: 'tvOSMaps: Using MapKit in a tvOS application'
apple_id: TP40017314
resource_type: Sample Code
platform: tvOS
topic: User Experience
technology: MapKit
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/tvOSMaps/Listings/tvOSMaps_AppDelegate_swift.html
archived_at: '2026-07-26T19:54:16.631863Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [tvOSMaps: Using MapKit in a tvOS application](tvOSMaps-%20Using%20MapKit%20in%20a%20tvOS%20application.md)


[Next](tvOSMaps-MapViewController.swift.md)[Previous](tvOSMaps-SearchResultsViewController.swift.md)

# tvOSMaps/AppDelegate.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The application's delegate class.
*/

import UIKit

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey : Any]? = [:]) -> Bool {
        // Add a search view controller to the root `UITabBarController`.
        if let tabController = window?.rootViewController as? UITabBarController {
            tabController.viewControllers?.append(packagedSearchController())
        }

        return true
    }

    // MARK: Convenience

    /*
         A method demonstrating how to encapsulate a `UISearchController` for presentation in, for example, a `UITabBarController`
    */
    func packagedSearchController() -> UIViewController {
        let storyboard = UIStoryboard(name: "Main", bundle: nil)
        guard let searchResultsController = storyboard.instantiateViewController(withIdentifier: SearchResultsViewController.storyboardIdentifier) as? SearchResultsViewController else { fatalError("Unable to instantiate a SearchResultsViewController.") }

        /*
            Create a UISearchController, passing the `searchResultsController` to
            use to display search results.
        */
        let searchController = UISearchController(searchResultsController: searchResultsController)
        searchController.searchResultsUpdater = searchResultsController
        searchController.searchBar.placeholder = NSLocalizedString("Enter keyword (e.g. bridge)", comment: "")

        // Contain the `UISearchController` in a `UISearchContainerViewController`.
        let searchContainer = UISearchContainerViewController(searchController: searchController)
        searchContainer.title = NSLocalizedString("Search", comment: "")

        // Finally contain the `UISearchContainerViewController` in a `UINavigationController`.
        let searchNavigationController = UINavigationController(rootViewController: searchContainer)
        return searchNavigationController
    }
}
```

[Next](tvOSMaps-MapViewController.swift.md)[Previous](tvOSMaps-SearchResultsViewController.swift.md)

