---
title: isMixed
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/togglestyleconfiguration/ismixed
source_url: 'https://developer.apple.com/documentation/swiftui/togglestyleconfiguration/ismixed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/togglestyleconfiguration/ismixed.json'
content_hash: 'sha256:528a94538b75547a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToggleStyleConfiguration](../togglestyleconfiguration.md)

# isMixed

<sub>Instance Property</sub>

Whether the [Toggle](../toggle.md) is currently in a mixed state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isMixed: Bool
```

## Discussion

Use this property to determine whether the toggle style should render a mixed state presentation. A mixed state corresponds to an underlying collection with a mix of true and false Bindings. To toggle the state, use the `Bool.toggle()` method on the [isOn](ison.md) binding.

In the following example, a custom style uses the `isMixed` property to render the correct toggle state using symbols:

```swift
struct SymbolToggleStyle: ToggleStyle {
    func makeBody(configuration: Configuration) -> some View {
        Button {
            configuration.isOn.toggle()
        } label: {
            Image(
                systemName: configuration.isMixed
                ? "minus.circle.fill" : configuration.isOn
                ? "checkmark.circle.fill" : "circle.fill")
            configuration.label
        }
    }
}
```

## See Also

### Managing the toggle state

- [isOn](ison.md) — A binding to a state property that indicates whether the toggle is on.
- [$isOn]($ison.md)
