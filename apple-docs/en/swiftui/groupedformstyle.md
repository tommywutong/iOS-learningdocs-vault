---
title: GroupedFormStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/groupedformstyle
source_url: 'https://developer.apple.com/documentation/swiftui/groupedformstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/groupedformstyle.json'
content_hash: 'sha256:cce0782c79ac08ef'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# GroupedFormStyle

<sub>Structure</sub>

A form style with grouped rows.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated struct GroupedFormStyle
```

## Overview

Rows in this form style have leading aligned labels and trailing aligned controls within visually grouped sections.

Use the [grouped](formstyle/grouped.md) static variable to create this style:

```swift
Form {
   ...
}
.formStyle(.grouped)
```

## Relationships

- **Conforms To**: [FormStyle](formstyle.md)

## Topics

### Creating the form style

- [init()](<groupedformstyle/init().md>) — Creates a form style with scrolling, grouped rows.

## See Also

### Supporting types

- [AutomaticFormStyle](automaticformstyle.md) — The default form style.
- [ColumnsFormStyle](columnsformstyle.md) — A non-scrolling form style with a trailing aligned column of labels next to a leading aligned column of values.
