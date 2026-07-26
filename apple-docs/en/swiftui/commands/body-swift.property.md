---
title: body
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/commands/body-swift.property
source_url: 'https://developer.apple.com/documentation/swiftui/commands/body-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/commands/body-swift.property.json'
content_hash: 'sha256:20feed054a8fd033'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Commands](../commands.md)

# body

<sub>Instance Property</sub>

The contents of the command hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@ContentBuilder @MainActor @preconcurrency var body: Self.Body { get }
```

## Discussion

For any commands that you create, provide a computed `body` property that defines the scene as a composition of other scenes. You can assemble a command hierarchy from built-in commands that SwiftUI provides, as well as other commands that you’ve defined.

## See Also

### Implementing commands

- [Body](body-swift.associatedtype.md) — The type of commands that represents the body of this command hierarchy.
