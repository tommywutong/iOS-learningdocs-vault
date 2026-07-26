---
title: Body
framework: SwiftUI
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/commands/body-swift.associatedtype
source_url: 'https://developer.apple.com/documentation/swiftui/commands/body-swift.associatedtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/commands/body-swift.associatedtype.json'
content_hash: 'sha256:58b24c0c675ef67f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Commands](../commands.md)

# Body

<sub>Associated Type</sub>

The type of commands that represents the body of this command hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
associatedtype Body : Commands
```

## Discussion

When you create custom commands, Swift infers this type from your implementation of the required [body](body-swift.property.md) property.

## See Also

### Implementing commands

- [body](body-swift.property.md) — The contents of the command hierarchy.
