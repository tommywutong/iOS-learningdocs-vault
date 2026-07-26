---
title: 'init(transferable:in:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/init(transferable:in:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/init(transferable:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/init%28transferable%3Ain%3A%29.json'
content_hash: 'sha256:3ce5abcb76c387f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# init(transferable:in:)

<sub>Initializer</sub>

Extract an attributed string from SwiftUI’s transferable representation in a certain environment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(transferable: AttributedTextFormatting.Transferable, in environment: EnvironmentValues) throws
```

## Discussion

Use this initializer with a `AttributedTextFormatting/Transferable` that was imported, e.g. in the `action` closure of the `View/dropDestination(for:action:isTargeted)` modifier.

> [!note] Note
> This initializer applies the `AttributedTextFormattingDefinition` in the given `environment` to the imported text before returning.

> [!info] See Also
> `View/attributedTextFormattingDefinition(_:)-uc57`, `AttributedTextValueConstraint/constrain(_:)-6cp64`
