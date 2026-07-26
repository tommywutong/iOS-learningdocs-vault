---
title: 'draggedItemIDs(for:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/dragsession/draggeditemids(for:)'
source_url: 'https://developer.apple.com/documentation/swiftui/dragsession/draggeditemids(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dragsession/draggeditemids%28for%3A%29.json'
content_hash: 'sha256:76aa229fa6b4efb9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DragSession](../dragsession.md)

# draggedItemIDs(for:)

<sub>Instance Method</sub>

Provides an array of identifiers of the currently dragged items in a case when the items conform to the `Identifiable` protocol, or identifiers were provided to SwiftUI separately.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func draggedItemIDs<ItemID>(for type: ItemID.Type) -> [ItemID] where ItemID : Hashable
```

## Discussion

Parameter type: The type of the identifiers. Returns: The array with the identifiers of the dragged items if provided. Returns an empty array if no dragged identifiers of a given type exist.
