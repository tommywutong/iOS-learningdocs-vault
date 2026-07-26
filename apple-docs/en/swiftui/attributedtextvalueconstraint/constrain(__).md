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
doc_path: '/documentation/swiftui/attributedtextvalueconstraint/constrain(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/attributedtextvalueconstraint/constrain(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/attributedtextvalueconstraint/constrain%28_%3A%29.json'
content_hash: 'sha256:b14a7340e7dd590e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AttributedTextValueConstraint](../attributedtextvalueconstraint.md)

# constrain(_:)

<sub>Instance Method</sub>

Enforce constraints on the attribute.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func constrain(_ container: inout Self.Attributes)
```

## Discussion

A function that transforms the [AttributeKey](attributekey.md) on the given `container` so it represents a formatting that the conforming type defines to be valid.

This function can generally read any attribute on `container` and it will produce a value that has been constrained by all [AttributedTextValueConstraint](../attributedtextvalueconstraint.md) listed in the associated text formatting definition above the constraint reading the attribute.

Consider the following example:

```swift
struct NoEqualForegroundAndBackground: AttributedTextValueConstraint {
    typealias Scope = MyTextFormattingDefinition.Scope
    typealias AttributeKey = AttributeScopes.SwiftUIAttributes.BackgroundColorAttribute

    func constrain(
        _ container: inout Attributes
    ) {
        if let color = container.foregroundColor,
           container.backgroundColor == color
        {
            container.backgroundColor = nil
        }
    }
}
```

When this constrain function accesses `container.foregroundColor`, the system establishes that the background color depends on the foreground color. At that time, it checks if the [AttributedTextFormattingDefinition](../attributedtextformattingdefinition.md) this constraint is part of defines constraints on the foreground color _above_ `NoEqualForegroundAndBackground` and applies them. Thus, when the access to `container.foregroundColor` returns, this function reads the constrained value.
