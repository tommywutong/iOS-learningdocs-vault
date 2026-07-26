---
title: UIApplication.LaunchOptionsKey
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/launchoptionskey
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/launchoptionskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/launchoptionskey.json'
content_hash: 'sha256:c8cda8137f6507ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# UIApplication.LaunchOptionsKey

<sub>Structure</sub>

The keys you use to access values in the launch options dictionary that the system passes to your app at initialization.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct LaunchOptionsKey
```

## Overview

These keys are passed to the options dictionary that’s passed to the [- application:willFinishLaunchingWithOptions:](<../uiapplicationdelegate/application(__willfinishlaunchingwithoptions_).md>) and [- application:didFinishLaunchingWithOptions:](<../uiapplicationdelegate/application(__didfinishlaunchingwithoptions_).md>) methods of the app delegate.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Accessing launch options

- [UIApplicationLaunchOptionsBluetoothCentralsKey](launchoptionskey/bluetoothcentrals.md) — A key indicating that the app was relaunched to handle Bluetooth-related events. _(deprecated)_
- [UIApplicationLaunchOptionsBluetoothPeripheralsKey](launchoptionskey/bluetoothperipherals.md) — A key indicating that the app should continue actions associated with its Bluetooth peripheral objects. _(deprecated)_
- [UIApplicationLaunchOptionsCloudKitShareMetadataKey](launchoptionskey/cloudkitsharemetadata.md) — A key indicating that the app received a CloudKit share invitation. _(deprecated)_
- [UIApplicationLaunchOptionsEventAttributionKey](launchoptionskey/eventattribution.md) — UserInfo contains a [UIEventAttribution](../uieventattribution.md) to go along with a URL open on launch _(deprecated)_
- [UIApplicationLaunchOptionsLocationKey](launchoptionskey/location.md) — A key indicating that the app was launched to handle an incoming location event. _(deprecated)_
- [UIApplicationLaunchOptionsNewsstandDownloadsKey](launchoptionskey/newsstanddownloads.md) — A key indicating that the app was launched to process newly downloaded Newsstand assets. _(deprecated)_
- [UIApplicationLaunchOptionsRemoteNotificationKey](launchoptionskey/remotenotification.md) — A key indicating that a remote notification is available for the app to process. _(deprecated)_
- [UIApplicationLaunchOptionsShortcutItemKey](launchoptionskey/shortcutitem.md) — A key indicating that the app was launched in response to the user selecting a Home screen quick action. _(deprecated)_
- [UIApplicationLaunchOptionsSourceApplicationKey](launchoptionskey/sourceapplication.md) — A key indicating that another app requested the launch of your app. _(deprecated)_
- [UIApplicationLaunchOptionsURLKey](launchoptionskey/url.md) — A key indicating that the app was launched so that it could open the specified URL. _(deprecated)_
- [UIApplicationLaunchOptionsUserActivityDictionaryKey](launchoptionskey/useractivitydictionary.md) — A key indicating a dictionary associated with an activity that the user wants to continue. _(deprecated)_
- [UIApplicationLaunchOptionsUserActivityTypeKey](launchoptionskey/useractivitytype.md) — A key indicating the type of user activity that the user wants to continue. _(deprecated)_
- [UIApplicationLaunchOptionsAnnotationKey](launchoptionskey/annotation.md) — A key indicating that the URL passed to your app contained custom annotation data from the source app. _(deprecated)_
- [UIApplicationLaunchOptionsLocalNotificationKey](launchoptionskey/localnotification.md) — A key indicating that the app was launched to handle a local notification. _(deprecated)_

### Creating a launch options key

- [init(rawValue:)](<launchoptionskey/init(rawvalue_).md>) — Creates a launch options key with the specified raw value.

## See Also

### Initializing the app

- [- application:willFinishLaunchingWithOptions:](<../uiapplicationdelegate/application(__willfinishlaunchingwithoptions_).md>) — Tells the delegate that the launch process has begun.
- [- application:didFinishLaunchingWithOptions:](<../uiapplicationdelegate/application(__didfinishlaunchingwithoptions_).md>) — Tells the delegate that the launch process is almost done and the app is almost ready to run.
- [UIApplicationDidFinishLaunchingNotification](didfinishlaunchingnotification.md) — A notification that posts immediately after the app finishes launching.
