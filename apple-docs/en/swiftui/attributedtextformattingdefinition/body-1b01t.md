---
title: body
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/attributedtextformattingdefinition/body-1b01t
source_url: 'https://developer.apple.com/documentation/swiftui/attributedtextformattingdefinition/body-1b01t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/attributedtextformattingdefinition/body-1b01t.json'
content_hash: 'sha256:b43de0b443d69865'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AttributedTextFormattingDefinition](../attributedtextformattingdefinition.md)

# body

<sub>Instance Property</sub>

The constraints of the formatting definition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@AttributedTextFormatting.DefinitionBuilder<Self.Scope> var body: Self.Body { get }
```

## Discussion

When you implement a custom definition, you must implement a computed `body` property to provide the constraints of your definition. Return a definition that’s composed of built-in definitions that SwiftUI provides, such as [ValueConstraint](valueconstraint.md) and [AttributedTextValueConstraint](../attributedtextvalueconstraint.md)s, plus other composite [AttributedTextFormattingDefinition](../attributedtextformattingdefinition.md)s that you’ve already defined:

```swift
struct MyTextFormattingDefinition: AttributedTextFormattingDefinition {
    var body: some AttributedTextFormattingDefinition<
        AttributeScopes.SwiftUIAttributes
    > {
        ValueConstraint(
            for: \.underlineStyle,
            values: [nil, .single],
            default: .single)
        MyAttributedTextValueConstraint()
    }
}
```

Note that the order of the constraints in the result builder matters as constraints are applied in order. For details, see `AttributedTextValueConstraint/constrain(_:)-(Attributes)`.

## Default Implementations

### AttributedTextFormattingDefinition Implementations

- [body](body-48m9l.md)
