---
title: projectedValue
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/focusedbinding/projectedvalue
source_url: 'https://developer.apple.com/documentation/swiftui/focusedbinding/projectedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/focusedbinding/projectedvalue.json'
content_hash: 'sha256:fc745d49773ca44f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FocusedBinding](../focusedbinding.md)

# projectedValue

<sub>Instance Property</sub>

A binding to the optional value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var projectedValue: Binding<Value?> { get }
```

## Discussion

The unwrapped value is `nil` when no focused view hierarchy has published a corresponding binding.

## See Also

### Getting the value

- [wrappedValue](wrappedvalue.md) — The unwrapped value for the focus key given the current scope and state of the focused view hierarchy.
