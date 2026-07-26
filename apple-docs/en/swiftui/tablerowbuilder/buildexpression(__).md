---
title: 'buildExpression(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tablerowbuilder/buildexpression(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablerowbuilder/buildexpression(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablerowbuilder/buildexpression%28_%3A%29.json'
content_hash: 'sha256:da6c7c266f595981'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableRowBuilder](../tablerowbuilder.md)

# buildExpression(_:)

<sub>Type Method</sub>

Builds an expression within the builder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) static func buildExpression<Content>(_ content: Content) -> Content where Value == Content.TableRowValue, Content : TableRowContent
```

## See Also

### Building a row from conditionals

- [buildIf(_:)](<buildif(__).md>) — Creates a row result for conditional statements.
- [buildEither(first:)](<buildeither(first_).md>) — Creates a row result for the first of two row content alternatives.
- [buildEither(second:)](<buildeither(second_).md>) — Creates a row result for the second of two row content alternatives.
