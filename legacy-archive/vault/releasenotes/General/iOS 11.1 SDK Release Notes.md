---
title: iOS 11.1 SDK Release Notes
apple_id: TP40017683
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2017-10-30'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-iOS-11.1/index.html
archived_at: '2026-07-18T02:54:41.170766Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# iOS 11.1 SDK Release Notes

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmobtfvbuqmjnknltg)
- [Tools and Developer Resources](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmobtfvbuqmjnknlti)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmobtfvbuqmjnknltk)
- [Release Notes Updates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmobtfvbuqmjnknltenzy)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmobtfvbuqmjnknltc)

### Introduction

iOS 11.1 SDK provides support for developing iOS apps. It’s packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for iOS, watchOS, tvOS, and macOS. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

With this software you can develop apps for iPhone, iPad, or iPod touch running iOS 11.1. You can also test your apps using the included Simulator, which supports iOS 11.1. iOS 11.1 SDK requires a Mac computer running macOS Sierra 10.12.6 or later.

This version of iOS is intended for installation only on devices registered with the Apple Developer Program. Attempting to install this version of iOS in an unauthorized manner could put your device in an unusable state.

### Tools and Developer Resources

You obtain Xcode 9.1 from the Mac App Store. It is a free download that installs directly into the Applications folder.

The Apple Developer Program provides everything you need to build and distribute your apps on the App Store for iPhone, iPad, Mac, and Apple Watch. Membership includes access to beta OS releases, advanced app capabilities, and tools to develop, test, and distribute apps and Safari extensions. For more information, visit [Apple Developer Program](https://developer.apple.com/programs/).

Apple provides the following resources to support your development:

- Developer documentation is available both on the [Apple Developer website](https://developer.apple.com/documentation) and from Xcode by choosing Help > Developer Documentation.
- [Apple Developer Forums](https://forums.developer.apple.com/). Participate in discussions about developing for Apple platforms and using developer tools.
- [Bug Reporter](http://bugreport.apple.com/). Report issues, enhancement requests, and feedback to Apple. Provide detailed information, including the system and developer tools version information, and any relevant crash logs or console messages.
- [Apple Developer website](https://developer.apple.com/). Get the latest development information.
- [iOS homepage](https://developer.apple.com/ios/). Get high-level information about the latest release of iOS. Download current and beta iOS releases.
- For help with using Xcode, Simulator, or Instruments, choose Help > _app name_ Help.

### Bug Reporting

For issues not mentioned in [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmobtfvbuqmjnknltc), please file bugs through the Apple Developer website [https://developer.apple.com/bug-reporting/](https://developer.apple.com/bug-reporting/).

When filing a bug, please include the full version number in the bug title and in the description. To find the version number, open Settings > General > About. The version number is shown next to Version and looks like _11.1 (15Bxxx)_.

Additionally, you may discuss these issues and iOS 11 SDK in the Apple Developer Forums: [https://forums.developer.apple.com/welcome](https://forums.developer.apple.com/welcome). To get more information about iCloud for Developers, go to [https://developer.apple.com/icloud](https://developer.apple.com/icloud).

### Release Notes Updates

_iOS Release Notes_ is sometimes updated after a release is distributed. You can check for the most up-to-date version of _iOS Release Notes_ at the Apple Developer website by checking [http://developer.apple.com/go/?id=ios-sdk-release-notes](https://developer.apple.com/go/?id=ios-sdk-release-notes).

_Revision: iOS1110 - IRN1_

### Notes and Known Issues

The following items relate to using iOS 11 SDK to develop code.

### ARKit

### Known Issues

- Continuing from a breakpoint while debugging an [ARSession](https://developer.apple.com/documentation/arkit/arsession) may result in VIO breaking. Any visual objects placed in the world/anchor are not visible. (31561202)

### AVFoundation

### Known Issues

- When using the TrueDepth front-facing camera on iPhone X, setting the capture device’s [activeFormat](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1389221-activeformat) to a binned video format (see [isVideoBinned](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/1624597-isvideobinned)) for capture and enabling delivery of camera calibration data causes the resulting [AVCameraCalibrationData](https://developer.apple.com/documentation/avfoundation/avcameracalibrationdata) to contain invalid information for the [intrinsicMatrix](https://developer.apple.com/documentation/avfoundation/avcameracalibrationdata/2881135-intrinsicmatrix) property. (34200225)

  _Workaround_: Select an alternate capture format whose `isVideoBinned` property is `false`.

  > [!NOTE]
  > 

### EventKit

### Known Issues

- Initializing an [EKCalendarChooser](https://developer.apple.com/documentation/eventkitui/ekcalendarchooser) from EventKit can result in an app crash. (34608102)
- Storing data to a nondefault event store in EventKit may not work. (31335830)

### Files App (Simulator)

### Known Issues

- In Simulator, documents saved in Local Storage won't load again through the Document Browser. (32509670)

### Foundation

### Known Issues

- Clients of [NSURLSessionStreamTask](https://developer.apple.com/documentation/foundation/nsurlsessionstreamtask) that use a non-secure connection fail to connect when an error occurs during PAC file evaluation and the system is configured for either Web Proxy Auto Discovery (WPAD) or Proxy Automatic Configuration (PAC). A PAC evaluation failure can occur when the PAC file contains invalid JavaScript or the HTTP host serving the PAC file is unreachable. (33609198)

  _Workaround_: Use [startSecureConnection()](https://developer.apple.com/documentation/foundation/urlsessionstreamtask/1411567-startsecureconnection) to establish a secure connection.

### Replay Kit

### Known Issues

- For a broadcast extension that a user starts from within an app, the value for the [RPVideoSampleOrientationKey](https://developer.apple.com/documentation/replaykit/rpvideosampleorientationkey) of the [CMSampleBuffer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer) of type [RPSampleBufferType](https://developer.apple.com/documentation/replaykit/rpsamplebuffertype) is always portrait. Starting the broadcast extension from the Control Center returns the correct value. (34559925)

### Vision

### Known Issues

- [VNFaceLandmarkRegion2D](https://developer.apple.com/documentation/vision/vnfacelandmarkregion2d) is currently unavailable in Swift. (33191123)
- Facial landmarks identified by the Vision framework may flicker in temporal use cases such as video. (32406440)

### Xcode

### Known Issues

- Debugging a disabled Messages extension may cause the Messages app to crash. (33657938)

  _Workaround_: Enable the extension before starting the debug session.
- After a simulated iOS device starts up, it’s not possible to pull down the Notification center. (33274699)

  _Workaround_: Lock and unlock the simulated device and then reopen Home screen.
