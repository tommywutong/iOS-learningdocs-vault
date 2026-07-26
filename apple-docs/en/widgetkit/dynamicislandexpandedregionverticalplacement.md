---
title: DynamicIslandExpandedRegionVerticalPlacement
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/dynamicislandexpandedregionverticalplacement
source_url: 'https://developer.apple.com/documentation/widgetkit/dynamicislandexpandedregionverticalplacement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/dynamicislandexpandedregionverticalplacement.json'
content_hash: 'sha256:f0ed5827eee0f8ca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# DynamicIslandExpandedRegionVerticalPlacement

<sub>Structure</sub>

Vertical view positions of an expanded Live Activity that appears in the Dynamic Island.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
struct DynamicIslandExpandedRegionVerticalPlacement
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md)

## Topics

### Configuring vertical content placement

- [default](dynamicislandexpandedregionverticalplacement/default.md) — The system’s default vertical placement.
- [belowIfTooWide](dynamicislandexpandedregionverticalplacement/belowiftoowide.md) — Vertical placement below the default vertical position for content that’s too wide to fit next to the TrueDepth camera.

## See Also

### Creating the expanded presentation

- [init(_:priority:content:)](<dynamicislandexpandedregion/init(__priority_content_).md>) — Creates the object that defines and positions the content of an expanded Live Activity in the Dynamic Island.
- [DynamicIslandExpandedRegionPosition](dynamicislandexpandedregionposition.md) — View positions of an expanded Live Activity that appears in the Dynamic Island.
- [dynamicIsland(verticalPlacement:)](<../swiftui/view/dynamicisland(verticalplacement_).md>) — Specifies the vertical placement for a view of an expanded Live Activity that appears in the Dynamic Island.
- [DynamicIslandExpandedContent](dynamicislandexpandedcontent.md) — A view that describes the expanded presentation of a Live Activity that appears in the Dynamic Island.
- [DynamicIslandExpandedContentBuilder](dynamicislandexpandedcontentbuilder.md) — A result builder that constructs the content of an expanded Live Activity in the Dynamic Island.
