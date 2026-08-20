---
title: iOS 8.1.1 Release Notes
apple_id: TP40014993
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-11-03'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-iOSSDK-8.1/index.html
archived_at: '2026-07-18T02:54:42.220614Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# iOS SDK Release Notes for iOS 8.1.1

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dsojtfvbuqmjnknlte)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dsojtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Performance Improvements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dsojtfvbuqmjnknltg)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dsojtfvbuqmjnknlti)

### Introduction

iOS SDK 8.1.1 provides support for developing iOS apps. It is packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for iOS and OS X. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

With this software you can develop apps for iPhone, iPad, or iPod touch running iOS 8. You can also test your apps using the included iOS Simulator, which supports iOS 8. iOS SDK 8.1.1 requires a Mac computer running OS X v10.9.3 (Mavericks) or later.

This version of iOS is intended for installation only on devices registered with the Apple Developer Program. Attempting to install this version of iOS in an unauthorized manner could put your device in an unusable state.

For more information and additional support resources, visit [http://developer.apple.com/programs/ios/](https://developer.apple.com/programs/ios/).

### Bug Reporting

For issues not mentioned in the [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dsojtfvbuqmjnknlti) section, please file bugs through the Apple Developer website ([https://developer.apple.com/bug-reporting/ios/](https://developer.apple.com/bugreporter/)). Additionally, you may discuss these issues and iOS SDK 8.1.1 in the Apple Developer Forums: [http://devforums.apple.com](http://devforums.apple.com/). To get more information about iCloud for Developers, go to [http://developer.apple.com/icloud](https://developer.apple.com/icloud).

### Performance Improvements

This release includes bug fixes, increased stability and performance improvements for iPad 2 and iPhone 4s.

### Notes and Known Issues

The following issues relate to using iOS SDK 8.1.1 to develop code.

### AVCapture

### Known Issue

Use of the new constant, [AVCaptureISOCurrent](https://developer.apple.com/documentation/avfoundation/avcaptureisocurrent), will result in inconsistent ISO values (as observed on the ISO property) if [setExposureModeCustomWithDuration:ISO:completionHandler:](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624646-setexposuremodecustom) is called repeatedly.

### CloudKit

### Note

A single [CKAsset](https://developer.apple.com/documentation/cloudkit/ckasset) instance can no longer be set as a value on multiple CKRecords.

### Contacts

### Note

The Address Book UI people picker has been changed for iOS 8. A new mode with new API has been added where the app does not need access to the user’s contacts and the user will not be prompted for access. A temporary copy of the selected person is returned to the app. See `ABPeoplePickerNavigationController.h` for more details.

See the new _PeoplePicker: Picking a Person or Property_ sample project demonstrating usage of the new mode.

### Document Providers

### Notes

- Your app needs the iCloud entitlement to be able to be used as a document provider.
- The com.apple.developer.icloud-container-identifiers entitlement is required.

### Known Issues

- After rotating document picker to landscape, the status bar is hidden.
- Upon bringing up document picker in landscape, the containing view may be shifted beneath the navigation bar.

### Extensions

### Notes

- Extensions need an arm64 slice to run on 64-bit devices. If you try to run the armv7 slice on a 64-bit device it won’t work.
- Apps need to have an arm64 slice if the bundle contains a framework that both the app and the app extension link against.

### File System

### Note

The file system layout of app containers has changed on disk. Rather than relying on hard-coded directory structure, use the [NSSearchPathForDirectoriesInDomains](https://developer.apple.com/documentation/foundation/1414224-nssearchpathfordirectoriesindoma) function or the [URLForDirectory:inDomain:appropriateForURL:create:error:](https://developer.apple.com/documentation/foundation/filemanager/1407693-url) method of the [NSFileManager](https://developer.apple.com/documentation/foundation/filemanager) class. See [Accessing Files and Directories](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/AccessingFilesandDirectories/AccessingFilesandDirectories.html#//apple_ref/doc/uid/TP40010672-CH3) in _[File System Programming Guide](../../documentation/File%20Management/File%20System%20Programming%20Guide/About%20Files%20and%20Directories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzs)_.

### Fonts

### Note

The Thai system font has increased in size to improve readability. This will cause clipping in many places in your UI if you don’t take appropriate action:

1. Use [UILabel](https://developer.apple.com/documentation/uikit/uilabel) as much as possible. If you use Interface Builder, make sure that Clip Subviews is not checked. UIKit will grow the clipping region as necessary to not clip text.
2. Use Dynamic Type. This will ensure that you do not have overlapping glyphs in multiline labels or text fields.

If you can’t do 1 and 2 because you implement your own views, you must implement measures not to clip. You can use CoreText to figure out the appropriate clipping region for a line of text by calling:

```
CTLineGetBoundsWithOptions(lineRef, kCTLineBoundsIncludeLanguageExtents);
```

To avoid overlapping glyphs in multiline text elements, adjust the line height. An additional 30% is recommended.

This measure will also help your app perform better in other languages, including Arabic, Hindi, and Vietnamese.

### HealthKit

### Note

Code that attempts to read workout information in HealthKit may be unable to make subsequent queries to HealthKit.

If you are using HKWorkouts you should avoid reading workouts when running on iOS versions prior to 8.1 with:

```
NSOperatingSystemVersion ios8_1_0 = (NSOperatingSystemVersion){8, 1, 0};
if ([[NSProcessInfo processInfo] isOperatingSystemAtLeastVersion:ios8_1_0]) {
// Read and write workout information to HealthKit.
} else {
// Write workout information to HealthKit
}
```


### Known Issue

Blood glucose data is currently not displayed in the Health app. 3rd party access and APIs are not affected. Access controls for Blood Glucose and all other Health data can still be managed in the Health app and in Settings > Privacy > Health.

For more information, see [https://support.apple.com/kb/HT6533](https://support.apple.com/kb/HT6533).

### iCloud

### Note

Mail handoff and AirDrop may stop working after changing your iCloud password at appleid.apple.com.

__Workaround:__ Sign out and back into iCloud on the device.

### iCloud Drive

### Note

[URLForUbiquityContainerIdentifier:](https://developer.apple.com/documentation/foundation/nsfilemanager/1411653-urlforubiquitycontaineridentifie) might return `nil` when running your application in Xcode. If so, open System Preferences, navigate to iCloud > iCloud Drive, and enable Xcode.

### Keyboards

### Known Issue

Additional Keyboards, including 3rd party keyboards, may not appear in Safari, Maps or 3rd party apps on the Simulator.

__Workaround:__  Keyboards should be testable in Calendar, Spotlight, Contacts, and Photos.

### Notification Center

### Note

The schedule and intended use of [widgetPerformUpdateWithCompletionHandler:](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding/1490262-widgetperformupdatewithcompletio) is intended as a convenient home for all data/model update logic. If implemented, the system will call at opportune times for the widget to update its state, both when Notification Center is visible, as well as in the background. An implementation is required to enable background updates. It’s expected that the widget will perform the work to update asynchronously and off the main thread as much as possible. Widgets should call the argument block when the work is complete, passing the appropriate `NCUpdateResult`. Widgets should NOT block returning from [viewWillAppear:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621510-viewwillappear) on the results of this operation. Instead, widgets should load cached state in [viewWillAppear:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621510-viewwillappear) in order to match the state of the view from the last [viewWillDisappear:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621485-viewwilldisappear), then transition smoothly to the new data when it arrives.

### NSURLSession

### Note

The [NSURLSessionTask](https://developer.apple.com/documentation/foundation/nsurlsessiontask) class provides a new “priority” property with three associated constants: `NSURLSessionTaskPriorityDefault`, `NSURLSessionTaskPriorityLow`, and `NSURLSessionTaskPriorityHigh`. `NSURLSessionTask` priorities can be used to specify how multiple requests and responses to the same host should be prioritized. Note that the priority is a hint and not a strict guarantee of `NSURLSessionTask` performance.

For complete usage details of `NSURLSessionTask` priorities, refer to the `NSURLSession.h` header file, which is provided by the Foundation framework.

### Phone

### Notes

To activate Wi-Fi Calling functionality for T-Mobile (U.S. only), follow these steps:

- Go to Settings > Phone > Wi-Fi Calling.
- Toggle the Wi-Fi Calling switch to ON.
- If the carrier does not have the user’s registered emergency address, you will be asked to add it before the feature is activated.

### Photos

### Notes

- Maintain a backup of your photo library before enabling and while using iCloud Photo Library beta by:

  - Importing to your Mac using iPhoto
  - Importing to your Mac using Image Capture
- iCloud Photo Library beta will not download photos and videos that were synced to your device from iTunes. Any photos and videos synced to your device from iTunes will be removed when you enable iCloud Photo Library beta.
- iPhoto for iOS will not launch on iOS 8 Beta. Launching Photos.app will migrate your iPhoto edits to the iOS 8 Photo Library. Make sure your iPhoto for iOS data is included in your device backup.
- The ability to automatically optimize device space is enabled for all accounts larger than 5GB.
- When using iCloud Family Sharing, both iCloud Photo Sharing and My Photo Stream are enabled.

### Provisioning Profiles

### Known Issue

If you have upgraded to the 8.1.1 Beta from iOS 8 Betas you may see your apps crashing due to provisioning profile issues.

__Workaround:__

1. Connect the device via USB to your Mac
2. Launch Xcode
3. Choose Window -> Devices
4. Right click on the device in left column, choose "Show Provisioning Profiles"
5. Click on the provisioning profile in question
6. Press the "-" button
7. Continue to removing all affected profiles.
8. Re-install the app

### UIKit

### Notes

- [UILabel](https://developer.apple.com/documentation/uikit/uilabel) has a default value of YES for [clipsToBounds](https://developer.apple.com/documentation/uikit/uiview/1622415-clipstobounds). This differs from the normal [UIView](https://developer.apple.com/documentation/uikit/uiview) default of NO.
- The `leftLayoutGuide` and `rightLayoutGuide` APIs have been removed. Please use the [layoutMargins](https://developer.apple.com/documentation/uikit/uiview/1622566-layoutmargins) property instead.

### WebKit

### Notes

The Navigation Timing API has been disabled only on iOS due to performance issues.

### Wi-Fi Calling (T-Mobile US only)

### Note

The carrier name in the status bar will show “T-Mobile Wi-Fi” when the device is able to make and receive Wi-Fi calls.
