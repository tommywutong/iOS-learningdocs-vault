---
title: EnvironmentObject.Wrapper
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentobject/wrapper
source_url: 'https://developer.apple.com/documentation/swiftui/environmentobject/wrapper'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentobject/wrapper.json'
content_hash: 'sha256:11e93d66c6fe078b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentObject](../environmentobject.md)

# EnvironmentObject.Wrapper

<sub>Structure</sub>

A wrapper of the underlying environment object that can create bindings to its properties using dynamic member lookup.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @dynamicMemberLookup @frozen @preconcurrency struct Wrapper
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting a binding value

- [subscript(dynamicMember:)](<wrapper/subscript(dynamicmember_).md>) — Returns a binding to the resulting value of a given key path.

## See Also

### Getting the value

- [wrappedValue](wrappedvalue.md) — The underlying value referenced by the environment object.
- [projectedValue](projectedvalue.md) — A projection of the environment object that creates bindings to its properties using dynamic member lookup.
