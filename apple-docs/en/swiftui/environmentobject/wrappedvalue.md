---
title: wrappedValue
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentobject/wrappedvalue
source_url: 'https://developer.apple.com/documentation/swiftui/environmentobject/wrappedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentobject/wrappedvalue.json'
content_hash: 'sha256:c699da77eb76c4b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentObject](../environmentobject.md)

# wrappedValue

<sub>Instance Property</sub>

The underlying value referenced by the environment object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency var wrappedValue: ObjectType { get }
```

## Discussion

This property provides primary access to the value’s data. However, you don’t access `wrappedValue` directly. Instead, you use the property variable created with the [EnvironmentObject](../environmentobject.md) attribute.

When a mutable value changes, the new value is immediately available. However, a view displaying the value is updated asynchronously and may not show the new value immediately.

## See Also

### Getting the value

- [projectedValue](projectedvalue.md) — A projection of the environment object that creates bindings to its properties using dynamic member lookup.
- [Wrapper](wrapper.md) — A wrapper of the underlying environment object that can create bindings to its properties using dynamic member lookup.
