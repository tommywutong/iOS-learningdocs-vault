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
doc_path: /documentation/swiftui/binding/wrappedvalue
source_url: 'https://developer.apple.com/documentation/swiftui/binding/wrappedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/binding/wrappedvalue.json'
content_hash: 'sha256:b27b370349226f31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Binding](../binding.md)

# wrappedValue

<sub>Instance Property</sub>

The underlying value referenced by the binding variable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var wrappedValue: Value { get nonmutating set }
```

## Discussion

This property provides primary access to the value’s data. However, you don’t access `wrappedValue` directly. Instead, you use the property variable created with the [Binding](../binding.md) attribute. In the following code example, the binding variable `isPlaying` returns the value of `wrappedValue`:

```swift
struct PlayButton: View {
    @Binding var isPlaying: Bool

    var body: some View {
        Button(isPlaying ? "Pause" : "Play") {
            isPlaying.toggle()
        }
    }
}
```

When a mutable binding value changes, the new value is immediately available. However, updates to a view displaying the value happens asynchronously, so the view may not show the change immediately.

## See Also

### Getting the value

- [projectedValue](projectedvalue.md) — A projection of the binding value that returns a binding.
- [subscript(dynamicMember:)](<subscript(dynamicmember_).md>) — Returns a binding to the resulting value of a given key path.
