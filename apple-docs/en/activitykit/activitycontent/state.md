---
title: state
framework: ActivityKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.2+, iPadOS 16.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activitycontent/state
source_url: 'https://developer.apple.com/documentation/activitykit/activitycontent/state'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activitycontent/state.json'
content_hash: 'sha256:a8afd7c2fcbd79ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [ActivityContent](../activitycontent.md)

# state

<sub>Instance Property</sub>

The current state of a Live Activity in its life cycle.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
let state: State
```

## Discussion

This value is the same as [activityState](../activity/activitystate.md).

## See Also

### Describing a Live Activity

- [init(state:staleDate:relevanceScore:)](<init(state_staledate_relevancescore_).md>) — Creates the object that describes the state and configuration of a Live Activity.
- [staleDate](staledate.md) — The date when the system considers the Live Activity to be out of date.
- [relevanceScore](relevancescore.md) — A score you assign that determines the order in which your Live Activities appear when you start several Live Activities for your app.
