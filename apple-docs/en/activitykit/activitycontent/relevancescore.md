---
title: relevanceScore
framework: ActivityKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.2+, iPadOS 16.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activitycontent/relevancescore
source_url: 'https://developer.apple.com/documentation/activitykit/activitycontent/relevancescore'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activitycontent/relevancescore.json'
content_hash: 'sha256:711832ddb02dce3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [ActivityContent](../activitycontent.md)

# relevanceScore

<sub>Instance Property</sub>

A score you assign that determines the order in which your Live Activities appear when you start several Live Activities for your app.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
let relevanceScore: Double
```

## Discussion

If you start more than one Live Activity in your app, the Live Activity with the highest relevance score appears in the Dynamic Island. If Live Activities have the same relevance score, the system displays the Live Activity that started first. Additionally, the `relevanceScore` determines the order of your Live Activities on the Lock Screen.

## See Also

### Describing a Live Activity

- [init(state:staleDate:relevanceScore:)](<init(state_staledate_relevancescore_).md>) — Creates the object that describes the state and configuration of a Live Activity.
- [state](state.md) — The current state of a Live Activity in its life cycle.
- [staleDate](staledate.md) — The date when the system considers the Live Activity to be out of date.
