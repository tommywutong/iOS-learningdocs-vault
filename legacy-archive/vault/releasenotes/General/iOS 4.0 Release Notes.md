---
title: iOS 4.0 Release Notes
apple_id: TP40009763
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2010-07-07'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-iPhoneSDK-4_0/index.html
archived_at: '2026-07-18T02:54:42.735270Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# iOS SDK Release Notes for iOS 4

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tonrtfvbuqmjnknltg)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tonrtfvbuqmjnknlti)
- [Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tonrtfvbuqmjnknlte)

### Introduction

iOS SDK 4 provides support for developing iPhone applications and includes the complete set of Xcode tools, compilers, and frameworks for creating applications for iOS and Mac OS X. These tools include the Xcode IDE and the Instruments analysis tool among many others.

With this software you can develop applications that run on iPhone or iPod touch using the included iOS Simulator, which runs iOS 4. Installing iOS SDK 4 requires a Macintosh computer running Mac OS X 10.6.2 (Snow Leopard) or later.

We encourage developers to apply to the iOS Developer Program for access to additional support resources, including provisioning resources to enable development directly on an iPhone or iPod touch. For more information visit:

[http://developer.apple.com/devcenter/ios/program/](https://developer.apple.com/devcenter/ios/program/)

### Bug Reporting

Please report any bugs not mentioned in the "Known Issues" section using the Apple Bug Reporter on the Developer Connection website at: [http://developer.apple.com/bugreporter/](https://developer.apple.com/bugreporter/).

### Known Issues

### AV Foundation

- In this release, the `AVAssetReader` and `AVAssetWriter` classes have been removed from the AV Foundation framework.

### Xcode

- LLVM GCC and LLVM compiler are now included as optional compilers for iPhone development.
- When selecting a target and then choosing "Update Current Target for iPad," new nib files are created but not converted to iPad. To fix this problem:

  - Either select each nib file that was copied, open it in Interface Builder, select the "File -> Create iPad Version" menu option, then select "Save As…" for the document, and save over the nib file.
  - Or invoke this command in the terminal from the project's folder:

    `find Resources-iPad -type f -name "*.xib" -exec ibtool --sdk "" --change-target-runtime IBIPadFramework {} --write {} \;`

### Debugger

- When debugging your multitasking enabled app, avoid manually pausing and continuing from the debugger when the application is suspended in the background. Pausing an application that is suspended in the background disrupts proper multitasking behavior until the application is relaunched.
- Using a datatip on a uninitialized object, or turning it open in the variables view, will sometimes make it look like the program has crashed. The status bar at the bottom of Xcode's windows will show `Program received signal: "EXC_BAD_ACCESS"` and the toolbar buttons for stepping through the code will be disabled. To recover, choose “Sync with Debugger” from the Run menu and continue debugging.

### Interface Builder

- iOS 4 includes a new [UINib](https://developer.apple.com/documentation/uikit/uinib) class to support rapidly unarchiving nib files. While this class is new to iOS SDK 4, it was present but private, in previous releases. Special care needs to be taken when deploying code that uses the `UINib` class and also runs on iOS releases prior to version 4. Specifically, you cannot determine the availability of the class solely using the [NSClassFromString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSClassFromString) function, because that check returns a private class on iOS 3.x and earlier. Instead, after getting the `UINib` class using `NSClassFromString`, you must also use the [respondsToSelector:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intfm/NSObject/respondsToSelector:) method of the returned class to see if it responds to the [nibWithNibName:bundle:](https://developer.apple.com/documentation/uikit/uinib/1614138-nibwithnibname) method. If it responds to that method, you can use the class.

### Core Graphics

- [CGFontCreateWithFontName](https://developer.apple.com/documentation/coregraphics/1396330-cgfontcreatewithfontname) can hang in some circumstances when using the `UIAppFonts` key in the `Info.plist`.

### GameKit

- The `desiredPlayers` property has been removed from the [GKMatchRequest](https://developer.apple.com/documentation/gamekit/gkmatchrequest) class
- `GameKitBeta.h` has been renamed to `GameKitPreview.h`. This will break existing projects that link against `GameKitBeta.h`. Please recompile as needed.

### Mail

- Mail now supports the following RFC extensions:

  - COMPRESS (4978)
  - ESEARCH (4731)
  - CHUNKING (3030)
  - 8BITMIME (1652)
  - ENHANCEDSTATUSCODES (3463)
  - BINARYMIME (3030)
  - CONDSTORE (4551)

### MediaPlayer

- The [MPMoviePlayerController](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller) class changed behavior in iOS 3.2. The behavior of this class is as follows:

  - In iOS SDK 3.1.x and earlier, the movie player always plays full screen.
  - In iOS SDK 3.2 and later, you must embed the movie player’s view into your application’s interface. (This behavior applies to iPhone, iPad, and Universal applications.)

  If you link a Universal application against iOS SDK 3.2, you must be prepared to embed the movie player view in your interface when running on iOS 4 and later. In this specific case, the value of the `userInterfaceIdiom` property is not a reliable way to determine the behavior of the media player controller. Instead, you should test for the existence of the `view` property of the `MPMoviePlayerController` class to determine if you need to insert the view into your view hierarchy. For more information on how to perform these checks, see _[SDK Compatibility Guide](../../documentation/Developer%20Tools/SDK%20Compatibility%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3dg2i)_.
- In iOS 3.2 and later, the `MPMoviePlayerController` class now defaults to share the application's audio session for audio playback and related audio behaviors. This allows the movie player's audio to mix with the rest of the application's audio, as well as to conform to the behaviors of the application audio session's audio category (such as mixing with other applications' audio and/or obeying the Silent Switch). In iOS 3.1.3 and earlier, this class always uses a system-supplied audio session. To obtain that same behavior in iOS 3.2 and later, you must set the [useApplicationAudioSession](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620897-useapplicationaudiosession) property of the movie player controller object to `NO`. Please refer to the _[Audio Session Programming Guide](../../documentation/Audio/Audio%20Session%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzv)_, including the Working with Movies and iPod Music section, and the _[MPMoviePlayerController Class Reference](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller)_ for more about audio sessions and their behaviors with `MPMoviePlayerController`.

### Multitasking

- In this and future releases, there are changes to networking behavior for suspended apps:

  - Cancel any Bonjour-related services before being suspended.] When your application moves to the background, and before it is suspended, it should unregister from Bonjour and close listening sockets associated with any network services. A suspended application cannot respond to incoming service requests anyway. Closing out those services prevents them from appearing to be available when they actually are not. If you do not close out Bonjour services yourself, the system closes out those services automatically when your application is suspended.
  - Be prepared to handle connection failures in your network-based sockets.] The system may tear down socket connections while your application is suspended for any number of reasons. As long as your socket-based code is prepared for other types of network failures, such as a lost signal or network transition, this should not lead to any unusual problems. When your application resumes, if it encounters a failure upon using a socket, simply reestablish the connection.
- The time limit for task completion changed from 5 minutes to 10 minutes.
- In order to preserve the user's context when switching between apps, applications linked on or after iOS 4 will no longer automatically cancel alerts and action sheets when the application is sent to the background.

### Simulator

- iOS Simulator can now simulate multiple iOS versions from a single build. Currently the simulator supports iOS 3.2 and iOS 4.0, allowing simulation of a single Universal binary on both iPad and iOS Simulators.
- With the base SDK set to 3.2 but running in the 4.0 simulator, an application calling [stat](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/stat.2.html#//apple_ref/doc/man/2/stat) writes beyond the end of `stat bufferstat()` and can cause unexpected behavior or a crash.
- The Camera application shows up on the iOS 4 simulator (but not on the normal simulator). This causes the [UIImagePickerController](https://developer.apple.com/documentation/uikit/uiimagepickercontroller) object to hang an application when launched in the iOS 4 simulator. The cancel button is disabled and the only way out of an application once the image picker is shown (with the camera for the source type) is to kill the application manually.

### UIKit

- `UIInvalidBackgroundTask` has been renamed to [UIBackgroundTaskInvalid](https://developer.apple.com/documentation/uikit/uibackgroundtaskinvalid)
- On iOS 4.0, applications that add a text field to a [UIAlertView](https://developer.apple.com/documentation/uikit/uialertview) will need to stop moving the `UIAlertView` by hand to avoid layout issues.
- Setting animatable properties inside transition animation block may not work.
- Tile backgrounds created with the [colorWithPatternImage:](https://developer.apple.com/documentation/uikit/uicolor/1621935-colorwithpatternimage) method of `UIColor` appear with the image upside down. This is correct behavior, as the pattern and normal coordinate spaces now match.
- The default behavior for the new `UIView` block-based animation API in 4.0 is to disable user interactions across the whole interface while the animation is playing. Developers should not rely on this behavior remaining the default as it may be reversed in future releases, thereby allowing user interactions to occur by default while the animation is playing. Programs compiled against iOS SDK 4 will continue to work as-is but code compiled under future versions of the SDK may require setting a different option flag to enable the original behavior.
- The default behavior for the new `UIView` block-based animation API in 4.0 is to inherit the animation duration from an enclosing animation block (when present). Developers should not rely on this behavior remaining the default, as it may be reversed in future releases, thereby preventing animations from automatically inheriting the duration of their enclosing animation. Programs compiled against iOS SDK 4 will continue to work as-is but code compiled under future versions of the SDK may require setting a different option flag to enable the original behavior.
- iPhone 4 uses a different system font than earlier devices. References to the Helvetica font in nib files will be decoded as the system font on these newer devices.
- The UIKit Text Input System never calls the methods found in the documentation under the "Determining Layout and Writing Direction" category.
