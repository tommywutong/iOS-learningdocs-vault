---
title: 'end(_:dismissalPolicy:)'
framework: ActivityKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.2+, iPadOS 16.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/activitykit/activity/end(_:dismissalpolicy:)'
source_url: 'https://developer.apple.com/documentation/activitykit/activity/end(_:dismissalpolicy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activity/end%28_%3Adismissalpolicy%3A%29.json'
content_hash: 'sha256:f89bcda69ef31d10'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [Activity](../activity.md)

# end(_:dismissalPolicy:)

<sub>Instance Method</sub>

Ends an active Live Activity.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func end(_ content: ActivityContent<Activity<Attributes>.ContentState>?, dismissalPolicy: ActivityUIDismissalPolicy = .default) async
```

## Parameters

- `content` — The latest and final dynamic content for the Live Activity that ended. The size of the encoded content can’t exceed 4KB in size.

- `dismissalPolicy` — Describes how and when the system should dismiss a Live Activity and and remove it from the Lock Screen.

## Discussion

End an active Live Activity while your app is in the foreground or while it’s in the background — for example, by using [Background Tasks](../../backgroundtasks.md). When you end a Live Activity, include a final content update using the `content` parameter to ensure the Live Activity shows the latest and final content update after it ends. This is important because the Live Activity may remain visible until the system or the person removes it.

## See Also

### Ending a Live Activity

- [ActivityUIDismissalPolicy](../activityuidismissalpolicy.md) — The structure that describes when the system should remove a Live Activity that ended.
- [end(_:dismissalPolicy:timestamp:)](<end(__dismissalpolicy_timestamp_).md>) — Ends an active Live Activity.
