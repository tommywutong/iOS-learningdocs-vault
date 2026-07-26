---
title: pushToken
framework: ActivityKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activity/pushtoken
source_url: 'https://developer.apple.com/documentation/activitykit/activity/pushtoken'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activity/pushtoken.json'
content_hash: 'sha256:4041bdfb219b0d7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [Activity](../activity.md)

# pushToken

<sub>Instance Property</sub>

The token you use to send ActivityKit push notifications to a Live Activity.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var pushToken: Data? { get }
```

## Discussion

The push token for a Live Activity may change over time. Use the [pushTokenUpdates](pushtokenupdates-swift.property.md) asynchronous sequence to receive the updated push token. When you receive an updated push token, make sure to send it to your server and invalidate the outdated token.

## See Also

### Using ActivityKit push notifications

- [pushTokenUpdates](pushtokenupdates-swift.property.md) — An asynchronous sequence you use to observe changes to the push token of a Live Activity.
- [PushTokenUpdates](pushtokenupdates-swift.struct.md) — A structure that offers functionality to observe changes to the push token of a Live Activity.
- [pushToStartToken](pushtostarttoken.md) — The token you use to start a Live Activity with an ActivityKit push notification.
- [pushToStartTokenUpdates](pushtostarttokenupdates.md) — An asynchronous sequence you use to observe changes to the token for starting a Live Activity with an ActivityKit push notification.
