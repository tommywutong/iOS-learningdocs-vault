---
title: pushToStartToken
framework: ActivityKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.2+, iPadOS 17.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activity/pushtostarttoken
source_url: 'https://developer.apple.com/documentation/activitykit/activity/pushtostarttoken'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activity/pushtostarttoken.json'
content_hash: 'sha256:c53fe162dfb7f5fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [Activity](../activity.md)

# pushToStartToken

<sub>Type Property</sub>

The token you use to start a Live Activity with an ActivityKit push notification.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
static var pushToStartToken: Data? { get }
```

## Discussion

The push token for a Live Activity may change over time. Use the [pushToStartTokenUpdates](pushtostarttokenupdates.md) asynchronous sequence to receive an updated push-to-start token. When you receive an updated push token, make sure to send it to your server and invalidate the outdated token.

## See Also

### Using ActivityKit push notifications

- [pushToken](pushtoken.md) — The token you use to send ActivityKit push notifications to a Live Activity.
- [pushTokenUpdates](pushtokenupdates-swift.property.md) — An asynchronous sequence you use to observe changes to the push token of a Live Activity.
- [PushTokenUpdates](pushtokenupdates-swift.struct.md) — A structure that offers functionality to observe changes to the push token of a Live Activity.
- [pushToStartTokenUpdates](pushtostarttokenupdates.md) — An asynchronous sequence you use to observe changes to the token for starting a Live Activity with an ActivityKit push notification.
