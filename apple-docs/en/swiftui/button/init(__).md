---
title: 'init(_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/button/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/button/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/button/init%28_%3A%29.json'
content_hash: 'sha256:5208d63cc56a2dfb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Button](../button.md)

# init(_:)

<sub>Initializer</sub>

Creates a button based on a configuration for a style with a custom appearance and custom interaction behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(_ configuration: PrimitiveButtonStyleConfiguration)
```

## Parameters

- `configuration` — A configuration for a style with a custom appearance and custom interaction behavior.

## Discussion

Use this initializer within the [makeBody(configuration:)](<../primitivebuttonstyle/makebody(configuration_).md>) method of a [PrimitiveButtonStyle](../primitivebuttonstyle.md) to create an instance of the button that you want to style. This is useful for custom button styles that modify the current button style, rather than implementing a brand new style.

For example, the following style adds a red border around the button, but otherwise preserves the button’s current style:

```swift
struct RedBorderedButtonStyle: PrimitiveButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        Button(configuration)
            .border(Color.red)
    }
}
```
