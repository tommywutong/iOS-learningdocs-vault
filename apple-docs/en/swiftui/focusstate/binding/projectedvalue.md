---
title: projectedValue
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/focusstate/binding/projectedvalue
source_url: 'https://developer.apple.com/documentation/swiftui/focusstate/binding/projectedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/focusstate/binding/projectedvalue.json'
content_hash: 'sha256:5a7755cece27b8da'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [FocusState](../../focusstate.md) · [Binding](../binding.md)

# projectedValue

<sub>Instance Property</sub>

A projection of the binding value that returns a binding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var projectedValue: FocusState<Value>.Binding { get }
```

## Discussion

Use the projected value to pass a binding value down a view hierarchy.

## See Also

### Inspecting the binding

- [wrappedValue](wrappedvalue.md) — The underlying value referenced by the bound property.
