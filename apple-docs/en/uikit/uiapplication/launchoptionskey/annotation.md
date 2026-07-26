---
title: annotation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.2+（16.0 起废弃）, iPadOS 3.2+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, tvOS（16.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiapplication/launchoptionskey/annotation
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/launchoptionskey/annotation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/launchoptionskey/annotation.json'
content_hash: 'sha256:3749816fd7a78b0e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIApplication](../../uiapplication.md) · [LaunchOptionsKey](../launchoptionskey.md)

# annotation

<sub>Type Property</sub>

A key indicating that the URL passed to your app contained custom annotation data from the source app.

> [!warning] Deprecated
> The system doesn’t use this key.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
static let annotation: UIApplication.LaunchOptionsKey
```

## Discussion

The presence of this key indicates that custom data was provided by the app that requested the opening of the URL. The value of this key is a property-list object containing the custom data. The same object is also passed to the annotation parameter of the  [- application:openURL:sourceApplication:annotation:](<../../uiapplicationdelegate/application(__open_sourceapplication_annotation_).md>) method. The contents of this property-list object are specific to the app that made the request.

## See Also

### Accessing launch options

- [UIApplicationLaunchOptionsBluetoothCentralsKey](bluetoothcentrals.md) — A key indicating that the app was relaunched to handle Bluetooth-related events. _(deprecated)_
- [UIApplicationLaunchOptionsBluetoothPeripheralsKey](bluetoothperipherals.md) — A key indicating that the app should continue actions associated with its Bluetooth peripheral objects. _(deprecated)_
- [UIApplicationLaunchOptionsCloudKitShareMetadataKey](cloudkitsharemetadata.md) — A key indicating that the app received a CloudKit share invitation. _(deprecated)_
- [UIApplicationLaunchOptionsEventAttributionKey](eventattribution.md) — UserInfo contains a [UIEventAttribution](../../uieventattribution.md) to go along with a URL open on launch _(deprecated)_
- [UIApplicationLaunchOptionsLocationKey](location.md) — A key indicating that the app was launched to handle an incoming location event. _(deprecated)_
- [UIApplicationLaunchOptionsNewsstandDownloadsKey](newsstanddownloads.md) — A key indicating that the app was launched to process newly downloaded Newsstand assets. _(deprecated)_
- [UIApplicationLaunchOptionsRemoteNotificationKey](remotenotification.md) — A key indicating that a remote notification is available for the app to process. _(deprecated)_
- [UIApplicationLaunchOptionsShortcutItemKey](shortcutitem.md) — A key indicating that the app was launched in response to the user selecting a Home screen quick action. _(deprecated)_
- [UIApplicationLaunchOptionsSourceApplicationKey](sourceapplication.md) — A key indicating that another app requested the launch of your app. _(deprecated)_
- [UIApplicationLaunchOptionsURLKey](url.md) — A key indicating that the app was launched so that it could open the specified URL. _(deprecated)_
- [UIApplicationLaunchOptionsUserActivityDictionaryKey](useractivitydictionary.md) — A key indicating a dictionary associated with an activity that the user wants to continue. _(deprecated)_
- [UIApplicationLaunchOptionsUserActivityTypeKey](useractivitytype.md) — A key indicating the type of user activity that the user wants to continue. _(deprecated)_
- [UIApplicationLaunchOptionsLocalNotificationKey](localnotification.md) — A key indicating that the app was launched to handle a local notification. _(deprecated)_
