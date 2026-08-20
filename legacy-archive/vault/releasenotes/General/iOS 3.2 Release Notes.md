---
title: iOS 3.2 Release Notes
apple_id: TP40009477
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2010-09-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-iPhoneSDK-3_2/index.html
archived_at: '2026-07-18T02:54:42.695265Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# iOS SDK Release Notes for iOS 3.2

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tinzxfvbuqmjnknltcmy)
- [New in iOS SDK 3.2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tinzxfvbuqmjnknltcnq)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tinzxfvbuqmjnknltg)
- [Known Issues and Fixes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tinzxfvbuqmjnknlte)

### Introduction

iOS SDK 3.2 provides support for developing iPad applications and includes the complete set of Xcode 3.2.2 tools, compilers, and frameworks for creating applications for iOS and Mac OS X. These tools include the Xcode IDE and the Instruments analysis tool among many others.

With this software you can develop applications that run on iPad using the included iOS Simulator, which runs iOS 3.2. Additionally, you can develop applications for iPhone and iPod touch, which run on iOS 3.1.3. (This software does not include any of the 2.x versions of the iOS SDK.) Installing iOS SDK 3.2 requires a Macintosh computer running Mac OS X 10.6.2 (Snow Leopard) or later.

We encourage developers to apply to the iOS Developer Program for access to additional support resources, including provisioning resources to enable development directly on an iPad, iPhone, or iPod touch. For more information visit:

[http://developer.apple.com/devcenter/ios/program/](https://developer.apple.com/devcenter/ios/program/)

### New in iOS SDK 3.2

- Xcode 3.2.2 adds support for developing iPad and Universal iPad/iPhone apps.

  - Xcode simplifies the process of sharing code between your iPhone and iPad applications by helping you update your existing iPhone projects to include the necessary files to support the new device. The Upgrade Current Target for iPad… command (in the Project menu) allows you to choose one of the following options:

    - Upgrade your existing iPhone target to a Universal application that supports both iPhone and iPad.
    - Create a separate iPad application target based on your existing iPhone target.

    It also creates copies of some of your project’s xib files and updates them to support iPad's larger screen size.
  - After using the Upgrade Current Target for iPad… command, you can adjust your project’s build settings further if needed:

    - A Universal application that runs on both iPad and iPhone needs to have the following Build Settings:

      - The Base SDK build setting (in the Architectures section) must be set to “iOS SDK 3.2”.
      - The iOS Deployment Target build setting must be set to iOS 3.1.3 or earlier.
    - For iPad-only development, set the Base SDK to iOS SDK 3.2 and set the iOS Deployment Target to iOS 3.2.
    - For iPhone-only development, set the Base SDK to iOS SDK 3.1.3 or earlier and set the iOS Deployment Target to iOS 3.1.3 or earlier.
    - Set the Targeted Device Family build option to iPad, iPhone, or iPhone/iPad as appropriate for your application.
  - The iOS Simulator 3.2 always runs applications with the assumption that they are running on an iPad. Therefore running a universal application in iOS Simulator 3.2 will always run it as an iPad application, and thereby run the iPad code paths. If you want to run a universal application as an iPhone application, and thereby test the iPhone code paths, you must do so on an iPhone or iPod touch device.
- Developers are encouraged to use Xcode's new Build > Build and Archive command to create an archive of their application and its associated [.dSYM] file. This archive can then be used with the Validate Application…, Share Application…, and Submit Application to iTunes Connect… sharing options in the new Archived Application source in the Organizer. The Validate Application… and Submit Application to iTunes Connect… sharing options require an iTunes Connect account and metadata prepared for that application; Validate Application… will run all of the validation tests that will be run upon submission to the App Store so that you can fix any problems before submitting your app. Submit Application to iTunes Connect… runs the same validation tests as Validate Application… and then, if all the tests pass, uploads your application for App Store review.
- You can now easily transfer your iPhone developer identity to a new computer. The new Developer Profile source in the Organizer allows you to export your provisioning profiles and identities (code signing certificates) as a secure single file. To begin developing on a new computer, import that file into Xcode using the Organizer or by double-clicking it in Finder.
- Interface Builder supports the new view controllers and window sizes available for the iPad platform.

For the latest security information visit: [http://support.apple.com/kb/HT1222](http://support.apple.com/kb/HT1222). For more detailed information about new tools features, see the complete Xcode 3.2.2 release notes.

### Bug Reporting

Please report any bugs not mentioned in the "Known Issues" section using the Apple Bug Reporter on the Developer Connection website at: [http://developer.apple.com/bugreporter/](https://developer.apple.com/bugreporter/).

### Known Issues and Fixes

### Xcode/Developer Tools

- You cannot use the simulator to test an iPhone app on the 3.2 OS.
- You may only use `.png` files for application icons for the device.
- When running and debugging on a device, be sure to turn off Passcode lock.
- Trying to debug two applications at the same time on the same device fails with a broken pipe error in the debugger console.
- After upgrading an existing iPhone target to a Universal application target using the Project > Upgrade Current Target for iPad… command, you should verify that the upgraded target’s iOS Deployment Target setting is set to iOS 3.1.3 or earlier.

### Core Graphics

- [CGFontCreateWithFontName](https://developer.apple.com/documentation/coregraphics/1396330-cgfontcreatewithfontname) can hang in some circumstances when using the `UIAppFonts` key in the `Info.plist`.

### Interface Builder

- To support external localization tools and workflows, Interface Builder 3.2.2 supports an option to save iPhone documents in an editable nib format. Additionally, the Xcode build settings "Flatten Compiled XIB Files" and "Strip NIB Files" now apply to iPhone Interface Builder documents in the same way they apply to Mac OS X documents. By default, nib files will be stripped when built.
- iOS 3.2 supports loading unstripped nib files, but iOS releases prior to 3.2 do not. If you choose to build unstripped nib files to support a localization workflow, you should either use ibtool's --strip command to strip nib files after localizing, or temporarily revert the "Flatten Compiled XIB Files" and "Strip NIB Files" build settings to build nib files compatible with previous iOS releases.
- Building an iPhone application that uses [UITableViewCell](https://developer.apple.com/documentation/uikit/uitableviewcell) objects encoded in XIB files and then running that application in the simulator or on a device with a version less than 3.2 will result in a runtime exception. To workaround this, use the simulator with iOS SDK 3.2.

### MapKit

- Previously, directions URLs were handed as a single point-to-point request. In iOS 3.2, it is handled as 2 sets of search queries and results, which can be run concurrently. The Maps UI for spellchecking, refinements and map pan/zoom now support concurrent searches.

### MediaPlayer

- The [MPMoviePlayerPlaybackDidFinishNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1620936-mpmovieplayerplaybackdidfinish) notification is not sent from the Done button when a movie is launched non-fullscreen and switched to fullscreen. Playback is not ended when you tap the Done button -- the video is still ready to play, just paused. Refer to [MPMoviePlayerWillExitFullscreenNotification](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerwillexitfullscreennotification)/[MPMoviePlayerDidExitFullscreenNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1620945-mpmovieplayerdidexitfullscreen) instead.
- You can incorporate several movie views into your application, but only one of those views can be playing its movie at any given time.

### MessageUI

- The Message UI framework exports class names without prefixes, which can cause namespace confusion. If you are using the Message UI framework, watch for compiler warnings about duplicate symbols. To avoid namespace issues, you can add prefixes to your own class names.

### Simulator

- Launching the Photos application under the iPad Simulator will initially show three tabs: Photos, Albums, and Camera. The Camera tab represents photos available via the Camera Connection Kit for iPad, and is not relevant for the Simulator. The Camera tab will disappear after a few seconds.

### Springboard

- _FIXED:_ Springboard is now using a new `Info.plist` key that defines the `Default.png` image name: `UILaunchImageFile`.

### Status Bar

- Making the status bar transparent is not supported on the iPad.

### UIKit

- The Text Input System never calls the methods found in the documentation under the "Geometry and Hit-Testing Methods" category.
- The Text Input System never calls the methods found in the documentation under the "Determining Layout and Writing Direction" category.

### UIPopoverController

- The [MPMediaPickerController](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontroller) and [UIImagePickerController](https://developer.apple.com/documentation/uikit/uiimagepickercontroller) classes are not supported from the [presentModalViewController:animated:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621465-presentmodalviewcontroller) method of `UIViewController`. These pickers should instead be displayed using a `UIPopoverController` object.
- Popovers are now required to have an arrow.
- _NEW:_ Popovers ignore the value in the [contentSizeForViewInPopover](https://developer.apple.com/documentation/uikit/uiviewcontroller/1619323-contentsizeforviewinpopover) property when initialized in the [viewWillAppear:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621510-viewwillappear) method.

### UITableView

- The [UITableViewCellStyleValue1](https://developer.apple.com/documentation/uikit/uitableviewcellstyle/uitableviewcellstylevalue1) style now also supports images.
- The [UITableViewRowAnimationMiddle](https://developer.apple.com/documentation/uikit/uitableviewrowanimation/uitableviewrowanimationmiddle) style now provides animation for row deletion.

### UIWebView

- The user agent string has been updated for the iPad.
