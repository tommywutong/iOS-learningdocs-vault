---
title: eventAttribution
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.5+（26.0 起废弃）, iPadOS 14.5+（26.0 起废弃）, Mac Catalyst 14.5+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiapplication/launchoptionskey/eventattribution
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/launchoptionskey/eventattribution'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/launchoptionskey/eventattribution.json'
content_hash: 'sha256:dd587e0f340c6172'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIApplication](../../uiapplication.md) · [LaunchOptionsKey](../launchoptionskey.md)

# eventAttribution

<sub>Type Property</sub>

UserInfo contains a [UIEventAttribution](../../uieventattribution.md) to go along with a URL open on launch

> [!warning] Deprecated
> Use UIScene lifecycle and UIScene.ConnectionOptions.eventAttribution instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static let eventAttribution: UIApplication.LaunchOptionsKey
```

## See Also

### Accessing launch options

- [UIApplicationLaunchOptionsBluetoothCentralsKey](bluetoothcentrals.md) — A key indicating that the app was relaunched to handle Bluetooth-related events. _(deprecated)_
- [UIApplicationLaunchOptionsBluetoothPeripheralsKey](bluetoothperipherals.md) — A key indicating that the app should continue actions associated with its Bluetooth peripheral objects. _(deprecated)_
- [UIApplicationLaunchOptionsCloudKitShareMetadataKey](cloudkitsharemetadata.md) — A key indicating that the app received a CloudKit share invitation. _(deprecated)_
- [UIApplicationLaunchOptionsLocationKey](location.md) — A key indicating that the app was launched to handle an incoming location event. _(deprecated)_
- [UIApplicationLaunchOptionsNewsstandDownloadsKey](newsstanddownloads.md) — A key indicating that the app was launched to process newly downloaded Newsstand assets. _(deprecated)_
- [UIApplicationLaunchOptionsRemoteNotificationKey](remotenotification.md) — A key indicating that a remote notification is available for the app to process. _(deprecated)_
- [UIApplicationLaunchOptionsShortcutItemKey](shortcutitem.md) — A key indicating that the app was launched in response to the user selecting a Home screen quick action. _(deprecated)_
- [UIApplicationLaunchOptionsSourceApplicationKey](sourceapplication.md) — A key indicating that another app requested the launch of your app. _(deprecated)_
- [UIApplicationLaunchOptionsURLKey](url.md) — A key indicating that the app was launched so that it could open the specified URL. _(deprecated)_
- [UIApplicationLaunchOptionsUserActivityDictionaryKey](useractivitydictionary.md) — A key indicating a dictionary associated with an activity that the user wants to continue. _(deprecated)_
- [UIApplicationLaunchOptionsUserActivityTypeKey](useractivitytype.md) — A key indicating the type of user activity that the user wants to continue. _(deprecated)_
- [UIApplicationLaunchOptionsAnnotationKey](annotation.md) — A key indicating that the URL passed to your app contained custom annotation data from the source app. _(deprecated)_
- [UIApplicationLaunchOptionsLocalNotificationKey](localnotification.md) — A key indicating that the app was launched to handle a local notification. _(deprecated)_
