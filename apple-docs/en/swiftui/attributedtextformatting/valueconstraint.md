---
title: AttributedTextFormatting.ValueConstraint
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/attributedtextformatting/valueconstraint
source_url: 'https://developer.apple.com/documentation/swiftui/attributedtextformatting/valueconstraint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/attributedtextformatting/valueconstraint.json'
content_hash: 'sha256:35601fc1af8c2322'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AttributedTextFormatting](../attributedtextformatting.md)

# AttributedTextFormatting.ValueConstraint

<sub>Structure</sub>

A text formatting definition that constrains the value of a single attribute to the members of a set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ValueConstraint<Scope, AttributeKey> where Scope : AttributeScope, AttributeKey : AttributedStringKey, AttributeKey.Value : Sendable
```

## Overview

```swift
struct MyTextFormattingDefinition: AttributedTextFormattingDefinition {
    var body: some AttributedTextFormattingDefinition<
        AttributeScopes.SwiftUIAttributes
    > {
        // Allow no underline or the `.single` underline style. If
        // a text has any other underline style, it is corrected
        // to the default value `.single`
        ValueConstraint(
            for: \.underlineStyle,
            values: [nil, .single],
            default: .single)
    }
}
```

## Relationships

- **Conforms To**: [AttributedTextFormattingDefinition](../attributedtextformattingdefinition.md), [AttributedTextValueConstraint](../attributedtextvalueconstraint.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(for:values:default:)](<valueconstraint/init(for_values_default_).md>) — Create a definition that constrains an attribute’s value to a defined set of allowed values.
