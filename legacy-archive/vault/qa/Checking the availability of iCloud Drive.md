---
title: Checking the availability of iCloud Drive
apple_id: DTS40017629
resource_type: QA
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CloudKit
published: '2017-04-11'
source_url: https://developer.apple.com/library/archive/qa/qa1935/_index.html
archived_at: '2026-07-18T02:37:14.833895Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1935

# Checking the availability of iCloud Drive

## Q:  Why does FileManager.default.ubiquityIdentityToken always return nil in my app?

A: `FileManager`’s `ubiquityIdentityToken` property is an API to check whether iCloud Drive is available for your app. Based on the iCloud Drive availability on different platforms, it may return a valid token or nil.

On iOS and macOS, iCloud Drive is available, so the API returns a valid token if iCloud is properly configured for your app and your testing device. The reasons you see it returning nil can be:

1. Your testing device doesn’t have an iCloud account signed in; or it has but iCloud Drive is off for your app. To turn on iCloud Drive, launch `Settings` on your iOS device or `System Preferences` on your Mac, sign in iCloud with your Apple ID, then navigate to the iCloud setting screen and make sure iCloud Drive is on. If your app is listed there, be sure to turn on its checkbox as well. (On a Mac, you could click the `Options...` button to show the app list.)
2. The iCloud capability is not added to your app. You can add it by opening your project with the latest version of Xcode, selecting your app target, then checking the iCloud box in the `Capabilities` pane and picking the service you need. See [Adding iCloud Support](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/AddingCapabilities/AddingCapabilities.html#//apple_ref/doc/uid/TP40012582-CH26-SW2) for details. (Before doing that, be sure to let Xcode manage the provisioning for your app by turning on the `Automatically manage signing` option and specifying an appropriate team in the `General` pane, as described in [QA1814](https://developer.apple.com/library/content/qa/qa1814/_index.html#//apple_ref/doc/uid/DTS40014030).)

On watchOS and tvOS, iCloud Drive is unavailable, `ubiquityIdentityToken` hence always returns nil for watchOS 2 WatchKit extensions and tvOS apps. When accessing the property for the first time, you might see an error (Code=4099) complaining that the connection to the system's token service was invalidated on your Xcode console, as shown in Listing 1.

__Listing 1__  Error message generated when ubiquityIdentityToken is first-time accessed on watchOS or tvOS.

```
[ERROR] error while getting ubiquityIdentityToken: Error Domain=NSCocoaErrorDomain Code=4099 "The connection to service named com.apple.bird.token was invalidated." UserInfo={NSDebugDescription=The connection to service named com.apple.bird.token was invalidated.}
```

Since iCloud Drive is unavailable on watchOS and tvOS (and iCloud Key-Value Store is unavailable on watchOS), you might consider [CloudKit](https://developer.apple.com/library/content/documentation/DataManagement/Conceptual/CloudKitQuickStart/Introduction/Introduction.html) when an iCloud service is needed on those platforms, and use `CKContainer`'s `accountStatus(completionHandler:)` method for iCloud account availability checking.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-04-11 | New document that describes the iCloud Drive availability on Apple's platforms. |

