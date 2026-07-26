---
title: 'buildIf(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, visionOS 1.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tablecolumnbuilder/buildif(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablecolumnbuilder/buildif(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablecolumnbuilder/buildif%28_%3A%29.json'
content_hash: 'sha256:afa46484b519b775'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableColumnBuilder](../tablecolumnbuilder.md)

# buildIf(_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) static func buildIf<C>(_ content: C?) -> C? where RowValue == C.TableRowValue, C : TableColumnContent, C.TableColumnSortComparator == Never
```
