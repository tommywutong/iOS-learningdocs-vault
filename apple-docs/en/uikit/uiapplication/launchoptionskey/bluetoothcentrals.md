---
title: bluetoothCentrals
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+（26.0 起废弃）, iPadOS 7.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, tvOS 9.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiapplication/launchoptionskey/bluetoothcentrals
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/launchoptionskey/bluetoothcentrals'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/launchoptionskey/bluetoothcentrals.json'
content_hash: 'sha256:4e511bf0fa8e3e88'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIApplication](../../uiapplication.md) · [LaunchOptionsKey](../launchoptionskey.md)

# bluetoothCentrals

<sub>Type Property</sub>

A key indicating that the app was relaunched to handle Bluetooth-related events.

> [!warning] Deprecated
> Store restoration identifiers and reinstantiate central managers with those identifiers on app launch to resume previous functionality.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static let bluetoothCentrals: UIApplication.LaunchOptionsKey
```

## Discussion

The presence of this key indicates that the app previously had one or more [CBCentralManager](../../../corebluetooth/cbcentralmanager.md) objects and was relaunched by the Bluetooth system to continue actions associated with those objects. The value of this key is an [NSArray](../../../foundation/nsarray.md) object containing one or more [NSString](../../../foundation/nsstring.md) objects.

Each string in the array represents the restoration identifier for a central manager object. This is the same string you assigned to the [CBCentralManagerOptionRestoreIdentifierKey](../../../corebluetooth/cbcentralmanageroptionrestoreidentifierkey.md) key when you initialized the central manager object previously. The system provides the restoration identifiers only for central managers that had active or pending peripheral connections or were scanning for peripherals.

## See Also

### Accessing launch options

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
- [UIApplicationLaunchOptionsLocalNotificationKey](localnotification.md) — A key indicating that the app was launched to handle a local notification. _(deprecated)_
