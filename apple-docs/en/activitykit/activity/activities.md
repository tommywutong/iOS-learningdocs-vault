---
title: activities
framework: ActivityKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activity/activities
source_url: 'https://developer.apple.com/documentation/activitykit/activity/activities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activity/activities.json'
content_hash: 'sha256:e8f92d49af066271'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [Activity](../activity.md)

# activities

<sub>Type Property</sub>

An array of your app’s current Live Activities.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
static var activities: [Activity<Attributes>] { get }
```

## See Also

### Accessing Live Activities

- [activityUpdates](activityupdates-swift.type.property.md) — An asynchronous sequence you use to observe changes to ongoing Live Activities and to asynchronously access a Live Activity when you start it.
- [ActivityUpdates](activityupdates-swift.struct.md) — A structure that offers functionality to observe changes to a Live Activity.
