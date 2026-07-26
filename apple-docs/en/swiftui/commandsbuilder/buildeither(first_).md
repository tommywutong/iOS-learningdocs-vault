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
doc_path: '/documentation/swiftui/commandsbuilder/buildeither(first:)'
source_url: 'https://developer.apple.com/documentation/swiftui/commandsbuilder/buildeither(first:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/commandsbuilder/buildeither%28first%3A%29.json'
content_hash: 'sha256:343ff1a01369e91f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CommandsBuilder](../commandsbuilder.md)

# buildEither(first:)

<sub>Type Method</sub>

Produces content for a conditional statement in a multi-statement closure when the condition is true.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F> where T : Commands, F : Commands
```

## See Also

### Building conditionally

- [buildEither(second:)](<buildeither(second_).md>) — Produces content for a conditional statement in a multi-statement closure when the condition is false.
- [buildIf(_:)](<buildif(__).md>) — Produces an optional widget for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.
- [buildLimitedAvailability(_:)](<buildlimitedavailability(__).md>) — Processes commands for a conditional compiler-control statement that performs an availability check.
- [buildExpression(_:)](<buildexpression(__).md>) — Builds an expression within the builder.
