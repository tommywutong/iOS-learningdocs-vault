---
title: AutomaticFormStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/automaticformstyle
source_url: 'https://developer.apple.com/documentation/swiftui/automaticformstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/automaticformstyle.json'
content_hash: 'sha256:4dfa7a03fce03ff6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AutomaticFormStyle

<sub>Structure</sub>

The default form style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated struct AutomaticFormStyle
```

## Overview

Use the [automatic](formstyle/automatic.md) static variable to create this style:

```swift
Form {
   ...
}
.formStyle(.automatic)
```

## Relationships

- **Conforms To**: [FormStyle](formstyle.md)

## Topics

### Creating the form style

- [init()](<automaticformstyle/init().md>) — Creates a default form style.

## See Also

### Supporting types

- [ColumnsFormStyle](columnsformstyle.md) — A non-scrolling form style with a trailing aligned column of labels next to a leading aligned column of values.
- [GroupedFormStyle](groupedformstyle.md) — A form style with grouped rows.
