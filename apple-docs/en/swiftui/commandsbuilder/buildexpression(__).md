---
title: 'buildExpression(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/commandsbuilder/buildexpression(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/commandsbuilder/buildexpression(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/commandsbuilder/buildexpression%28_%3A%29.json'
content_hash: 'sha256:5c006785f7d5ce33'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CommandsBuilder](../commandsbuilder.md)

# buildExpression(_:)

<sub>Type Method</sub>

Builds an expression within the builder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) static func buildExpression<Content>(_ content: Content) -> Content where Content : Commands
```

## See Also

### Building conditionally

- [buildEither(first:)](<buildeither(first_).md>) — Produces content for a conditional statement in a multi-statement closure when the condition is true.
- [buildEither(second:)](<buildeither(second_).md>) — Produces content for a conditional statement in a multi-statement closure when the condition is false.
- [buildIf(_:)](<buildif(__).md>) — Produces an optional widget for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.
- [buildLimitedAvailability(_:)](<buildlimitedavailability(__).md>) — Processes commands for a conditional compiler-control statement that performs an availability check.
