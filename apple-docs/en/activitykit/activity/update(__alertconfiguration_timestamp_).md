---
title: 'update(_:alertConfiguration:timestamp:)'
framework: ActivityKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.2+, iPadOS 17.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/activitykit/activity/update(_:alertconfiguration:timestamp:)'
source_url: 'https://developer.apple.com/documentation/activitykit/activity/update(_:alertconfiguration:timestamp:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activity/update%28_%3Aalertconfiguration%3Atimestamp%3A%29.json'
content_hash: 'sha256:75aa8850d585bef6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [Activity](../activity.md)

# update(_:alertConfiguration:timestamp:)

<sub>Instance Method</sub>

Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func update(_ content: ActivityContent<Activity<Attributes>.ContentState>, alertConfiguration: AlertConfiguration? = nil, timestamp: Date) async
```

## Parameters

- `content` — The updated dynamic content for the Live Activity. The size of its [state](../activitycontent/state.md) property can’t exceed 4KB in size.

- `alertConfiguration` — The alert configuration you use to configure how the system notifies a person about the updated content of the Live Activity.

- `timestamp` — The time the data in the payload was generated. If this is older than a previous update or push payload, the system ignores this update.

## Discussion

The system ignores updates to a Live Activity that’s in the [ActivityState.ended](../activitystate/ended.md) state.

## See Also

### Updating a Live Activity

- [update(_:)](<update(__).md>) — Updates the dynamic content of the Live Activity.
- [update(_:alertConfiguration:)](<update(__alertconfiguration_).md>) — Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update.
- [AlertConfiguration](../alertconfiguration.md) — A structure you use to configure an alert that appears when you update your Live Activity.
