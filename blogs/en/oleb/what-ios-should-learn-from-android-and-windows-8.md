---
title: What iOS Should Learn From Android and Windows 8
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2012/02/what-ios-should-learn-from-android-and-windows-8/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:75681ba4a3729ed1'
translated: false
---

> 原文：[What iOS Should Learn From Android and Windows 8](https://oleb.net/blog/2012/02/what-ios-should-learn-from-android-and-windows-8/)　·　Ole Begemann

# What iOS Should Learn From Android and Windows 8

Following up on my post about [the new Share sheets in Mountain Lion and what they might mean for the future of content sharing in iOS](https://oleb.net/blog/2012/02/share-sheets-only-half-way-there/), let’s take a more technical look at how Apple’s competition implements content sharing across apps. In this article, I will first investigate how Android and Windows 8 solve the issue and then hopefully come to a conclusion what Apple could learn and/or adopt from these implementations.

Note that I am no expert on either of the two platforms so my remarks will probably contain some mistakes. I will gladly update the post with any corrections you send me.

# Android

## Activities

![Android displaying a list of apps that can receive the content to be shared](https://oleb.net/media/android-app-sharing-text.png)

<sub>Android displaying a list of apps that can receive the content to be shared.</sub>

A typical Android app consists of several so-called [Activities](https://developer.android.com/guide/topics/fundamentals/activities.html). An activity is an app component that provides a single screen[1](#fn:1) in an app and manages how users can interact with this screen. As such, the concept is somewhat comparable to [view controllers in iOS](https://developer.apple.com/library/ios/featuredarticles/ViewControllerPGforiPhoneOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007457-CH1-SW1).

But there is an important difference: while iOS view controllers are pretty tightly coupled to the app they belong to, activities on Android are more loosely bound to each other. An Android app can not only launch its own activities but also access and launch activities that have been provided by other apps. This way, activities from many different apps can end up on the activity stack. The user can use the device’s back button to navigate back up the stack, thereby implicitly switching from app to app.

Android uses activities to enable sharing between apps. An Android app has a manifest file (an XML config file similar to Apple’s `Info.plist`) in which it can list all its activities and how they can be activated from other apps.

## Intents

The launch of an activity is done with so-called [Intents](https://developer.android.com/guide/topics/intents/intents-filters.html). Intent is just another name for a message data structure that contains an operation to be performed by the system. One of the several possible message types is to start an activity. Activities to be launched can be either named directly (if you want to launch a specific activity in a specific app) or the intent can specify the predefined action [`ACTION_SEND`](https://developer.android.com/training/sharing/send.html) to indicate that it wants to send data from one activity to another. Based on the data and its type that your app passes to the intent object, the OS will then identify all activities from all apps that can handle this type of data[2](#fn:2) and present them to the user in a list.

When the user selects the activity/app he wants to use, the system launches the activity and passes it the data contained in the intent object. By default, activities do not report anything back to their caller. A backchannel from the launched to the launching activity can optionally be established by using the [`startActivityForResult()`](https://developer.android.com/reference/android/app/Activity.html#startActivityForResult(android.content.Intent,%20int)) method, however.

# Windows 8

I have chosen to take a look at the Windows 8 APIs rather than Windows Phone 7 here for two reasons. Firstly, Windows Phone 7 has no generic content sharing API. There do exist classes to [share links](http://msdn.microsoft.com/en-us/library/microsoft.phone.tasks.sharelinktask(v=vs.92).aspx) and [status messages](http://msdn.microsoft.com/en-us/library/microsoft.phone.tasks.sharestatustask(v=vs.92).aspx) on selected social networks but the list of sharing services does not seem to be extensible. A feature called “app-to-app communication” (whatever that means) is [rumored to be part of Windows Phone 8](http://pocketnow.com/windows-phone/exclusive-windows-phone-8-detailed). Secondly, it seems at least possible (if not probable) that [Windows Phone will soon be based on the Windows 8 platform](http://www.theverge.com/2011/11/15/2564399/microsoft-bringing-windows-8-to-phones) and Microsoft’s new [WinRT API](http://msdn.microsoft.com/en-us/library/windows/apps/hh464942.aspx) will also be relevant for Windows Phone development.

## Charms

![Windows 8 displaying the Share action in the Charms bar](https://oleb.net/media/windows-8-metro-share-contract.png)

<sub>Windows 8 displaying the Share action in the Charms bar.</sub>

In the Windows 8 Metro interface, users can swipe from the screen edge to display the so-called [Charms bar](http://msdn.microsoft.com/en-us/library/windows/apps/br211373.aspx), regardless of the app they are currently using. The Charms bar contains buttons for several often-used actions, such as going back to the start screen or accessing the current app’s settings. Other charms include Search (to search for content from your app, other participating apps, or the file system) and Share (to share content from your app with other users, web services, or other apps).

## Contracts

Each of those charms is related to and governed by a so-called [Contract](http://msdn.microsoft.com/en-us/library/windows/apps/hh464906.aspx). The documentation describes contracts as

> agreements between Windows and one or more Metro style apps, called contract participants, to support some kind of user interaction. There is a contract for each type of interaction, like playing music from an application to a connected stereo, and the contract specifies the types of capabilities the participant has. For example, Windows lets users share content from one application to another. The application that shares content out supports a source contract by meeting specific requirements while the application that receives the shared content supports a target contract by meeting a different set of requirements. Every application that participates in the sharing contract can be confident that the sharing workflow is completely supported, end-to-end.

Similar to Android, Metro apps must declare the contracts they support. They can do this either by specifying them in the app’s manifest file or even dynamically at runtime. In the current developer preview release, Windows 8 supports [five contracts](http://msdn.microsoft.com/en-us/library/windows/apps/hh464906.aspx):

- to search an app’s locally stored content or have an app control a search query that goes out to the web for searching. For example, a YouTube app could offer YouTube online search through this contract.
- to share content from your app with another app or web service.
- to play music and video from an app on other connected devices that support the

  DLNA

  standard. This looks similar to Apple’s

  AirPlay

  .
- to provide access to an app’s settings.
- to let an app directly pick files from another app. This looks like a very elegant solution to the problem that, when all apps are sandboxed, there does not exist a shared folder on the file system that users could use to exchange files between apps. With this contract, a Dropbox client for Windows Metro could offer the user the option to open files that are in the Dropbox directly from within another app, for example.

## The Sharing Contract

Let’s have a look at how content sharing works with the Sharing contract. To make this work, the source application must first declare to the OS that it supports the role of acting as a [sharing source](http://msdn.microsoft.com/en-us/library/windows/apps/hh465261.aspx). The application listens for an event that signifies to the app that the user activated the Share charm. In response to this event, it will then create a [`DataPackage`](http://msdn.microsoft.com/en-us/library/windows/apps/windows.applicationmodel.datatransfer.datapackage.aspx) object that contains the content to be shared. DataPackages are very flexible: they can contain any combination of plain text, URLs, HTML, rich text, images, files or arbitrary binary data. The source application passes the packaged data on to the operating system.

If large amounts of data should be shared, or if the format of the data is not yet determined because it is up to the target application to select one of multiple supported formats, the source application can also set up a sharing delegate that only prepares and packages the data once it has been requested by the target application.[3](#fn:3)

The OS will now present the user with a list of apps that can handle the shared content. Again, the set of suitable apps is determined by parsing the manifest files of all installed apps. Valid apps are those that support the “Receive Shared Content” contract and have indicated that they can handle the data types the OS is currently dealing with.

When the user selects an app from the list, the OS will activate the target app and pass it the shared `DataPackage` object. The app is now expected to deal with the shared data. Depending on the size of the data, it has the option to do this synchronously or asynchronously in the background, thereby letting the user return to the source application before the actual processing is complete. The target app is free in its decision whether to display its own UI or not. When the operation is completed, the SDK provides APIs for the target app to report success or failure to the source app.

# Learnings for iOS

Comparing the two approaches, Android’s system of intents and activities seems extremely flexible. It cannot only be used for sharing content between apps but also for sharing functionality. For example, a Twitter client on Android can seamlessly launch a web browser activity to display a web page, and the user can always go back to the tweet list by using the device’s back button. For a Twitter app on iOS, launching the browser to read an article would result in a very bad user experience.

Microsoft’s concept of contracts seems to be better suited to iOS’s application model. Rather than directly accessing parts of an app (activities/view controllers), the target application of a sharing charm is launched normally and has to decide upon activation how to react to the sharing operation in process. This is very similar to how iOS deals with push notifications or app launches through a URL scheme.

So far, Apple’s approach to content sharing in iOS seems to be offering piecemeal solutions. Over the years, Apple has gradually added system-defined view controllers for system-defined actions: as of iOS 5, apps can share stuff via [e-mail](https://developer.apple.com/library/ios/#documentation/MessageUI/Reference/MFMailComposeViewController_class/Reference/Reference.html), [SMS](https://developer.apple.com/library/ios/#documentation/MessageUI/Reference/MFMessageComposeViewController_class/Reference/Reference.html) or [Twitter](https://developer.apple.com/library/ios/#documentation/Twitter/Reference/TWTweetSheetViewControllerClassRef/Reference/Reference.html) using the built-in view controllers. In addition, apps have write access to the device’s photo library and can sort of share images that way.

## We Need a Generic Sharing API

What’s missing is the generic design. Even if we will see `FBFacebookShareViewController` and `IGInstagramSharePhotoViewController` in the next iOS release, Apple will never be able (or willing) to support a large enough number of sharing services and apps. And interaction between apps via custom URL schemes as currently implemented in iOS also doesn’t cut it: since a source application would need to know about and implement the URL schemes of all potential target apps, this idea just doesn’t scale to 500,000 apps.

A generic sharing API like the ones described above would solve tons of developer issues at one go. For instance, Instapaper developer Marco Arment has been complaining for a long time that [requiring your users to install a bookmarklet in Mobile Safari sucks](http://www.marco.org/2010/10/10/an-open-enhancement-request-to-the-mobile-safari-team). If both Safari and the Instapaper app supported the sharing of URLs and/or web page content, this problem would be solved. Similarly, developers of Twitter apps would no longer have to talk to the Instapaper API directly if they could just share a link with the Instapaper app on the device.[4](#fn:4)

My dream feature for iOS 6 is a combination of the share sheets introduced in Mountain Lion (for displaying the available sharing options) and an implementation similar to Windows 8 contracts that allow for both silent (non-invasive, no UI) and more explicit (with a custom UI like the current mail or tweet compose view controllers) content sharing between apps. If you agree, please [file an enhancement request with Apple](http://bugreport.apple.com/).

1. Activities are usually presented covering the entire screen but this is not a requirement. An activity can also be displayed in a floating window or embedded inside of another activity. These features will remind iOS developers of [popover views](https://developer.apple.com/library/ios/#documentation/uikit/reference/UIPopoverController_class/Reference/Reference.html) on the iPad and [container view controllers](https://developer.apple.com/library/ios/featuredarticles/ViewControllerPGforiPhoneOS/AboutViewControllers/AboutViewControllers.html#//apple_ref/doc/uid/TP40007457-CH112-SW17) in iOS 5. [↩︎](#fnref:1)
2. Identified by the data’s MIME type. The matching of data types and activities is performed based on the information in every app’s manifest file where the developer can list the data types any of their activities can deal with. [↩︎](#fnref:2)
3. OS X uses the same mechanism for drag and drop operations. [↩︎](#fnref:3)
4. Especially if the sharing process could optionally be non-interactive so as to make it a one-tap operation. Windows 8 supports the innovative concept of [QuickLinks](http://msdn.microsoft.com/en-us/library/windows/apps/windows.applicationmodel.datatransfer.sharetarget.quicklink.aspx) where the target app can return a link that corresponds to the last sharing operation that the OS can then display in the Charms bar. [↩︎](#fnref:4)
