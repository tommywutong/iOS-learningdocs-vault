---
title: CustomLeafReflectable
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/customleafreflectable
source_url: 'https://developer.apple.com/documentation/swift/customleafreflectable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/customleafreflectable.json'
content_hash: 'sha256:03d2478e485ec395'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# CustomLeafReflectable

<sub>Protocol</sub>

A type that explicitly supplies its own mirror, but whose descendant classes are not represented in the mirror unless they also override `customMirror`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol CustomLeafReflectable : CustomReflectable
```

## Relationships

- **Inherits From**: [CustomReflectable](customreflectable.md)

## See Also

### Customizing Your Type’s Reflection

- [CustomReflectable](customreflectable.md) — A type that explicitly supplies its own mirror.
- [CustomPlaygroundDisplayConvertible](customplaygrounddisplayconvertible.md) — A type that supplies a custom description for playground logging.
- [PlaygroundQuickLook](playgroundquicklook.md) — The sum of types that can be used as a Quick Look representation.
- [DebugDescription()](<debugdescription().md>) — Converts description definitions to a debugger Type Summary.
