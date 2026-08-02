---
title: Information Property List Key Reference
apple_id: TP40009247
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: General
technology: null
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/RevisionHistory.html
archived_at: '2026-07-15T07:34:59.492390Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Information Property List Key Reference](About%20Info.plist%20Keys%20and%20Values.md)


[Previous](App%20Extension%20Keys.md)

# Document Revision History

This table describes the changes to _Information Property List Key Reference_.

| __Date__ | __Notes__ |
| 2018-06-04 | Revisions to various property list keys, including armv7 and arm64. |
| 2018-01-25 | Add information about the UIAppSupportsHDR key for tvOS. |
| 2017-11-06 | Updated the nfc UIRequiredDeviceCapabilities key and the CFBundleIconName Core Foundation key documentation. |
| 2017-09-12 | Described the arkit and nfc UIRequiredDeviceCapabilities keys. Described the CFBundleIconName Core Foundation key. |
| 2017-06-22 | Updated watchOS keys. Added keys for the document browser and the File Provider extension. |
| 2017-06-08 | Added new SiriKit keys for specifying app synonyms. |
| 2017-03-27 | Added information about the CFBundleAlternateIcons key and the launch storyboard keys. |
|  | For the [NSAppTransportSecurity](Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomzt) key, added a new section: [Supporting Older Operating Systems](Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonry). |
| 2016-11-14 | Corrected the App Transport Security key name for media loads, to NSAllowsArbitraryLoadsForMedia. |
| 2016-10-27 | Updated guidance in [App Store Review for ATS](Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonjz). |
| 2016-09-13 | Added keys for providing purpose strings for accessing user data or device resources: [NSAppleMusicUsageDescription](Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonbx), [NSHomeKitUsageDescription](Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonjq), [NSSiriUsageDescription](Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonjr), [NSSpeechRecognitionUsageDescription](Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonjs), and [NSVideoSubscriberAccountUsageDescription](Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonjt). |
|  | Throughout the [Cocoa Keys](Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomi) chapter, added warnings to all purpose string (`…UsageDescription`) keys explaining that, to support user privacy, you must statically declare your intent to use protected resources. |
|  | Added a description for the iOS keys [CoreSpotlightContinuation](iOS%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjsfvjvonbt), [UIWhitePointAdaptivityStyle](iOS%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjsfvjvomzr), and [UIApplicationShortcutWidget](iOS%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjsfvjvomzs). |
|  | Added descriptions for four [NSAppTransportSecurity](Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomzt) subkeys: `NSAllowsArbitraryLoadsInMedia`, `NSAllowsArbitraryLoadsInWebContent`, `NSAllowsLocalNetworking`, and `NSRequiresCertificateTransparency`. Also expanded and clarified the description of the NSAppTransportSecurity key. |
|  | Removed all mention of the following third-party-server exception keys from the description for the [NSAppTransportSecurity](Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomzt) key; Apple no longer expects apps to specify any of them: `NSThirdPartyExceptionAllowsInsecureHTTPLoads`, `NSThirdPartyExceptionRequiresForwardSecrecy`, `NSThirdPartyExceptionMinimumTLSVersion`. |
|  | Added a note in the See Also section, in [About Info.plist Keys and Values](About%20Info.plist%20Keys%20and%20Values.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbyfvjvomi), describing keys specific to kernel extension development. |
|  | Clarified the guidance for use of the [CFBundleShortVersionString](Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgeytgnbz) and [NSHomeKitUsageDescription](Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonjq) keys. |
|  | Corrected the information about language IDs for the [CFBundleDevelopmentRegion](Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgmydimzq) key. |
|  | Added the [Safari App Extension Keys](App%20Extension%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomzy) section to the [App Extension Keys](App%20Extension%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomi) chapter. |
|  | Added listing of two tvOS app extension keys, `com.apple.broadcast-services` and `com.apple.tv-services`, in [Table 2](App%20Extension%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvoni). |
|  | Added description for the [WKBackgroundModes](watchOS%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojyfvjvomjq) key, as well as watchOS information for the `audio` subkey of the [UIBackgroundModes](iOS%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjsfvjvomrs) key. |
|  | Added description for the [UIUserInterfaceStyle](iOS%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjsfvjvonbu) key for tvOS. |
|  | Added description for the [GCSupportsMultipleMicroGamepads](Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonrw) key for tvOS and for the [GCSupportedGameControllers](Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonrx) key for tvOS, iOS, and macOS. |
|  | Renamed the “OS X Keys” chapter to [macOS Keys](macOS%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjtfvjvomi). |
| 2016-03-01 | Added a description for the [NSSupportsPurgeableLocalStorage](Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonbv) key for declaring support for Shared iPad, a feature of iOS device management. |
|  | Added a description for the [NETestAppMapping](Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonbw) key for testing and development of per-app VPN app extensions. |
| 2015-12-08 | Improved and expanded the guidance for the [NSAppTransportSecurity](Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomzt) (App Transport Security) key. |
| 2015-10-21 | Added descriptions for the keys for configuring App Transport Security (ATS). See the [NSAppTransportSecurity](Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomzt) section. |
|  | Added information, in the [CFBundleIcons](Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbzfvjvomjt) section, about use of icon files in tvOS. |
| 2015-09-16 | Added descriptions for the [UIApplicationShortcutItems](iOS%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjsfvjvomzw) key, and related keys, for specifying static Home screen quick actions on devices that support 3D Touch. |
|  | Added a description for the [LSSupportsOpeningDocumentsInPlace](Launch%20Services%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjqfvjvomjt) Launch Services key. |
| 2015-08-25 | Added a new chapter: [watchOS Keys](watchOS%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojyfvjvomi). |
|  | Updated guidance in the [Creating Platform- and Device-Specific Keys](About%20Information%20Property%20List%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjufvjvooi) section. |
|  | Added information about the [LSApplicationQueriesSchemes](Launch%20Services%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjqfvjvomju) key, which lets you specify the URL schemes an app is able to test with the [canOpenURL:](https://developer.apple.com/documentation/uikit/uiapplication/1622952-canopenurl) method. |
|  | Updated the description of the [CFBundleURLTypes](Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgazdembx) key to mention its relationship with the LSApplicationQueriesSchemes key. |
| 2015-03-09 | Added the [NSExtensionPointIdentifier](App%20Extension%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomjv) string for a WatchKit App extension. |
| 2014-09-17 | Added new keys introduced in iOS 8. |
| 2014-02-11 | Added the opengles-3 key for required device capabilities. |
| 2013-09-18 | Added OS X v10.9 availability for NSLocationUsageDescription. |
|  | Added keys introduced in iOS 7. |
| 2012-09-19 | Added keys related to the configuration of an app to support 3rd party map directions and keys related to user privacy. |
| 2012-02-16 | Added info to CFBundleURLTypes regarding RSS feeds. |
| 2011-10-12 | Added a new value to the UIRequiredDeviceCapabilities key to reflect support for low-power Bluetooth hardware. |
|  | Incorporates keys introduced in iOS 5.0. |
| 2011-06-06 | Added information about key support in OS X v10.7. |
| 2010-11-15 | Corrected the availability of the LSMinimumSystemVersion and MinimumOSVersion keys. |
| 2010-08-20 | Fixed some typographical errors. |
| 2010-07-08 | Changed references of iOS to iOS. |
| 2010-06-14 | Added new keys introduced in iOS 4.0. |
| 2010-03-23 | Added keys specific to iOS 3.2. |
|  | Removed the `LSHasLocalizedDisplayName` key, which was deprecated in OS X v10.2. |
| 2009-10-19 | New document describing the keys you can use in a bundle's Info.plist file. |

[Previous](App%20Extension%20Keys.md)

