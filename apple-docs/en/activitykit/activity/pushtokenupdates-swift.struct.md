---
title: Activity.PushTokenUpdates
framework: ActivityKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activity/pushtokenupdates-swift.struct
source_url: 'https://developer.apple.com/documentation/activitykit/activity/pushtokenupdates-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activity/pushtokenupdates-swift.struct.json'
content_hash: 'sha256:85dcd79ebdebac5c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [Activity](../activity.md)

# Activity.PushTokenUpdates

<sub>Structure</sub>

A structure that offers functionality to observe changes to the push token of a Live Activity.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
struct PushTokenUpdates
```

## Relationships

- **Conforms To**: [AsyncSequence](../../swift/asyncsequence.md)

## Topics

### Creating an iterator

- [makeAsyncIterator()](<pushtokenupdates-swift.struct/makeasynciterator().md>) — Creates the asynchronous iterator that produces results from this asynchronous sequence.
- [Iterator](pushtokenupdates-swift.struct/iterator.md) — An iterator for accessing individual data entries from the series.
- [Element](pushtokenupdates-swift.struct/element.md) — The type of element this asynchronous sequence produces.

## See Also

### Using ActivityKit push notifications

- [pushToken](pushtoken.md) — The token you use to send ActivityKit push notifications to a Live Activity.
- [pushTokenUpdates](pushtokenupdates-swift.property.md) — An asynchronous sequence you use to observe changes to the push token of a Live Activity.
- [pushToStartToken](pushtostarttoken.md) — The token you use to start a Live Activity with an ActivityKit push notification.
- [pushToStartTokenUpdates](pushtostarttokenupdates.md) — An asynchronous sequence you use to observe changes to the token for starting a Live Activity with an ActivityKit push notification.
