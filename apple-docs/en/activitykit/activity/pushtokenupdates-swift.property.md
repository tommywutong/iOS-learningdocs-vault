---
title: pushTokenUpdates
framework: ActivityKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activity/pushtokenupdates-swift.property
source_url: 'https://developer.apple.com/documentation/activitykit/activity/pushtokenupdates-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activity/pushtokenupdates-swift.property.json'
content_hash: 'sha256:dd59d290ccf485b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [Activity](../activity.md)

# pushTokenUpdates

<sub>Instance Property</sub>

An asynchronous sequence you use to observe changes to the push token of a Live Activity.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var pushTokenUpdates: Activity<Attributes>.PushTokenUpdates { get }
```

## See Also

### Using ActivityKit push notifications

- [pushToken](pushtoken.md) — The token you use to send ActivityKit push notifications to a Live Activity.
- [PushTokenUpdates](pushtokenupdates-swift.struct.md) — A structure that offers functionality to observe changes to the push token of a Live Activity.
- [pushToStartToken](pushtostarttoken.md) — The token you use to start a Live Activity with an ActivityKit push notification.
- [pushToStartTokenUpdates](pushtostarttokenupdates.md) — An asynchronous sequence you use to observe changes to the token for starting a Live Activity with an ActivityKit push notification.
