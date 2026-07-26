---
title: 'constrain(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/attributedtextformattingdefinition/constrain(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/attributedtextformattingdefinition/constrain(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/attributedtextformattingdefinition/constrain%28_%3A%29.json'
content_hash: 'sha256:84d0d2f253b297c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AttributedTextFormattingDefinition](../attributedtextformattingdefinition.md)

# constrain(_:)

<sub>Instance Method</sub>

Applies all value constraints to a given attribute container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func constrain(_ container: inout AttributeContainer)
```

## Discussion

Modifies the given `container` by applying all [AttributedTextValueConstraint](../attributedtextvalueconstraint.md)s that are part of this definition to the container.

Use this function to test your [AttributedTextFormattingDefinition](../attributedtextformattingdefinition.md), or to ensure your constraints are applied before passing content to API that cannot itself apply the definition.
