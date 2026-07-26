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
doc_path: /documentation/swiftui/accessibilityfocusstate/projectedvalue
source_url: 'https://developer.apple.com/documentation/swiftui/accessibilityfocusstate/projectedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessibilityfocusstate/projectedvalue.json'
content_hash: 'sha256:63c35fbaaeb07a6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AccessibilityFocusState](../accessibilityfocusstate.md)

# projectedValue

<sub>Instance Property</sub>

A projection of the state value that can be used to establish bindings between view content and accessibility focus placement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var projectedValue: AccessibilityFocusState<Value>.Binding { get }
```

## Discussion

Use `projectedValue` in conjunction with [accessibilityFocused(_:equals:)](<../view/accessibilityfocused(__equals_).md>) to establish bindings between view content and accessibility focus placement.

## See Also

### Getting the state

- [wrappedValue](wrappedvalue.md) — The current state value, taking into account whatever bindings might be in effect due to the current location of focus.
- [Binding](binding.md)
