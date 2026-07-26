---
title: 'init(expanded:compactLeading:compactTrailing:minimal:)'
framework: WidgetKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/dynamicisland/init(expanded:compactleading:compacttrailing:minimal:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/dynamicisland/init(expanded:compactleading:compacttrailing:minimal:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/dynamicisland/init%28expanded%3Acompactleading%3Acompacttrailing%3Aminimal%3A%29.json'
content_hash: 'sha256:a85af8a174a45cf6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [DynamicIsland](../dynamicisland.md)

# init(expanded:compactLeading:compactTrailing:minimal:)

<sub>Initializer</sub>

Creates a configuration object with views that appear in the Dynamic Island.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
init<Expanded, CompactLeading, CompactTrailing, Minimal>(@DynamicIslandExpandedContentBuilder expanded: @escaping () -> DynamicIslandExpandedContent<Expanded>, @ViewBuilder compactLeading: @escaping () -> CompactLeading, @ViewBuilder compactTrailing: @escaping () -> CompactTrailing, @ViewBuilder minimal: @escaping () -> Minimal) where Expanded : View, CompactLeading : View, CompactTrailing : View, Minimal : View
```

## Parameters

- `expanded` — A closure that builds the view for the expanded presentation of the Live Activity.

- `compactLeading` — A closure that builds the view for the compact leading presentation of the Live Activity.

- `compactTrailing` — A closure that builds the view for the compact trailing presentation of the Live Activity.

- `minimal` — A closure that builds the view for the minimal presentation of the Live Activity.

## See Also

### Creating the view for the Dynamic Island

- [DynamicIslandExpandedRegion](../dynamicislandexpandedregion.md) — A structure that defines and positions the content of an expanded Live Activity in the Dynamic Island.
