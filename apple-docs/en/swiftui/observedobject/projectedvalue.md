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
doc_path: /documentation/swiftui/observedobject/projectedvalue
source_url: 'https://developer.apple.com/documentation/swiftui/observedobject/projectedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/observedobject/projectedvalue.json'
content_hash: 'sha256:72a31c97373ad36a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ObservedObject](../observedobject.md)

# projectedValue

<sub>Instance Property</sub>

A projection of the observed object that creates bindings to its properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency var projectedValue: ObservedObject<ObjectType>.Wrapper { get }
```

## Discussion

Use the projected value to get a [Binding](../binding.md) to a property of an observed object. To access the projected value, prefix the property variable with a dollar sign (`$`). For example, you can get a binding to a model’s `isEnabled` Boolean so that a [Toggle](../toggle.md) can control its value:

```swift
struct MySubView: View {
    @ObservedObject var model: DataModel

    var body: some View {
        Toggle("Enabled", isOn: $model.isEnabled)
    }
}
```

> [!important] Important
> A `Binding` created by the projected value must only be read from, or written to by the main actor. Failing to do so may result in undefined behavior, or data loss. When this occurs, SwiftUI will issue a runtime warning. In a future release, a crash will occur instead.

## See Also

### Getting the value

- [wrappedValue](wrappedvalue.md) — The underlying value that the observed object references.
- [Wrapper](wrapper.md) — A wrapper of the underlying observable object that can create bindings to its properties.
