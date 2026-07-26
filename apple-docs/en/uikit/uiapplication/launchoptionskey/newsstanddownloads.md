---
title: newsstandDownloads
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+（26.0 起废弃）, iPadOS 5.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiapplication/launchoptionskey/newsstanddownloads
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/launchoptionskey/newsstanddownloads'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/launchoptionskey/newsstanddownloads.json'
content_hash: 'sha256:e5fa535f0221e099'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIApplication](../../uiapplication.md) · [LaunchOptionsKey](../launchoptionskey.md)

# newsstandDownloads

<sub>Type Property</sub>

A key indicating that the app was launched to process newly downloaded Newsstand assets.

> [!warning] Deprecated
> This dictionary key is no longer used.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static let newsstandDownloads: UIApplication.LaunchOptionsKey
```

## Discussion

The value of this key is an array of string identifiers that identify the `NKAssetDownload` objects corresponding to the assets. Although you can use the identifiers for cross-checking purposes, you should obtain the definitive array of `NKAssetDownload` objects (representing asset downloads in progress or in error) through the `downloadingAssets` property of the `NKLibrary` object representing the Newsstand app’s library.

## See Also

### Accessing launch options

- [UIApplicationLaunchOptionsBluetoothCentralsKey](bluetoothcentrals.md) — A key indicating that the app was relaunched to handle Bluetooth-related events. _(deprecated)_
- [UIApplicationLaunchOptionsBluetoothPeripheralsKey](bluetoothperipherals.md) — A key indicating that the app should continue actions associated with its Bluetooth peripheral objects. _(deprecated)_
- [UIApplicationLaunchOptionsCloudKitShareMetadataKey](cloudkitsharemetadata.md) — A key indicating that the app received a CloudKit share invitation. _(deprecated)_
- [UIApplicationLaunchOptionsEventAttributionKey](eventattribution.md) — UserInfo contains a [UIEventAttribution](../../uieventattribution.md) to go along with a URL open on launch _(deprecated)_
- [UIApplicationLaunchOptionsLocationKey](location.md) — A key indicating that the app was launched to handle an incoming location event. _(deprecated)_
- [UIApplicationLaunchOptionsRemoteNotificationKey](remotenotification.md) — A key indicating that a remote notification is available for the app to process. _(deprecated)_
- [UIApplicationLaunchOptionsShortcutItemKey](shortcutitem.md) — A key indicating that the app was launched in response to the user selecting a Home screen quick action. _(deprecated)_
- [UIApplicationLaunchOptionsSourceApplicationKey](sourceapplication.md) — A key indicating that another app requested the launch of your app. _(deprecated)_
- [UIApplicationLaunchOptionsURLKey](url.md) — A key indicating that the app was launched so that it could open the specified URL. _(deprecated)_
- [UIApplicationLaunchOptionsUserActivityDictionaryKey](useractivitydictionary.md) — A key indicating a dictionary associated with an activity that the user wants to continue. _(deprecated)_
- [UIApplicationLaunchOptionsUserActivityTypeKey](useractivitytype.md) — A key indicating the type of user activity that the user wants to continue. _(deprecated)_
- [UIApplicationLaunchOptionsAnnotationKey](annotation.md) — A key indicating that the URL passed to your app contained custom annotation data from the source app. _(deprecated)_
- [UIApplicationLaunchOptionsLocalNotificationKey](localnotification.md) — A key indicating that the app was launched to handle a local notification. _(deprecated)_
