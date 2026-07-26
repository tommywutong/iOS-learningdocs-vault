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
doc_path: /documentation/swiftui/state/wrappedvalue
source_url: 'https://developer.apple.com/documentation/swiftui/state/wrappedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/state/wrappedvalue.json'
content_hash: 'sha256:c22391207207e610'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [State](../state.md)

# wrappedValue

<sub>Instance Property</sub>

The underlying value referenced by the state variable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var wrappedValue: Value { get nonmutating set }
```

## Discussion

This property provides primary access to the value’s data. However, you don’t typically access `wrappedValue` explicitly. Instead, you gain access to the wrapped value by referring to the property variable that you create with the `@State` attribute.

In the following example, the button’s label depends on the value of `isPlaying` and the button’s action toggles the value of `isPlaying`. Both of these accesses implicitly access the state property’s wrapped value:

```swift
struct PlayButton: View {
    @State private var isPlaying: Bool = false

    var body: some View {
        Button(isPlaying ? "Pause" : "Play") {
            isPlaying.toggle()
        }
    }
}
```

## See Also

### Getting the value

- [projectedValue](projectedvalue.md) — A binding to the state value.
