---
title: 'init(named:)'
framework: User Notifications
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/usernotifications/unnotificationsound/init(named:)'
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationsound/init(named:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationsound/init%28named%3A%29.json'
content_hash: 'sha256:27db737cfb07f208'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationSound](../unnotificationsound.md)

# init(named:)

<sub>Initializer</sub>

Creates a sound object that represents a custom sound file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
convenience init(named name: UNNotificationSoundName)
```

## Parameters

- `name` — The name of the sound file to play. This parameter must not be `nil`.

## Return Value

A sound object representing the custom sound.

## Discussion

This method searches for sound files in the following locations, in order:

1. The _\<app_container\>_`/Library/Sounds` directory, where _\<app_container\>_ is the app’s container directory.
2. The _\<group_container\>_`/Library/Sounds` directory, where _\<group_container\>_ is one of the app’s shared group container directories. For information about how to configure group containers for your app, see [Configure app groups](https://help.apple.com/xcode/mac/current/#/dev8dd3880fe).
3. The main bundle of the current executable.

The method chooses the first file it finds with the specified name.

## See Also

### Creating Notification Sounds

- [defaultSound](default.md) — Returns an object representing the default sound for notifications.
