---
title: 'buildLimitedAvailability(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.5+, iPadOS 17.5+, Mac Catalyst 17.5+, macOS 14.5+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/commandsbuilder/buildlimitedavailability(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/commandsbuilder/buildlimitedavailability(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/commandsbuilder/buildlimitedavailability%28_%3A%29.json'
content_hash: 'sha256:e36fd6ce7fd1b56c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CommandsBuilder](../commandsbuilder.md)

# buildLimitedAvailability(_:)

<sub>Type Method</sub>

Processes commands for a conditional compiler-control statement that performs an availability check.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) static func buildLimitedAvailability(_ content: any Commands) -> some Commands

```

## See Also

### Building conditionally

- [buildEither(first:)](<buildeither(first_).md>) — Produces content for a conditional statement in a multi-statement closure when the condition is true.
- [buildEither(second:)](<buildeither(second_).md>) — Produces content for a conditional statement in a multi-statement closure when the condition is false.
- [buildIf(_:)](<buildif(__).md>) — Produces an optional widget for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.
- [buildExpression(_:)](<buildexpression(__).md>) — Builds an expression within the builder.
