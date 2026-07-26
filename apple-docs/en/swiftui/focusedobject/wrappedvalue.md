---
title: wrappedValue
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/focusedobject/wrappedvalue
source_url: 'https://developer.apple.com/documentation/swiftui/focusedobject/wrappedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/focusedobject/wrappedvalue.json'
content_hash: 'sha256:a4e3abf648518940'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FocusedObject](../focusedobject.md)

# wrappedValue

<sub>Instance Property</sub>

The underlying value referenced by the focused object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency var wrappedValue: ObjectType? { get }
```

## Discussion

This property provides primary access to the value’s data. However, you don’t access `wrappedValue` directly. Instead, you use the property variable created with the [FocusedObject](../focusedobject.md) attribute.

When a mutable value changes, the new value is immediately available. However, a view displaying the value is updated asynchronously and may not show the new value immediately.

## See Also

### Getting the value

- [projectedValue](projectedvalue.md) — A projection of the focused object that creates bindings to its properties using dynamic member lookup.
- [Wrapper](wrapper.md) — A wrapper around the underlying focused object that can create bindings to its properties using dynamic member lookup.
