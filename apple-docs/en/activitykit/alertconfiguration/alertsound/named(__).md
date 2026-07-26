---
title: 'named(_:)'
framework: ActivityKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/activitykit/alertconfiguration/alertsound/named(_:)'
source_url: 'https://developer.apple.com/documentation/activitykit/alertconfiguration/alertsound/named(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/alertconfiguration/alertsound/named%28_%3A%29.json'
content_hash: 'sha256:6af38b290b5fd48e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [ActivityKit](../../../activitykit.md) · [AlertConfiguration](../../alertconfiguration.md) · [AlertSound](../alertsound.md)

# named(_:)

<sub>Type Method</sub>

A function you use to configure a custom sound for a Live Activity update alert.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
static func named(_ name: String) -> AlertConfiguration.AlertSound
```

## Parameters

- `name` — The name of the sound file to use for the alert. Choose a file that’s in your app’s main bundle or the `Library/Sounds` folder of your app’s data container.

## See Also

### Configuring the alert sound

- [default](default.md) — A value that represents the system’s default alert sound.
