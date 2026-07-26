---
title: defaultCritical
framework: User Notifications
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/usernotifications/unnotificationsound/defaultcritical
source_url: 'https://developer.apple.com/documentation/usernotifications/unnotificationsound/defaultcritical'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/usernotifications/unnotificationsound/defaultcritical.json'
content_hash: 'sha256:9fda70721150fbe1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [User Notifications](../../usernotifications.md) · [UNNotificationSound](../unnotificationsound.md)

# defaultCritical

<sub>Type Property</sub>

The default sound used for critical alerts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@NSCopying class var defaultCritical: UNNotificationSound { get }
```

## Discussion

Critical alerts ingore the mute switch and Do Not Disturb. They require a special entitlement issued by Apple.

## See Also

### Getting Critical Sounds

- [+ defaultCriticalSoundWithAudioVolume:](<defaultcriticalsound(withaudiovolume_).md>) — Creates a sound object that plays the default critical alert sound at the volume you specify.
- [+ criticalSoundNamed:](<criticalsoundnamed(__).md>) — Creates a custom sound object for critical alerts.
- [+ criticalSoundNamed:withAudioVolume:](<criticalsoundnamed(__withaudiovolume_).md>) — Creates a custom sound object for critical alerts with the volume you specify.
