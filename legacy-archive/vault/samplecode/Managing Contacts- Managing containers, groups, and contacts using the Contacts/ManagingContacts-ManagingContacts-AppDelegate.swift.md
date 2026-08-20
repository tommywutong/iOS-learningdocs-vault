---
title: 'Managing Contacts: Managing containers, groups, and contacts using the Contacts
  framework'
apple_id: TP40017031
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: Contacts
published: '2017-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/ManagingContacts/Listings/ManagingContacts_ManagingContacts_AppDelegate_swift.html
archived_at: '2026-07-18T03:14:27.440985Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Managing Contacts: Managing containers, groups, and contacts using the Contacts framework](Managing%20Contacts-%20Managing%20containers%2C%20groups%2C%20and%20contacts%20using%20the%20Contacts.md)


[Next](ManagingContacts-ManagingContacts-GroupsMenu.swift.md)[Previous](ManagingContacts-ManagingContacts-MGCSegue.swift.md)

# ManagingContacts/ManagingContacts/AppDelegate.swift

```swift
/*
    Copyright (C) 2017 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    The application delegate.
*/

import UIKit

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?


    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
        // Override point for customization after application launch.
        return true
    }

    func applicationWillResignActive(_ application: UIApplication) {
        /* Sent when the application is about to move from active to inactive 
           state. This can occur for certain types of temporary interruptions 
           (such as an incoming phone call or SMS message) or when the user 
           quits the application and it begins the transition to the background
           state. Use this method to pause ongoing tasks, disable timers, and 
           throttle down OpenGL ES frame rates. Games should use this method to 
           pause the game.
       */
    }

    func applicationDidEnterBackground(_ application: UIApplication) {
        /* Use this method to release shared resources, save user data, 
           invalidate timers, and store enough application state information to 
           restore your application to its current state in case it is 
           terminated later. If your application supports background execution, 
           this method is called instead of applicationWillTerminate: when the
           user quits.
        */
    }

    func applicationWillEnterForeground(_ application: UIApplication) {
        /* Called as part of the transition from the background to the inactive 
           state; here you can undo many of the changes made on entering the 
           background.
        */
    }

    func applicationDidBecomeActive(_ application: UIApplication) {
        /* Restart any tasks that were paused (or not yet started) while the 
           application was inactive. If the application was previously in the
           background, optionally refresh the user interface.
        */
    }

    func applicationWillTerminate(_ application: UIApplication) {
        /* Called when the application is about to terminate. Save data if 
           appropriate. See also applicationDidEnterBackground:.
        */
    }
}
```

[Next](ManagingContacts-ManagingContacts-GroupsMenu.swift.md)[Previous](ManagingContacts-ManagingContacts-MGCSegue.swift.md)

