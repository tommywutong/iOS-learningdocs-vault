---
title: FocusedObject.Wrapper
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/focusedobject/wrapper
source_url: 'https://developer.apple.com/documentation/swiftui/focusedobject/wrapper'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/focusedobject/wrapper.json'
content_hash: 'sha256:719ebade3ee62a2d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FocusedObject](../focusedobject.md)

# FocusedObject.Wrapper

<sub>Structure</sub>

A wrapper around the underlying focused object that can create bindings to its properties using dynamic member lookup.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency @dynamicMemberLookup @frozen struct Wrapper
```

## Topics

### Accessing members

- [subscript(dynamicMember:)](<wrapper/subscript(dynamicmember_).md>) — Returns a binding to the value of a given key path.

## See Also

### Getting the value

- [projectedValue](projectedvalue.md) — A projection of the focused object that creates bindings to its properties using dynamic member lookup.
- [wrappedValue](wrappedvalue.md) — The underlying value referenced by the focused object.
