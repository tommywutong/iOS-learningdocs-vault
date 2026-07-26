---
title: ObservedObject.Wrapper
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/observedobject/wrapper
source_url: 'https://developer.apple.com/documentation/swiftui/observedobject/wrapper'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/observedobject/wrapper.json'
content_hash: 'sha256:f8a86f122c77b990'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ObservedObject](../observedobject.md)

# ObservedObject.Wrapper

<sub>Structure</sub>

A wrapper of the underlying observable object that can create bindings to its properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @dynamicMemberLookup @preconcurrency @frozen struct Wrapper
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Subscripts

- [subscript(dynamicMember:)](<wrapper/subscript(dynamicmember_).md>) — Gets a binding to the value of a specified key path.

## See Also

### Getting the value

- [wrappedValue](wrappedvalue.md) — The underlying value that the observed object references.
- [projectedValue](projectedvalue.md) — A projection of the observed object that creates bindings to its properties.
