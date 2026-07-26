---
title: 'contentMargins(_:_:)'
framework: WidgetKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/dynamicislandexpandedregion/contentmargins(_:_:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/dynamicislandexpandedregion/contentmargins(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/dynamicislandexpandedregion/contentmargins%28_%3A_%3A%29.json'
content_hash: 'sha256:fc9b098ceacab510'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [DynamicIslandExpandedRegion](../dynamicislandexpandedregion.md)

# contentMargins(_:_:)

<sub>Instance Method</sub>

Overrides default content margins for the provided edges in the Dynamic Island.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func contentMargins(_ edges: Edge.Set = .all, _ length: Double) -> DynamicIslandExpandedRegion<Content>
```

## Parameters

- `edges` — The edges that use the custom content margins.

- `length` — The length of the custom margin for the given `edges`.

## Return Value

The view for the Dynamic Island expanded region with the updated content margins.

## Discussion

If you repeatedly use the `contentMargins(_:_:)` modifier, the system uses the innermost specified values. The following example results in a margin of 8 points for the trailing, top, and bottom edges, and uses the default margin for the leading edge:

```swift
DynamicIslandContentRegion(.trailing) {
    ContainerRelativeShape()
    .aspectRatio(1, contentMode:.fit)
}.contentMargins([.trailing, .top, .bottom], 8)
```

Note that the system applies the provided custom content margins to content that’s adjacent to the modified content margin edges.
