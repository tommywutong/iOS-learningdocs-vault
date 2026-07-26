---
title: 'end(_:dismissalPolicy:timestamp:)'
framework: ActivityKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.2+, iPadOS 17.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/activitykit/activity/end(_:dismissalpolicy:timestamp:)'
source_url: 'https://developer.apple.com/documentation/activitykit/activity/end(_:dismissalpolicy:timestamp:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activity/end%28_%3Adismissalpolicy%3Atimestamp%3A%29.json'
content_hash: 'sha256:04aeaca0efd8b9cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [Activity](../activity.md)

# end(_:dismissalPolicy:timestamp:)

<sub>Instance Method</sub>

Ends an active Live Activity.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func end(_ content: ActivityContent<Activity<Attributes>.ContentState>?, dismissalPolicy: ActivityUIDismissalPolicy = .default, timestamp: Date) async
```

## Parameters

- `content` — The latest and final dynamic content for the Live Activity that ended. The size of the encoded content can’t exceed 4KB in size.

- `dismissalPolicy` — Describes how and when the system should dismiss a Live Activity and remove it from the Lock Screen.

- `timestamp` — The time the data in the payload was generated. If this is older than a previous update or push payload, the system ignores this update.

## Discussion

End an active Live Activity while your app is in the foreground or while it’s in the background — for example, by using [Background Tasks](../../backgroundtasks.md). When you end a Live Activity, include a final content update using the `content` parameter to ensure the Live Activity shows the latest and final content update after it ends. This is important because the Live Activity may remain visible until the system or the person removes it.

## See Also

### Ending a Live Activity

- [end(_:dismissalPolicy:)](<end(__dismissalpolicy_).md>) — Ends an active Live Activity.
- [ActivityUIDismissalPolicy](../activityuidismissalpolicy.md) — The structure that describes when the system should remove a Live Activity that ended.
