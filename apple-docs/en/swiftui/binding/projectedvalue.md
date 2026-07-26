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
doc_path: /documentation/swiftui/binding/projectedvalue
source_url: 'https://developer.apple.com/documentation/swiftui/binding/projectedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/binding/projectedvalue.json'
content_hash: 'sha256:d4dd996fc155b26c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Binding](../binding.md)

# projectedValue

<sub>Instance Property</sub>

A projection of the binding value that returns a binding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var projectedValue: Binding<Value> { get }
```

## Discussion

Use the projected value to pass a binding value down a view hierarchy. To get the `projectedValue`, prefix the property variable with `$`. For example, in the following code example `PlayerView` projects a binding of the state property `isPlaying` to the `PlayButton` view using `$isPlaying`.

```swift
struct PlayerView: View {
    var episode: Episode
    @State private var isPlaying: Bool = false

    var body: some View {
        VStack {
            Text(episode.title)
                .foregroundStyle(isPlaying ? .primary : .secondary)
            PlayButton(isPlaying: $isPlaying)
        }
    }
}
```

## See Also

### Getting the value

- [wrappedValue](wrappedvalue.md) — The underlying value referenced by the binding variable.
- [subscript(dynamicMember:)](<subscript(dynamicmember_).md>) — Returns a binding to the resulting value of a given key path.
