---
title: 'init(_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tablerow/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablerow/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablerow/init%28_%3A%29.json'
content_hash: 'sha256:cb18e43db3ba2c24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableRow](../tablerow.md)

# init(_:)

<sub>Initializer</sub>

Creates a table row for the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init(_ value: Value)
```

## Parameters

- `value` — The value of the row.

## Discussion

The table provides the value of a row to each column of a table, which produces the cells for each row in the column.

The following example creates a row for one instance of the `Person` type. The table delivers this value to its columns, which displays different fields of `Person`.

```swift
 TableRow(Person(givenName: "Tom", familyName: "Clark"))
```
