---
title: 'init(_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/controlgroup/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/controlgroup/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/controlgroup/init%28_%3A%29.json'
content_hash: 'sha256:e96cf243e9704d57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ControlGroup](../controlgroup.md)

# init(_:)

<sub>Initializer</sub>

Creates a control group based on a style configuration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated init(_ configuration: ControlGroupStyleConfiguration)
```

## Discussion

Use this initializer within the [makeBody(configuration:)](<../controlgroupstyle/makebody(configuration_).md>) method of a [ControlGroupStyle](../controlgroupstyle.md) instance to create an instance of the control group being styled. This is useful for custom control group styles that modify the current control group style.

For example, the following code creates a new, custom style that places a red border around the current control group:

```swift
struct RedBorderControlGroupStyle: ControlGroupStyle {
    func makeBody(configuration: Configuration) -> some View {
        ControlGroup(configuration)
            .border(Color.red)
    }
}
```
