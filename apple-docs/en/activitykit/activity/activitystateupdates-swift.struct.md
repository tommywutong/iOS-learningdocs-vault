---
title: Activity.ActivityStateUpdates
framework: ActivityKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activity/activitystateupdates-swift.struct
source_url: 'https://developer.apple.com/documentation/activitykit/activity/activitystateupdates-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activity/activitystateupdates-swift.struct.json'
content_hash: 'sha256:cdeeb27f635fff35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [Activity](../activity.md)

# Activity.ActivityStateUpdates

<sub>Structure</sub>

A structure that offers functionality to observe state changes of a Live Activity.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
struct ActivityStateUpdates
```

## Relationships

- **Conforms To**: [AsyncSequence](../../swift/asyncsequence.md)

## Topics

### Creating an iterator

- [makeAsyncIterator()](<activitystateupdates-swift.struct/makeasynciterator().md>) — Creates the asynchronous iterator that produces results from this asynchronous sequence.
- [Iterator](activitystateupdates-swift.struct/iterator.md) — An iterator for accessing individual data entries from the series.
- [Element](activitystateupdates-swift.struct/element.md) — The type of element this asynchronous sequence produces.

## See Also

### Observing the Live Activity life cycle

- [activityState](activitystate.md) — The current state of a Live Activity in its life cycle.
- [ActivityState](../activitystate.md) — The enum that describes the state of a Live Activity in its life cycle.
- [activityStateUpdates](activitystateupdates-swift.property.md) — An asynchronous sequence you use to observe activity state changes.
