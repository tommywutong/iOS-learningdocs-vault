---
title: AlertConfiguration.AlertSound
framework: ActivityKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/alertconfiguration/alertsound
source_url: 'https://developer.apple.com/documentation/activitykit/alertconfiguration/alertsound'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/alertconfiguration/alertsound.json'
content_hash: 'sha256:45b096bc7e510787'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [AlertConfiguration](../alertconfiguration.md)

# AlertConfiguration.AlertSound

<sub>Structure</sub>

An object that describes the sound to play for a Live Activity update alert.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
struct AlertSound
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Configuring the alert sound

- [named(_:)](<alertsound/named(__).md>) — A function you use to configure a custom sound for a Live Activity update alert.
- [default](alertsound/default.md) — A value that represents the system’s default alert sound.

## See Also

### Configuring Live Activity alerts

- [init(title:body:sound:)](<init(title_body_sound_).md>) — Initializes a new alert configuration for a Live Activity update.
- [title](title.md) — A short title that describes the purpose of the Live Activity update on Apple Watch.
- [body](body.md) — The main text that appears on the alert for a Live Activity update on Apple Watch.
- [sound](sound.md) — The sound the system plays when the Live Activity alert appears on a person’s device.
