---
title: label
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/togglestyleconfiguration/label-swift.property
source_url: 'https://developer.apple.com/documentation/swiftui/togglestyleconfiguration/label-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/togglestyleconfiguration/label-swift.property.json'
content_hash: 'sha256:2f923ba418d4d7d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToggleStyleConfiguration](../togglestyleconfiguration.md)

# label

<sub>Instance Property</sub>

A view that describes the effect of switching the toggle between states.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let label: ToggleStyleConfiguration.Label
```

## Discussion

Use this value in your implementation of the [makeBody(configuration:)](<../togglestyle/makebody(configuration_).md>) method when defining a custom [ToggleStyle](../togglestyle.md). Access it through the that method’s `configuration` parameter.

Because the label is a [View](../view.md), you can incorporate it into the view hierarchy that you return from your style definition. For example, you can combine the label with a circle image in an [HStack](../hstack.md):

```swift
HStack {
    Image(systemName: configuration.isOn
        ? "checkmark.circle.fill"
        : "circle")
    configuration.label
}
```

## See Also

### Getting the label view

- [Label](label-swift.struct.md) — A type-erased label of a toggle.
