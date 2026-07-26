---
title: AlertConfiguration
framework: ActivityKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/alertconfiguration
source_url: 'https://developer.apple.com/documentation/activitykit/alertconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/alertconfiguration.json'
content_hash: 'sha256:ea974c7542524664'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [ActivityKit](../activitykit.md)

# AlertConfiguration

<sub>Structure</sub>

A structure you use to configure an alert that appears when you update your Live Activity.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
struct AlertConfiguration
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Configuring Live Activity alerts

- [init(title:body:sound:)](<alertconfiguration/init(title_body_sound_).md>) — Initializes a new alert configuration for a Live Activity update.
- [title](alertconfiguration/title.md) — A short title that describes the purpose of the Live Activity update on Apple Watch.
- [body](alertconfiguration/body.md) — The main text that appears on the alert for a Live Activity update on Apple Watch.
- [sound](alertconfiguration/sound.md) — The sound the system plays when the Live Activity alert appears on a person’s device.
- [AlertSound](alertconfiguration/alertsound.md) — An object that describes the sound to play for a Live Activity update alert.

## See Also

### Updating a Live Activity

- [update(_:)](<activity/update(__).md>) — Updates the dynamic content of the Live Activity.
- [update(_:alertConfiguration:)](<activity/update(__alertconfiguration_).md>) — Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update.
- [update(_:alertConfiguration:timestamp:)](<activity/update(__alertconfiguration_timestamp_).md>) — Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update.
