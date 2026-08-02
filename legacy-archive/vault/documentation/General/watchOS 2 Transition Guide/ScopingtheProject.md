---
title: watchOS 2 Transition Guide
apple_id: TP40015234
resource_type: Guide
platform: watchOS
topic: General
technology: WatchKit
published: '2016-02-02'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/AppleWatch2TransitionGuide/ScopingtheProject.html
archived_at: '2026-07-15T07:33:23.147656Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [watchOS 2 Transition Guide](index.md)



## Scoping the Project

Use the following information, as well as your app’s compatibility and data requirements, to scope the work for updating to watchOS 2 and migrating your existing code.

### Xcode Project Changes

Xcode lets you create new Watch app and WatchKit extension targets that run on watchOS 2. Creating new targets gives you a fresh starting point for your app and ensures that the targets are configured properly to run on Apple Watch.

Because the fundamental architecture has not changed, you can start with the same storyboard files and source files you used in your Watch app for watchOS 1. As a result, migrating your project mostly involves adding your source files to the new targets provided by Xcode. However, you need to change the implementations of some of your classes to support the changes introduced in watchOS 2.

To create the targets you need to support watchOS 2, see [Configure the Xcode Project](ConfiguretheXcodeProject.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temzufvbuqnjnknltc). To modify your existing code to run on watchOS 2, see [Update Your Existing Code](UpdatetheAppCode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temzufvbuqnrnknltc).

### Framework Changes

In watchOS 2, you build your WatchKit extension using the watchOS SDK, which contains a subset of the frameworks found in the iOS SDK. Most of the frameworks you might need are still available, but some may not be. If your Watch app relies on features that are not present, you must assess the amount of work required to support that feature.

As much as possible, your Watch app should stand on its own so that your app can operate without the presence of the user’s iPhone. However, if a feature is important enough, you may need to update your iOS app to provide the needed information or get the information in a different way.

See [Available System Technologies](LeverageSystemTechnologies.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temzufvbuqobnknltc).

### The Extension Delegate

Some behaviors in your watchOS 1 app have moved to a new object called the extension delegate. The extension delegate conforms to the [WKExtensionDelegate](https://developer.apple.com/documentation/watchkit/wkextensiondelegate) protocol. It works with an extension object to manage centralized services, such as life cycle events and responses to actionable notifications. All new apps written for watchOS 2 should have an extension delegate object, and Xcode provides one for you with every new project.

See [Implementing the Extension Delegate](UpdatetheAppCode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temzufvbuqnrnknlte) and [Updating Your Notification Action Handler Code](UpdatetheAppCode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temzufvbuqnrnknltk).

### iOS App Coordination

If your watchOS 1 app uses the [openParentApplication:reply:](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619531-openparentapplication) method to communicate with its companion iOS app, you must replace calls to that method with code based on the Watch Connectivity framework. The Watch Connectivity framework supports bidirectional communication between your WatchKit extension and iOS app, providing you with options to transfer data in the foreground or background.

See [Communicating with Your Companion iOS App](UpdatetheAppCode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temzufvbuqnrnknlti).

### Data Management Changes

If your existing Watch app and iOS app use a shared group container or iCloud to exchange data, you must change the way you exchange that data in watchOS 2. Because the WatchKit extension now runs on Apple Watch, the extension must exchange data with the iOS app wirelessly. You can do that using an [NSURLSession](https://developer.apple.com/documentation/foundation/urlsession) object or using the Watch Connectivity framework, which supports bidirectional communication between your iOS app and WatchKit extension.

See [Managing Your Data](UpdatetheAppCode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temzufvbuqnrnknlts).

### Complications Support

Complications are UI elements that the user can add to the watch face to display app-specific information. Like a glance, a complication is a way to communicate information to the user quickly. Complications are not appropriate for all apps, but if you have data that makes sense to display on the watch face, you use the ClockKit framework to provide that data to the system.

See [Creating a Complication](CreatingaComplication.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temzufvbuqmjqfvjvomi).

[Before You Start](index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temzufvbuqmrnknltc)

[Available System Technologies](LeverageSystemTechnologies.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temzufvbuqobnknltc)
