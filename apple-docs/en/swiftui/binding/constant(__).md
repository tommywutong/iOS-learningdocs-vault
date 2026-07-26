---
title: 'constant(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/binding/constant(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/binding/constant(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/binding/constant%28_%3A%29.json'
content_hash: 'sha256:ab481501c3c0b4a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Binding](../binding.md)

# constant(_:)

<sub>Type Method</sub>

Creates a binding with an immutable value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func constant(_ value: Value) -> Binding<Value>
```

## Parameters

- `value` — An immutable value.

## Discussion

Use this method to create a binding to a value that cannot change. This can be useful when using a [PreviewProvider](../previewprovider.md) to see how a view represents different values.

```swift
// Example of binding to an immutable value.
PlayButton(isPlaying: Binding.constant(true))
```

## See Also

### Creating a binding

- [init(_:)](<init(__).md>) — Creates a binding by projecting the base value to a hashable value.
- [init(projectedValue:)](<init(projectedvalue_).md>) — Creates a binding from the value of another binding.
- [init(get:set:)](<init(get_set_).md>) — Creates a binding with closures that read and write the binding value.
