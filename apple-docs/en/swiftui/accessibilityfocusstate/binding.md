---
title: AccessibilityFocusState.Binding
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/accessibilityfocusstate/binding
source_url: 'https://developer.apple.com/documentation/swiftui/accessibilityfocusstate/binding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessibilityfocusstate/binding.json'
content_hash: 'sha256:fa254b03832ae55c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AccessibilityFocusState](../accessibilityfocusstate.md)

# AccessibilityFocusState.Binding

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@propertyWrapper @frozen struct Binding
```

## Topics

### Getting the state

- [projectedValue](binding/projectedvalue.md) — The currently focused element.
- [wrappedValue](binding/wrappedvalue.md) — The underlying value referenced by the bound property.

## See Also

### Getting the state

- [projectedValue](projectedvalue.md) — A projection of the state value that can be used to establish bindings between view content and accessibility focus placement.
- [wrappedValue](wrappedvalue.md) — The current state value, taking into account whatever bindings might be in effect due to the current location of focus.
