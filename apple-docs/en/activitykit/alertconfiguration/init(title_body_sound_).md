---
title: 'init(title:body:sound:)'
framework: ActivityKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/activitykit/alertconfiguration/init(title:body:sound:)'
source_url: 'https://developer.apple.com/documentation/activitykit/alertconfiguration/init(title:body:sound:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/alertconfiguration/init%28title%3Abody%3Asound%3A%29.json'
content_hash: 'sha256:8cef364e336b3d29'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [AlertConfiguration](../alertconfiguration.md)

# init(title:body:sound:)

<sub>Initializer</sub>

Initializes a new alert configuration for a Live Activity update.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
init(title: LocalizedStringResource, body: LocalizedStringResource, sound: AlertConfiguration.AlertSound)
```

## Parameters

- `title` — The short title that describes the purpose of the Live Activity update.

- `body` — The main text of the alert for a Live Activity update.

- `sound` — The sound that the system plays when the alert appears on a person’s device.

## See Also

### Configuring Live Activity alerts

- [title](title.md) — A short title that describes the purpose of the Live Activity update on Apple Watch.
- [body](body.md) — The main text that appears on the alert for a Live Activity update on Apple Watch.
- [sound](sound.md) — The sound the system plays when the Live Activity alert appears on a person’s device.
- [AlertSound](alertsound.md) — An object that describes the sound to play for a Live Activity update alert.
