---
title: 'init(_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/menu/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/menu/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menu/init%28_%3A%29.json'
content_hash: 'sha256:dd76e31bbcd0a02e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Menu](../menu.md)

# init(_:)

<sub>Initializer</sub>

Creates a menu based on a style configuration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated init(_ configuration: MenuStyleConfiguration)
```

## Discussion

Use this initializer within the [makeBody(configuration:)](<../menustyle/makebody(configuration_).md>) method of a [MenuStyle](../menustyle.md) instance to create an instance of the menu being styled. This is useful for custom menu styles that modify the current menu style.

For example, the following code creates a new, custom style that adds a red border around the current menu style:

```swift
struct RedBorderMenuStyle: MenuStyle {
    func makeBody(configuration: Configuration) -> some View {
        Menu(configuration)
            .border(Color.red)
    }
}
```
