---
title: 'buildEither(first:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tablerowbuilder/buildeither(first:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablerowbuilder/buildeither(first:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablerowbuilder/buildeither%28first%3A%29.json'
content_hash: 'sha256:8d9e4c50f87e0733'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableRowBuilder](../tablerowbuilder.md)

# buildEither(first:)

<sub>Type Method</sub>

Creates a row result for the first of two row content alternatives.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F> where Value == T.TableRowValue, T : TableRowContent, F : TableRowContent, T.TableRowValue == F.TableRowValue
```

## Discussion

This method provides support for “if” statements in multi-statement closures, producing conditional content for the “then” branch.

## See Also

### Building a row from conditionals

- [buildIf(_:)](<buildif(__).md>) — Creates a row result for conditional statements.
- [buildEither(second:)](<buildeither(second_).md>) — Creates a row result for the second of two row content alternatives.
- [buildExpression(_:)](<buildexpression(__).md>) — Builds an expression within the builder.
