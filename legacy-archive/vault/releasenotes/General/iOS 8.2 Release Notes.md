---
title: iOS 8.2 Release Notes
apple_id: TP40015020
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-iOSSDK-8.2/index.html
archived_at: '2026-07-18T02:54:42.271187Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# iOS SDK Release Notes for iOS 8.2

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tamrqfvbuqmjnknlte)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tamrqfvbuqmjnknltg)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tamrqfvbuqmjnknlti)

### Introduction

iOS SDK 8.2 provides support for developing iOS apps. The SDK is packaged with a complete set of tools, compilers, and frameworks for creating apps for iOS and OS X. The tools include the Xcode IDE and the Instruments analysis tool, among many others.

With this software, you can develop apps for iPhone, iPad, or iPod touch running iOS 8. It now includes WatchKit, a framework for developing Apple Watch apps. You can test your apps using the included iOS Simulator.

iOS SDK 8.2 requires a Mac computer running OS X v10.9.4 (Mavericks) or later.

This version of iOS is intended for installation only on devices registered with the Apple Developer Program. Attempting to install this version of iOS in an unauthorized manner could put your device in an unusable state.

For more information and additional support resources, visit [http://developer.apple.com/programs/ios/](https://developer.apple.com/programs/ios/).

### Bug Reporting

For issues not mentioned in the [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tamrqfvbuqmjnknlti) section, please file bugs through the Apple Developer website ([https://developer.apple.com/bug-reporting/ios/](https://developer.apple.com/bugreporter/)). Additionally, you may discuss these issues and iOS SDK 8.2 in the Apple Developer Forums: [http://devforums.apple.com](http://devforums.apple.com/). To get more information about iCloud for Developers, go to [http://developer.apple.com/icloud](https://developer.apple.com/icloud).

### Notes and Known Issues

The following issues relate to using iOS SDK 8.2 to develop code.

### App Extensions

### Notes

- App extensions need an arm64 slice to run on 64-bit devices. If you try to run the armv7 slice on a 64-bit device it won’t work.
- Apps need to have an arm64 slice if the bundle contains a framework that both the app and the app extension link against.

### Document Providers

### Notes

- Your app needs the iCloud entitlement to be able to be used as a document provider.
- The `com.apple.developer.icloud-container-identifiers` entitlement is required.

### Healthkit

### Notes

- Blood glucose data is now displayed in the Health app.
- Code that attempts to read workout information in HealthKit may be unable to make subsequent queries to HealthKit.
  If you are using [HKWorkout](https://developer.apple.com/documentation/healthkit/hkworkout), you should avoid reading workouts when running on iOS versions prior to 8.1 with:

```
NSOperatingSystemVersion ios8_1_0 = (NSOperatingSystemVersion){8, 1, 0};
if ([[NSProcessInfo processInfo] isOperatingSystemAtLeastVersion:ios8_1_0]) {
// Read and write workout information to HealthKit.
} else {
// Write workout information to HealthKit
}
```


### iCloud Drive

### Note

[URLForUbiquityContainerIdentifier:](https://developer.apple.com/documentation/foundation/nsfilemanager/1411653-urlforubiquitycontaineridentifie) might return `nil` when running your application in Xcode. If so, open System Preferences, navigate to iCloud > iCloud Drive, and enable Xcode.

### Notification Center

### Note

The schedule and intended use of [widgetPerformUpdateWithCompletionHandler:](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding/1490262-widgetperformupdatewithcompletio) is as a convenient home for all data/model update logic. If implemented, the system will call at opportune times for the widget to update its state, both when Notification Center is visible, as well as in the background. An implementation is required to enable background updates. It’s expected that the widget will perform the work to update asynchronously and off the main thread as much as possible. Widgets should call the argument block when the work is complete, passing the appropriate `NCUpdateResult`. Widgets should NOT block returning from [viewWillAppear:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621510-viewwillappear) on the results of this operation. Instead, widgets should load cached state in [viewWillAppear:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621510-viewwillappear) in order to match the state of the view from the last [viewWillDisappear:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621485-viewwilldisappear), then transition smoothly to the new data when it arrives.

### NSURLSession

### Note

The [NSURLSessionTask](https://developer.apple.com/documentation/foundation/nsurlsessiontask) class provides a new “priority” property with three associated constants: `NSURLSessionTaskPriorityDefault`, `NSURLSessionTaskPriorityLow`, and `NSURLSessionTaskPriorityHigh`. `NSURLSessionTask` priorities can be used to specify how multiple requests and responses to the same host should be prioritized. Note that the priority is a hint and not a strict guarantee of `NSURLSessionTask` performance.

For complete usage details of `NSURLSessionTask` priorities, refer to the `NSURLSession.h` header file, which is provided by the Foundation framework.

### UIKit

### Notes

- [UILabel](https://developer.apple.com/documentation/uikit/uilabel) has a default value of `YES` for [clipsToBounds](https://developer.apple.com/documentation/uikit/uiview/1622415-clipstobounds). This differs from the normal [UIView](https://developer.apple.com/documentation/uikit/uiview) default of `NO`.
- The `leftLayoutGuide` and `rightLayoutGuide` APIs have been removed. Please use the [layoutMargins](https://developer.apple.com/documentation/uikit/uiview/1622566-layoutmargins) property instead.

### WatchKit

### Note

The value for the `WKCompanionAppBundleIdentifier` key in the `Info.plist` of your WatchKit app must match the bundle ID of your iPhone app, or custom notification UI will not work.

### Known Issues

- Creating an animated image using the [UIImage](https://developer.apple.com/documentation/uikit/uiimage) method [animatedImageWithImages:duration:](https://developer.apple.com/documentation/uikit/uiimage/1624149-animatedimagewithimages) and then playing the animation using `startAnimating` ignores the duration and plays back as fast as possible.

  __Workaround:__ Use `startAnimatingWithImagesInRange:duration:repeatCount:` instead.
- When updating existing [WKInterfaceTable](https://developer.apple.com/documentation/watchkit/wkinterfacetable) row controller content and simultaneously inserting or deleting rows, indexes might lose coherence.

  __Workaround:__ Perform all insertions and deletions before making any updates to ensure that the correct modifications are performed.
