---
title: DynamicViewContent
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dynamicviewcontent
source_url: 'https://developer.apple.com/documentation/swiftui/dynamicviewcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dynamicviewcontent.json'
content_hash: 'sha256:737e6d2f6932b759'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DynamicViewContent

<sub>Protocol</sub>

A type of view that generates views from an underlying collection of data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol DynamicViewContent<Data> : View
```

## Relationships

- **Inherits From**: [View](view.md)

- **Conforming Types**: [ForEach](foreach.md), [ModifiedContent](modifiedcontent.md)

## Topics

### Managing the data

- [data](dynamicviewcontent/data-swift.property.md) — The collection of underlying data.
- [Data](dynamicviewcontent/data-swift.associatedtype.md) — The type of the underlying collection of data.

### Responding to updates

- [onDelete(perform:)](<dynamicviewcontent/ondelete(perform_).md>) — Sets the deletion action for the dynamic view. You must delete the corresponding item within `action`, as it will be called after the row has already been removed from the [List](list.md).
- [onInsert(of:perform:)](<dynamicviewcontent/oninsert(of_perform_).md>) — Sets the insert action for the dynamic view.
- [onMove(perform:)](<dynamicviewcontent/onmove(perform_).md>) — Sets the move action for the dynamic view.
- [dropDestination(for:action:)](<dynamicviewcontent/dropdestination(for_action_).md>) — Sets the insert action for the dynamic view.

### Reordering

- [reorderable()](<dynamicviewcontent/reorderable().md>) — Enables reordering of views from this content inside the scope of a reorderable container modifier. _(beta)_
- [reorderable(collectionID:)](<dynamicviewcontent/reorderable(collectionid_).md>) — Enables reordering views from this content within and between sections in the scope of a reorderable container modifier. _(beta)_

### Deprecated symbols

- [onInsert(of:perform:)](<dynamicviewcontent/oninsert(of_perform_)-40hwa.md>) — Sets the insert action for the dynamic view. _(deprecated)_

## See Also

### Iterating over dynamic data

- [ForEach](foreach.md) — A structure that computes views on demand from an underlying collection of identified data.
- [ForEachSectionCollection](foreachsectioncollection.md) — A collection which allows a view to be treated as a collection of its sections in a for each loop.
- [ForEachSubviewCollection](foreachsubviewcollection.md) — A collection which allows a view to be treated as a collection of its subviews in a for each loop.
