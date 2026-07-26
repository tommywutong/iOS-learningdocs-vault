---
title: 'onInsert(of:perform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/dynamicviewcontent/oninsert(of:perform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/dynamicviewcontent/oninsert(of:perform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dynamicviewcontent/oninsert%28of%3Aperform%3A%29.json'
content_hash: 'sha256:16a44ac317c7fce8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DynamicViewContent](../dynamicviewcontent.md)

# onInsert(of:perform:)

<sub>Instance Method</sub>

Sets the insert action for the dynamic view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func onInsert(of supportedContentTypes: [UTType], perform action: @escaping (Int, [NSItemProvider]) -> Void) -> some DynamicViewContent

```

## Parameters

- `supportedContentTypes` — An array of UTI types that the dynamic view supports.

- `action` — A closure that SwiftUI invokes when elements are added to the view. The closure takes two arguments: The first argument is the offset relative to the dynamic view’s underlying collection of data. The second argument is an array of [NSItemProvider](../../foundation/nsitemprovider.md) items that represents the data that you want to insert.

## Return Value

A view that calls `action` when elements are inserted into the original view.

## See Also

### Responding to updates

- [onDelete(perform:)](<ondelete(perform_).md>) — Sets the deletion action for the dynamic view. You must delete the corresponding item within `action`, as it will be called after the row has already been removed from the [List](../list.md).
- [onMove(perform:)](<onmove(perform_).md>) — Sets the move action for the dynamic view.
- [dropDestination(for:action:)](<dropdestination(for_action_).md>) — Sets the insert action for the dynamic view.
