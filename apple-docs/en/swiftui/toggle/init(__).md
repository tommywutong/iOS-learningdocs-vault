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
doc_path: '/documentation/swiftui/toggle/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/toggle/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toggle/init%28_%3A%29.json'
content_hash: 'sha256:aa5e353303211f17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Toggle](../toggle.md)

# init(_:)

<sub>Initializer</sub>

Creates a toggle based on a toggle style configuration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(_ configuration: ToggleStyleConfiguration)
```

## Parameters

- `configuration` — The properties of the toggle, including a label and a binding to the toggle’s state.

## Discussion

You can use this initializer within the [makeBody(configuration:)](<../togglestyle/makebody(configuration_).md>) method of a [ToggleStyle](../togglestyle.md) to create an instance of the styled toggle. This is useful for custom toggle styles that only modify the current toggle style, as opposed to implementing a brand new style.

For example, the following style adds a red border around the toggle, but otherwise preserves the toggle’s current style:

```swift
struct RedBorderToggleStyle: ToggleStyle {
    func makeBody(configuration: Configuration) -> some View {
        Toggle(configuration)
            .padding()
            .border(.red)
    }
}
```
