---
title: Information Property List Key Reference
apple_id: TP40009247
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: General
technology: null
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/watchOSKeys.html
archived_at: '2026-07-15T07:34:59.466140Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Information Property List Key Reference](About%20Info.plist%20Keys%20and%20Values.md)


[Next](App%20Extension%20Keys.md)[Previous](iOS%20Keys.md)

# watchOS Keys

The watchOS frameworks provide the infrastructure you need for creating Watch apps. You use the keys associated with this framework to configure your Watch app and WatchKit extension.

Table 1 contains an alphabetical listing of watchOS keys, the corresponding name for that key in the Xcode property list editor, a high-level description of each key, and the platforms on which you use it. Detailed information about each key is available in later sections.

__Table 1__  Summary of watchOS keys

| Key | Xcode name | Summary | Availability |
| CLKComplicationSupportedFamilies | None | Specifies the complication families for which the app can provide data. See [CLKComplicationSupportedFamilies](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojyfvjvona) for details. | watchOS 2.0 and later |
| CLKComplicationPrincipalClass | None | Specifies the name of the class that implements the complication data source protocol. See [CLKComplicationPrincipalClass](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojyfvjvoni) for details. | watchOS 2.0 and later |
| PUICAutoLaunchAudioOptOut | “Opt out of Auto-launch Audio App” | Allows an Apple Watch audio app to opt out of auto-launch when its corresponding iOS app starts playing audio. See `[PUICAutoLaunchAudioOptOut](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojyfvjvomjr)` for details. | watchOS 5.0 and later |
| WKAppBundleIdentifier | None | Specifies the bundle ID of the Watch app. See [WKAppBundleIdentifier](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojyfvjvooa) for details. | watchOS 1.0 and later |
| WKBackgroundModes | None | Provides execution time, for a WatchKit extension running in the background, to update UI values in its app or to perform view navigation for workout processing. See [WKBackgroundModes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojyfvjvomjq) for details. | watchOS 3.0 and later |
| WKCompanionAppBundleIdentifier | None | Specifies the bundle ID of the companion iOS app. See [WKCompanionAppBundleIdentifier](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojyfvjvooi) for details. | watchOS 1.0 and later |
| WKExtensionDelegateClassName | None | Specifies the name of the class that manages lifecycle events for the WatchKit extension. See [WKExtensionDelegateClassName](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojyfvjvonq) for details. | watchOS 2.0 and later |
| WKWatchKitApp | None | Specifies a Boolean indicating whether the app is the launchable Watch app. See [WKWatchKitApp](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojyfvjvony) for details. | watchOS 1.0 and later |

`CLKComplicationSupportedFamilies` (`Array` - watchOS) contains an array of strings, each of which represents the name of a complication family. Family names include `CLKComplicationFamilyModularSmall`, `CLKComplicationFamilyModularLarge`, `CLKComplicationFamilyUtilitarianSmall`, `CLKComplicationFamilyUtilitarianLarge`, `CLKComplicationFamilyCircular`. A WatchKit extension that implements a complication includes this key to let watchOS know which families it supports.

This key applies to the WatchKit extension only and you do not need to configure it manually. Xcode configures it automatically using the complications configuration settings of your WatchKit extension target.

This key is supported in watchOS 2.0 and later.

`CLKComplicationPrincipalClass` (`String` - watchOS) specifies the name of the class that acts as the complication data source. The specified class must implement the [CLKComplicationDataSource](https://developer.apple.com/documentation/clockkit/clkcomplicationdatasource) protocol.

This key applies to the WatchKit extension only and you do not need to configure it manually. Xcode configures it automatically using the complications configuration settings of your WatchKit extension target.

This key is supported in watchOS 2.0 and later.

`PUICAutoLaunchAudioOptOut` (`Boolean` - watchOS) By default, an audio app on Apple Watch automatically launches when its corresponding iOS app starts playing audio content. This lets the Watch app prepare its user interface. When the user looks at their Watch, the Watch app is displayed, allowing the user to control the audio on the iPhone. This key lets apps opts out of this feature. In Xcode, the info plist editor shows this string: ‘Opt out of Auto-launch Audio App’.

This key is supported in watchOS 5.0 and later.

`WKAppBundleIdentifier` (`String` - watchOS) specifies the bundle identifier of the Watch app that works with the WatchKit extension. Xcode adds this key to your Watch app’s `Info.plist` file automatically.

Apart from the addition of the `.watchkitapp` string, the bundle identifier of the Watch app must match the bundle identifier of the iOS app. (The bundle identifier of the WatchKit extension must also be based on the bundle identifier of the iOS app.) The system does not launch a Watch app whose bundle identifier does not match the bundle identifier of its WatchKit extension or iOS app.

This key applies to the WatchKit extension only and you do not need to configure it manually. Xcode adds it to the `[NSExtensionAttributes](AppExtensionKeys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomjr)` dictionary of the WatchKit extension. If you change the bundle identifier of your iOS app, you must change the value of this key to match.

This key is supported in watchOS 1.0 and later.

`WKBackgroundModes` (`Array` - watchOS) provides execution time, for a WatchKit extension running in the background, to update UI values in its app or to perform view navigation, for workout processing.

The one allowed value for this key is `workout-processing`.

See also the audio key description in [UIBackgroundModes](iOS%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjsfvjvomrs).

This key is supported in watchOS 3.0 and later.

`WKCompanionAppBundleIdentifier` (`String` - watchOS) specifies the bundle identifier of the iOS app with which the Watch app is paired. Xcode adds this key to your Watch app’s `Info.plist` file automatically.

This key applies to the Watch app only and you do not need to configure it manually. Xcode configures it automatically when you create the targets for your Watch app.

This key is supported in watchOS 1.0 and later.

`WKExtensionDelegateClassName` (`String` - watchOS) specifies the name of the class that acts as the delegate for the [WKExtension](https://developer.apple.com/documentation/watchkit/wkextension) object in a WatchKit extension. The specified class must implement the [WKExtensionDelegate](https://developer.apple.com/documentation/watchkit/wkextensiondelegate) protocol. The class you specify is instantiated automatically at launch time by WatchKit and assigned to the extension object. You do not have to instantiate this class yourself.

This key applies to the WatchKit extensions only. Xcode configures this key automatically when you create the targets for your Watch app. If you change the class of your extension delegate, you can modify the value.

This key is supported in watchOS 2.0 and later.

`WKWatchKitApp` (`BOOL` - watchOS) specifies whether the bundle is the Watch app that the user launches. The Watch app relies on its matching WatchKit extension for any runtime behavior. Xcode adds this key to your Watch app’s `Info.plist` file automatically.

This key applies to the Watch app only and you do not need to configure it manually. Xcode configures it automatically when you create the targets for your Watch app.

This key is supported in watchOS 1.0 and later.

[Next](App%20Extension%20Keys.md)[Previous](iOS%20Keys.md)

