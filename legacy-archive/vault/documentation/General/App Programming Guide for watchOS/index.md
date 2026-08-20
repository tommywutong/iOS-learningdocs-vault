---
title: App Programming Guide for watchOS
apple_id: TP40014969
resource_type: Guide
platform: watchOS|iOS
topic: General
technology: WatchKit
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html
archived_at: '2026-07-27T06:57:09.298908Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)



## Developing for Apple Watch

> [!IMPORTANT]

With Apple Watch, users can now access information in a way that is both distinctly personal and unobtrusive. With just a raise of the wrist, users can receive and respond to notifications, see essential information in a complication, and much more. Developing for Apple Watch means providing your users with important, helpful, and impactful information in the most immediate, convenient way (Figure 1-1).

__Figure 1-1__The Apple Watch with complications
（原归档配图获取待重试：`watchHeroImage_2x.png`）

The projects you create for Apple Watch consist of two related bundles: a _Watch app bundle_ and a _WatchKit extension bundle_. The Watch app bundle contains the storyboards and resource files associated with all of your app’s user interfaces. The WatchKit extension bundle lives inside the Watch app bundle and contains the code for managing those interfaces and for responding to user interactions. (The two bundles are known collectively as the _Watch app_.) You distribute the Watch app inside your iOS app bundle, but iOS copies your app to the user’s Apple Watch, where it runs locally.

The Watch app is the core of your watchOS project, and provides your app’s main interface, but it is not the only thing that users see. Watch apps can also provide custom notification and complication interfaces. These interfaces present your app content in distinct and separate ways, but are packaged as part of the Watch app itself. Specifically, the code for managing notification and complication interfaces is in your WatchKit extension and the storyboard scenes are part of the main storyboard in your Watch app bundle. Although optional, notifications and complications are an important way to communicate with users and are often the interfaces used most by users.

### The Watch App

The Watch app is what the user launches from the Apple Watch Home screen. The Watch app presents your app’s full user interface, which can include multiple screens of custom content and support sophisticated user interactions. Use the Watch app to present all of the content you support on Apple Watch.

Creation of a Watch app involves choosing a navigation model for your content and designing screens with the content you want to present. For information about the core architecture of Watch apps, see [The Watch App Architecture](https://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/DesigningaWatchKitApp.html#//apple_ref/doc/uid/TP40014969-CH3-SW1). For information about how to design the screens of your Watch app interface, see [UI Essentials](https://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/CreatingtheUserInterface.html#//apple_ref/doc/uid/TP40014969-CH4-SW1).

### Complications

Complications are small visual elements on the watch face that communicate important information to the user. The term _complication_ comes from watch making, where the addition of features added complexity to the watch construction. Complications are visible whenever the user looks at the watch face, and users can customize which complications are displayed. The number of slots available for complications on a given watch face varies, but most support at least two or three complications.

Complications provide several opportunities for you as a developer:

- Complications let you show important information in a frequently viewed location, making your app more visible to the user.
- When your complication is on the watch face, your app stays in memory, which reduces the amount of time it takes to launch your app.
- When your complication is on the watch face, your app receives more time to execute background tasks, as described in [Background Tasks](https://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/DesigningaWatchKitApp.html#//apple_ref/doc/uid/TP40014969-CH3-SW2).

Apple recommends that all Watch apps include a complication, even if that complication only acts as a button to launch the app. For information about complications and how to implement them, see [Complication Essentials](https://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/ComplicationEssentials.html#//apple_ref/doc/uid/TP40014969-CH27-SW1).

### Notifications

Apple Watch presents local and remote notifications using a distinct set of interfaces. When a notification first arrives, Apple Watch displays a minimal interface called a _short look_, which provides a glanceable version of the notification content. If the user’s wrist remains raised, the minimal interface changes to a more detailed interface called a _long look_.

You can customize the long look interface of your Watch app to incorporate custom graphics, dynamic content, and additional information. Providing a custom interface lets you incorporate branding and other elements that are familiar to users of your app. You can even provide different interfaces for different types of notifications, focusing each interface on the most important aspects of the notification.

In watchOS, you use the User Notifications framework to schedule and handle notifications directly from your WatchKit extension. This framework supports the creation of time-based and location-based local notifications. You also use it to configure your app’s actionable notifications and to handle local and remote notifications delivered to Apple Watch.

For information on how watchOS handles notifications, and information about how to add notification interfaces to your Watch app, see [Notification Essentials](https://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/BasicSupport.html#//apple_ref/doc/uid/TP40014969-CH18-SW1). For more information about how to schedule and handle local and remote notifications, see _[Local and Remote Notification Programming Guide](../../Networking%20Internet/Local%20and%20Remote%20Notification%20Programming%20Guide/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcoju)_.

### User Interfaces on watchOS

The personal nature of Apple Watch requires a different approach when it comes to designing Watch app, notification, and complication interfaces. Your interfaces need to display information quickly and facilitate fast navigation and interactions. Creating that kind of interface means you should not simply port your existing iOS app behavior over to Apple Watch. Instead, make the experience of using your Watch app complementary to the experience of your iOS app.

As part of creating a great user experience, understand that the Watch app, notifications, and complications each have their own unique role. Complications provide access to information directly from the watch face, but space for that information is limited and you must carefully choose what information to show. Notifications keep users informed about recent events, giving you a way to communicate with users even when your app is not running. Watch apps provide a richer experience by letting you present more content and interact with the user, but those interactions must be quick and intuitive to keep users engaged.

For information and guidance on how to design effective interfaces for Apple Watch, see [Apple Watch Human Interface Guidelines](https://developer.apple.com/watchos/human-interface-guidelines/).

[Configuring Your Xcode Project](https://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/ConfiguringYourXcodeProject.html#//apple_ref/doc/uid/TP40014969-CH2-SW1)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-12-12](https://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/RevisionHistory.html#//apple_ref/doc/uid/TP40014969-CH99-SW1)
