---
title: iOS 11.3 SDK Release Notes
apple_id: TP40017699
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2018-03-29'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-iOS-11.3/index.html
archived_at: '2026-07-18T02:54:41.284448Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# iOS 11.3 SDK Release Notes

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmojzfvbuqmjnknltg)
- [Tools and Developer Resources](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmojzfvbuqmjnknlti)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmojzfvbuqmjnknltk)
- [Release Notes Updates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmojzfvbuqmjnknltenzy)
- [New in iOS 11.3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmojzfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmojzfvbuqmjnknltc)

### Introduction

iOS 11.3 SDK provides support for developing iOS apps. It’s packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for iOS, watchOS, tvOS, and macOS. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

With this software you can develop apps for iPhone, iPad, or iPod touch running iOS 11.3. You can also test your apps using the included Simulator, which supports iOS 11.3. iOS 11.3 SDK requires a Mac computer running macOS Sierra 10.12.6 or later.

### Tools and Developer Resources

You obtain Xcode 9.3 from the Mac App Store. It is a free download that installs directly into the Applications folder.

The Apple Developer Program provides everything you need to build and distribute your apps on the App Store for iPhone, iPad, Mac, and Apple Watch. Membership includes access to beta OS releases, advanced app capabilities, and tools to develop, test, and distribute apps and Safari extensions. For more information, visit [Apple Developer Program](https://developer.apple.com/programs/).

Apple provides the following resources to support your development:

- Developer documentation is available both on the [Apple Developer website](https://developer.apple.com/documentation) and from Xcode by choosing Help > Developer Documentation.
- [Apple Developer Forums](https://forums.developer.apple.com/). Participate in discussions about developing for Apple platforms and using developer tools.
- [Bug Reporter](http://bugreport.apple.com/). Report issues, enhancement requests, and feedback to Apple. Provide detailed information, including the system and developer tools version information, and any relevant crash logs or console messages.
- [Apple Developer website](https://developer.apple.com/). Get the latest development information.
- [iOS homepage](https://developer.apple.com/ios/). Get high-level information about the latest release of iOS. Download current and beta iOS releases.
- For help with using Xcode, Simulator, or Instruments, choose Help > _app name_ Help.

### Bug Reporting

For issues not mentioned in [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmojzfvbuqmjnknltc), please file bugs through the Apple Developer website [https://developer.apple.com/bug-reporting/](https://developer.apple.com/bug-reporting/).

When filing a bug, please include the full version number in the bug title and in the description. To find the version number, open Settings > General > About. The version number is shown next to Version and looks like _11.3 (15Exxx)_.

Additionally, you may discuss these issues and iOS 11 SDK in the Apple Developer Forums: [https://forums.developer.apple.com/welcome](https://forums.developer.apple.com/welcome). To get more information about iCloud for Developers, go to [https://developer.apple.com/icloud](https://developer.apple.com/icloud).

### Release Notes Updates

_iOS Release Notes_ is sometimes updated after a release is distributed. You can check for the most up-to-date version of _iOS Release Notes_ at the Apple Developer website by checking [http://developer.apple.com/go/?id=ios-sdk-release-notes](https://developer.apple.com/go/?id=ios-sdk-release-notes).

_Revision: iOS1130 - IRN2_

### New in iOS 11.3

### iPhone X and iTunes 12.7.3

Starting with iOS 11.3, users performing tethered updates or restores on iPhone X with iTunes require iTunes 12.7.3. Certain features, including Face ID, may not work as expected when using older version of iTunes. (36546243)

### Notes and Known Issues

The following items relate to using iOS 11 SDK to develop code.

### General

### Resolved Issues

- Devices should now be recognized by the host computer after updating a device to iOS 11.3.
- iOS 11.3 supports iPod touch (6th generation).

### 3rd Party Apps

### Resolved Issues

- Skype no longer crashes on launch or after sign-in. (36501124)

### ARKit

### New Features

- The default video capture format for ARKit in iOS 11.3 is 1080p. The default in earlier versions is unchanged. For more information, see the [supportedVideoFormats](https://developer.apple.com/documentation/arkit/arconfiguration/2942261-supportedvideoformats) property.
- Added support for vertical planes to [ARPlaneDetection](https://developer.apple.com/documentation/arkit/arplanedetection).
- Added rough shape estimation of planar surfaces to [ARPlaneAnchor](https://developer.apple.com/documentation/arkit/arplaneanchor).
- Added [setWorldOrigin(relativeTransform:)](https://developer.apple.com/documentation/arkit/arsession/2942278-setworldorigin) to change the origin of the world coordinate system.
- Added the ability to detect the position of a known image in the environment. For more information, see the [Recognizing Images in an AR Experience](https://developer.apple.com/documentation/arkit/recognizing_images_in_an_ar_experience) sample code.
- Apps can now opt into an interactive process to recover world-tracking state after an ARsession is interrupted. For more information, see the [sessionShouldAttemptRelocalization(_:)](https://developer.apple.com/documentation/arkit/arsessionobserver/2941046-sessionshouldattemptrelocalizati) delegate method.

### Resolved Issues

- Continuing from a breakpoint while debugging an [ARSession](https://developer.apple.com/documentation/arkit/arsession) may result in VIO breaking. Any visual objects placed in the world/anchor are not visible. (31561202)

### Foundation

### Known Issues

- Clients of [NSURLSessionStreamTask](https://developer.apple.com/documentation/foundation/nsurlsessionstreamtask) that use a non-secure connection fail to connect when an error occurs during PAC file evaluation and the system is configured for either Web Proxy Auto Discovery (WPAD) or Proxy Automatic Configuration (PAC). A PAC evaluation failure can occur when the PAC file contains invalid JavaScript or the HTTP host serving the PAC file is unreachable. (33609198)

  _Workaround_: Use [startSecureConnection()](https://developer.apple.com/documentation/foundation/urlsessionstreamtask/1411567-startsecureconnection) to establish a secure connection.

### Health

### Resolved Issues

- Health Record accounts and data are properly synced to Health in iCloud. (35431094)

### iBooks

### Resolved Issues

- Managed books now open reliably in iBooks. (37124818)

### Keychain

### Known Issues

- The shared web credentials API always returns the error “Autofill disabled”. (36989569)

### Maps

### Resolved Issues

- Maps no longer crashes when tapping the “Destinations” UI while connected to CarPlay. (34862998)

### MediaPlayer

### Resolved Issues

- The `startItem` property of `MPMusicPlayerMediaItemQueueDescriptor` class is no longer ignored. (33567879)

### Messages

### Resolved Issues

- Messages threads should no longer have a delay when opened. (35394897)

### Mobile Device Management

### New Features

- Added new configuration settings for device management. For details of the new settings, see the [Configuration Profile Reference](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html) and the [MDM Protocol Reference](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/1-Introduction/Introduction.html#//apple_ref/doc/uid/TP40017387-CH1-SW1).

  - Delay the ability to see and install iOS updates for up to 90 days.
  - Disable USB Restricted Mode.
  - Enable and disable Bluetooth if the Bluetooth settings are not restricted.
  - Find information for an installed app including update availability, if it is assigned to the device or the user, and if the source of the app is the App Store, an Enterprise app, or a beta.
  - Arrange WebClips to the Home Screen Layout payload.
  - Prevent unmanaged apps from accessing contacts in managed accounts.
  - Skip the Proximity Setup screen on first reboot after using the EraseDevice command.
  - Skip the Privacy screen during setup.
  - Specify the version number of an iOS update when using the ScheduleOSUpdate command.
  - Require teacher permission for a student to leave an unmanaged class in Classroom.
  - Restrict the Remote app from connecting to specific Apple TV devices.
  - Reinstall deleted system apps with the InstallApplication command.
  - Allow MMS messages to bypass Always-On IKEv2 VPN.

### Music

### Resolved Issues

- Using Music with VoiceOver or Switch Control should now work as expected. (36998727)

### Safari

### Resolved Issues

- WebApps saved to the home screen and webpages in [SFSafariViewController](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller) can now use the camera to capture images. (35542231)

### Single Sign On

### Resolved Issues

- Background tasks now correctly authenticate in an app that uses Kerberos for single sign-on. (36301557)

### Vision

### Known Issues

- Facial landmarks identified by the Vision framework may flicker in temporal use cases such as video. (32406440)

### Xcode

### Known Issues

- Debugging a disabled Messages extension may cause the Messages app to crash. (33657938)

  _Workaround_: Before starting the debug session, enable the extension by tapping the More (…) button to show the list of apps, then tapping the Edit button, and then tapping the switch to turn on the extension.
- After a simulated iOS device starts up, it’s not possible to pull down the Notification center. (33274699)

  _Workaround_: Lock and unlock the simulated device and then reopen Home screen.
