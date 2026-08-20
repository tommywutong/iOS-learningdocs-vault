---
title: iOS 11.2 SDK Release Notes
apple_id: TP40017694
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2017-12-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-iOS-11.2/index.html
archived_at: '2026-07-18T02:54:41.214841Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# iOS 11.2 SDK Release Notes

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmojufvbuqmjnknltg)
- [Tools and Developer Resources](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmojufvbuqmjnknlti)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmojufvbuqmjnknltk)
- [Release Notes Updates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmojufvbuqmjnknltenzy)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmojufvbuqmjnknltc)

### Introduction

iOS 11.2 SDK provides support for developing iOS apps. It’s packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for iOS, watchOS, tvOS, and macOS. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

With this software you can develop apps for iPhone, iPad, or iPod touch running iOS 11.2. You can also test your apps using the included Simulator, which supports iOS 11.2. iOS 11.2 SDK requires a Mac computer running macOS Sierra 10.12.6 or later.

### Tools and Developer Resources

You obtain Xcode 9.2 from the Mac App Store. It is a free download that installs directly into the Applications folder.

The Apple Developer Program provides everything you need to build and distribute your apps on the App Store for iPhone, iPad, Mac, and Apple Watch. Membership includes access to beta OS releases, advanced app capabilities, and tools to develop, test, and distribute apps and Safari extensions. For more information, visit [Apple Developer Program](https://developer.apple.com/programs/).

Apple provides the following resources to support your development:

- Developer documentation is available both on the [Apple Developer website](https://developer.apple.com/documentation) and from Xcode by choosing Help > Developer Documentation.
- [Apple Developer Forums](https://forums.developer.apple.com/). Participate in discussions about developing for Apple platforms and using developer tools.
- [Bug Reporter](http://bugreport.apple.com/). Report issues, enhancement requests, and feedback to Apple. Provide detailed information, including the system and developer tools version information, and any relevant crash logs or console messages.
- [Apple Developer website](https://developer.apple.com/). Get the latest development information.
- [iOS homepage](https://developer.apple.com/ios/). Get high-level information about the latest release of iOS. Download current and beta iOS releases.
- For help with using Xcode, Simulator, or Instruments, choose Help > _app name_ Help.

### Bug Reporting

For issues not mentioned in [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmojufvbuqmjnknltc), please file bugs through the Apple Developer website [https://developer.apple.com/bug-reporting/](https://developer.apple.com/bug-reporting/).

When filing a bug, please include the full version number in the bug title and in the description. To find the version number, open Settings > General > About. The version number is shown next to Version and looks like _11.2 (15Cxxx)_.

Additionally, you may discuss these issues and iOS 11 SDK in the Apple Developer Forums: [https://forums.developer.apple.com/welcome](https://forums.developer.apple.com/welcome). To get more information about iCloud for Developers, go to [https://developer.apple.com/icloud](https://developer.apple.com/icloud).

### Release Notes Updates

_iOS Release Notes_ is sometimes updated after a release is distributed. Please check this document for updates.

_Revision: iOS1120 - IRN1_

### Notes and Known Issues

The following items relate to using iOS 11 SDK to develop code.

### ARKit

### Known Issues

- Continuing from a breakpoint while debugging an [ARSession](https://developer.apple.com/documentation/arkit/arsession) may result in VIO breaking. Any visual objects placed in the world/anchor are not visible. (31561202)

### AVFoundation

### Resolved Issues

- [AVCameraCalibrationData](https://developer.apple.com/documentation/avfoundation/avcameracalibrationdata) now contains correct information for the [activeFormat](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1389221-activeformat) property when usihg the TrueDepth camera on the iPhone X. (34200225)

### EventKit

### Resolved Issues

- Initializing an [EKCalendarChooser](https://developer.apple.com/documentation/eventkitui/ekcalendarchooser) from EventKit no longer result in an app crash. (34608102)

### Known Issues

- Storing data to a nondefault event store in EventKit may not work. (31335830)

### Files App (Simulator)

### Known Issues

- In Simulator, documents saved in Local Storage won't load again through the Document Browser. (32509670)

### Foundation

### Known Issues

- Clients of [NSURLSessionStreamTask](https://developer.apple.com/documentation/foundation/nsurlsessionstreamtask) that use a non-secure connection fail to connect when an error occurs during PAC file evaluation and the system is configured for either Web Proxy Auto Discovery (WPAD) or Proxy Automatic Configuration (PAC). A PAC evaluation failure can occur when the PAC file contains invalid JavaScript or the HTTP host serving the PAC file is unreachable. (33609198)

  _Workaround_: Use [startSecureConnection()](https://developer.apple.com/documentation/foundation/urlsessionstreamtask/1411567-startsecureconnection) to establish a secure connection.

### Photos UI API Extensions

### New Features

- In iOS 11.2 or later, the user interface of a photo editing extension is no longer limited to the safe area. Apple recommends following the [Human Interface Guidelines](https://developer.apple.com/ios/human-interface-guidelines/overview/) for content insets. (34189209)

### UIKit

### Resolved Issues

- Displaying a page control in [UIPageViewController](https://developer.apple.com/documentation/uikit/uipageviewcontroller) on iPhone X no longer overlaps the home indicator at the bottom of the screen. (34478195)

### Vision

### Resolved Issues

- Using a model that outputs an image with [VNCoreMLRequest](https://developer.apple.com/documentation/vision/vncoremlrequest) now works correctly. (34023914)
- [VNHomographicImageRegistrationRequest](https://developer.apple.com/documentation/vision/vnhomographicimageregistrationrequest) and [VNDetectBarcodesRequest](https://developer.apple.com/documentation/vision/vndetectbarcodesrequest) now work correctly with images when using a request handler based on a URL. (34919881)
- [VNFaceLandmarkRegion2D](https://developer.apple.com/documentation/vision/vnfacelandmarkregion2d) is now available in Swift. (33191123)

### Known Issues

- Facial landmarks identified by the Vision framework may flicker in temporal use cases such as video. (32406440)

### Xcode

### Known Issues

- Debugging a disabled Messages extension may cause the Messages app to crash. (33657938)

  _Workaround_: Enable the extension before starting the debug session.
- After a simulated iOS device starts up, it’s not possible to pull down the Notification center. (33274699)

  _Workaround_: Lock and unlock the simulated device and then reopen Home screen.
