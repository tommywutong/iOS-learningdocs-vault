---
title: 'background(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/uihostingconfiguration/background(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/uihostingconfiguration/background(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uihostingconfiguration/background%28_%3A%29.json'
content_hash: 'sha256:4bf52eff40f06175'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIHostingConfiguration](../uihostingconfiguration.md)

# background(_:)

<sub>Instance Method</sub>

Sets the background contents for the hosting configuration’s enclosing cell.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func background<S>(_ style: S) -> UIHostingConfiguration<Content, _UIHostingConfigurationBackgroundView<S>> where S : ShapeStyle
```

## Parameters

- `style` — The shape style to be used as the background of the cell.

## Discussion

The following example sets a custom view to the background of the cell:

```swift
UIHostingConfiguration {
    Text("My Contents")
}
.background(Color.blue)
```

## See Also

### Setting the background

- [background(content:)](<background(content_).md>) — Sets the background contents for the hosting configuration’s enclosing cell.
