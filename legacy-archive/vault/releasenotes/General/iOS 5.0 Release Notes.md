---
title: iOS 5.0 Release Notes
apple_id: TP40010949
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2011-10-25'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-iOSSDK-5_0/index.html
archived_at: '2026-07-18T02:54:41.814254Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# iOS SDK Release Notes for iOS 5.0

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydsnbzfvbuqmjnknlte)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydsnbzfvbuqmjnknltg)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydsnbzfvbuqmjnknlti)

### Introduction

iOS SDK 5 provides support for developing iOS applications and includes the complete set of Xcode tools, compilers, and frameworks for creating applications for iOS and Mac OS X. These tools include the Xcode IDE and the Instruments analysis tool among many others.

With this software you can develop applications that run on iPhone, iPad, or iPod touch running iOS 5. You can also test your applications using the included iOS Simulator, which supports iOS 5. There are two Xcode iOS SDK 5 images, one for installing on a Macintosh computer running Mac OS X 10.6.7 (Snow Leopard) or later, the other for installing on a Macintosh computer running Mac OS X 10.7 (Lion).

This version of iOS is intended only for installation on devices registered with Apple's developer program. Attempting to install this version of iOS in an unauthorized manner could put your device in an unusable state.

For more information and additional support resources, visit:

[http://developer.apple.com/programs/ios/](https://developer.apple.com/programs/ios/)

### Bug Reporting

Please report any bugs not mentioned in the [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydsnbzfvbuqmjnknlte) section using the Apple Bug Reporter on the Apple Developer website ([http://developer.apple.com/bugreporter/](https://developer.apple.com/bugreporter/)). Additionally, you may discuss these issues and iOS SDK 5 in the Apple Developer Forums: [http://devforums.apple.com](http://devforums.apple.com/). You can also access more information about iCloud for Developers at: [http://developer.apple.com/icloud](https://developer.apple.com/icloud)

### Notes and Known Issues

The following issues relate to using the 5 SDK to develop code.

### Accounts

- When creating an iCloud account, you can use any Apple ID as long as it is a full email address and not a MobileMe account. If you have a MobileMe account, you can move that account to iCloud. You can find more information at: [http://me.com/move](https://developer.apple.com/icloud)

### AirPlay

- Starting in iOS 5, AirPlay is enabled by default for video content in applications and websites.
- In iOS 5, AV Foundation adds support for video playback via AirPlay.

### APIs

- The [NSNetService](https://developer.apple.com/documentation/foundation/netservice) class and CFNetService APIs do no include P2P interfaces by default. To browse, register, or resolve services over P2P interfaces, an application needs to use the Bonjour `DNSService*()` APIs noted below.
- Setting the _interfaceIndex_ parameter to [kDNSServiceInterfaceIndexAny](https://developer.apple.com/documentation/dnssd/kdnsserviceinterfaceindexany) in the following API's will not include P2P interfaces by default. To include P2P interfaces, you must now set the `kDNSServiceFlagsIncludeP2P` flag when using `kDNSServiceInterfaceIndexAny` or set the interfaceIndex to `kDNSServiceInterfaceIndexP2P`. The affected APIs are:

  - [DNSServiceBrowse](https://developer.apple.com/documentation/dnssd/1804742-dnsservicebrowse)
  - [DNSServiceRegister](https://developer.apple.com/documentation/dnssd/1804733-dnsserviceregister)
  - [DNSServiceResolve](https://developer.apple.com/documentation/dnssd/1804744-dnsserviceresolve)
  - [DNSServiceRegisterRecord](https://developer.apple.com/documentation/dnssd/1804727-dnsserviceregisterrecord)
  - [DNSServiceQueryRecord](https://developer.apple.com/documentation/dnssd/1804747-dnsservicequeryrecord)

### API Validation

- In the iOS 5 development tools, it is possible to extract APIs used by an application and have them checked for use of private APIs. This option is offered when you validate your application for app submission.

### Apple TV

- The Apple TV Software enables users to mirror the contents of an iPad 2 to an Apple TV (2nd generation) using AirPlay. This software also enables Photo Stream on Apple TV so users can access photos stored in iCloud. The Apple TV Software beta is provided to test the latest AirPlay functionality in your iOS 5 apps and web sites. If you wish to install the Apple TV Software beta on your device, you must first register your device UDID in the iOS Developer Program Portal.

### Automatic Reference Counting

- In Xcode, if the configuration is set to Device and there is a space in the path of one of the source files (more commonly, the project is inside a directory with spaces), the “Convert to Automatic Reference Counting” step (after Precheck) will fail with error: `Error in format of file: <path>`.

  If encountered, the user should switch to Simulator and retry the migration.

### Binary Compatibility

- On applications linked against the iOS 5 SDK, scroll view content offsets will no longer be rounded to integral pixels during a pinch gesture.

### GameKit

- Match data for turn-based matches is limited to 4 KB.
- _FIXED:_ Auto-matching with the turn-based view controller does not work. Invites or the direct auto-match API can be used as a workaround.

### iCloud Backup

- Backups made prior to September 22nd are no longer available. It is strongly advised to upgrade to this version of iOS 5 in order to continue backing up your devices

### iCloud Storage

- In the iCloud key-value store, the maximum number of keys has been raised to 256.
- All newly generated provisioning profiles are now automatically enabled for iCloud. If you are using an Xcode managed Team Provisioning Profile, click refresh in the Xcode Organizer to obtain a new iCloud-enabled profile. To enable all other provisioning profiles for iCloud, simply regenerate your profiles in the iOS Provisioning Portal.
- If your application is using the [NSMetadataQuery](https://developer.apple.com/documentation/foundation/nsmetadataquery) class, you must set a predicate and the predicate is now honored. But the predicate is an [NSPredicate](https://developer.apple.com/documentation/foundation/nspredicate)-style predicate, not a Spotlight-style predicate. An example of the difference is that you must use `LIKE` instead of `=` for wildcard matching. The differences are defined in more detail at: [http://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/Predicates/Articles/pSpotlightComparison.html#//apple_ref/doc/uid/TP40002370-SW1](https://developer.apple.com/icloud).
- The [setSortDescriptors:](https://developer.apple.com/documentation/foundation/nsmetadataquery/1411847-sortdescriptors) method of `NSMetadataQuery` is not supported.
- To enable iCloud storage within your apps in iOS 5, click the Enable Entitlements checkbox in the Summary pane of your project. Xcode creates a custom entitlements file for your project that automatically includes your Team ID. You can add additional iCloud Container values as required by your application. (Note that you must regenerate your existing provisioning profiles, either with Xcode or in the iOS Provisioning Portal, to use iCloud storage.)
- The container identifier string you pass to the [URLForUbiquityContainerIdentifier:](https://developer.apple.com/documentation/foundation/nsfilemanager/1411653-urlforubiquitycontaineridentifie) method of `NSFileManager` _must_ include the team ID at the beginning of the string. As a convenience, you can pass `nil` to retrieve the first document container ID specified in your app’s entitlements.
- In iOS 5, files that are protected via Data Protection cannot be used with iCloud Storage APIs.
- File presenters—objects that adopt the [NSFilePresenter](https://developer.apple.com/documentation/foundation/nsfilepresenter) protocol—do not receive some of the messages that they are supposed to receive, including:

  - [presentedSubitemDidChangeAtURL:](https://developer.apple.com/documentation/foundation/nsfilepresenter/1411135-presentedsubitemdidchangeaturl)

  As a work around, implement the [relinquishPresentedItemToWriter:](https://developer.apple.com/documentation/foundation/nsfilepresenter/1413688-relinquishpresenteditemtowriter) method and check to see if the writer actually wrote when your file presenter reacquires the file.
- If you report a bug related to the iCloud storage interfaces, please include the logs collected during your debugging session. To generate these logs, you must install a special debug profile on your device.

  The debug profile can be obtained from [http://connect.apple.com](http://connect.apple.com/). This profile enables the generation of debug logs that are needed to diagnose any problems using iCloud storage. The instructions to collect the logs are:

  1. Install the profile. (The easiest way to do this is to mail it to yourself and open the attachment on your device.)
  2. Reproduce the bug.
  3. Sync with iTunes to pull the logs off your device.
  4. Attach the logs to your bug report. You can find the logs in `~/Library/Logs/CrashReporter/MobileDevice/DeviceName/DiagnosticLogs`.

  These logs can grow large very quickly, so you should remove the profile after you have reproduced the problem and pulled the logs of your device.
- File names are case-insensitive in Mac OS X but case-sensitive in iOS. This can lead to problems when sharing files between the two using iCloud. You should take steps on iOS to avoid creating files whose names differ only by case.

### Movie Player

Starting in iOS 5.0, in order to facilitate finer-grained playback control, a movie player is not automatically prepared to play upon creation. Call the [prepareToPlay](https://developer.apple.com/documentation/mediaplayer/mpmediaplayback/1616251-preparetoplay) method to prepare the movie player. For more information, see _[MPMoviePlayerController Class Reference](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller)_.

### Music Player

- _FIXED:_ When deleting a song or video from Music/Videos on the device, the Music Player app crashes.

### Security

- In iOS 5, the signing of certificates with MD5 signatures is not supported. Please ensure that certificates use signature algorithms based on SHA1 or SHA2.

### Springboard

- Push and local notifications for apps appear in the new Notification Center in iOS 5. Notification Center displays notifications that are considered "unread.” To accommodate push and local notifications that have no unread status, set your application’s badge count to 0 to clear that app’s notifications from Notification Center.

### UI Automation

- When using the `performTaskWithPathArgumentsTimeout` method of `UIAHost` in a UI Automation script where the API outputs excessively (say, thousands of lines of text) to standard out or standard error, the task may deadlock until the timeout is reached, at which point it will throw a JavaScript exception.
- The `lock()` and `unlock()` functions of `UIATarget` have been replaced with the `lockForDuration(`_<seconds>_`)` function.
- In iOS 5, you can now trigger the execution of a UI Automation script on an iOS device from the host terminal by using the instruments tool. The command is:

  - `instruments -w <device id> -t <template> <application>`
- When using the cli instruments for UI Automation you can now target the default Automation Template and pass the script and results path into the tool as environment variable options. For example:

  - `instruments -w <device id> -t /Developer/Platforms/iPhoneOS.platform/Developer/Library/Instruments/PlugIns/AutomationInstrument.bundle/Contents/Resources/Automation.tracetemplate <application> -e UIASCRIPT <script> -e UIARESULTSPATH <results path>`

### UIKit

- Rotation callbacks in iOS 5 are not applied to view controllers that are presented over a full screen. What this means is that if your code presents a view controller over another view controller, and then the user subsequently rotates the device to a different orientation, upon dismissal, the underlying controller (i.e. presenting controller) will not receive any rotation callbacks. Note however that the presenting controller will receive a [viewWillLayoutSubviews](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621437-viewwilllayoutsubviews) call when it is redisplayed, and the [interfaceOrientation](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621373-interfaceorientation) property can be queried from this method and used to lay out the controller correctly.
- In iOS 5, the [UIPickerView](https://developer.apple.com/documentation/uikit/uipickerview) class doesn't send its [pickerView:didSelectRow:inComponent:](https://developer.apple.com/documentation/uikit/uipickerviewdelegate/1614371-pickerview) delegate message in response to the programatic selection of an item.
- Returning `nil` from the [tableView:viewForHeaderInSection:](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614901-tableview) method (or its footer equivalent) is no longer sufficient to hide a header. You must override [tableView:heightForHeaderInSection:](https://developer.apple.com/documentation/uikit/uitableviewdelegate/1614855-tableview) and return `0.0` to hide a header.
- In iOS 5, the [UITableView](https://developer.apple.com/documentation/uikit/uitableview) class has two methods to move one cell from one row to another with defined parameters. These APIs are:

  - [moveSection:toSection:](https://developer.apple.com/documentation/uikit/uitableview/1614940-movesection)
  - [moveRowAtIndexPath:toIndexPath:](https://developer.apple.com/documentation/uikit/uitableview/1614987-moverow)
- Using the [UIWebView](https://developer.apple.com/documentation/uikit/uiwebview) class in Interface Builder, setting a transparent background color is possible in iOS 5. Developers compiling against the new SDK can check their XIB for the `UIWebView` transparent setting.
- In iOS 5, the [UINavigationBar](https://developer.apple.com/documentation/uikit/uinavigationbar), [UIToolbar](https://developer.apple.com/documentation/uikit/uitoolbar), and [UITabBar](https://developer.apple.com/documentation/uikit/uitabbar) implementations have changed so that the [drawRect:](https://developer.apple.com/documentation/uikit/uiview/1622529-draw) method is not called unless it is implemented in a subclass. Apps that have re-implemented `drawRect:` in a category on any of these classes will find that the `drawRect:` method isn't called. UIKit does link-checking to keep the method from being called in apps linked before iOS 5 but does not support this design on iOS 5 or later. Apps can either:

  - Use the customization API for bars in iOS 5 and later, which is the preferred way.
  - Subclass `UINavigationBar` (or the other bar classes) and override `drawRect:` in the subclass.
- The [indexPathForRow:inSection:](https://developer.apple.com/documentation/foundation/nsindexpath/1614934-init), `section`, and `row` methods of [NSIndexPath](https://developer.apple.com/documentation/foundation/nsindexpath) now use [NSInteger](https://developer.apple.com/documentation/objectivec/nsinteger) instead of [NSUInteger](https://developer.apple.com/documentation/objectivec/nsuinteger), so that these types match with methods defined on [UITableView](https://developer.apple.com/documentation/uikit/uitableview).
- The behavior of the [UITableView](https://developer.apple.com/documentation/uikit/uitableview) class’s [scrollToRowAtIndexPath:atScrollPosition:animated:](https://developer.apple.com/documentation/uikit/uitableview/1614997-scrolltorowatindexpath) method has changed. If a scroll position of [UITableViewScrollPositionTop](https://developer.apple.com/documentation/uikit/uitableview/scrollposition/top) or [UITableViewScrollPositionBottom](https://developer.apple.com/documentation/uikit/uitableviewscrollposition/uitableviewscrollpositionbottom) is specified, the method now adjusts for the top and bottom portions of the [contentInset](https://developer.apple.com/documentation/uikit/uiscrollview/1619406-contentinset) property.
- In releases prior to iOS 5, the [UIPopoverController](https://developer.apple.com/documentation/uikit/uipopovercontroller) class would unconditionally set the autoresizing masks of view controllers that provided the content for the popover controller. It would also unconditionally set the autoresizing masks of the views of view controllers pushed on to a [UINavigationController](https://developer.apple.com/documentation/uikit/uinavigationcontroller) object which was the content view controller of the popover controller.

  The `UIPopoverController` class no longer does this for applications linked against iOS 5 or later. Developers should ensure that the autoresizing masks of views are set properly to allow for arbitrary resizing within any container, not just popovers. A mask of `(`[UIViewAutoresizingFlexibleWidth](https://developer.apple.com/documentation/uikit/uiviewautoresizing/uiviewautoresizingflexiblewidth) `|` [UIViewAutoresizingFlexibleHeight](https://developer.apple.com/documentation/uikit/uiviewautoresizing/uiviewautoresizingflexibleheight)`)` is reasonable.
- The completion handler for [saveToURL:forSaveOperation:completionHandler:](https://developer.apple.com/documentation/uikit/uidocument/1619988-save) is called outside of the coordinated write block.
- The [autosaveWithCompletionHandler:](https://developer.apple.com/documentation/uikit/uidocument/1619981-autosave) method is now only called for period-based saves when it is safe to return without saving. Documents must save, though, if the [saveToURL:forSaveOperation:completionHandler:](https://developer.apple.com/documentation/uikit/uidocument/1619988-save) method is invoked.

### Safari and WebKit

- In iOS 5, a new inherited CSS property, `-webkit-overflow-scrolling`, is available. The value `touch` allows the web developer to opt in to native-style scrolling in an `overflow:scroll` element. The default value for this property is `auto`, which allows single-finger scrolling without momentum.
- The WebKit framework has been updated to a version which closely matches the engine used by Safari 5.1 on the Desktop. There are some areas to be aware of with the new WebKit framework on iOS 5. Specifically, for web sites and native apps that use UIWebView:

  - There is a new HTML5-compliant parser.
  - Text layout width may change slightly because word-rounding behavior now has floating-point-based precision.
  - There is improved validation of the `<input type=number>` form field, which includes removing leading zeros and number formatting.
  - Touch events are now supported on input fields.
  - `<input type=range>` is now supported.
  - `window.onerror` is now supported.
  - There is a new user agent that does not have locale information in the User Agent string.
  - URLs are now canonicalized by making the scheme all lowercase. If a fake URL is used to pass information from a [UIWebView](https://developer.apple.com/documentation/uikit/uiwebview) back to native code, make sure that the scheme is always lowercase, or that the native code compares the scheme in a case-insensitive manner.

### Wi-Fi Syncing

- Wireless syncing support requires Mac OS X 10.6.8 or Lion. You will see an option to enable wireless syncing when you connect your device to iTunes with the USB cable. It is recommended you perform your initial sync with a cable after restoring your device.

  - Wireless syncing is triggered automatically when the device is connected to power and on the same network as the paired computer. Or, you can manually trigger a sync from iTunes or from Settings > General > iTunes Sync (same network as paired computer required).
  - If you find issues with apps, media and/or photos synced to your device, you can reset then resync. From Settings > General > Reset, choose Erase all Content and Settings. Then reconnect to iTunes and sync again.

### Xcode Tools

For information about changes to Xcode, Interface Builder, Instruments, and iOS Simulator, see _[Xcode Release Notes](../Developer%20Tools/Xcode%20Release%20Notes/Xcode%20Release%20Notes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanjr)_.
