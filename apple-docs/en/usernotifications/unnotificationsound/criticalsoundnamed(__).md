---
title: 'criticalSoundNamed(_:)'
framework: User Notifications
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/usernotifications/unnotificationsound/criticalsoundnamed(_:)'
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationsound/criticalsoundnamed(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationsound/criticalsoundnamed%28_%3A%29.json'
content_hash: 'sha256:148a23ab4728b0bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationSound](../unnotificationsound.md)

# criticalSoundNamed(_:)

<sub>Type Method</sub>

Creates a custom sound object for critical alerts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class func criticalSoundNamed(_ name: UNNotificationSoundName) -> Self
```

## Parameters

- `name` — The name of the sound file to play. This file must be located in the current executable’s main bundle or in the `Library/Sounds` directory of the current app container directory. If files exist at both locations, the system uses the file from the `Library/Sounds` directory. This parameter must not be `nil`.

## Return Value

A sound object representing a custom critical alert sound.

## Discussion

Critical alerts ignore the mute switch and Do Not Disturb. They require a special entitlement issued by Apple.

## See Also

### Getting Critical Sounds

- [defaultCriticalSound](defaultcritical.md) — The default sound used for critical alerts.
- [+ defaultCriticalSoundWithAudioVolume:](<defaultcriticalsound(withaudiovolume_).md>) — Creates a sound object that plays the default critical alert sound at the volume you specify.
- [+ criticalSoundNamed:withAudioVolume:](<criticalsoundnamed(__withaudiovolume_).md>) — Creates a custom sound object for critical alerts with the volume you specify.
