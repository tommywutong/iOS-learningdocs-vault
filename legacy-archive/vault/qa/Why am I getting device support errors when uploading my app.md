---
title: Why am I getting device support errors when uploading my app?
apple_id: DTS40010601
resource_type: QA
platform: iOS
topic: Languages & Utilities
technology: null
published: '2012-09-18'
source_url: https://developer.apple.com/library/archive/qa/qa1623/_index.html
archived_at: '2026-07-18T02:32:58.211156Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1623

# Why am I getting device support errors when uploading my app?

## Q:  Why am I getting an error about supporting previous devices when I upload an update of my app?

A: iTunes Connect does not allow uploading an updated version of an app when the update runs on fewer devices than the version of the app currently in the App Store. This is by design.

An update to an app must work for every customer who has already purchased the app, and is running a current version of iOS.

Developers who wish to issue updates, but remove device support, have three choices:

- Fix their app so that it can work on the devices they originally set out to support. See Supporting All Devices for details.
- Target a newer version of iOS that requires a newer device. See Targeting the Latest iOS for details.
- Remove their app from the store, and upload the new app with a different bundle ID. See Replacing Your App in the Store for details.

Depending on how you narrow the devices your app supports, you will get one of two error messages from Xcode when uploading your update to the App Store.

__"This bundle is invalid. The key UIRequiredDeviceCapabilities in the Info.plist may not contain values that would prevent this application from running on devices that were supported by previous versions."__

When you see this error message, you have added a new constraint, under the [UIRequiredDeviceCapabilities](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.html#//apple_ref/doc/uid/TP40009252-SW3) key in your app's info.plist file.

__"This bundle does not support one or more of the devices that were supported in the previous bundle for this app. Bundles must continue to support any devices previously supported."__

When you see this error message, you have changed the "Targeted Device Family" build setting (which modifies the [UIDeviceFamily](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.html#//apple_ref/doc/uid/TP40009252-SW11) info.plist key.)

An update to an app can always require a newer version of iOS. This will drop support for devices that cannot run that version of iOS.

The "iOS Deployment Target" build setting is the minimum version of iOS your app supports. Your app cannot be installed or run on any device that cannot run that version of iOS.

Because an `armv7` processor is required to run versions of iOS later than 4.2.1, setting the "iOS Deployment target" to 4.3 or later means you no longer have to build your app for `armv6`.

For example, if your app is no longer built with `armv6`, you should not add `armv7` to your `UIRequiredDeviceCapabilities`. This may cause Xcode or iTunes Connect to erroneously reject your update.

You can detect capabilities of the device and operating system your app is running on, and selectively enable or disable features as appropriate. See [Using Runtime Checks to Create Conditional Code Paths](https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/AdvancedAppTricks/AdvancedAppTricks.html#//apple_ref/doc/uid/TP40007072-CH7-SW23) for more information.

While it is fine to disable a feature that is not supported by the device your app is running on, be aware that apps won't be accepted into the App Store if they don't have sufficient functionality with the feature disabled. (See "[App Store Review Guidelines](https://developer.apple.com/appstore/resources/approval/guidelines.html)" 2.12.)

__Listing 1__  Objective-C Class:

```
if([NewClass class]){
    NewClass * myObject = [[NewClass alloc] init];
} else {
    //NewClass not supported on this system…
}
```


__Listing 2__  Objective-C Method:

```
 if [myObject respondsToSelector:@selector(updatedMethod)]) {
    [myObject updatedMethod];
} else {
    // -updatedMethod not supported on this system…
}
```


__Listing 3__  Constant:

```
 if (&kNewConstant != NULL) {
    [myObject methodWithOption:kNewConstant];
} else {
    // kNewConstant not supported on this system,
    //using it will cause a crash trying to load from NULL
    [myObject methodWithOption:kOldConstant];
}
```


__Listing 4__  Function:

```
 if (NewFunction != NULL) {
    NewFunction(...);
} else {
    // NewFunction not supported on this system…
}
```


[MessageComposer](https://developer.apple.com/library/ios/samplecode/MessageComposer/) is an example project that supports old systems, while using modern APIs.

Removing your app from the store, and uploading the update with a different bundle ID, will allow you to narrow the range of devices your update supports. However the update will be listed on the store as a separate app. Existing users of your app must purchase the update through the App Store, just like new customers.

Because the update will be treated as a different app, it must have a different name in iTunes Connect than the name of the app already in the store.

For more information on working with iTunes Connect see the [iTunes Connect Developer Guide](http://itunesconnect.apple.com/docs/iTunesConnect_DeveloperGuide.pdf).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2012-09-18 | Added information about targeting the latest version of iOS. |
| 2010-12-23 | New document that explains how to deal with errors from attempting to narrow the class of devices an app supports. |

