---
title: FocusState.Binding
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/focusstate/binding
source_url: 'https://developer.apple.com/documentation/swiftui/focusstate/binding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/focusstate/binding.json'
content_hash: 'sha256:f46cc3148049619b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FocusState](../focusstate.md)

# FocusState.Binding

<sub>Structure</sub>

A property wrapper type that can read and write a value that indicates the current focus location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen @propertyWrapper struct Binding
```

## Topics

### Inspecting the binding

- [projectedValue](binding/projectedvalue.md) — A projection of the binding value that returns a binding.
- [wrappedValue](binding/wrappedvalue.md) — The underlying value referenced by the bound property.

## See Also

### Inspecting the focus state

- [projectedValue](projectedvalue.md) — A projection of the focus state value that returns a binding.
- [wrappedValue](wrappedvalue.md) — The current state value, taking into account whatever bindings might be in effect due to the current location of focus.
