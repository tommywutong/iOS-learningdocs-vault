---
title: wrappedValue
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/accessibilityfocusstate/wrappedvalue
source_url: 'https://developer.apple.com/documentation/swiftui/accessibilityfocusstate/wrappedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessibilityfocusstate/wrappedvalue.json'
content_hash: 'sha256:5c114e6299e2f7e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AccessibilityFocusState](../accessibilityfocusstate.md)

# wrappedValue

<sub>Instance Property</sub>

The current state value, taking into account whatever bindings might be in effect due to the current location of focus.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var wrappedValue: Value { get nonmutating set }
```

## Discussion

When focus is not in any view that is bound to this state, the wrapped value will be `nil` (for optional-typed state) or `false` (for `Bool`- typed state).

## See Also

### Getting the state

- [projectedValue](projectedvalue.md) — A projection of the state value that can be used to establish bindings between view content and accessibility focus placement.
- [Binding](binding.md)
