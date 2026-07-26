---
title: 'onMove(perform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/dynamicviewcontent/onmove(perform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/dynamicviewcontent/onmove(perform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dynamicviewcontent/onmove%28perform%3A%29.json'
content_hash: 'sha256:478100853871ca2b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DynamicViewContent](../dynamicviewcontent.md)

# onMove(perform:)

<sub>Instance Method</sub>

Sets the move action for the dynamic view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func onMove(perform action: Optional<(IndexSet, Int) -> Void>) -> some DynamicViewContent

```

## Parameters

- `action` — A closure that SwiftUI invokes when elements in the dynamic view are moved. The closure takes two arguments that represent the offset relative to the dynamic view’s underlying collection of data. Pass `nil` to disable the ability to move items.

## Return Value

A view that calls `action` when elements are moved within the original view.

## See Also

### Responding to updates

- [onDelete(perform:)](<ondelete(perform_).md>) — Sets the deletion action for the dynamic view. You must delete the corresponding item within `action`, as it will be called after the row has already been removed from the [List](../list.md).
- [onInsert(of:perform:)](<oninsert(of_perform_).md>) — Sets the insert action for the dynamic view.
- [dropDestination(for:action:)](<dropdestination(for_action_).md>) — Sets the insert action for the dynamic view.
