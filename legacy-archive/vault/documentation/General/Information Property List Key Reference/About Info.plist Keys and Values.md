---
title: Information Property List Key Reference
apple_id: TP40009247
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: General
technology: null
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Introduction/Introduction.html
archived_at: '2026-07-15T07:34:59.480726Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](About%20Information%20Property%20List%20Files.md)

# About Info.plist Keys and Values

To provide a better experience for users, iOS and macOS rely on the presence of special metadata in each app or bundle. This metadata is used in many different ways. Some of it is displayed to the user, some of it is used internally by the system to identify your app and the document types it supports, and some of it is used by the system frameworks to facilitate the launch of apps. The way an app provides its metadata to the system is through the use of a special file called an _information property list file_, or `Info.plist` for short.

A property list is a way to structure arbitrary data that the system can access at runtime. An _information_ property list is a specialized type of property list that contains configuration data for a bundle. The keys and values in the file describe the various behaviors and configuration options you want applied to your bundle. An Xcode project template typically specifies an information property list file with an initial set of keys and appropriate default values. You can edit the file to change or add keys and values, as appropriate for your project.

This document describes the keys and corresponding values that you can include in an information property list file. This document also includes an overview of information property list files to help you understand their importance and to provide tips on how to configure them.

### The Info.plist File Configures Your App

Every app and plug-in uses an `Info.plist` file to store configuration data in a place where the system can easily access it. macOS and iOS use `Info.plist` files to determine what icon to display for a bundle, what document types an app supports, and many other behaviors that have an impact outside the bundle itself.

### Core Foundation Keys Describe Common Behavior

There are many keys that you always specify, regardless of the type of bundle you are creating. Those keys start with a CF prefix and are known as the Core Foundation keys. Xcode includes the most important keys in your `Info.plist` automatically but there are others you must add manually.

### Launch Services Keys Describe Launch-Time Behavior

Launch Services provides support for launching apps. To do this, though, it needs to know information about how your app wants to be launched. The Launch Services keys describe the way your app prefers to be launched.

### Cocoa Keys Describe Behavior for Cocoa and Cocoa Touch Apps

The Cocoa and Cocoa Touch frameworks use keys to identify high-level information such as your app’s main nib file and principal class. The Cocoa keys describe those and other keys that affect how the Cocoa and Cocoa Touch frameworks initialize and run your app.

### macOS Keys Describe Behavior for macOS Apps

Some macOS frameworks use keys to modify their basic behavior. Developers of Mac apps might include these keys during testing or to modify certain aspects of your app’s behavior.

### iOS Keys Describe Behavior for iOS Apps

An iOS app communicates a lot of information to the system using `Info.plist` keys. Xcode supplies a standard `Info.plist` with the most important keys but most apps need to augment the standard file with additional keys describing everything from the app’s initial orientation to whether it supports file sharing.

### watchOS Keys Describe Behavior for Watch Apps

Use the `Info.plist` keys associated with the watchOS frameworks to configure your Watch apps and WatchKit extensions.

### App Extension Keys Describe Behavior for iOS and macOS App Extensions

App extensions let you make custom behaviors available in other apps and in system facilities such as notification center. Xcode’s app extension templates each supply a standard `Info.plist` file with the most important keys, but you can specify additional keys that describe custom behavior for your app extensions.

For an introduction to property lists, including how they are structured and how you use them in general, see _[Property List Programming Guide](../../Cocoa/Property%20List%20Programming%20Guide/Introduction%20to%20Property%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2dq2i)_.

Some `Info.plist` keys use Uniform Type Identifiers (UTIs) to refer to data of different types. For an introduction to UTIs and how they are specified, see _[Uniform Type Identifiers Overview](../../File%20Management/Uniform%20Type%20Identifiers%20Overview/Introduction%20to%20Uniform%20Type%20Identifiers%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgmjz)_.

Kernel extension developers need to use certain `Info.plist` keys in different ways than app developers do, and also need some kernel-extension-specific keys that have no use in app development. _If you are developing a kernel extension_, refer to the chapter [Info.plist Properties for Kernel Extensions](https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KEXTConcept/Articles/infoplist_keys.html#//apple_ref/doc/uid/TP40009481) in _[Kernel Extension Programming Topics](../../Darwin/Kernel%20Extension%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrt)_.

[Next](About%20Information%20Property%20List%20Files.md)

