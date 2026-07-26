---
title: pushToStartTokenUpdates
framework: ActivityKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.2+, iPadOS 17.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activity/pushtostarttokenupdates
source_url: 'https://developer.apple.com/documentation/activitykit/activity/pushtostarttokenupdates'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activity/pushtostarttokenupdates.json'
content_hash: 'sha256:afa5871ade9d37fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [Activity](../activity.md)

# pushToStartTokenUpdates

<sub>Type Property</sub>

An asynchronous sequence you use to observe changes to the token for starting a Live Activity with an ActivityKit push notification.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
static var pushToStartTokenUpdates: Activity<Attributes>.PushTokenUpdates { get }
```

## Discussion

Adopt push notifications to not only update ongoing Live Activities, but also to start a new Live Activity. For additional information, see [Starting and updating Live Activities with ActivityKit push notifications](../starting-and-updating-live-activities-with-activitykit-push-notifications.md).

## See Also

### Using ActivityKit push notifications

- [pushToken](pushtoken.md) — The token you use to send ActivityKit push notifications to a Live Activity.
- [pushTokenUpdates](pushtokenupdates-swift.property.md) — An asynchronous sequence you use to observe changes to the push token of a Live Activity.
- [PushTokenUpdates](pushtokenupdates-swift.struct.md) — A structure that offers functionality to observe changes to the push token of a Live Activity.
- [pushToStartToken](pushtostarttoken.md) — The token you use to start a Live Activity with an ActivityKit push notification.
