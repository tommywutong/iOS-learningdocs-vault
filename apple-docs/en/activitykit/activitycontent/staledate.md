---
title: staleDate
framework: ActivityKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.2+, iPadOS 16.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activitycontent/staledate
source_url: 'https://developer.apple.com/documentation/activitykit/activitycontent/staledate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activitycontent/staledate.json'
content_hash: 'sha256:bf4bff4e4f906361'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [ActivityContent](../activitycontent.md)

# staleDate

<sub>Instance Property</sub>

The date when the system considers the Live Activity to be out of date.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
let staleDate: Date?
```

## Discussion

When time reaches the configured stale date, the system considers the Live Activity out of date, and the [ActivityState](../activitystate.md) of the Live Activity changes to [ActivityState.stale](../activitystate/stale.md).

## See Also

### Describing a Live Activity

- [init(state:staleDate:relevanceScore:)](<init(state_staledate_relevancescore_).md>) — Creates the object that describes the state and configuration of a Live Activity.
- [state](state.md) — The current state of a Live Activity in its life cycle.
- [relevanceScore](relevancescore.md) — A score you assign that determines the order in which your Live Activities appear when you start several Live Activities for your app.
