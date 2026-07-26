---
title: 'buildIf(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tablerowbuilder/buildif(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablerowbuilder/buildif(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablerowbuilder/buildif%28_%3A%29.json'
content_hash: 'sha256:781f592f95cd00fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableRowBuilder](../tablerowbuilder.md)

# buildIf(_:)

<sub>Type Method</sub>

Creates a row result for conditional statements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) static func buildIf<C>(_ content: C?) -> C? where Value == C.TableRowValue, C : TableRowContent
```

## Discussion

This method provides support for “if” statements in multi-statement closures, producing an optional value that is visible only when the condition evaluates to `true`.

## See Also

### Building a row from conditionals

- [buildEither(first:)](<buildeither(first_).md>) — Creates a row result for the first of two row content alternatives.
- [buildEither(second:)](<buildeither(second_).md>) — Creates a row result for the second of two row content alternatives.
- [buildExpression(_:)](<buildexpression(__).md>) — Builds an expression within the builder.
