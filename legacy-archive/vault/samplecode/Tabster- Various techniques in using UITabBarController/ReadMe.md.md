---
title: 'Tabster: Various techniques in using UITabBarController'
apple_id: DTS40011213
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2018-02-15'
source_url: https://developer.apple.com/library/archive/samplecode/Tabster/Listings/ReadMe_md.html
archived_at: '2026-07-18T03:26:19.440414Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tabster: Various techniques in using UITabBarController](Tabster-%20Various%20techniques%20in%20using%20UITabBarController.md)


[Next](LICENSE.txt.md)[Previous](Tabster-main.m.md)

# ReadMe.md

```objc
# Tabster

## Description

Tabster is an eclectic-style application designed to show how to build a tab-bar based iPhone application using [`UITabBarController`](https://developer.apple.com/documentation/uikit/uitabbarcontroller).

It's an iOS sample app that takes the "Tab Bar Application" Xcode template a few steps further by going over useful topics in implementing a `UITabBarController` in your application.

It goes over the following topics:

Demonstrates the architectural design of a tab bar-based app containing multiple types of `UIViewControllers`:

a) It contains six separate tabs each containing their own navigation controller.
b) One of the three tabs (`TwoViewController`) containing table view that navigates to a full screen view controller.
c) `ThreeViewController` - shows badging with an input value to change that badge.
d) `FourViewController` - shows setting its tab bar item programmatically.

## `UITabBarItem` customization
This sample shows how to customize the appearance of its tab items by setting a custom image and title.  The iOS SDK provides a big set of default icons (Favorites, Features, Top Rated, etc.) that give you built in localized titles.  There will be a time when you want your own.  This sample shows how to set these up in Storyboards or through code.

## `UITabBar` appearance customization
Set the "kCustomizeTabBar" compile-time flag in AppDelegate.m to a positive non-zero value to change the color of the UITabBar to gray.

## Loading a view controller from a separate storyboard
This sample has all of its view controllers loaded from the same Storyboard, with exception to `FourViewController`.  In general it is good practice to keep a group of view controllers in separate storyboards to organize your Stoyboards more efficiently.

## User Defaults

What to do when home button is pressed, incoming call SMS, etc. since your app can be interrupted:

     - (void)applicationDidEnterBackground:(UIApplication *)application
            In iOS 4 and later this method called when the application is no longer visible.  The application
            is still in memory and this method has five seconds to perform any cleanup before the application
            stops receiving CPU time.
            It is recommended that background enabled applications save their state here.

     - (void)applicationWillTerminate:(UIApplication *)application;
            In iOS 4.x and later, this is called when the system must completely terminate 
            your application.  In both cases, your app will be started "cold" on its next launch.

    - (void)applicationWillResignActive:(UIApplication *)application;
        This method is called when the application is no longer the first responder.  This can occur when
           the user presses the home button or when the user is deciding whether to take an incoming phone call.

    - (void)applicationDidBecomeActive:(UIApplication *)application;
        This method is called when your app resumes, for example, after a call was not taken or when
           the user switches back to your app.  We don't need to restore the state here since we were still in memory.

This sample uses `NSUserDefaults` to store the following:
1. The tab ordering
The user may reorder the tabs and the selectedIndex value won't match the tab anymore.  So this sample stores the class name as a string and at launch walks through the view controller list and selects the proper view controller.  In this sample the tabs in the tab bar are ordered but they are not ordered in the More screen.

2. `ThreeViewController` has a "badge value" that persists across launches.
This value is stored when the view is hidden and retrieved when the view is shown.

## Autorotation
All you need is `UISupportedInterfaceOrientations` defined in your Info.plist.

## More Page
This sample shows how to customize the look of the "More" page by changing is navigation bar color.
In addition, `FourViewController`, `FavoritesViewController` and `FeaturedViewController` were designed NOT to have a navigation bar.  But the `UITabBarController` places a navigation bar on them so they can navigate in and out of the "More" page.  You get this automatically.  So by design, you need to take this into consideration that a navigation bar may or may not appear for Favorites and Featured.  Both these view controllers take this into account in `viewWillAppear` by hiding their `UILabel` titles accordingly.

## Hiding the Tab Bar
You will notice the `OneViewController` pushes the tab bar away when you navigate through its table.  This is because `SubLevelViewController` sets its `hidesBottomBarWhenPushed` property to YES using Storyboards.  If your drill down user interface in a table requires more screen space, keep this property mind.

## Animated Transition
This sample illustrates how to use `UIViewControllerAnimatedTransitioning` to implement a custom cross-fade transition between view controller one and two.


## Build Requirements
iOS SDK 11.0 or later

## Runtime Requirements
iOS 10.0 or later

Copyright (C) 2011-2017 Apple Inc. All rights reserved.
```

[Next](LICENSE.txt.md)[Previous](Tabster-main.m.md)

