---
title: iOS 5.1 Release Notes
apple_id: TP40011329
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2012-03-07'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-iOSSDK-5_1/index.html
archived_at: '2026-07-18T02:54:41.872889Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# iOS SDK Release Notes for iOS 5.1

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmrzfvbuqmjnknlte)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmrzfvbuqmjnknltg)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmrzfvbuqmjnknlti)

### Introduction

iOS SDK 5.1 provides support for developing iOS applications and includes the complete set of Xcode tools, compilers, and frameworks for creating applications for iOS and OS X. These tools include the Xcode IDE and the Instruments analysis tool among many others.

With this software you can develop applications that run on iPhone, iPad, or iPod touch running iOS 5.1. You can also test your applications using the included iOS Simulator, which supports iOS 5.1. iOS SDK 5.1 requires a Macintosh computer running OS X 10.7 (Lion).

This version of iOS is intended only for installation on devices registered with Apple's developer program. Attempting to install this version of iOS in an unauthorized manner could put your device in an unusable state.

For more information and additional support resources, visit:

[http://developer.apple.com/programs/ios/](https://developer.apple.com/programs/ios/)

### Bug Reporting

Please report any bugs not mentioned in the [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytgmrzfvbuqmjnknlte) section using the Apple Bug Reporter on the Apple Developer website ([http://developer.apple.com/bugreporter/](https://developer.apple.com/bugreporter/)). Additionally, you may discuss these issues and iOS SDK 5 in the Apple Developer Forums: [http://devforums.apple.com](http://devforums.apple.com/). You can also access more information about iCloud for Developers at: [http://developer.apple.com/icloud](https://developer.apple.com/icloud)

### Notes and Known Issues

The following issues relate to using the 5.1 SDK to develop code.

### Accounts

- When creating an iCloud account, you can use any Apple ID as long as it is a full email address and not a MobileMe account. If you have a MobileMe account, you must move that account to iCloud. You can find more information at: [http://me.com/move](https://developer.apple.com/icloud)

### APIs

- The [NSNetService](https://developer.apple.com/documentation/foundation/netservice) class and CFNetService APIs do not include P2P interfaces by default. To browse, register, or resolve services over P2P interfaces, an application needs to use the Bonjour `DNSService*()` APIs noted below. For more information, see _[Bonjour over Bluetooth on iOS 5 and Later](https://developer.apple.com/library/archive/qa/qa1753/_index.html#//apple_ref/doc/uid/DTS40011315)_.
- Setting the _interfaceIndex_ parameter to [kDNSServiceInterfaceIndexAny](https://developer.apple.com/documentation/dnssd/kdnsserviceinterfaceindexany) in the following API's will not include P2P interfaces by default. To include P2P interfaces, you must now set the `kDNSServiceFlagsIncludeP2P` flag when using `kDNSServiceInterfaceIndexAny` or set the interfaceIndex to `kDNSServiceInterfaceIndexP2P`. The affected APIs are:

  - [DNSServiceBrowse](https://developer.apple.com/documentation/dnssd/1804742-dnsservicebrowse)
  - [DNSServiceRegister](https://developer.apple.com/documentation/dnssd/1804733-dnsserviceregister)
  - [DNSServiceResolve](https://developer.apple.com/documentation/dnssd/1804744-dnsserviceresolve)
  - [DNSServiceRegisterRecord](https://developer.apple.com/documentation/dnssd/1804727-dnsserviceregisterrecord)
  - [DNSServiceQueryRecord](https://developer.apple.com/documentation/dnssd/1804747-dnsservicequeryrecord)

### Backup

- iOS 5.1 introduces a new API to mark files or directories that should not be backed up. For `NSURL` objects, add the [NSURLIsExcludedFromBackupKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1408756-isexcludedfrombackupkey) attribute to prevent the corresponding file from being backed up. For `CFURLRef` objects, use the corresponding [kCFURLIsExcludedFromBackupKey](https://developer.apple.com/documentation/corefoundation/kcfurlisexcludedfrombackupkey) attribute.

  Apps running on iOS 5.1 and later must use the newer attributes and not add the `com.apple.MobileBackup` extended attribute directly, as previously documented. The `com.apple.MobileBackup` extended attribute is deprecated and support for it may be removed in a future release.

### iCloud Photo Stream

- Photos taken using iOS 5.1 can be deleted from Photo Stream on your device and will be removed automatically from Photo Stream on your other iOS 5.1 devices. Older photos can be manually deleted from your iOS 5.1 devices.

### iCloud Storage

- Provisioning profiles must be enabled for iCloud in the iOS Provisioning Portal. To enable a provisioning profile for iCloud, navigate to the App ID section of the iOS Provisioning Portal and configure your App ID for iCloud. After enabling the App ID for iCloud, regenerate your provisioning profiles to enable them for iCloud.
- The [setSortDescriptors:](https://developer.apple.com/documentation/foundation/nsmetadataquery/1411847-sortdescriptors) method of `NSMetadataQuery` is not supported.
- In iOS 5, files that are protected via Data Protection cannot be used with iCloud Storage APIs.
- File names are case-insensitive in OS X but case-sensitive in iOS. This can lead to problems when sharing files between the two using iCloud. You should take steps on iOS to avoid creating files whose names differ only by case.

### Movie Player

- Starting in iOS 5.0, in order to facilitate finer-grained playback control, a movie player is not automatically prepared to play upon creation. Call the [prepareToPlay](https://developer.apple.com/documentation/mediaplayer/mpmediaplayback/1616251-preparetoplay) method to prepare the movie player. For more information, see _[MPMoviePlayerController Class Reference](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller)_.

### Security

- In iOS 5, signing a certificate with an MD5 signature is not supported. Please ensure that certificates use signature algorithms based on SHA1 or SHA2.

### UIKIT

- In 5.1 the [UISplitViewController](https://developer.apple.com/documentation/uikit/uisplitviewcontroller) class adopts the sliding presentation style when presenting the left view (previously only seen in Mail). This style is used when presentation is initiated either by the existing bar button item provided by the delegate methods or by a swipe gesture within the right view. No additional API adoption is required to obtain this behavior, and all existing API, including that of the `UIPopoverController` instance provided by the delegate, will continue to work as before. If the gesture cannot be supported in your app, set the `presentsWithGesture` property of your split view controller to `NO` to disable the gesture. However, disabling the gesture is discouraged because its use preserves a consistent user experience across all applications.

### Xcode/Developer Tools

- This release of Xcode 4.3 is distributed as a single application bundle, [Xcode.app]. Delivering the Xcode tools in a single app bundle allows Xcode to be installed directly from the App Store, without the additional step of running the Install Xcode app. To develop for iOS 5.1, install Xcode from the App Store.

  Within Xcode, you can launch additional developer tools, such as Instruments and FileMerge, via the menu item Xcode -> Open Developer Tool. You can then pin the tool on your Dock for access when Xcode is not running. Many of the tools previously included in the Xcode installer are now available as additional packages from the Downloads Preference Pane.
