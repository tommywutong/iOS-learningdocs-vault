---
title: AttributedTextFormattingDefinition
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/attributedtextformattingdefinition
source_url: 'https://developer.apple.com/documentation/swiftui/attributedtextformattingdefinition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/attributedtextformattingdefinition.json'
content_hash: 'sha256:8916d712a9f3c794'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AttributedTextFormattingDefinition

<sub>Protocol</sub>

A protocol for defining how text can be styled in a view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol AttributedTextFormattingDefinition<Scope>
```

## Overview

A formatting definition consists of an attribute scope and a number of value constraints. It is applied to a view hierarchy using the [attributedTextFormattingDefinition(_:)](<view/attributedtextformattingdefinition(__)-81jn6.md>) view modifier and affects nested [Text](text.md) and [TextEditor](texteditor.md) views when initialized with [AttributedString](../foundation/attributedstring.md).

Create a formatting definition by first choosing an attribute scope that contains all attributes relevant for your view. All other attributes will be ignored by value constraints and by the affected views.

Use the `Foundation/AttributeScopes/SwiftUIAttributes` for the default set of attributes supported by SwiftUI. You can create your own scope only listing out a subset of the attributes in SwiftUI’s attribute scope. You can also include custom attributes in your scope. This allows you to take advantage of advanced attributed string features, such as [runBoundaries](../foundation/attributedstringkey/runboundaries.md).

Custom attributes also allow you to separate semantic information stored on the text, e.g. the information that a sequence of characters refers a specific person in contacts, from how this part of the text is to be formatted, e.g. with the foreground color “purple”. The rules defining what values attributes can have, are called [AttributedTextValueConstraint](attributedtextvalueconstraint.md)s.

```swift
struct ContactsArePurple: AttributedTextValueConstraint {
    typealias Scope = MyScope
    typealias AttributeKey = Scope.ForegroundColorAttribute

    func constrain(_ container: inout Attributes) {
        if container.annotation == .contact {
            container.foregroundColor = .purple
        } else {
            container.foregroundColor = nil
        }
    }
}
```

While associating formatting with custom semantic attributes is one important use case, value constraints are a generic mechanism for constraining the formatting that is available in a text editor - with or without dependencies on other attributes. For example, a value constraint could also be used to only allow a single, solid underline, but not a double underline or a dashed underline.

SwiftUI validates formatting UI provided by the system to the user to make sure only controls that are compatible with your formatting definition and its constraints are visible and enabled. If the system formatting UI does not provide sufficient utility based on your formatting definition, or you provide custom UI that is better tailored to your text editing experience, consider hiding the system-provided UI using the [textInputFormattingControlVisibility(_:for:)](<view/textinputformattingcontrolvisibility(__for_).md>) view modifier.

To declare the attributed text formatting definition, specify the attribute scope in the generic of the [body](attributedtextformattingdefinition/body-1b01t.md)’s type, and list all value constraints inside the [body](attributedtextformattingdefinition/body-1b01t.md) using result builder syntax:

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
        ContactsArePurple()
    }
}
```

Use the [attributedTextFormattingDefinition(_:)](<view/attributedtextformattingdefinition(__)-81jn6.md>) view modifier to apply the definition to a view.

## Relationships

- **Inherited By**: [AttributedTextValueConstraint](attributedtextvalueconstraint.md)

- **Conforming Types**: [AnyDefinition](attributedtextformatting/anydefinition.md), [EmptyDefinition](attributedtextformatting/emptydefinition.md), [TupleDefinition](attributedtextformatting/tupledefinition.md), [ValueConstraint](attributedtextformatting/valueconstraint.md)

## Topics

### Associated Types

- [Body](attributedtextformattingdefinition/body-swift.associatedtype.md) — The type of view representing the body of this formatting definition.
- [Scope](attributedtextformattingdefinition/scope.md) — The text formatting definition only allows usage of attributes in this attribute scope.

### Instance Properties

- [body](attributedtextformattingdefinition/body-1b01t.md) — The constraints of the formatting definition.

### Instance Methods

- [constrain(_:)](<attributedtextformattingdefinition/constrain(__).md>) — Applies all value constraints to a given attribute container.

### Type Aliases

- [ValueConstraint](attributedtextformattingdefinition/valueconstraint.md) — A text formatting definition that permits a single attribute to be used, optionally constrained to a set of values.

## See Also

### Controlling text style

- [bold(_:)](<view/bold(__).md>) — Applies a bold font weight to the text in this view.
- [italic(_:)](<view/italic(__).md>) — Applies italics to the text in this view.
- [underline(_:pattern:color:)](<view/underline(__pattern_color_).md>) — Applies an underline to the text in this view.
- [strikethrough(_:pattern:color:)](<view/strikethrough(__pattern_color_).md>) — Applies a strikethrough to the text in this view.
- [textCase(_:)](<view/textcase(__).md>) — Sets a transform for the case of the text contained in this view when displayed.
- [textCase](environmentvalues/textcase.md) — A stylistic override to transform the case of `Text` when displayed, using the environment’s locale.
- [monospaced(_:)](<view/monospaced(__).md>) — Modifies the fonts of all child views to use the fixed-width variant of the current font, if possible.
- [monospacedDigit()](<view/monospaceddigit().md>) — Modifies the fonts of all child views to use fixed-width digits, if possible, while leaving other characters proportionally spaced.
- [AttributedTextValueConstraint](attributedtextvalueconstraint.md) — A protocol for defining a constraint on the value of a certain attribute.
- [AttributedTextFormatting](attributedtextformatting.md) — A namespace for types related to attributed text formatting definitions.
