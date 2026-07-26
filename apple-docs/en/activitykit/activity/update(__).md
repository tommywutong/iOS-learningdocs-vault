---
title: 'update(_:)'
framework: ActivityKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.2+, iPadOS 16.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/activitykit/activity/update(_:)'
source_url: 'https://developer.apple.com/documentation/activitykit/activity/update(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activity/update%28_%3A%29.json'
content_hash: 'sha256:8e3786e7ebed4db9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [Activity](../activity.md)

# update(_:)

<sub>Instance Method</sub>

Updates the dynamic content of the Live Activity.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func update(_ content: ActivityContent<Activity<Attributes>.ContentState>) async
```

## Parameters

- `content` — The updated dynamic content for the Live Activity. The size of its [state](../activitycontent/state.md) property can’t exceed 4KB in size.

## Discussion

Use this function to update the Live Activity while your app is in the foreground or while it’s in the background — for example, by using [Background Tasks](../../backgroundtasks.md).

> [!note] Note
> The system ignores attempts to update a Live Activity that ended.

## See Also

### Updating a Live Activity

- [update(_:alertConfiguration:)](<update(__alertconfiguration_).md>) — Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update.
- [AlertConfiguration](../alertconfiguration.md) — A structure you use to configure an alert that appears when you update your Live Activity.
- [update(_:alertConfiguration:timestamp:)](<update(__alertconfiguration_timestamp_).md>) — Updates the dynamic content of a Live Activity and alerts a person about the Live Activity update.
