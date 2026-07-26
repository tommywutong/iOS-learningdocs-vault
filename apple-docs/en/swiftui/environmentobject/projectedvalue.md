---
title: projectedValue
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentobject/projectedvalue
source_url: 'https://developer.apple.com/documentation/swiftui/environmentobject/projectedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentobject/projectedvalue.json'
content_hash: 'sha256:52506c552b395857'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentObject](../environmentobject.md)

# projectedValue

<sub>Instance Property</sub>

A projection of the environment object that creates bindings to its properties using dynamic member lookup.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency var projectedValue: EnvironmentObject<ObjectType>.Wrapper { get }
```

## Discussion

Use the projected value to pass an environment object down a view hierarchy.

## See Also

### Getting the value

- [wrappedValue](wrappedvalue.md) — The underlying value referenced by the environment object.
- [Wrapper](wrapper.md) — A wrapper of the underlying environment object that can create bindings to its properties using dynamic member lookup.
