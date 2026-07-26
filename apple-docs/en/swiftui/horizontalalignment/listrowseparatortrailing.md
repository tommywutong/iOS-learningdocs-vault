---
title: listRowSeparatorTrailing
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/horizontalalignment/listrowseparatortrailing
source_url: 'https://developer.apple.com/documentation/swiftui/horizontalalignment/listrowseparatortrailing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/horizontalalignment/listrowseparatortrailing.json'
content_hash: 'sha256:a865727f3fa2d484'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [HorizontalAlignment](../horizontalalignment.md)

# listRowSeparatorTrailing

<sub>Type Property</sub>

A guide marking the trailing edge of a `List` row separator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let listRowSeparatorTrailing: HorizontalAlignment
```

## Discussion

Use this guide to align the trailing end of the bottom `List` row separator with any other horizontal guide of a view that is part of the cell content.

To change the visibility or tint of the row separator use respectively [listRowSeparator(_:edges:)](<../view/listrowseparator(__edges_).md>) and [listRowSeparatorTint(_:edges:)](<../view/listrowseparatortint(__edges_).md>).

## See Also

### Getting guides

- [leading](leading.md) — A guide that marks the leading edge of the view.
- [center](center.md) — A guide that marks the horizontal center of the view.
- [trailing](trailing.md) — A guide that marks the trailing edge of the view.
- [listRowSeparatorLeading](listrowseparatorleading.md) — A guide marking the leading edge of a `List` row separator.
