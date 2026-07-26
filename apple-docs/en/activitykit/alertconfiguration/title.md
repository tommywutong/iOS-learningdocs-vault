---
title: title
framework: ActivityKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/alertconfiguration/title
source_url: 'https://developer.apple.com/documentation/activitykit/alertconfiguration/title'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/alertconfiguration/title.json'
content_hash: 'sha256:35d45035238328d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [AlertConfiguration](../alertconfiguration.md)

# title

<sub>Instance Property</sub>

A short title that describes the purpose of the Live Activity update on Apple Watch.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var title: LocalizedStringResource
```

## Discussion

Apple Watch displays this string briefly as part of the alert that appears when you update a Live Activity and choose to alert people about the update. Choose text that’s easy to read at a glance. For example, a pizza delivery app could use “On the way.”

## See Also

### Configuring Live Activity alerts

- [init(title:body:sound:)](<init(title_body_sound_).md>) — Initializes a new alert configuration for a Live Activity update.
- [body](body.md) — The main text that appears on the alert for a Live Activity update on Apple Watch.
- [sound](sound.md) — The sound the system plays when the Live Activity alert appears on a person’s device.
- [AlertSound](alertsound.md) — An object that describes the sound to play for a Live Activity update alert.
