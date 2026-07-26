---
title: DynamicIslandExpandedContent
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/dynamicislandexpandedcontent
source_url: 'https://developer.apple.com/documentation/widgetkit/dynamicislandexpandedcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/dynamicislandexpandedcontent.json'
content_hash: 'sha256:08eb35e77003fcdc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# DynamicIslandExpandedContent

<sub>Structure</sub>

A view that describes the expanded presentation of a Live Activity that appears in the Dynamic Island.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
struct DynamicIslandExpandedContent<Content> where Content : View
```

## Overview

This view holds the intermediate content for the [DynamicIslandExpandedContentBuilder](dynamicislandexpandedcontentbuilder.md).

## See Also

### Creating the expanded presentation

- [init(_:priority:content:)](<dynamicislandexpandedregion/init(__priority_content_).md>) — Creates the object that defines and positions the content of an expanded Live Activity in the Dynamic Island.
- [DynamicIslandExpandedRegionPosition](dynamicislandexpandedregionposition.md) — View positions of an expanded Live Activity that appears in the Dynamic Island.
- [dynamicIsland(verticalPlacement:)](<../swiftui/view/dynamicisland(verticalplacement_).md>) — Specifies the vertical placement for a view of an expanded Live Activity that appears in the Dynamic Island.
- [DynamicIslandExpandedRegionVerticalPlacement](dynamicislandexpandedregionverticalplacement.md) — Vertical view positions of an expanded Live Activity that appears in the Dynamic Island.
- [DynamicIslandExpandedContentBuilder](dynamicislandexpandedcontentbuilder.md) — A result builder that constructs the content of an expanded Live Activity in the Dynamic Island.
