---
title: 'init(_:isExpanded:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/disclosuretablerow/init(_:isexpanded:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/disclosuretablerow/init(_:isexpanded:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/disclosuretablerow/init%28_%3Aisexpanded%3Acontent%3A%29.json'
content_hash: 'sha256:92d7d9a87e033730'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DisclosureTableRow](../disclosuretablerow.md)

# init(_:isExpanded:content:)

<sub>Initializer</sub>

Creates a disclosure group with the given value and table rows, and a binding to the expansion state (expanded or collapsed).

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init<Value>(_ value: Value, isExpanded: Binding<Bool>? = nil, @TableRowBuilder<Value> content: @escaping () -> Content) where Label == TableRow<Value>, Value == Content.TableRowValue
```

## Parameters

- `value` — The value of the disclosable table row.

- `isExpanded` — A binding to a Boolean value that determines the group’s expansion state (expanded or collapsed).

- `content` — The table row shown when the disclosure group expands.
