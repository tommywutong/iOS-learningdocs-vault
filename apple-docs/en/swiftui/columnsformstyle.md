---
title: ColumnsFormStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/columnsformstyle
source_url: 'https://developer.apple.com/documentation/swiftui/columnsformstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/columnsformstyle.json'
content_hash: 'sha256:fe305100547c9cc2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ColumnsFormStyle

<sub>Structure</sub>

A non-scrolling form style with a trailing aligned column of labels next to a leading aligned column of values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated struct ColumnsFormStyle
```

## Overview

Use the [columns](formstyle/columns.md) static variable to create this style:

```swift
Form {
   ...
}
.formStyle(.columns)
```

## Relationships

- **Conforms To**: [FormStyle](formstyle.md)

## Topics

### Creating the form style

- [init()](<columnsformstyle/init().md>) — A non-scrolling form style with a trailing aligned column of labels next to a leading aligned column of values.

## See Also

### Supporting types

- [AutomaticFormStyle](automaticformstyle.md) — The default form style.
- [GroupedFormStyle](groupedformstyle.md) — A form style with grouped rows.
