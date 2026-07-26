---
title: 'onDelete(perform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/dynamicviewcontent/ondelete(perform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/dynamicviewcontent/ondelete(perform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dynamicviewcontent/ondelete%28perform%3A%29.json'
content_hash: 'sha256:1e47f88103714d7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DynamicViewContent](../dynamicviewcontent.md)

# onDelete(perform:)

<sub>Instance Method</sub>

Sets the deletion action for the dynamic view. You must delete the corresponding item within `action`, as it will be called after the row has already been removed from the [List](../list.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func onDelete(perform action: Optional<(IndexSet) -> Void>) -> some DynamicViewContent

```

## Parameters

- `action` — The action that you want SwiftUI to perform when elements in the view are deleted. SwiftUI passes a set of indices to the closure that’s relative to the dynamic view’s underlying collection of data.

## Return Value

A view that calls `action` when elements are deleted from the original view.

## See Also

### Responding to updates

- [onInsert(of:perform:)](<oninsert(of_perform_).md>) — Sets the insert action for the dynamic view.
- [onMove(perform:)](<onmove(perform_).md>) — Sets the move action for the dynamic view.
- [dropDestination(for:action:)](<dropdestination(for_action_).md>) — Sets the insert action for the dynamic view.
