---
title: 'defaultCriticalSound(withAudioVolume:)'
framework: User Notifications
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/usernotifications/unnotificationsound/defaultcriticalsound(withaudiovolume:)'
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationsound/defaultcriticalsound(withaudiovolume:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationsound/defaultcriticalsound%28withaudiovolume%3A%29.json'
content_hash: 'sha256:bff2369a8ad4196e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationSound](../unnotificationsound.md)

# defaultCriticalSound(withAudioVolume:)

<sub>Type Method</sub>

Creates a sound object that plays the default critical alert sound at the volume you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
class func defaultCriticalSound(withAudioVolume volume: Float) -> Self
```

## Parameters

- `volume` — The volume must be a value between 0.0 and 1.0.

## Return Value

A sound object representing the default critical alert sound at the specified volume.

## Discussion

Critical alerts ignore the mute switch and Do Not Disturb. They require a special entitlement issued by Apple.

## See Also

### Getting Critical Sounds

- [defaultCriticalSound](defaultcritical.md) — The default sound used for critical alerts.
- [+ criticalSoundNamed:](<criticalsoundnamed(__).md>) — Creates a custom sound object for critical alerts.
- [+ criticalSoundNamed:withAudioVolume:](<criticalsoundnamed(__withaudiovolume_).md>) — Creates a custom sound object for critical alerts with the volume you specify.
