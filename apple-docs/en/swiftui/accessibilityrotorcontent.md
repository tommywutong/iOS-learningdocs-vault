---
title: AccessibilityRotorContent
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/accessibilityrotorcontent
source_url: 'https://developer.apple.com/documentation/swiftui/accessibilityrotorcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessibilityrotorcontent.json'
content_hash: 'sha256:93fb098c2aee124e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AccessibilityRotorContent

<sub>Protocol</sub>

Content within an accessibility rotor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency protocol AccessibilityRotorContent
```

## Overview

Generally generated from control flow constructs like `ForEach` and `if`, and `AccessibilityRotorEntry`.

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

- **Conforming Types**: [AccessibilityRotorEntry](accessibilityrotorentry.md), [ForEach](foreach.md), [Group](group.md), [TupleContent](tuplecontent.md)

## Topics

### Supporting types

- [body](accessibilityrotorcontent/body-swift.property.md) — The internal content of this `AccessibilityRotorContent`.
- [Body](accessibilityrotorcontent/body-swift.associatedtype.md) — The type for the internal content of this `AccessibilityRotorContent`.

## See Also

### Creating rotors

- [AccessibilityRotorContentBuilder](accessibilityrotorcontentbuilder.md) — Result builder you use to generate rotor entry content.
- [AccessibilityRotorEntry](accessibilityrotorentry.md) — A struct representing an entry in an Accessibility Rotor.
