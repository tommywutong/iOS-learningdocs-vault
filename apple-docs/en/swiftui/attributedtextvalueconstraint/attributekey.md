---
title: AttributeKey
framework: SwiftUI
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/attributedtextvalueconstraint/attributekey
source_url: 'https://developer.apple.com/documentation/swiftui/attributedtextvalueconstraint/attributekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/attributedtextvalueconstraint/attributekey.json'
content_hash: 'sha256:b8a04462839a8af5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AttributedTextValueConstraint](../attributedtextvalueconstraint.md)

# AttributeKey

<sub>Associated Type</sub>

The attribute constrained by this constraint.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype AttributeKey : AttributedStringKey where Self.AttributeKey.Value : Sendable
```

## Discussion

> [!note] Note
> This attribute must always be part of the associated `Scope`.
