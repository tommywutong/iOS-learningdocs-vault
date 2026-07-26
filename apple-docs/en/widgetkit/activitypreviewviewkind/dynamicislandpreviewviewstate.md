---
title: ActivityPreviewViewKind.DynamicIslandPreviewViewState
framework: WidgetKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.2+, iPadOS 16.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/activitypreviewviewkind/dynamicislandpreviewviewstate
source_url: 'https://developer.apple.com/documentation/widgetkit/activitypreviewviewkind/dynamicislandpreviewviewstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/activitypreviewviewkind/dynamicislandpreviewviewstate.json'
content_hash: 'sha256:f617fc8d72d9d907'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [ActivityPreviewViewKind](../activitypreviewviewkind.md)

# ActivityPreviewViewKind.DynamicIslandPreviewViewState

<sub>Enumeration</sub>

Values that represent the different presentations of a Live Activity in the Dynamic Island for use in Xcode previews.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@preconcurrency enum DynamicIslandPreviewViewState
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Dynamic Island presentations

- [ActivityPreviewViewKind.DynamicIslandPreviewViewState.compact](dynamicislandpreviewviewstate/compact.md) — The presentation of a Live Activity in the Dynamic Island that shows both the [compactLeading](../dynamicislandmode/compactleading.md) and [compactTrailing](../dynamicislandmode/compacttrailing.md) views combined.
- [ActivityPreviewViewKind.DynamicIslandPreviewViewState.minimal](dynamicislandpreviewviewstate/minimal.md) — The minimal presentation of a Live Activity in the Dynamic Island.
- [ActivityPreviewViewKind.DynamicIslandPreviewViewState.expanded](dynamicislandpreviewviewstate/expanded.md) — The expanded presentation of a Live Activity in the Dynamic Island.

## See Also

### Live Activity preview types

- [ActivityPreviewViewKind.content](content.md) — The Live Activity presentation that appears on the Lock Screen and as a banner on devices that don’t support the Dynamic Island.
- [ActivityPreviewViewKind.dynamicIsland(_:)](<dynamicisland(__).md>) — The Live Activity presentation that appears in the Dynamic Island.
