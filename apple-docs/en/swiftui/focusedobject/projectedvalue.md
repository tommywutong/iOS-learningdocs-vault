---
title: projectedValue
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/focusedobject/projectedvalue
source_url: 'https://developer.apple.com/documentation/swiftui/focusedobject/projectedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/focusedobject/projectedvalue.json'
content_hash: 'sha256:28a9f530fea3e3dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FocusedObject](../focusedobject.md)

# projectedValue

<sub>Instance Property</sub>

A projection of the focused object that creates bindings to its properties using dynamic member lookup.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency var projectedValue: FocusedObject<ObjectType>.Wrapper? { get }
```

## Discussion

Use the projected value to pass a focused object down a view hierarchy.

## See Also

### Getting the value

- [wrappedValue](wrappedvalue.md) — The underlying value referenced by the focused object.
- [Wrapper](wrapper.md) — A wrapper around the underlying focused object that can create bindings to its properties using dynamic member lookup.
