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
doc_path: /documentation/swiftui/state/projectedvalue
source_url: 'https://developer.apple.com/documentation/swiftui/state/projectedvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/state/projectedvalue.json'
content_hash: 'sha256:6ae571ec7bd4dab3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [State](../state.md)

# projectedValue

<sub>Instance Property</sub>

A binding to the state value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var projectedValue: Binding<Value> { get }
```

## Discussion

Use the projected value to get a [Binding](../binding.md) to the stored value. The binding provides a two-way connection to the stored value. To access the `projectedValue`, prefix the property variable with a dollar sign (`$`).

In the following example, `PlayerView` projects a binding of the state property `isPlaying` to the `PlayButton` view using `$isPlaying`. That enables the play button to both read and write the value:

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

- [wrappedValue](wrappedvalue.md) — The underlying value referenced by the state variable.
