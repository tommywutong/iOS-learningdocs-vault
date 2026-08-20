---
title: Data Management and Synchronization for Shared iPad
apple_id: DTS40016748
resource_type: Technical Note
platform: iOS
topic: Data Management
technology: null
published: '2016-03-01'
source_url: https://developer.apple.com/library/archive/technotes/tn2428/_index.html
archived_at: '2026-07-26T19:54:15.067876Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2428

# Data Management and Synchronization for Shared iPad

While any app can implement appropriate support for Shared iPad, developers building for the education market will want to adopt the following best practices to ensure that user-specific data is cloud-based and efficiently managed.

Since local data may be purged when switching users or when the device is reconfigured to meet changed classroom use needs, the following best practices describe the recommended approach for ensuring persistent storage depending on your application architecture and the type and volume of user-specific data.

__Important:__ Indicate support for purgeable local storage support.

Supporting purgeable local storage means that you either have no persistent content of consequence (for example a calculator app) or your app ensures that any content that requires persistence is stored in the cloud. Once you've implemented the following best practices, you'll want to indicate your support for Shared iPad by setting the [NSSupportsPurgeableLocalStorage](https://developer.apple.com/library/prerelease/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html) key to Yes in your project’s Info.plist. Doing so indicates that your app supports having its local data purged when the user logs out.

[Data Management Best Practices](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnzuhawugsbrfvke4vcbi4yq)[Store all user data in the cloud](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnzuhawugsbrfvke4vcbi4zq)[Fetch remote data on demand](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnzuhawugsbrfvke4vcbi42a)[Sync data as it changes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnzuhawugsbrfvke4vcbi42q)[Store first launch or progress flags in the cloud](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnzuhawugsbrfvke4vcbi4yta)[Limit background task assertion requirements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnzuhawugsbrfvke4vcbi43q)[Indicate purgeable local storage support in your project PList](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnzuhawugsbrfvke4vcbi4ytc)[Sync Technologies](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnzuhawugsbrfvke4vcbi4za)[Sync using NSURLSession](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnzuhawugsbrfvke4vcbi43a)[Synchronize credentials via Keychain](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnzuhawugsbrfvke4vcbi44a)[Synchronize data via iCloud](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnzuhawugsbrfvke4vcbi44q)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmnzuhawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Data Management Best Practices

### Store all user data in the cloud

Shared iPad requires a cloud-based synchronization model for any data required to persist between uses of the app. Send data to your own backend using NSURLSession, or use iCloud, NSUbiquitousKeyValueStore, and store credentials in Keychain.

### Fetch remote data on demand

Since all data associated with a given app may not be required at any given time, develop a download strategy that ensures you only download what’s needed when it’s needed or just before. Rather than bringing back all known user content you may need in the app, consider only pulling what’s required in the current context.

### Sync data as it changes

Sync user entered or created data as you get it. Be sure to synchronize during applicationWillResignActive at the minimum but keep in mind that waiting too long or holding an overly large batch for synchronization will provide an inferior user experience and may in rare cases lead to data loss.

### Store first launch or progress flags in the cloud

If your app determines the need for a first launch experience based on a flag currently stored in the local file system or NSUserDefaults, you should move these per-user flags to NSUbiquitousKeyValueStore and check there before presenting your first launch experience.

For more information on the NSUbiquitousKeyValueStore, check out the [NSUbiquitousKeyValueStore Class Reference](https://developer.apple.com/library/ios/documentation/Foundation/Reference/NSUbiquitousKeyValueStore_class/index.html) and [PrefsInCloud sample project](https://developer.apple.com/library/ios/samplecode/PrefsInCloud/Introduction/Intro.html).

### Limit background task assertion requirements

Limit the amount of work you do in background task assertions to the minimum needed to ensure data consistency and synchronization — generally calls to NSURLSession or iCloud APIs to upload the user's data. These APIs provide support to continue the network operation without blocking the transition between users.

### Indicate purgeable local storage support in your project PList

Indicate support for Shared iPad by setting the [NSSupportsPurgeableLocalStorage](https://developer.apple.com/library/prerelease/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html) key to Yes in your project’s Info.plist. Doing so indicates that your app supports having its local data purged when the user logs out.

[Back to Top](#)

## Sync Technologies

### Sync using NSURLSession

Apps using NSURLSession with the appropriate background configuration to push user-specific settings or data will be assured that their uploads will continue after the user has switched apps and, more importantly, after the current user has signed out on a shared iPad.

For more information on NSURLSession, review the WWDC 2015 video [Networking with NSURLSession](https://developer.apple.com/videos/play/wwdc2015-711/), the WWDC 2014 video [What’s New in Foundation Networking](https://developer.apple.com/videos/play/wwdc2014-707/), and the [NSURLSession Class Reference](https://developer.apple.com/library/ios/documentation/Foundation/Reference/NSURLSession_class/index.html).

### Synchronize credentials via Keychain

Keychain on Shared iPad provides automatic synchronization across devices using the same Apple ID. Storing credentials and other lightweight information in Keychain via Keychain Services API ensures they will be secure and available wherever the user signs in.

For more information on Keychain implementation, check out the [Keychain Services Programming Guide](https://developer.apple.com/library/ios/documentation/Security/Conceptual/keychainServConcepts/iPhoneTasks/iPhoneTasks.html).

### Synchronize data via iCloud

Implementing support for iCloud Documents and Key-Value Storage APIs means your user content will be in-sync without having to explicitly manage that synchronization process. While CloudKit is more transactional and under your explicit control, CloudKit operations are designed to ensure data you've committed arrives in iCloud storage even if the app is exited or the user signs out.

Check out the [iCloud Design Guide](https://developer.apple.com/library/ios/documentation/General/Conceptual/iCloudDesignGuide/Chapters/Introduction.html) for which storage API is best for your app.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-02-18 | New document that provides best practices to ensure that user-specific data is cloud-based and efficiently managed on a Shared iPad. |

