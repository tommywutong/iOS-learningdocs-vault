---
title: 'onInsert(of:perform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/dynamictablerowcontent/oninsert(of:perform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/dynamictablerowcontent/oninsert(of:perform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dynamictablerowcontent/oninsert%28of%3Aperform%3A%29.json'
content_hash: 'sha256:26da405b39560775'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DynamicTableRowContent](../dynamictablerowcontent.md)

# onInsert(of:perform:)

<sub>Instance Method</sub>

Sets the insert action for the dynamic table rows.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func onInsert(of supportedContentTypes: [UTType], perform action: @escaping (Int, [NSItemProvider]) -> Void) -> ModifiedContent<Self, OnInsertTableRowModifier>
```

## Parameters

- `supportedContentTypes` — An array of universal type identifiers types that the rows supports.

- `action` — A closure that SwiftUI invokes when adding elements to the collection of rows. The closure takes two arguments. The first argument is the offset relative to the dynamic view’s underlying collection of data. The second argument is an array of [NSItemProvider](../../foundation/nsitemprovider.md) items that represents the data that you want to insert.

## Return Value

A view that calls `action` when inserting elements into the original view.

## See Also

### Inserting rows

- [OnInsertTableRowModifier](../oninserttablerowmodifier.md) — A table row modifier that adds the ability to insert data in some base row content.
