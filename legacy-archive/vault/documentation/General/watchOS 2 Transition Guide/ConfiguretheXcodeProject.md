---
title: watchOS 2 Transition Guide
apple_id: TP40015234
resource_type: Guide
platform: watchOS
topic: General
technology: WatchKit
published: '2016-02-02'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/AppleWatch2TransitionGuide/ConfiguretheXcodeProject.html
archived_at: '2026-07-15T07:33:14.023289Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [watchOS 2 Transition Guide](index.md)



## Configure the Xcode Project

Xcode provides everything you need to get started creating your Watch app for watchOS 2. Use the Xcode templates to create and configure your bundle and to provide template files for your glance interface, notification interfaces, and complications. For testing, iOS Simulator supports running your Watch app side by side with your iOS app and debugging both processes at the same time. The simulator also provides support for testing and debugging your glance, notification interfaces, and complications.

### Adding a New Watch App to Your iOS Project

You must have an existing iOS app to create a corresponding Watch app for watchOS 2. The Watch app is implemented as a separate target of your Xcode project and is built and packaged inside your iOS app’s bundle.

If you have an existing Watch app for watchOS 1, you can ship your existing app alongside the new Watch app for watchOS 2. When you create the new Watch app target for watchOS 2, Xcode creates an entirely new set of targets rather than modifying your existing targets. The system automatically installs the most appropriate version of your Watch app on the user’s Apple Watch.

__To add a watchOS 2 app to your existing iOS app project__

1. Open your existing iOS project.
2. Select File > New > Target and navigate to the watchOS section.
3. Select WatchKit App and click Next.
4. Enter a name for your app in the Product Name field.
5. If you plan to implement a glance, custom notification interface, or complication, enable the appropriate checkboxes.

   For notification interfaces, it is recommended that you select the Include Notification Scene checkbox, even if you do not plan on implementing that interface right away. Selecting that checkbox adds a notification simulation file to your project to facilitate the debugging of your notification interfaces. You can also create that file manually at a later time if you prefer.
6. Click Finish.

The base bundle identifier of all your watch targets must be identical to the bundle identifier of your iOS app. This behavior applies even when you have separate targets for both watchOS 1 and watchOS 2. The only differences between the bundle identifiers of any of the targets is the extensions that Xcode adds to identify the Watch app and WatchKit extension. iOS does not install Watch apps whose bundle identifier does not match the bundle identifier of its iOS app.

### Building, Running, and Debugging Your New App

When you create a Watch app target for watchOS 2, Xcode automatically creates the necessary build schemes to run and debug each of your app’s interfaces in the simulator. Xcode provides separate simulators for Apple Watch and iOS devices so that you can debug your Watch app and iOS app at the same time. When you build and run your Watch app, Xcode automatically launches both simulators but only begins a debugging session for your Watch app.

__To debug your iPhone app at the same time as your Watch app__

1. Build and run your Watch app.
2. Select a build scheme for your iPhone app.
3. Click Run to run your iPhone app.

   Xcode launches your iPhone app in the simulator and adds it to the debugging pane.

### Sharing Code Between an iOS App and a watchOS App

In watchOS 2, you can share code, but not frameworks, between your iOS app and Watch app. Because the apps run on separate platforms with different architectures, source files must be compiled separately for each platform. If you still want to use a framework to manage any shared source files, you must create separate framework targets for each platform and add your shared source files to each framework.

If you already have a watchOS 1 app that shares a framework with your iOS app, duplicate your iOS framework target and modify it to support watchOS 2.

__To duplicate and configure your framework target for watchOS 2__

1. Open the project editor pane of Xcode. (The pane is normally closed.)
2. Control-click the target to display a context menu with a Duplicate command.
3. Change the name of the target so that you can identify it easily later.
4. In Build settings, change the following values:

   - Change the Supported Platforms setting to `watchOS`.
   - Change the Base SDK setting to the latest watchOS.
   - Change the Product Name setting so that it matches the name of your iOS framework. You want both frameworks to be built with the same name.
5. Add the framework to your WatchKit extension’s list of linked frameworks.

> [!NOTE]
> 

[Available System Technologies](LeverageSystemTechnologies.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temzufvbuqobnknltc)

[Update Your Existing Code](UpdatetheAppCode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2temzufvbuqnrnknltc)
