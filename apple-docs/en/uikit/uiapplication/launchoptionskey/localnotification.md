---
title: localNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+（10.0 起废弃）, iPadOS 4.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiapplication/launchoptionskey/localnotification
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/launchoptionskey/localnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/launchoptionskey/localnotification.json'
content_hash: 'sha256:c1e2b88d5b1f76bf'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIApplication](../../uiapplication.md) · [LaunchOptionsKey](../launchoptionskey.md)

# localNotification

<sub>Type Property</sub>

A key indicating that the app was launched to handle a local notification.

> [!warning] Deprecated
> Use [userNotificationCenter(_:didReceive:withCompletionHandler:)](<../../../usernotifications/unusernotificationcenterdelegate/usernotificationcenter(__didreceive_withcompletionhandler_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
static let localNotification: UIApplication.LaunchOptionsKey
```

## Discussion

The value of this key is the [UILocalNotification](../../uilocalnotification.md) object that was triggered. For additional information about handling local notifications, see the [- application:didReceiveLocalNotification:](<../../uiapplicationdelegate/application(__didreceive_).md>) method.

This key is also used to access the same value in the `userInfo` dictionary of the notification named [UIApplicationDidFinishLaunchingNotification](../didfinishlaunchingnotification.md).

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
- [UIApplicationLaunchOptionsAnnotationKey](annotation.md) — A key indicating that the URL passed to your app contained custom annotation data from the source app. _(deprecated)_
