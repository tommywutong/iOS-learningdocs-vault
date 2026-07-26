---
title: 'init(_:priority:content:)'
framework: WidgetKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/dynamicislandexpandedregion/init(_:priority:content:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/dynamicislandexpandedregion/init(_:priority:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/dynamicislandexpandedregion/init%28_%3Apriority%3Acontent%3A%29.json'
content_hash: 'sha256:baa8515f9770d7c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [DynamicIslandExpandedRegion](../dynamicislandexpandedregion.md)

# init(_:priority:content:)

<sub>Initializer</sub>

Creates the object that defines and positions the content of an expanded Live Activity in the Dynamic Island.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
init(_ position: DynamicIslandExpandedRegionPosition, priority: Double = 0, @ViewBuilder content: () -> Content)
```

## Parameters

- `position` — The position for Live Activity content.

- `priority` — The priority that tells the system which content to prioritize when it sizes the content of an expanded Live Activity in the Dynamic Island.

- `content` — The content of an expanded Live Activity.

## See Also

### Creating the expanded presentation

- [DynamicIslandExpandedRegionPosition](../dynamicislandexpandedregionposition.md) — View positions of an expanded Live Activity that appears in the Dynamic Island.
- [dynamicIsland(verticalPlacement:)](<../../swiftui/view/dynamicisland(verticalplacement_).md>) — Specifies the vertical placement for a view of an expanded Live Activity that appears in the Dynamic Island.
- [DynamicIslandExpandedRegionVerticalPlacement](../dynamicislandexpandedregionverticalplacement.md) — Vertical view positions of an expanded Live Activity that appears in the Dynamic Island.
- [DynamicIslandExpandedContent](../dynamicislandexpandedcontent.md) — A view that describes the expanded presentation of a Live Activity that appears in the Dynamic Island.
- [DynamicIslandExpandedContentBuilder](../dynamicislandexpandedcontentbuilder.md) — A result builder that constructs the content of an expanded Live Activity in the Dynamic Island.
