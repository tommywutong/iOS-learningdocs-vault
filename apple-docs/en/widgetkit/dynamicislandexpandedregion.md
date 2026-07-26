---
title: DynamicIslandExpandedRegion
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/dynamicislandexpandedregion
source_url: 'https://developer.apple.com/documentation/widgetkit/dynamicislandexpandedregion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/dynamicislandexpandedregion.json'
content_hash: 'sha256:076ab4f4e3c2dc41'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# DynamicIslandExpandedRegion

<sub>Structure</sub>

A structure that defines and positions the content of an expanded Live Activity in the Dynamic Island.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
struct DynamicIslandExpandedRegion<Content> where Content : View
```

## Overview

The expanded presentation of a Live Activity in the Dynamic Island consists of four regions:

- [center](dynamicislandexpandedregionposition/center.md) places content right below the TrueDepth camera.
- [leading](dynamicislandexpandedregionposition/leading.md) places content along the leading edge of the expanded Live Activity next to the TrueDepth camera and wraps additional content below it.
- [trailing](dynamicislandexpandedregionposition/trailing.md) places content along the trailing edge of the expanded Live Activity next to the TrueDepth camera and wraps additional content below it.
- [bottom](dynamicislandexpandedregionposition/bottom.md) places content below leading, trailing, and center content.

## Topics

### Creating the expanded presentation

- [init(_:priority:content:)](<dynamicislandexpandedregion/init(__priority_content_).md>) — Creates the object that defines and positions the content of an expanded Live Activity in the Dynamic Island.
- [DynamicIslandExpandedRegionPosition](dynamicislandexpandedregionposition.md) — View positions of an expanded Live Activity that appears in the Dynamic Island.
- [dynamicIsland(verticalPlacement:)](<../swiftui/view/dynamicisland(verticalplacement_).md>) — Specifies the vertical placement for a view of an expanded Live Activity that appears in the Dynamic Island.
- [DynamicIslandExpandedRegionVerticalPlacement](dynamicislandexpandedregionverticalplacement.md) — Vertical view positions of an expanded Live Activity that appears in the Dynamic Island.
- [DynamicIslandExpandedContent](dynamicislandexpandedcontent.md) — A view that describes the expanded presentation of a Live Activity that appears in the Dynamic Island.
- [DynamicIslandExpandedContentBuilder](dynamicislandexpandedcontentbuilder.md) — A result builder that constructs the content of an expanded Live Activity in the Dynamic Island.

### Specifying custom content margins

- [contentMargins(_:_:)](<dynamicislandexpandedregion/contentmargins(____).md>) — Overrides default content margins for the provided edges in the Dynamic Island.

## See Also

### Creating the view for the Dynamic Island

- [init(expanded:compactLeading:compactTrailing:minimal:)](<dynamicisland/init(expanded_compactleading_compacttrailing_minimal_).md>) — Creates a configuration object with views that appear in the Dynamic Island.
