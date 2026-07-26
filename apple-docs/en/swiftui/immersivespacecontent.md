---
title: ImmersiveSpaceContent
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [macOS 26.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/immersivespacecontent
source_url: 'https://developer.apple.com/documentation/swiftui/immersivespacecontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/immersivespacecontent.json'
content_hash: 'sha256:78c143193e3a972b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ImmersiveSpaceContent

<sub>Protocol</sub>

A type that you can use as the content of an immersive space.

<sub>macOS, visionOS</sub>

```swift
@MainActor @preconcurrency protocol ImmersiveSpaceContent
```

## Overview

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Relationships

- **Conforming Types**: [Content](compositorcontentbuilder/content.md), [ImmersiveSpaceViewContent](immersivespaceviewcontent.md)

## Topics

### Creating immersive space content

- [body](immersivespacecontent/body-swift.property.md)
- [Body](immersivespacecontent/body-swift.associatedtype.md)

## See Also

### Supporting types

- [ImmersiveSpaceViewContent](immersivespaceviewcontent.md) — Immersive space content that uses a SwiftUI view hierarchy as the content.
