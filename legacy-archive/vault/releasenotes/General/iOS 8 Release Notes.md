---
title: iOS 8 Release Notes
apple_id: TP40014223
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-09-30'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-iOSSDK-8.0/index.html
archived_at: '2026-07-18T02:54:42.166675Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# iOS SDK Release Notes for iOS 8.0 GM

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrtfvbuqmjnknlte)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrtfvbuqmjnknltg)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrtfvbuqmjnknlti)

### Introduction

iOS SDK 8.0 provides support for developing iOS apps. It is packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for iOS and OS X. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

With this software you can develop apps for iPhone, iPad, or iPod touch running iOS 8. You can also test your apps using the included iOS Simulator, which supports iOS 8. iOS SDK 8.0 requires a Mac computer running OS X v10.9.3 (Mavericks) or later.

This version of iOS is intended for installation only on devices registered with the Apple Developer Program. Attempting to install this version of iOS in an unauthorized manner could put your device in an unusable state.

For more information and additional support resources, visit [http://developer.apple.com/programs/ios/](https://developer.apple.com/programs/ios/).

### Bug Reporting

For issues not mentioned in the [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrtfvbuqmjnknlti) section, please file bugs through the Apple Developer website ([https://developer.apple.com/bug-reporting/ios/](https://developer.apple.com/bugreporter/)). Additionally, you may discuss these issues and iOS SDK 8.0 in the Apple Developer Forums: [http://devforums.apple.com](http://devforums.apple.com/). To get more information about iCloud for Developers, go to [http://developer.apple.com/icloud](https://developer.apple.com/icloud).

### Notes and Known Issues

The following issues relate to using iOS SDK 8.0 to develop code.

### AVCapture

### Known Issue

Use of the new constant, [AVCaptureISOCurrent](https://developer.apple.com/documentation/avfoundation/avcaptureisocurrent), will result in inconsistent ISO values (as observed on the ISO property) if [setExposureModeCustomWithDuration:ISO:completionHandler:](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624646-setexposuremodecustom) is called repeatedly.

### Backup and Restore

### Fixed in GM Seed

- Encrypted backups to iTunes fail.
- iOS 7 iCloud backups restored to an iOS 8 beta device may not properly restore photos.

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
- The com.apple.developer.icloud-container-identifiers entitlement will be required when iOS 8 is released.

### Fixed in GM Seed

On iPhone, bringing up DocMenu from Locations in DocPicker, overlaps with status bar.

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

### Find My Friends

### Note

Now that the Share My Location feature is integrated into Messages, Find My Friends only supports the Apple ID configured in Settings > iCloud.

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

### GameController

### Known Issue

GameController forwarding may not work.

__Workaround:__

- Verify that you are on the same Wi-Fi network on both devices, Handoff is enabled, and the same iCloud account is being used.
- Make sure no other instances of the game are running (e.g. only the target device has the game you are trying to connect).
- Reboot.

### HealthKit

### Known Issues

- Background delivery of HealthKit data does not work as expected in this build.
- Code that attempts to read workout information from HealthKit in iOS 8.0 may be unable to make subsequent queries to HealthKit.

  __Workaround:__ If you are using `HKWorkouts` and `HKWorkoutEvents`, you can avoid this by using the following pattern:

```
NSOperatingSystemVersion ios8_0_1 = (NSOperatingSystemVersion){8, 0, 1};
if ([[NSProcessInfo processInfo] isOperatingSystemAtLeastVersion:ios8_0_1]) {
// Read and write workout information to health kit.
} else {
// Write workout information to health kit
}
```


### HomeKit

### Notes

- After upgrading to the GM Seed, you should reset your home configuration in Settings > Privacy > HomeKit > Reset Home Configuration.
- You must sign into iCloud and enable Keychain sync to use HomeKit with this seed.

### Fixed in GM Seed

Siri may not immediately recognize HomeKit data changes.

### iCloud

### Note

Mail handoff and AirDrop may stop working after changing your iCloud password at appleid.apple.com.

__Workaround:__ Sign out and back into iCloud on the device.

### iCloud Drive

### Note

[URLForUbiquityContainerIdentifier:](https://developer.apple.com/documentation/foundation/nsfilemanager/1411653-urlforubiquitycontaineridentifie) might return nil when running your application in Xcode. If so, open System Preferences, navigate to iCloud > iCloud Drive, and enable Xcode.

### iCloud Keychain

### Known Issues

- When logging into iCloud, a user may experience a keychain reset on their other devices that were previously in the circle.
- Touch ID protected keychain items do not allow [SecItemUpdate](https://developer.apple.com/documentation/security/1393617-secitemupdate). SecItemUpdate always returns [errSecInteractionNotAllowed](https://developer.apple.com/documentation/security/errsecinteractionnotallowed).

  __Workaround:__ Instead of updating, the items have to be deleted and added again.

### iTunes Sync

### Fixed in GM Seed

Apps do not sync from a device to iTunes.

### Keyboards

### Known Issues

- Network access gets disabled after adding a new keyboard from the same bundle.
- Custom Keyboards may go blank after app switching.

  __Workaround:__ Dismiss the keyboard and bring it up again; this should reload the view.

### Mail

### Known Issue

Applying the Allow Account Modification restriction to a device with no mail accounts configured will still allow a user to create a Mail account by launching the Mail app.

### Maps

### Fixed in GM Seed

When viewed in the Simulator, the "Hybrid" view in Maps and MapKit apps does not show all of the tiles.

### Metal

### Known Issue

When you modify a metal file shader using offline compilation to create a metallib library that has shrunk in size, the metallib library will fail to load on the device.

__Workaround:__ Delete the metallib library before recreating it by doing a clean in Xcode or removing the file manually before building the archive.

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

- If you installed Beta 5 on the device, you should erase the device after installing the GM Seed. (Settings > General > Reset > Erase All Content and Settings).
- iCloud Photo Library requires the GM Seed.
- Maintain a backup of your photo library before enabling and while using iCloud Photo Library beta by:

  - Importing to your Mac using iPhoto
  - Importing to your Mac using Image Capture
- iCloud Photo Library beta will not download photos and videos that were synced to your device from iTunes.
- iPhoto for iOS will not launch on iOS 8 Beta. Launching Photos.app will migrate your iPhoto edits to the iOS 8 Photo Library. Make sure your iPhoto for iOS data is included in your device backup.

### Known Issues

- The ability to automatically optimize device space is enabled for all accounts larger than 5GB.
- When using iCloud Family Sharing, both iCloud Photo Sharing and My Photo Stream are enabled.
- If you exceed your iCloud storage quota, your Photos library will no longer update iCloud. Photos and videos can be downloaded or deleted from iCloud.com.

### Provisioning Profiles

### Known Issue

If you have upgraded to the GM seed from other betas you may see your apps crashing due to provisioning profile issues.

__Workaround:__

1. Connect the device via USB to your Mac
2. Launch Xcode
3. Choose Window -> Devices
4. Right click on the device in left column, choose "Show Provisioning Profiles"
5. Click on the provisioning profile in question
6. Press the "-" button
7. Continue to removing all affected profiles.
8. Re-install the app

### Quicklook

### Fixed in GM Seed

PDF files may not display in some applications.

### Safari

### Notes

- Safari now blocks ads from automatically redirecting to the App Store without user interaction. If you still see the previous behavior, or find legitimate redirection to the App Store to be broken in some way, please file a bug.
- You can now quickly add a site to Shared Links or save a bookmark by tapping and holding the bookmarks button.

### Settings

### Fixed in GM Seed

Some icons are missing in Settings and only appear after the row is tapped.

### Setup

### Fixed in GM Seed

Updating the iCloud settings screen may appear to hang during setup.

### Siri

### Known Issue

Shazam with Siri and Purchase iTunes Content with Siri are not functional in the GM seed. They will be available once iOS 8 is released to the general public.

### Speech Synthesis

### Known Issue

[AVSpeechSynthesizer](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer) may not work.

__Workaround:__ If you don’t hear speech in a particular language or dialect, go Settings > General > Accessibility > Speech >Voices >_Language_ and download the Enhanced Quality voice for that language/dialect.

### Stores

### Known Issue

Sometimes, loading certain pages or performing a search on the App Store or iTunes Store can be slow.

### UIKit

### Notes

- [UILabel](https://developer.apple.com/documentation/uikit/uilabel) has a default value of YES for [clipsToBounds](https://developer.apple.com/documentation/uikit/uiview/1622415-clipstobounds). This differs from the normal [UIView](https://developer.apple.com/documentation/uikit/uiview) default of NO.
- The `leftLayoutGuide` and `rightLayoutGuide` APIs have been removed. Please use the [layoutMargins](https://developer.apple.com/documentation/uikit/uiview/1622566-layoutmargins) property instead.

### Fixed in GM Seed

To use an action sheet-style [UIAlertController](https://developer.apple.com/documentation/uikit/uialertcontroller) on iPad, the sourceView of the alert controller's popoverPresentationController must be set.

### Known Issue

RTF file support in [UIWebView](https://developer.apple.com/documentation/uikit/uiwebview) is broken.

__Workaround:__ Show RTF files to the user is to use the Quick Look framework (QLPreviewController) or to load an NSAttributedString from the RTF file and show it in an UITextView, which will render the content in a much cleaner way.

### Wi-Fi Calling (T-Mobile US only)

### Note

The carrier name in the status bar will show “T-Mobile Wi-Fi” when the device is able to make and receive Wi-Fi calls.

### WebKit

### Notes

- Subpixel rendering is now on by default for all web content. Websites or in-app web views with extremely tight design constraints may render differently. Solutions for each issue will vary, but use Web Inspector to adjust position, border thickness, and width or height of elements.
- The `minimal-ui` viewport property is no longer supported in iOS 8.

### Known Issues

- The `window.outerWidth` and `window.outerHeight` DOM properties always return 0. Other DOM properties will need to be used instead. This may affect websites that use leaf.js.
- Third party apps that use [WKWebView](https://developer.apple.com/documentation/webkit/wkwebview) will not be able to participate in Kerberos Single Sign On reliably. To work around this issue, use [UIWebView](https://developer.apple.com/documentation/uikit/uiwebview) instead.
