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
doc_path: '/documentation/swiftui/dropsession/localsession-swift.struct/draggeditemids(for:)'
source_url: 'https://developer.apple.com/documentation/swiftui/dropsession/localsession-swift.struct/draggeditemids(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dropsession/localsession-swift.struct/draggeditemids%28for%3A%29.json'
content_hash: 'sha256:ccb059e05cfaa153'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [DropSession](../../dropsession.md) · [LocalSession](../localsession-swift.struct.md)

# draggedItemIDs(for:)

<sub>Instance Method</sub>

Provides an array of identifiers of the currently dragged items if available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func draggedItemIDs<ItemID>(for type: ItemID.Type) -> [ItemID] where ItemID : Hashable
```

## Discussion

If drag started within the application, the dragged items have identifiers, and SwiftUI has access to these identifiers, you can access them using this method.

Parameter type: The type of the identifiers. Returns: The array with the identifiers of the dragged items if provided. Returns an empty array if there are no dragged identifiers of a given type.
