---
title: 'init(state:staleDate:relevanceScore:)'
framework: ActivityKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.2+, iPadOS 16.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/activitykit/activitycontent/init(state:staledate:relevancescore:)'
source_url: 'https://developer.apple.com/documentation/activitykit/activitycontent/init(state:staledate:relevancescore:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activitycontent/init%28state%3Astaledate%3Arelevancescore%3A%29.json'
content_hash: 'sha256:18db32375babb981'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [ActivityContent](../activitycontent.md)

# init(state:staleDate:relevanceScore:)

<sub>Initializer</sub>

Creates the object that describes the state and configuration of a Live Activity.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
init(state: State, staleDate: Date?, relevanceScore: Double = 0.0)
```

## See Also

### Describing a Live Activity

- [state](state.md) — The current state of a Live Activity in its life cycle.
- [staleDate](staledate.md) — The date when the system considers the Live Activity to be out of date.
- [relevanceScore](relevancescore.md) — A score you assign that determines the order in which your Live Activities appear when you start several Live Activities for your app.
