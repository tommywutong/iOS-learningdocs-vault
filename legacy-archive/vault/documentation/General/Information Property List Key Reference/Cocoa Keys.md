---
title: Information Property List Key Reference
apple_id: TP40009247
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: General
technology: null
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html
archived_at: '2026-07-15T07:34:59.154581Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Information Property List Key Reference](About%20Info.plist%20Keys%20and%20Values.md)


[Next](macOS%20Keys.md)[Previous](Launch%20Services%20Keys.md)

# Cocoa Keys

Cocoa and Cocoa Touch are the environments used to define apps that run in macOS, iOS, tvOS, and watchOS. The keys associated with the Cocoa environments provide support for Interface Builder nib files and provide support for other user-facing features vended by your bundle.

Cocoa keys use the prefix `NS` to distinguish them from other keys. For information about developing Cocoa Touch apps for iOS, see _[App Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072)_. For information about developing Cocoa apps for macOS, see _[Cocoa Fundamentals Guide](../../Cocoa/Cocoa%20Fundamentals%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzu)_.

Table 1 contains an alphabetical listing of Cocoa keys, the corresponding name for that key in the Xcode property list editor, a high-level description of each key, and the platforms on which you use it. Detailed information about each key is available in later sections.

__Table 1__  Summary of Cocoa keys

| Key | Xcode name | Summary | Platforms |
| GCSupportedGameControllers | (none) | Specifies the types of game controllers allowed or required for your app. See [GCSupportedGameControllers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonrx) for details. | tvOS 9.0 and later, iOS 7.0 and later, macOS 10.9 and later |
| GCSupportsMultipleMicroGamepads | (none) | Specifies that the physical Apple TV Remote and the Apple TV Remote app should operate as separate game controllers. See [GCSupportsMultipleMicroGamepads](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonrw) for details. | tvOS |
| GKGameCenterBadgingDisabled | (none) | Specifies whether your app is badged. See [GKGameCenterBadgingDisabled](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomrs) for details. | iOS 7.0 and later |
| GKShowChallengeBanners | (none) | Specifies whether banners are shown within an app. See [GKShowChallengeBanners](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomrt)for details. | iOS 7.0 and later |
| NETestAppMapping | (none) | Enables testing of per-app VPN app extensions without using an MDM server. See [NETestAppMapping](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonbw) for details. | iOS 9.0 and later, macOS 10.11 and later |
| NFCReaderUsageDescription | "Privacy - NFC Reader Usage Description” | Specifies the reason for your app to use the device’s NFC reader. See [NFCReaderUsageDescription](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonzu) for details. | iOS 11 and later |
| NSAppleMusicUsageDescription | “Privacy - Media Library Usage Description” | Specifies the reason for your app to use the media library. See [NSAppleMusicUsageDescription](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonbx) for details. | iOS |
| NSAppleScriptEnabled | “Scriptable” | Specifies whether AppleScript is enabled. See [NSAppleScriptEnabled](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvoni) for details. | macOS |
| NSAppTransportSecurity | (none) | Specifies changes to the default strong security for HTTP connections in iOS and macOS apps and app extensions. See [NSAppTransportSecurity](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomzt) for details. | iOS 9.0 and later, macOS 10.11 and later |
| NSBluetoothPeripheralUsageDescription | “Privacy - Bluetooth Peripheral Usage Description” | Specifies the reason for your app to use Bluetooth. See [NSBluetoothPeripheralUsageDescription](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomrq) for details. | iOS 6.0 and later |
| NSCalendarsUsageDescription | “Privacy - Calendars Usage Description” | Specifies the reason for your app to access the user’s calendars. See [NSCalendarsUsageDescription](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomjv) for details. | iOS 6.0 and later |
| NSCameraUsageDescription | “Privacy - Camera Usage Description” | Specifies the reason for your app to access the device’s camera. See [NSCameraUsageDescription](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomru) for details. | iOS 7.0 and later |
| NSContactsUsageDescription | “Privacy - Contacts Usage Description” | Specifies the reason for your app to access the user’s contacts. See [NSContactsUsageDescription](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomju) for details. | iOS 6.0 and later, OS X v10.8 and later |
| NSDockTilePlugIn | ”Dock Tile Plugin path” | Specifies the name of app’s Dock tile plug-in, if present. See [NSDockTilePlugIn](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfuytcmzygqzq) for details. | macOS |
| NSFaceIDUsageDescription | "Privacy - Face ID Usage Description” | Specifies the reason for your app to use Face ID. See [NSFaceIDUsageDescription](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonzv) for details. | iOS 11 and later |
| NSHealthClinicalHealthRecordsShareUsageDescription | (none) | Specifies text that provides justification for accessing a user’s clinical health records. See `[NSHealthClinicalHealthRecordsShareUsageDescription](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonzw)` for details. | iOS 12.0 and later |
| NSHealthRequiredReadAuthorizationTypeIdentifier | (none) | Specifies an array of HealthKit type identifiers. See `[NSHealthRequiredReadAuthorizationTypeIdentifier](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonzx)` for details. | iOS 12.0 and later |
| NSHealthRequiredWriteAuthorizationTypeIdentifiers | (none) | Specifies an array of HealthKit type identifiers. See `[NSHealthRequiredWriteAuthorizationTypeIdentifiers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonzy)` for details. | iOS 12.0 and later |
| NSHealthShareUsageDescription | "Privacy - Health Share Usage Description” | Specifies the reason for your app to read the user’s health data. See [NSHealthShareUsageDescription](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonby) for details. | iOS 8.0 and later |
| NSHealthUpdateUsageDescription | "Privacy - Health Update Usage Description” | Specifies the reason for your app to make changes to the user’s health data. See [NSHealthUpdateUsageDescription](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonbz) for details. | iOS 8.0 and later |
| NSHomeKitUsageDescription | “Privacy - HomeKit Usage Description” | Specifies the reason for your app to access the user’s HomeKit configuration data. See [NSHomeKitUsageDescription](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonjq) for details. | iOS, watchOS |
| NSHumanReadableCopyright | “Copyright (human-readable)” | (Localizable) Specifies the copyright notice for the bundle. See [NSHumanReadableCopyright](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfuytcmrygu2c2vcqlbjekrrrge3q) for details.  This key replaces the obsolete `CFBundleGetInfoString` key. | macOS |
| NSJavaNeeded | “Cocoa Java application” | Specifies whether the program requires a running Java VM. See [NSJavaNeeded](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrga3tcnru) for details. | macOS |
| NSJavaPath | “Java classpaths” | An array of paths to classes whose components are preceded by `NSJavaRoot`. See [NSJavaPath](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgeytqojr) for details. | macOS |
| NSJavaRoot | “Java root directory” | The root directory containing the java classes. See [NSJavaRoot](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgeytsmbt) for details. | macOS |
| NSLocationAlwaysUsageDescription | “Privacy - Location Always Usage Description” | Specifies the reason for your app to access the user’s location information at all times. See [NSLocationAlwaysUsageDescription](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomjy) for details. | iOS 8.0 and later, macOS 10.10 and later |
| NSLocationUsageDescription | “Privacy - Location Usage Description” | __Unused.__ Use [NSLocationWhenInUseUsageDescription](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomrw) or [NSLocationAlwaysUsageDescription](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomjy) instead.  See [NSLocationUsageDescription](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomrx) for details. | iOS 6.0 and later, OS X v10.9 and later. __Unused__ in iOS 8 and later. |
| NSLocationWhenInUseUsageDescription | “Privacy - Location When In Use Usage Description” | Specifies the reason for your app to access the user’s location information while your app is in use. See [NSLocationWhenInUseUsageDescription](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomrw) for details. | iOS 8.0 and later, macOS 10.10 and later |
| NSMainNibFile | “Main nib file base name” | The name of an app’s main nib file. See [NSMainNibFile](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrga3temrr) for details. | iOS, macOS |
| NSMicrophoneUsageDescription | “Privacy - Microphone Usage Description” | Specifies the reason for your app to access any of the device’s microphones. See [NSMicrophoneUsageDescription](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomrv) for details. | iOS 7.0 and later |
| NSMotionUsageDescription | “Privacy - Motion Usage Description” | Specifies the reason for your app to access the device’s accelerometer. See [NSMotionUsageDescription](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomrr) for details. | iOS 7.0 and later |
| NSPersistentStoreTypeKey | “Core Data persistent store type” | The type of Core Data persistent store associated with a persistent document type. See [NSPersistentStoreTypeKey](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomq) for details. | macOS |
| NSPhotoLibraryAddUsageDescription | "Privacy - Photo Library Additions Usage Description” | Specifies the reason for your app to get write-only access to the user’s photo library. See [NSPhotoLibraryAddUsageDescription](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonzt) for details. | iOS 11 and later |
| NSPhotoLibraryUsageDescription | “Privacy - Photo Library Usage Description” | Specifies the reason for your app to access the user’s photo library. See [NSPhotoLibraryUsageDescription](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomjx) for details. | iOS 6.0 and later |
| NSPrefPaneIconFile | “Preference Pane icon file” | The name of an image file resource used to represent a preference pane in the System Preferences app. See [NSPrefPaneIconFile](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrge2dcnjs) for details. | macOS |
| NSPrefPaneIconLabel | “Preference Pane icon label” | The name of a preference pane displayed beneath the preference pane icon in the System Preferences app. See [NSPrefPaneIconLabel](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrge2dcnzu) for details. | macOS |
| NSPrincipalClass | “Principal class” | The name of the bundle’s main class. See [NSPrincipalClass](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomjr) for details. | macOS |
| NSRemindersUsageDescription | “Privacy - Reminders Usage Description” | Specifies the reason for your app to access the user’s reminders. See [NSRemindersUsageDescription](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomjw) for details. | iOS 6.0 and later |
| NSServices | “Services” | An array of dictionaries specifying the services provided by an app. See [NSServices](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrga3tenrv) for details. | macOS |
| NSSiriUsageDescription | (none) | Specifies the reason for your app to send user data to Siri. See [NSSiriUsageDescription](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonjr) for details. | iOS 10 and later |
| NSSpeechRecognitionUsageDescription | (none) | Specifies the reason for your app to send user data to Apple’s speech recognition servers. See [NSSpeechRecognitionUsageDescription](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonjs) for details. | iOS |
| NSSupportsAutomaticTermination | (none) | Specifies whether the app may be killed to reclaim memory. See [NSSupportsAutomaticTermination](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomjt) for details. | OS X v10.7 and later |
| NSSupportsPurgeableLocalStorage | (none) | Declares that the app can depend on nonlocal storage for user data. See [NSSupportsPurgeableLocalStorage](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonbv) for details. | iOS 9.3 and later |
| NSSupportsSuddenTermination | (none) | Specifies whether the app may be killed to allow for faster shut down or log out operations. See [NSSupportsSuddenTermination](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomjs) for details. | macOS |
| NSUbiquitousContainer | (none) | Specifies the iCloud Drive settings for each container. See [NSUbiquitousContainers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomzs) for details. | iOS, macOS |
| NSUbiquitousContainerIsDocumentScopePublic | (none) | Specifies whether the iCloud Drive should share the contents of this container. See [NSUbiquitousContainerIsDocumentScopePublic](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomrz) for details. | iOS, macOS |
| NSUbiquitousContainerName | (none) | Specifies the name that the iCloud Drive displays for your container. See [NSUbiquitousContainerName](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomzr) for details. | iOS, macOS |
| NSUbiquitousContainerSupportedFolderLevels | (none) | Specifies the maximum number of folder levels inside your container’s Documents directory. See [NSUbiquitousContainerSupportedFolderLevels](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomzq) for details. | iOS, macOS |
| NSUbiquitousDisplaySet | (none) | Specifies the mobile document data that the app can view. See [NSUbiquitousDisplaySet](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvona) for details. | iOS, macOS |
| NSUserActivityTypes | (none) | Specifies the user activity types that the app supports. See [NSUserActivityTypes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomry) for details. | iOS, macOS |
| NSUserNotificationAlertStyle | (none) | Specifies whether the notification style should be `banner`, `alert`, or `none`. The default value is `banner`, which is the recommended style. See [NSUserNotificationAlertStyle](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomjz) for details. | macOS |
| NSVideoSubscriberAccountUsageDescription | “Privacy - TV Provider Usage Description” | Specifies the reason for your app to access the user’s TV provider account. See [NSVideoSubscriberAccountUsageDescription](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonjt) for details. | tvOS |
| UTExportedTypeDeclarations | “Exported Type UTIs” | An array of dictionaries specifying the UTI-based types supported (and owned) by the app. See [UTExportedTypeDeclarations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvooa) for details. | iOS 5.0 and later, OS X v10.7 and later |
| UTImportedTypeDeclarations | “Imported Type UTIs” | An array of dictionaries specifying the UTI-based types supported (but not owned) by the app. See [UTImportedTypeDeclarations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvooi) for details. | iOS, macOS |

`GCSupportedGameControllers` (`array (dictionary (string : string))` - tvOS, iOS, and macOS) Optional key, used only during the App Store submission process, that specifies the types of game controllers allowed or required for your app.

The value for this key is an array. Each array element is a dictionary whose key string is “`ProfileName`” and whose value string is one of the following:

- `Gamepad` - Specifies the standard gamepad, supported in iOS 7.0 and later only, corresponding to a formfitting controller for an iOS device with a limited set of controls. Used with the [GCGamepad](https://developer.apple.com/documentation/gamecontroller/gcgamepad) class.
- `ExtendedGamepad` - Specifies the extended gamepad, supported in tvOS 9.0 and later, iOS 7.0 and later, macOS 10.9 and later, and corresponding to either a formfitting controller for an iOS device or a standalone controller for iOS, macOS, or tvOS with an extended set of controls. Used with the [GCExtendedGamepad](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad) class.
- `MicroGamepad` - Specifies the micro gamepad, supported in tvOS 9.0 and later, and corresponding to a Siri Remote or the Apple TV Remote app running on a connected iOS device. Used with the [GCMicroGamepad](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepad) class.

Supported in tvOS 9.0 and later, iOS 7.0 and later, macOS v10.9 and later.

`GCSupportsMultipleMicroGamepads` (`Boolean` - tvOS). Specifies that the Apple TV Siri Remote and devices running the Apple TV Remote app should each operate as a discrete game controller. Default value is `NO`, indicating that input from all connected remotes is unified.

Specifically, in a Game Controller framework-based tvOS app that uses a value of `NO` for this key, all connected remotes are routed to a single [GCController](https://developer.apple.com/documentation/gamecontroller/gccontroller) object in your app. When a user presses the A button on the Siri Remote, for example, the same in-app action is invoked as if they had pressed the A button on any connected Apple TV Remote app on a device.

If you instead specify a value of `YES` for this key, your tvOS app employs an independent `GCController` object for each connected remote.

Supported in tvOS 10.0 and later.

`GKGameCenterBadgingDisabled` (`Boolean` - iOS). This key determines if badges are added to your turn based app icon. Set the value of this key to `YES` to opt out of badging. Defaults to `NO`.

`GKShowChallengeBanners` (`Boolean` - iOS). This key determines if challenge banners are displayed within an app. Set the value of this key to `YES` to show challenge banners in the app. Set the value to `NO` to suppress challenge-related banners.

`NETestAppMapping` (`Dictionary` - iOS, macOS) Use this key only during development and testing to help you create a per-app VPN app extension. By using this key, you can test per-app VPN communication without the use of a mobile device management (MDM) server. For more information, refer to _[NETunnelProviderManager Class Reference](https://developer.apple.com/documentation/networkextension/netunnelprovidermanager)_.

`NFCReaderUsageDescription` (`String` - iOS). This key lets you describe the reason your app accesses the device’s NFC reader.

This key is supported in iOS 11 and later.

`NSAppleMusicUsageDescription` (`String` - iOS). This key lets you describe the reason your app accesses the user’s media library. When the system prompts the user to allow access, the value that you provide for this key is displayed as part of the alert.

This key is supported in iOS 10 and later and in macOS 10.12 and later.

`NSAppleScriptEnabled` (`Boolean` or `String` - macOS). This key identifies whether the app is scriptable. Set the value of this key to `YES` (when typed as `Boolean`) or `"YES"` (when typed as `String`) if your app supports AppleScript.

`NSAppTransportSecurity` (`Dictionary` - iOS, macOS) Use this key to describe your app’s intended HTTP connection behavior if you require exceptions from best security practices or you want to enable new security features.

On Apple platforms, a networking security feature called _App Transport Security_ (ATS) is available to apps and app extensions, and is enabled by default. It improves privacy and data integrity by ensuring your app’s network connections employ only industry-standard protocols and ciphers without known weaknesses. This helps instill user trust that your app does not accidentally leak transmitted data to malicious parties.

By configuring this key’s value in your app’s `Info.plist` file, you can customize the security of your network connections in a variety of ways. You can:

- Allow insecure communication with particular servers
- Allow insecure loads for web views or for media, while maintaining ATS protections elsewhere in your app
- Enable new security features such as Certificate Transparency

The `NSAppTransportSecurity` key is supported in iOS 9.0 and later and in macOS 10.11 and later, and is available in both apps and app extensions.

Starting in iOS 10.0 and later and in macOS 10.12 and later, the following subkeys are supported:

- `NSAllowsArbitraryLoadsForMedia`
- `NSAllowsArbitraryLoadsInWebContent`
- `NSRequiresCertificateTransparency`
- `NSAllowsLocalNetworking`

In this section:

- [ATS Configuration Basics](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomzv)
- [Using ATS in Apple Frameworks](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonjv)
- [Availability of ATS for Remote and Local Connections](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonju)
- [Requirements for Connecting Using ATS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonjx)
- [Certificate Transparency](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonjy)
- [ATS and HTTPS Server Trust Evaluation Requirements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonrr)
- [Supporting Older Operating Systems](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonry)
- [App Store Review for ATS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonjz)
- [ATS Dictionary Details](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonrq)
- [ATS Examples](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomzw)
- [Debugging ATS Connections](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonbq)
- [Using the nscurl Tool to Diagnose ATS Connection Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonbr)

App Transport Security (ATS) is enabled by default for apps linked against the iOS 9.0 or macOS 10.11 SDKs or later, as indicated by the default Boolean value of `NO` for the `NSAllowsArbitraryLoads` key. This key is at the root level of the `NSAppTransportSecurity` dictionary.

With ATS enabled, HTTP connections must use HTTPS ([RFC 2818](https://tools.ietf.org/html/rfc2818)). Attempts to connect using insecure HTTP fail. ATS employs the Transport Layer Security (TLS) protocol version 1.2 ([RFC 5246](https://tools.ietf.org/html/rfc5246)). For background on secure Internet connections, read _[HTTPS Server Trust Evaluation](https://developer.apple.com/library/archive/technotes/tn2232/_index.html#//apple_ref/doc/uid/DTS40012884)_.

The following listing represents the overall structure of the `NSAppTransportSecurity` dictionary, showing all possible keys, all of which are optional. Keep this structure in mind as you configure each element of the dictionary, as needed, for your app:

```
NSAppTransportSecurity : Dictionary {
    NSAllowsArbitraryLoads : Boolean
    NSAllowsArbitraryLoadsForMedia : Boolean
    NSAllowsArbitraryLoadsInWebContent : Boolean
    NSAllowsLocalNetworking : Boolean
    NSExceptionDomains : Dictionary {
        <domain-name-string> : Dictionary {
            NSIncludesSubdomains : Boolean
            NSExceptionAllowsInsecureHTTPLoads : Boolean
            NSExceptionMinimumTLSVersion : String
            NSExceptionRequiresForwardSecrecy : Boolean   // Default value is YES
            NSRequiresCertificateTransparency : Boolean
        }
    }
}
```

The `NSAppTransportSecurity` dictionary structure expresses two levels of configuration. At the primary level are keys to configure ATS protections for your app’s network connections in general. Also at this level is the `NSExceptionDomains` key; this key lets you opt in to custom configuration for named domains, relative to ATS defaults, as needed.

The primary ATS keys are:

- `NSAllowsArbitraryLoads`

  If set to `YES`, disables all ATS restrictions for all network connections, apart from the connections to domains that you configure individually in the optional `NSExceptionDomains` dictionary. Default value is `NO`.
- `NSAllowsArbitraryLoadsForMedia`

  If set to `YES`, disables all ATS restrictions for media that your app loads using the AV Foundation framework. Employ this key only for loading media that are already encrypted, such as files protected by FairPlay or by secure HLS, and that do not contain personalized information. Default value is `NO`.
- `NSAllowsArbitraryLoadsInWebContent`

  If set to `YES`, disables all ATS restrictions for requests made from web views. This lets your app use an embedded browser that can display arbitrary content, without disabling ATS for the rest of your app. Default value is `NO`.
- `NSAllowsLocalNetworking`

  If set to `YES`, allows loading of local resources without disabling ATS for the rest of your app. Default value is `NO`.
- `NSExceptionDomains`

  Optionally include this dictionary to configure ATS for one or more named domains.

  If you add this key to your `NSAppTransportSecurity` dictionary, any domains you then name within the dictionary obtain the default, full ATS protections—irrespective of the value you set for the global `NSAllowsArbitraryLoads` key. Subkeys of a domain-name key then let you alter that domain’s ATS protections from its defaults.

Read important, detailed information on the preceding primary keys in [Table 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomzu).

At the secondary level are the subkeys within the optional ATS `NSExceptionDomains` dictionary. The step of including an `NSExceptionDomains` dictionary in your app’s `Info.plist` file:

- Creates a container for one or more domain-specific dictionaries, letting you specify customized, per-domain HTTP connection properties
- Removes any general, app-wide ATS customizations you’ve specified using primary ATS keys

  For example, if you’ve added `NSAllowsArbitraryLoadsForMedia` key for your app in general, domains named in the exception domains dictionary _do not_ allow arbitrary media loading.

Having thus started with default ATS protections for the named domains, you can optionally decrease or increase their protections individually. You can _decrease_ a named domain’s protections to:

- Allow insecure _HTTP_ connections—without diminishing ATS protections for the HTTPS connections to a domain—by employing the `NSExceptionAllowsInsecureHTTPLoads` key with a value of `YES`; doing this triggers App Store review, as described in [App Store Review for ATS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonjz)
- Disable the perfect forward secrecy (PFS) requirement by employing the `NSExceptionRequiresForwardSecrecy` key with a value of `NO`
- Lower the minimum-allowed Transport Layer Security (TLS) version by employing the `NSExceptionMinimumTLSVersion` key

You can also _increase_ a named domain’s protections by requiring Certificate Transparency (see [Certificate Transparency](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonjy)).

The elements of the optional `NSExceptionDomains` dictionary are:

- `<domain-name-string>`

  A domain name string, identifying a domain for which you want to specify a connection configuration. You can add multiple instances of this key, letting you name any number of domains in the one `NSExceptionDomains` dictionary. Configure each `<domain-name-string>` dictionary to contain one or more of the following child keys:

  - `NSIncludesSubdomains`

    If set to `YES`, applies a named domain’s ATS configuration to all of its subdomains. Default value is `NO`.
  - `NSExceptionAllowsInsecureHTTPLoads`

    If set to `YES`, allows insecure HTTP loads for the named domain, but does not change Transport Layer Security (TLS) requirements and does not affect HTTPS loads for the named domain. Default value is `NO`.
  - `NSExceptionMinimumTLSVersion`

    Specifies the minimum TLS version for network connections for the named domain, allowing connection using an older, less secure version of Transport Layer Security.
  - `NSExceptionRequiresForwardSecrecy`

    If set to `NO`, allows TLS ciphers, for the named domain, that do not support perfect forward secrecy (PFS). Default value is `YES`.
  - `NSRequiresCertificateTransparency`

    If set to `YES`, requires valid, signed Certificate Transparency timestamps for server certificates for the named domain. Default value is `NO`.

Read important, detailed information on the preceding `NSExceptionDomains` keys in [Table 3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonbu).

App Transport Security (ATS) is enforced by the [NSURLSession](https://developer.apple.com/documentation/foundation/urlsession) class and all APIs that use it. ATS is automatically enabled when you link your app against the iOS 9.0 SDK or later or against the macOS 10.11 SDK or later. (The older [NSURLConnection](https://developer.apple.com/documentation/foundation/nsurlconnection) class also enforces ATS when you link against the iOS 9.0 SDK or later or against the macOS 10.11 SDK or later.) ATS protections are not available when using lower-level networking APIs provided by Apple, or when using third-party networking libraries.

ATS is not available on operating systems older than iOS 9.0 or macOS 10.11; those older operating systems ignore the `NSAppTransportSecurity` key. When ATS is not available, the system still provides standard HTTPS security and performs server trust evaluation per [RFC 2818](https://tools.ietf.org/html/rfc2818).

If you link your app against an SDK for an operating system older than iOS 9.0 or macOS 10.11, your Internet connections continue to work but ATS is disabled, no matter which version of operating system your app is running on.

App Transport Security (ATS) applies only to connections made to public host names. The system does not provide ATS protection to connections made to:

- Internet protocol (IP) addresses
- Unqualified host names
- Local hosts employing the `.local` top-level domain (TLD)

To connect to an unqualified host name or to a `.local` domain, you must set the value of the `NSAllowsLocalNetworking` key to `YES`.

With App Transport Security (ATS) fully enabled, the system requires that your app’s HTTP connections use HTTPS and that they satisfy the following security requirements:

- The X.509 digital server certificate must meet at least one of the following trust requirements:

  - Issued by a certificate authority (CA) whose root certificate is incorporated into the operating system
  - Issued by a trusted root CA and installed by the user or a system administrator
- The negotiated Transport Layer Security (TLS) version must be TLS 1.2. Attempts to connect without TLS/SSL protection, or with an older version of TLS/SSL, are denied by default.
- The connection must use either the AES-128 or AES-256 symmetric cipher. The negotiated TLS connection cipher suite must support perfect forward secrecy (PFS) through Elliptic Curve Diffie-Hellman Ephemeral (ECDHE) key exchange, and must be one of the following:

  - `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`
  - `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`
  - `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384`
  - `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA`
  - `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256`
  - `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA`
  - `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`
  - `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`
  - `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384`
  - `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`
  - `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA`
- The leaf server certificate must be signed with one of the following types of keys:

  - Rivest-Shamir-Adleman (RSA) key with a length of at least 2048 bits
  - Elliptic-Curve Cryptography (ECC) key with a size of at least 256 bits

  In addition, the leaf server certificate hashing algorithm must be Secure Hash Algorithm 2 (SHA-2) with a digest length, sometimes called a “fingerprint,” of at least 256 (that is, SHA-256 or greater).

The requirements listed in this section are current as of this document’s publication date, with stricter requirements possible in the future. Changes to these requirements will not break app binary compatibility.

Certificate Transparency employs logging of X.509 certificates, using cryptographic assurance and in a manner that can be publicly audited. This system facilitates identifying certificates that were mistakenly or maliciously issued. App Transport Security lets you configure your app to require Certificate Transparency (CT) for specific, named domains. Before such a domain can connect with your app, it must prove to the system that its X.509 digital certificate is present in at least two CT logs trusted by Apple.

To require Certificate Transparency, set the value of the `NSRequiresCertificateTransparency` key, within the appropriate domain-name dictionary, to `YES`. (See the overall structure of the `NSAppTransportSecurity` dictionary, in [ATS Configuration Basics](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomzv), to see exactly where the `NSRequiresCertificateTransparency` key should be placed.)

Enabling Certificate Transparency does not eliminate the need for your app to revoke invalid certificates and to refuse connections that employ them. To support certificate checking and revocation, use Online Certificate Status Protocol (OCSP) stapling, specified in [RFC6066](https://tools.ietf.org/html/rfc6066#section-8).

For details on Certificate Transparency, see [certificate-transparency.org](https://www.certificate-transparency.org/).

Your ability to loosen HTTPS server trust evaluation requirements depends on whether or not App Transport Security (ATS) is enabled for a domain, as follows:

- If ATS _is_ enabled for a domain, you cannot loosen the system’s HTTPS server trust evaluation requirements.
- If ATS _is not_ enabled for a domain, the system nonetheless performs HTTPS server trust evaluation, but you can loosen this requirement as described in _[HTTPS Server Trust Evaluation](https://developer.apple.com/library/archive/technotes/tn2232/_index.html#//apple_ref/doc/uid/DTS40012884)_.

Whether or not ATS is enabled for a domain, you can tighten trust evaluation requirements, such as by implementing certificate pinning.

If your app requires fine-grained transport security exceptions, such as to allow local networking while maintaining ATS protections elsewhere, the current versions of iOS and macOS support that by letting you configure the ATS dictionary using the following sub-keys:

- `NSAllowsArbitraryLoadsForMedia`
- `NSAllowsArbitraryLoadsInWebContent`
- `NSAllowsLocalNetworking`

However, this fine-grained control is not available in older operating systems (iOS 10.0 and older, or macOS 10.12 and older). To maintain backward-compatibility when you use any of these keys, you must also set the value of the `NSAllowsArbitraryLoads` key to `YES`, taking advantage of its version-specific behavior. It works as follows:

To make it clear how this works, here is an example:

1. Start by supporting your users who are running current versions of the operating system, by ensuring they enjoy maximum ATS protections. Do this by requesting only the minimal, specific exceptions needed by your app. For example, if your app needs access to local resources, set the value of the `NSAllowsLocalNetworking` key to `YES`.
2. Next, support your users who are running older versions of the operating system, by taking advantage of the special behavior of the `NSAllowsArbitraryLoads` key. Do this by setting the value of the `NSAllowsArbitraryLoads` key to `YES` as well.

   In summary, for this example you provide fine-grained security in current operating systems, while maintaining backward-compatibility for your app’s networking requirements, by setting the following ATS key values:

```
NSAllowsArbitraryLoads:  YES  // Course-grained opt-out for users on old OS
NSAllowsLocalNetworking: YES  // Fine-grained exception for users on current OS
```

Now, when your app runs in an older operating system that does not support fine-grained ATS exceptions, your networking features work because you have set the value of the `NSAllowsArbitraryLoads` key to `YES`. ATS is then disabled for these users, thereby allowing access, in this example, to local resources.

When your app runs in a current operating system, the specific exception keys are available and your settings for them are respected. General ATS protections remain enabled for your app because the effective value of the `NSAllowsArbitraryLoads` key, due to its special behavior described in this section, is `NO`.

Your use of certain App Transport Security (ATS) keys triggers additional App Store review for your app, and requires you to provide justification. These keys are:

- `NSAllowsArbitraryLoads`
- `NSAllowsArbitraryLoadsForMedia`
- `NSAllowsArbitraryLoadsInWebContent`
- `NSExceptionAllowsInsecureHTTPLoads`
- `NSExceptionMinimumTLSVersion`

Some examples of justifications eligible for consideration are:

- Must connect to a server managed by another entity that does not support secure connections
- Must support connecting to devices that cannot be upgraded to use secure connections, and that must be accessed via public host names
- Must provide embedded web content from a variety of sources, but cannot use a class supported by the `NSAllowsArbitraryLoadsInWebContent` key
- App loads media content that is encrypted and that contains no personalized information

When submitting your app to the App Store, provide sufficient information for the App Store to determine why your app cannot make secure connections by default.

Table 2 shows the primary keys within the `NSAppTransportSecurity` dictionary for describing your app’s intended network behavior. For the sub-keys associated with the `NSExceptionDomains` dictionary, see [Table 3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonbu).

__Table 2__  App Transport Security dictionary primary keys

| Key | Xcode name | Type | Description |
| `NSAllowsArbitraryLoads` | “Allow Arbitrary Loads” | Boolean | An optional Boolean value that, when set to `YES`, disables App Transport Security (ATS) for all domains for which you do not explicitly reenable ATS by using an exception domain dictionary (as specified using the `NSExceptionDomains` key).  _Use of this key triggers App Store review and requires justification._  Enable this key for cases where your app allows the user to specify connection to an arbitrary URL.  Enabling this key can also be useful for debugging and development.  In iOS 10 and later, and macOS 10.12 and later, the value of this key is ignored—resulting in an effective value for this key of its default value of `NO`—if any of the following keys are present in your app’s `Info.plist` file:   - `NSAllowsArbitraryLoadsForMedia` - `NSAllowsArbitraryLoadsInWebContent` - `NSAllowsLocalNetworking`   __NOTE__ Disabling ATS allows connection regardless of HTTP or HTTPS configuration, allows connection to servers with lower Transport Layer Security (TLS) versions, and allows connection using cipher suites that do not support perfect forward secrecy (PFS).  This key’s default value of `NO` results in default ATS behavior for all connections except those for which you have specified an exception domain dictionary (see [Table 3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonbu)). |
| `NSAllowsArbitraryLoadsForMedia` | (none) | Boolean | An optional Boolean value that, when set to `YES`, disables all App Transport Security restrictions for media loaded using APIs from the AV Foundation framework, as described in _[AV Foundation Framework Reference](https://developer.apple.com/documentation/avfoundation)_.  _Use of this key triggers App Store review and requires justification._  Employ this key only for loading media that are already encrypted, such as files protected by FairPlay or by secure HLS, and that do not contain personalized information.  If you add this key to your `Info.plist` file, then, irrespective of the value of the key, ATS ignores the value of the `NSAllowsArbitraryLoads` key, instead using that key’s default value of `NO`.  Default value is `NO`.  Available starting in iOS 10.0 and macOS 10.12. |
| `NSAllowsArbitraryLoadsInWebContent` | (none) | Boolean | An optional Boolean value that applies only to content to be loaded into an instance of the following classes:   - [WKWebView](https://developer.apple.com/documentation/webkit/wkwebview) - [UIWebView](https://developer.apple.com/documentation/uikit/uiwebview) (iOS only) - WebView (macOS only)   Set this key’s value to `YES` to obtain exemption from ATS policies in your app’s web views, without affecting the ATS-mandated security of your [NSURLSession](https://developer.apple.com/documentation/foundation/urlsession) connections.  Default value is `NO`.  _Use of this key triggers App Store review and requires justification._  To support older versions of iOS and macOS, you can employ this key and still manually configure ATS. To do so, set this key’s value to `YES` and also configure the `NSAllowsArbitraryLoads` subkeys.  If you add this key to your `Info.plist` file, then, irrespective of the value of the key, ATS ignores the value of the `NSAllowsArbitraryLoads` key, instead using that key’s default value of `NO`.  Available starting in iOS 10.0 and macOS 10.12. |
| `NSAllowsLocalNetworking` | (none) | Boolean | An optional Boolean value that, when set to `YES`, removes App Transport Security protections for connections to unqualified domains and to `.local` domains, without disabling ATS for the rest of your app.  In iOS 10 and later and in macOS 10.12 and later, if you set this key’s value to `YES`, then App Transport Security ignores the value of the `NSAllowsArbitraryLoads` key, instead using that key’s default value of `NO`. This behavior supports adoption of App Transport Security protections while allowing embedded browsers to continue working in iOS 9 and earlier and in macOS 10.11 and earlier. (Specifically, to obtain this behavior, set the value of this key to `YES` and set the value of the `NSAllowsArbitraryLoads` key to `YES` as well.)  Default value is `NO`.  Available starting in iOS 10.0 and macOS 10.12. |
| `NSExceptionDomains` | “Exception Domains” | Dictionary | An optional dictionary of ATS exceptions for specific domains. Each value in the dictionary is itself a dictionary, and describes a domain-specific network connection configuration exception.  An exception domain’s top-level key is the domain name string for which you want to specify a connection configuration; for example, `www.apple.com`. A domain name key for an exception dictionary:   - Must be lowercased to work correctly - Must not include a port number - Must not be a numerical IP address (but rather a string) - Must not end with a trailing dot, unless you only want to match a domain string with a trailing dot. For example, `example.com.` (with a trailing dot) matches “_example.com._” but not “_example.com_”. Similarly, `example.com` matches “_example.com_” but not “_example.com._”.   For details on configuring an exception domain dictionary, see [Table 3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonbu). |

Table 3 shows the keys for describing server-specific exceptions to your app’s overall intended network behavior.

__Table 3__  Exception domains dictionary keys

| Key | Xcode name | Type | Description |
| `NSIncludesSubdomains` | (none) | Boolean | An optional Boolean value that, when set to `YES`, applies the `NSExceptionDomains` ATS exceptions to all subdomains (of the domain whose name is the top-level key in the `NSExceptionDomains` dictionary).  Default value is `NO`. |
| `NSRequiresCertificateTransparency` | (none) | Boolean | An optional Boolean value that, when set to `YES`, requires that valid, signed Certificate Transparency (CT) timestamps, from known CT logs, be presented for server (X.509) certificates on a domain.  Default value is `NO`.  Available starting in iOS 10.0 and macOS 10.12. |
| `NSExceptionAllowsInsecureHTTPLoads` | (none) | Boolean | An optional Boolean value that, when set to `YES`, allows insecure HTTP loads but does not change Transport Layer Security (TLS) requirements. Use this key to describe your app’s intended connection behavior for a domain whose security attributes you have control over.  _Use of this key triggers App Store review and requires justification._    With this key’s value set to `YES`, your app can make secure connections to a secure server but can also connect insecurely to a server with no certificate, or a self-signed, expired, or host-name-mismatched certificate.  Set this key’s value to `YES`, if needed, to:   - Enable connection to an insecure HTTP server - Enable connection to an untrusted HTTPS server - Enable connection to an HTTPS server for which you want to perform your own server trust evaluation   In some cases you need to use other exception-dictionary keys along with this one to establish connection. For example, to connect to an HTTPS server that uses a self-signed certificate and a TLS version lower than 1.2, set the `NSExceptionAllowsInsecureHTTPLoads` value to `YES` and also set an appropriate value for the `NSExceptionMinimumTLSVersion` key.    Default value is `NO`. |
| `NSExceptionRequiresForwardSecrecy` | (none) | Boolean | An optional Boolean value for overriding the requirement that a server support perfect forward secrecy (PFS). Use this key to describe your app’s intended connection behavior for a domain whose security attributes you have control over.  Default value is `YES`, which limits the accepted ciphers to those listed in [ATS Configuration Basics](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomzv).  Setting the value to `NO` results in the following ciphers, which do not support FS, also being accepted:   - `TLS_RSA_WITH_AES_256_GCM_SHA384` - `TLS_RSA_WITH_AES_128_GCM_SHA256` - `TLS_RSA_WITH_AES_256_CBC_SHA256` - `TLS_RSA_WITH_AES_256_CBC_SHA` - `TLS_RSA_WITH_AES_128_CBC_SHA256` - `TLS_RSA_WITH_AES_128_CBC_SHA` |
| `NSExceptionMinimumTLSVersion` | (none) | String | An optional string value that specifies the minimum Transport Layer Security (TLS) version for network connections. Use this key to describe your app’s intended connection behavior for a domain whose security attributes you have control over.  _Use of this key triggers App Store review and requires justification._  Valid values are:   - `TLSv1.0` - `TLSv1.1` - `TLSv1.2`   Default value is `TLSv1.2`. |

This section shows how to specify some common networking behaviors using the `NSAppTransportSecurity` key.

To use ATS generally but allow connection to a specific server that does not support the HTTPS protocol—for example, a media server that your app uses—employ the following configuration pattern in your `Info.plist` file:

```
NSAppTransportSecurity
    NSExceptionDomains
        "media-server.example.com"
            NSExceptionAllowsInsecureHTTPLoads = YES
```


To use a less-secure HTTPS connection to a specified server that uses an older version of TLS and that does not support perfect forward secrecy (PFS), while retaining the default, best-practice ATS behavior elsewhere, employ the following configuration pattern in your `Info.plist` file:

```
NSAppTransportSecurity
    NSExceptionDomains
        "less-secure.example.com"
            NSExceptionRequiresForwardSecrecy = NO
            NSExceptionMinimumTLSVersion = "TLSv1.0"
```


If your app is a web browser, or otherwise allows a user to enter an arbitrary URL, your app must be able to load resources from anywhere. In such a scenario, your app should still use ATS when communicating with servers whose security attributes you control, such as your update server.

To require ATS connections to domains that you control, while allowing insecure HTTP access to all other URLs, employ the following configuration pattern in your `Info.plist` file:

```
NSAppTransportSecurity
    NSExceptionDomains
        "domain-i-control.example.com"
            NSExceptionAllowsInsecureHTTPLoads = NO
            NSExceptionRequiresForwardSecrecy = YES
            NSExceptionMinimumTLSVersion = "TLSv1.2"
        "other-domain-i-control.example.com"
            NSExceptionAllowsInsecureHTTPLoads = NO
            NSExceptionRequiresForwardSecrecy = YES
            NSExceptionMinimumTLSVersion = "TLSv1.2"
    NSAllowsArbitraryLoads = YES
```


If you are seeing Internet connection problems that you suspect are related to ATS, try the following troubleshooting approach:

1. Disable ATS entirely to confirm that ATS is involved with the connection problem. Do this by using the following configuration pattern:

```
NSAppTransportSecurity
    NSAllowsArbitraryLoads = YES
```

   If entirely disabling ATS solves your connection problem, proceed with step 2. (If you still cannot connect with ATS disabled, the problem lies somewhere other than with ATS.)
2. Test whether a specific domain under your control is causing the connection problem. Do this by reenabling ATS except on that specific domain, using the following configuration pattern:

```
NSAppTransportSecurity
    NSAllowsArbitraryLoads = NO  // Shown for clarity; this is the default
    NSExceptionDomains
        "secure-server-i-control.example.com"
            NSExceptionAllowsInsecureHTTPLoads = YES
            NSExceptionRequiresForwardSecrecy = NO
            NSExceptionMinimumTLSVersion = "TLSv1.0"
```

   If connection continues to work with this configuration, it is likely that the problem lies with the specific domain named in your `NSExceptionDomains` dictionary.

   If connection fails with this configuration, the problem is likely one of two things:

   - An ATS misconfiguration on the server named in the `NSExceptionDomains` dictionary
   - An ATS misconfiguration on another server that the connection is redirected to

   Once you have pinpointed the server at blame for the connection problem, proceed with step 3.
3. Use the _[TLSTool](https://developer.apple.com/library/archive/samplecode/sc1236/Introduction/Intro.html#//apple_ref/doc/uid/DTS40014927)_ sample code project to investigate the details of the TLS version, server certificate, and cipher suite the problematic server is using.

   If the new information you’ve gathered allows you to reconfigure the server to support ATS, do so.

   If you are unable to reconfigure the server, use the information you’ve gathered using the _[TLSTool](https://developer.apple.com/library/archive/samplecode/sc1236/Introduction/Intro.html#//apple_ref/doc/uid/DTS40014927)_ app to define an appropriate `NSExceptionDomains` dictionary for that server.

In addition, you can enable logging of [NSURLSession](https://developer.apple.com/documentation/foundation/urlsession) class errors by employing the following environment variable in your Xcode project:

```
CFNETWORK_DIAGNOSTICS=1
```

For more information about using this environment variable, read _[CFNetwork Diagnostic Logging](https://developer.apple.com/library/archive/qa/qa1887/_index.html#//apple_ref/doc/uid/DTS40015177)_. For help interpreting error codes, read _[Security Framework Error Codes](https://developer.apple.com/library/archive/qa/qa1499/_index.html#//apple_ref/doc/uid/DTS10004158)_.

In macOS 10.11 and later, you can use the `/usr/bin/nscurl` tool to help diagnose connection issues due to App Transport Security.

The `--ats-diagnostics` option tries to connect with the specified URL using different combinations of values for the `NSAllowsArbitraryLoads`, `NSExceptionMinimumTLSVersion`, `NSExceptionRequiresForwardSecrecy`, and `NSExceptionAllowsInsecureHTTPLoads` keys shown in [Table 3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonbu). A summary of the results is printed to the command line.

The format for the command is:

`/usr/bin/nscurl --ats-diagnostics [--verbose] URL`

- __URL.__ The URL for the host. This is required.
- __verbose.__ Specifying this option includes more information for each connection attempt including the keys and associated values used.

Listing 1 shows partial output of diagnosing a connection to `https://apple.com`.

__Listing 1__  Partial output of `nscurl`

```
> /usr/bin/nscurl --ats-diagnostics https://apple.com
Starting ATS Diagnostics

Configuring ATS Info.plist keys and displaying the result of HTTPS loads to https://apple.com.
A test will "PASS" if URLSession:task:didCompleteWithError: returns a nil error.
Use '--verbose' to view the ATS dictionaries used and to display the error received in URLSession:task:didCompleteWithError:.
================================================================================

Default ATS Secure Connection
---
ATS Default Connection
2015-09-09 09:53:01.592 nscurl[9207:5187047] CFNetwork SSLHandshake failed (-9824)
2015-09-09 09:53:01.593 nscurl[9207:5187047] NSURLSession/NSURLConnection HTTP load failed (kCFStreamErrorDomainSSL, -9824)
Result : FAIL
---

================================================================================

Allowing Arbitrary Loads

---
Allow All Loads
Result : PASS
---

================================================================================

Configuring TLS exceptions for apple.com

---
TLSv1.2
2015-09-09 09:53:02.145 nscurl[9207:5187047] CFNetwork SSLHandshake failed (-9824)
2015-09-09 09:53:02.146 nscurl[9207:5187047] NSURLSession/NSURLConnection HTTP load failed (kCFStreamErrorDomainSSL, -9824)
Result : FAIL
---

---
TLSv1.1
2015-09-09 09:53:02.270 nscurl[9207:5187047] CFNetwork SSLHandshake failed (-9824)
2015-09-09 09:53:02.271 nscurl[9207:5187047] NSURLSession/NSURLConnection HTTP load failed (kCFStreamErrorDomainSSL, -9824)
Result : FAIL
---

---
TLSv1.0
2015-09-09 09:53:02.407 nscurl[9207:5187047] CFNetwork SSLHandshake failed (-9824)
2015-09-09 09:53:02.408 nscurl[9207:5187047] NSURLSession/NSURLConnection HTTP load failed (kCFStreamErrorDomainSSL, -9824)
Result : FAIL
---

================================================================================

Configuring PFS exceptions for apple.com
…
```

Listing 2 shows partial output when using the`--verbose` option. The two main differences are showing the values of the keys from `Info.plist` from lines 10 to 17, and a longer error result shown on line 19.

__Listing 2__  Partial output of `nscurl` using `--verbose`

```
> /usr/bin/nscurl --ats-diagnostics --verbose https://apple.com
Starting ATS Diagnostics
…

Configuring PFS exceptions and allowing insecure HTTP for apple.com

---
Disabling Perfect Forward Secrecy and Allowing Insecure HTTP
ATS Dictionary:
{
    NSExceptionDomains =     {
        "apple.com" =         {
            NSExceptionAllowsInsecureHTTPLoads = YES;
            NSExceptionRequiresForwardSecrecy = NO;
        };
    };
}
Result : FAIL
Error : Error Domain=NSURLErrorDomain Code=-1022 "The resource could not be loaded because the App Transport Security policy requires the use of a secure connection." UserInfo={NSUnderlyingError=0x7fc6a9d11900 {Error Domain=kCFErrorDomainCFNetwork Code=-1022 "(null)"}, NSErrorFailingURLStringKey=http://www.apple.com/apple-events/september-2015/, NSErrorFailingURLKey=http://www.apple.com/apple-events/september-2015/, NSLocalizedDescription=The resource could not be loaded because the App Transport Security policy requires the use of a secure connection.}
---
…
```


`NSBluetoothPeripheralUsageDescription` (`String` - iOS) This key lets you describe the reason your app uses Bluetooth. When the system prompts the user to allow usage, the value that you provide for this key is displayed as part of the alert.

This key is supported in iOS 6.0 and later.

`NSCalendarsUsageDescription` (`String` - iOS) This key lets you describe the reason your app accesses the user’s calendars. When the system prompts the user to allow access, this string is displayed as part of the alert.

This key is supported in iOS 6.0 and later.

`NSCameraUsageDescription` (`String` - iOS) describes the reason that the app (including an iMessage app) accesses the device’s camera. When the system prompts the user to allow access, this string is displayed as part of the alert.

This key is supported in iOS 7.0 and later.

`NSContactsUsageDescription` (`String` - iOS) The key lets you describe the reason your app accesses the user’s contacts. When the system prompts the user to allow access, this string is displayed as part of the alert.

This key is supported in iOS 6.0 and later.

`NSDockTilePlugIn` (`String` - macOS). This key contains the name of a plug-in bundle with the `.docktileplugin` filename extension and residing in the app’s `Contents/PlugIns` directory. The bundle must contain the Dock tile plug-in for the app. For information about creating a Dock tile plug-in, see _Dock Tile Programming Guide_.

NSFaceIDUsageDescription (`String` - iOS). This key lets you describe the reason your app uses Face ID.

This key is supported in iOS 11 and later.

NSHealthClinicalHealthRecordsShareUsageDescription (`String` - iOS). This key contains a string that is displayed in an authorization prompt when your app requests access to the user’s clinical records. This string should provide justification for accessing these records.

This key is supported in iOS 12.0 and later.

NSHealthRequiredReadAuthorizationTypeIdentifier (`Array` - iOS). This key must contain an array of three or more HealthKit type identifiers. If the user does not authorize permission for all the required types, authorization fails with a `HKErrorRequiredAuthorizationDenied` error.

This key is supported in iOS 12.0 and later.

NSHealthRequiredWriteAuthorizationTypeIdentifiers (`Array` - iOS). This key must contain an array of three or more HealthKit type identifiers. If the user does not authorize permission for all the required types, authorization fails with a `HKErrorRequiredAuthorizationDenied` error.

This key is supported in iOS 12.0 and later.

NSHealthShareUsageDescription (`String` - iOS). This key lets you describe the reason your app reads the user’s health data. The system prompts the user to allow access when you call the [requestAuthorizationToShareTypes:readTypes:completion:](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614152-requestauthorization) method, and this string is displayed as part of the alert. For more information, read _[HKHealthStore Class Reference](https://developer.apple.com/documentation/healthkit/hkhealthstore)_ and Setting Up HealthKit. This string is localizable.

This key is supported in iOS 8.0 and later.

NSHealthUpdateUsageDescription (`String` - iOS). This key lets you describe the reason your app makes changes to the user’s health data. The system prompts the user to allow access when you call the [requestAuthorizationToShareTypes:readTypes:completion:](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614152-requestauthorization) method, and this string is displayed as part of the alert. For more information, read _[HKHealthStore Class Reference](https://developer.apple.com/documentation/healthkit/hkhealthstore)_ and Setting Up HealthKit. This string is localizable.

This key is supported in iOS 8.0 and later.

NSHomeKitUsageDescription (`String` - iOS, watchOS). This key lets you describe the reason your app access the user’s HomeKit configuration data. When the system prompts the user to allow access, this string is displayed as part of the alert.

`NSHumanReadableCopyright` (`String` - macOS). This key contains a string with the copyright notice for the bundle; for example, `© 2016, My Company`. You can load this string and display it in an About dialog box. The system uses this string in the app’s Info window in Finder.

This key can be localized by including it in your `InfoPlist.strings` files.

This key replaces the obsolete `CFBundleGetInfoString` key.

See also [CFBundleShortVersionString](Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgeytgnbz).

`NSJavaNeeded` (`Boolean` or `String` - macOS). This key specifies whether the Java VM must be loaded and started up prior to executing the bundle code. This key is required only for Cocoa Java apps to tell the system to launch the Java environment. If you are writing a pure Java app, do not include this key.

You can also specify a string type with the value “YES” instead of a Boolean value if desired.

Deprecated in OS X v10.5.

`NSJavaPath` (`Array` - macOS). This key contains an array of paths. Each path points to a Java class. The path can be either an absolute path or a relative path from the location specified by the key [NSJavaRoot](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgeytsmbt). The development environment (or, specifically, its jamfiles) automatically maintains the values in the array.

Deprecated in OS X v10.5.

`NSJavaRoot` (`String` - macOS). This key contains a string identifying a directory. This directory represents the root directory of the app’s Java class files.

`NSLocationAlwaysUsageDescription` (`String` - iOS) This key lets you describe the reason your app accesses the user’s location information at all times. Include this key when your app uses location services in a potentially nonobvious way while running in the foreground or the background. For example, a social app might include this key when it uses location information to track the user’s location and display other users that are nearby. In this case, the fact that the app is tracking the user’s location might not be readily apparent. The system includes the value of this key in the alert panel displayed to the user when requesting permission to use location services.

This key is required when you use the [requestAlwaysAuthorization](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620551-requestalwaysauthorization) method of the [CLLocationManager](https://developer.apple.com/documentation/corelocation/cllocationmanager) class to request authorization for location services. If this key is not present and you call the `requestAlwaysAuthorization` method, the system ignores your request and prevents your app from using location services.

This key is supported in iOS 8.0 and later.

`NSLocationUsageDescription` (`String` - iOS) __Unused__ in iOS 8 and later. If you link your app on or after iOS 8, use the [NSLocationAlwaysUsageDescription](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomjy) or [NSLocationWhenInUseUsageDescription](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomrw) key instead.

This key lets you describe the reason your app accesses the user’s location information. When the system prompts the user to allow access, this string is displayed as part of the alert panel.

This key is supported in iOS 6.0 through iOS 7. This key is ignored in iOS 8 and later.

`NSLocationWhenInUseUsageDescription` (`String` - iOS) This key lets you describe the reason your app accesses the user’s location information while your app runs in the foreground and otherwise when in use. Include this key when your app uses location services to track the user’s current location directly. This key does not support using location services to monitor regions or monitor the user’s location using the significant location change service. The system includes the value of this key in the alert panel displayed to the user when requesting permission to use location services.

This key is required when you use the [requestWhenInUseAuthorization](https://developer.apple.com/documentation/corelocation/cllocationmanager/1620562-requestwheninuseauthorization) method of the [CLLocationManager](https://developer.apple.com/documentation/corelocation/cllocationmanager) class to request authorization for location services. If the key is not present when you call the `requestWhenInUseAuthorization` method without including this key, the system ignores your request.

This key is supported in iOS 8.0 and later.

`NSMainNibFile` (`String` - iOS, macOS). This key contains a string with the name of the app’s main nib file (minus the `.nib` extension). A nib file is an Interface Builder archive containing the description of a user interface along with any connections between the objects of that interface. The main nib file is automatically loaded when an app is launched.

This key is mutually exclusive with the [UIMainStoryboardFile](iOS%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjsfvjvooi) key. You should include one of the keys in your `Info.plist` file but not both.

`NSMicrophoneUsageDescription` (`String` - iOS) This key lets you describe the reason your app (including an iMessage app) accesses any of the device’s microphones. When the system prompts the user to allow access, this string is displayed as part of the alert.

This key is supported in iOS 7.0 and later.

`NSMotionUsageDescription` (`String` - iOS) This key lets you describe the reason your app accesses the device’s accelerometer. When the system prompts the user to allow access, this string is displayed as part of the alert.

This key is supported in iOS 7.0 and later.

`NSPersistentStoreTypeKey` (`String` - macOS). This key contains a string that specifies the type of Core Data persistent store associated with a document type (see [CFBundleDocumentTypes](Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgaytmobv)).

`NSPhotoLibraryAddUsageDescription` (`String` - iOS) This key lets you describe the reason your app seeks write-only access to the user’s photo library. When the system prompts the user to allow access, this string is displayed as part of the alert.

This key is supported in iOS 11.0 and later.

`NSPhotoLibraryUsageDescription` (`String` - iOS) This key lets you describe the reason your app accesses the user’s photo library. When the system prompts the user to allow access, this string is displayed as part of the alert.

Although this keys governs read and write access to the user’s photo library, it’s best to use [NSPhotoLibraryAddUsageDescription](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonzt) if your app needs only to add assets to the library and does not need to read any assets.

This key is supported in iOS 6.0 and later.

`NSPrefPaneIconFile` (`String` - macOS). This key contains a string with the name of an image file (including extension) containing the preference pane’s icon. This key should only be used by preference pane bundles. The image file should contain an icon 32 by 32 pixels in size. If this key is omitted, the System Preferences app looks for the image file using the `CFBundleIconFile` key instead.

`NSPrefPaneIconLabel` (`String` - macOS). This key contains a string with the name of a preference pane. This string is displayed below the preference pane’s icon in the System Preferences app. You can split long names onto two lines by including a newline character (‘\n’) in the string. If this key is omitted, the System Preferences app gets the name from the `CFBundleName` key.

This key can be localized and included in the `InfoPlist.strings` files of a bundle.

`NSPrincipalClass` (`String` - macOS). This key contains a string with the name of a bundle’s principal class. This key is used to identify the entry point for dynamically loaded code, such as plug-ins and other dynamically-loaded bundles. The principal class of a bundle typically controls all other classes in the bundle and mediates between those classes and any classes outside the bundle. The class identified by this value can be retrieved using the `principalClass` method of `NSBundle`. For Cocoa apps, the value for this key is `NSApplication` by default.

`NSRemindersUsageDescription` (`String` - iOS) This key lets you describe the reason your app accesses the user’s reminders. When the system prompts the user to allow access, this string is displayed as part of the alert.

This key is supported in iOS 6.0 and later.

`NSServices` (`Array` - macOS). This key contains an array of dictionaries specifying the services provided by the app. Table 4 lists the keys for specifying a service:

__Table 4__  Keys for NSServices dictionaries

| Key | Xcode name | Type | Description | Platforms |
| __NSPortName__ | “Incoming service port name” | `String` | This key specifies the name of the port your app monitors for incoming service requests. Its value depends on how the service provider app is registered. In most cases, this is the app name. For more information, see _[Services Implementation Guide](../../Cocoa/Services%20Implementation%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydc2i)_. | macOS |
| __NSMessage__ | “Instance method name” | `String` | This key specifies the name of the instance method to invoke for the service. In Objective-C, the instance method must be of the form `messageName:userData:error:`. In Java, the instance method must be of the form `messageName(NSPasteBoard,String)`. | macOS |
| __NSSendFileTypes__ | (none) | `Array` | This key specifies an array of strings. Each string should contain a UTI defining a supported file type. Only UTI types are allowed; pasteboard types are not permitted. To specify pasteboard types, continue to use the `NSSendTypes` key.  By assigning a value to this key, your service declares that it can operate on files whose type conforms to one or more of the given file types. Your service will receive a pasteboard from which you can read file URLs.  Available in OS X v10.6 and later. For information on UTIs, see _[Uniform Type Identifiers Overview](../../File%20Management/Uniform%20Type%20Identifiers%20Overview/Introduction%20to%20Uniform%20Type%20Identifiers%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgmjz)_. | macOS |
| __NSSendTypes__ | “Send Types” | `Array` | This key specifies an optional array of data type names that can be read by the service. The `NSPasteboard` class description lists several common data types. You must include this key, the `NSReturnTypes` key, or both.  In OS X v10.5 and earlier, this key is required. In OS X v10.6 and later, you should use the `NSSendFileTypes` key instead. | macOS |
| __NSServiceDescription__ | (none) | `String` | This key specifies a description of your service that is suitable for presentation to users. This description string may be long to give users adequate information about your service.  To localize the menu item text, create a `ServicesMenu.strings` file for each localization in your bundle. This strings file should contain this key along with the translated description string as its value. For more information about creating strings files, see _[Resource Programming Guide](../../Cocoa/Resource%20Programming%20Guide/About%20Resources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tc2i)_.  Available in OS X v10.6 and later. | macOS |
| __NSRequiredContext__ | (none) | `Dictionary` or `Array` | This key specifies a dictionary with the conditions under which your service is made available to the user. Alternatively, you can specify an array of dictionaries, each of which contains a set of conditions for enabling your service.  See the discussion after this table for information about specifying the value of this key. Available in OS X v10.6 and later. | macOS |
| __NSRestricted__ | (none) | `Boolean` | Specifying a value of `YES` for this key prevents the service from being invoked by a sandboxed app. You should set the value to `YES` if your service performs privileged or potentially dangerous operations that would allow a sandboxed app to escape its containment. For example, you should set it to `YES` if your service executes arbitrary files or text strings as scripts, reads or writes any file specified by a path, or retrieves the contents of an arbitrary URL from the network on behalf of the client of the service.  The default value for this key is `false`. Available in OS X v10.7 and later. | macOS |
| __NSReturnTypes__ | “Return Types” | `Array` | This key specifies an array of data type names that can be returned by the service. The `NSPasteboard` class description lists several common data types. You must include this key, the `NSSendTypes` key, or both. | macOS |
| __NSMenuItem__ | “Menu” | `Dictionary` | This key contains a dictionary that specifies the text to add to the Services menu. The only key in the dictionary is called `default` and its value is the menu item text.  In OS X v10.5 and earlier, menu items must be unique. You can ensure a unique name by combining the app name with the command name and separating them with a slash character “`/`”. This effectively creates a submenu for your services. For example, `Mail/Send` would appear in the Services menu as a menu named Mail with an item named Send.  Submenus are not supported (or necessary) in OS X v10.6 and later. If you specify a slash character in OS X v10.6 and later, the slash and any text preceding it are discarded. Instead, services with the same name are disambiguated by adding the app name in parenthesis after the menu item text.  To localize the menu item text, create a `ServicesMenu.strings` file for each localization in your bundle. This strings file should contain the `default` key along with the translated menu item text as its value. For more information about creating strings files, see _[Resource Programming Guide](../../Cocoa/Resource%20Programming%20Guide/About%20Resources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tc2i)_. | macOS |
| __NSKeyEquivalent__ | “Menu key equivalent” | `Dictionary` | This key is optional and contains a dictionary with the keyboard equivalent used to invoke the service menu command. Similar to `NSMenuItem`, the only key in the dictionary is called `default` and its value is a single character. Users invoke this keyboard equivalent by pressing the Command modifier key along with the character. The character is case sensitive, so you can assign different commands to the uppercase and lowercase versions of a character. To specify the uppercase character, the user must press the Shift key in addition to the other keys. | macOS |
| __NSUserData__ | “User Data” | `String` | This key is an optional string that contains a value of your choice. | macOS |
| __NSTimeout__ | “Timeout value (in milliseconds)” | `String` | This key is an optional numerical string that indicates the number of milliseconds Services should wait for a response from the app providing a service when a response is required. | macOS |

In OS X v10.6 and later, the `NSRequiredContext` key may contain a dictionary or an array of dictionaries describing the conditions under which the service appears in the Services menu. If you specify a single dictionary, all of the conditions in that dictionary must be met for the service to appear. If you specify an array of dictionaries, all of the conditions in only one of those dictionaries must be met for the service to appear. Each dictionary may contain one or more of the keys listed in Table 5. All keys in the dictionary are optional.

__Table 5__  Contents of the `NSRequiredContext` dictionary

| Key | Xcode name | Type | Description | Platform |
| __NSApplicationIdentifier__ | (none) | `String` or `Array` | The value of this key is a string or an array of strings, each of which contains the bundle ID (`CFBundleIdentifier` key) of an app. Your service appears only if the bundle ID of the current app matches one of the specified values. | macOS |
| __NSTextScript__ | (none) | `String` or `Array` | The value of this key is a string or an array of strings, each of which contains a standard four-letter script tag, such as `Latn` or `Cyrl`. Your service appears only if the dominant script of the selected text matches one of the specified script values. | macOS |
| __NSTextLanguage__ | (none) | `String` or `Array` | The value of this key is a string or an array of strings, each of which contains a BCP-47 tag indicating the language of the desired text. Your service appears if the overall language of the selected text matches one of the specified values.  Matching is performed using a prefix-matching scheme. For example, specifying the value en matches text whose full BCP-47 code is `en-US`, `en-GB`, or `en-AU`. | macOS |
| __NSWordLimit__ | (none) | `Number` | The value of this key is an integer indicating the maximum number of selected words on which the service can operate. For example, a service to look up a stock by ticker symbol might have a value of 1 because ticker symbols cannot contain spaces. | macOS |
| __NSTextContext__ | (none) | `String` or `Array` | The value of this key is a string or an array of strings, each of which contains one of the following values: `URL`, `Date`, `Address`, `Email`, or `FilePath`. The service is displayed only if the selected text contains data of a corresponding type. For example, if the selected text contained an HTTP-based link, the service would be displayed if the value of this key were set to `URL`.  Note that all of the selected text is provided to the service-vending app, not just the parts found to contain the given data types. | macOS |

For additional information about implementing services in your app, see _[Services Implementation Guide](../../Cocoa/Services%20Implementation%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydc2i)_.

NSSiriUsageDescription (`String` - iOS) This key lets you describe the reason your app sends user data to Siri. The first time that your app explicitly requests access to Siri, the system displays this string as part of the alert. If the user’s first interaction with your app occurs in Siri itself, a default string may be used instead.

NSSpeechRecognitionUsageDescription (`String` - iOS) This key lets you describe the reason your app sends user data to Apple’s speech recognition servers. When the system prompts the user to allow access, this string is displayed as part of the alert.

`NSSupportsAutomaticTermination` (`Boolean` - macOS). This key contains a Boolean value that indicates whether the app supports automatic termination in OS X v10.7 and later. Automatic termination allows an app that is running to be terminated automatically by the system when certain conditions apply. Primarily, the app can be terminated when it is hidden or does not have any visible windows and is not currently being used. The system may terminate such an app in order to reclaim the memory used by the app.

An app may programmatically disable and reenable automatic termination support using the `disableAutomaticTermination` and `enableAutomaticTermination` methods of `NSProcessInfo`. The app might do this to prevent being terminated during a critical operation.

`NSSupportsPurgeableLocalStorage` (`Boolean` - iOS). This key contains a Boolean value that indicates whether the app is designed to work, without disruption to the user, with the local data container treated as a volatile cache by the system. The default value of this key is `NO`. If your app supports Shared iPad (a feature of iOS device management), set this key’s value to `YES`.

When set to `YES`, the system is enabled to purge local storage, at the system’s discretion, when the user is logged out.

Supporting Shared iPad entails different work depending on where your app chooses to store nonlocal user data, as follows:

- User data stored in iCloud is automatically restored by the system, as needed.
- Nonlocal user data that is _not_ stored in iCloud must be restored explicitly, by your app, from the app’s non-iCloud service.

If your app uses only local storage and does not depend on its persistence (for example, a simple calculator app), you can declare support for Shared iPad by setting this key’s value to `YES`.

`NSSupportsSuddenTermination` (`Boolean` - macOS). This key contains a Boolean value that indicates whether the system may kill the app outright in order to log out or shut down more quickly. Use this key to specify whether the app can be killed immediately after launch. The app can still enable or disable sudden termination at runtime using the methods of the [NSProcessInfo](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSProcessInfo/Description.html#//apple_ref/occ/cl/NSProcessInfo) class. The default value of this key is `NO`.

`NSUbiquitousContainers` (`Dictionary` - iOS and macOS) Specifies the iCloud Drive settings for each container. This dictionary’s keys are the container identifiers for your app’s iCloud containers. The values are dictionaries containing the `NSUbiquitousContainerIsDocumentScopePublic`, `NSUbiquitousContainerName` and `NSUbiquitousContainerSupportedFolderLevels` entries for each container. You must specify the sharing permissions separately for each container.

`NSUbiquitousContainerIsDocumentScopePublic` (`Boolean` - iOS and macOS) Specifies whether the iCloud drive should share the contents of this container. Defaults to `NO`.

`NSUbiquitousContainerName` (`String` - iOS and macOS) Specifies the name that the iCloud Drive displays for your container. By default, the iCloud Drive will use the name of the bundle that owns the container.

`NSUbiquitousContainerSupportedFolderLevels` (`String` - iOS and macOS) Specifies the maximum number of folder levels inside your container’s Documents directory. This key can take three different values:

- `None`

  The iCloud Drive only has access to the container’s Documents directory. Your app promises that it does not create any directories inside the Document’s directory. In macOS, the Finder prevents users from creating subdirectories inside your iCloud Drive directory.
- `One`

  The iCloud Drive has access to the container’s Documents directory and one additional layer of subdirectories. Your app promises that it only creates a single layer of directories inside the Documents directory. In macOS, the Finder prevents users from creating more than one layer of subdirectories inside your iCloud Drive directory.
- `Any`

  The iCloud Drive has complete access to your container’s Documents directory. Both your app and the Finder can create as many layers of subdirectories as you (or the user) desire.

`NSUbiquitousDisplaySet` (`String` - iOS, macOS) contains the identifier string that you configured in iTunesConnect for managing your app’s storage. The assigned display set determines from which mobile data folder (in the user’s mobile account) the app retrieves its data files.

If you create multiple apps, you can use the same display set for your apps or assign different display sets to each. For example, if you create a “lite” version of your app, in addition to a full-featured version, you might use the same display set for both versions because they create and use the same basic data files. Each app should recognize the file types stored in its mobile data folder and be able to open them.

`NSUserActivityTypes` (Array of strings - iOS and macOS) Specifies the user activity types that the app supports. This key is valid in iOS 8 and macOS 10.10 and later.

`NSUserNotificationAlertStyle` (`String` - macOS) specifies the notification style the app should use. The default value, `banner`, is recommended; most apps should not need to use the `alert` style.

NSVideoSubscriberAccountUsageDescription (`String` - tvOS). This key lets you describe the reason your app access the user’s TV provider account. When the system prompts the user to allow access, this string is displayed as part of the alert.

`UTExportedTypeDeclarations` (`Array` - iOS, macOS) declares the uniform type identifiers (UTIs) owned and exported by the app. You use this key to declare your app’s custom data formats and associate them with UTIs. Exporting a list of UTIs is the preferred way to register your custom file types; however, Launch Services recognizes this key and its contents only in OS X v10.5 and later. This key is ignored on versions of OS X prior to version 10.5.

The value for the `UTExportedTypeDeclarations` key is an array of dictionaries. Each dictionary contains a set of key-value pairs identifying the attributes of the type declaration. Table 6 lists the keys you can include in this dictionary along with the typical values they contain. These keys can also be included in array of dictionaries associated with the [UTImportedTypeDeclarations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvooi) key.

__Table 6__  UTI property list keys

| Key | Xcode name | Type | Description | Platforms |
| __UTTypeConformsTo__ | “Conforms to UTIs” | `Array` | (Required) Contains an array of strings. Each string identifies a UTI to which this type conforms. These keys represent the parent categories to which your custom file format belongs. For example, a JPEG file type conforms to the `public.image` and `public.data` types. For a list of high-level types, see _[Uniform Type Identifiers Overview](../../File%20Management/Uniform%20Type%20Identifiers%20Overview/Introduction%20to%20Uniform%20Type%20Identifiers%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgmjz)_. | iOS, macOS |
| __UTTypeDescription__ | “Description” | `String` | A user-readable description of this type. The string associated with this key may be localized in your bundle’s `InfoPlist.strings` files. | iOS, macOS |
| __UTTypeIconFile__ | “Icon file name” | `String` | The name of the bundle icon resource to associate with this UTI. You should include this key only for types that your app exports. This file should have a `.icns` filename extension. You can create this file using the Icon Composer app that comes with Xcode Tools. | macOS |
| __UTTypeIdentifier__ | “Identifier” | `String` | (Required) The UTI you want to assign to the type. This string uses the reverse-DNS format, whereby more generic types come first. For example, a custom format for your company would have the form `com.<yourcompany>.<type>.<subtype>`. | iOS, macOS |
| __UTTypeReferenceURL__ | “Reference URL” | `String` | The URL for a reference document that describes this type. | macOS |
| __UTTypeTagSpecification__ | “Equivalent Types” | `Dictionary` | (Required) A dictionary defining one or more equivalent type identifiers. The key-value pairs listed in this dictionary identify the filename extensions, MIME types, OSType codes, and pasteboard types that correspond to this type. For example, to specify filename extensions, you would use the key `public.filename-extension` and associate it with an array of strings containing the actual extensions. For more information about the keys for this dictionary, see _[Uniform Type Identifiers Overview](../../File%20Management/Uniform%20Type%20Identifiers%20Overview/Introduction%20to%20Uniform%20Type%20Identifiers%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgmjz)_. | iOS, macOS |

The way you specify icon files in macOS and iOS is different because of the supported file formats on each platform. In iOS, each icon resource file is typically a PNG file that contains only one image. Therefore, it is necessary to specify different image files for different icon sizes. However, when specifying icons in macOS, you use an icon file (with extension `.icns`), which is capable of storing the icon at several different resolutions.

This key is supported in iOS 3.2 and later and in OS X v10.5 and later. For more information about UTIs and their use, see _[Uniform Type Identifiers Overview](../../File%20Management/Uniform%20Type%20Identifiers%20Overview/Introduction%20to%20Uniform%20Type%20Identifiers%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgmjz)_.

`UTImportedTypeDeclarations` (`Array` - iOS, macOS) declares the uniform type identifiers (UTIs) inherently supported (but not owned) by the app. You use this key to declare any supported types that your app recognizes and wants to ensure are recognized by Launch Services, regardless of whether the app that owns them is present. For example, you could use this key to specify a file format that is defined by another company but which your program can read and export.

The value for this key is an array of dictionaries and uses the same keys as those for the [UTExportedTypeDeclarations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvooa) key. For a list of these keys, see [Table 6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomjq).

This key is supported in iOS 3.2 and later and in OS X v10.5 and later. For more information about UTIs and their use, see _[Uniform Type Identifiers Overview](../../File%20Management/Uniform%20Type%20Identifiers%20Overview/Introduction%20to%20Uniform%20Type%20Identifiers%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgmjz)_.

[Next](macOS%20Keys.md)[Previous](Launch%20Services%20Keys.md)

