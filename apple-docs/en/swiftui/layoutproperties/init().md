---
title: init()
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/layoutproperties/init()
source_url: 'https://developer.apple.com/documentation/swiftui/layoutproperties/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/layoutproperties/init%28%29.json'
content_hash: 'sha256:8d64b654a8494439'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [LayoutProperties](../layoutproperties.md)

# init()

<sub>Initializer</sub>

Creates a default set of properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init()
```

## Discussion

Use a layout properties instance to provide information about a type that conforms to the [Layout](../layout.md) protocol. For example, you can create a layout properties instance in your layout’s implementation of the [layoutProperties](../layout/layoutproperties.md) method, and use it to indicate that the layout has a [Axis.vertical](../axis/vertical.md) orientation:

```swift
extension BasicVStack {
    static var layoutProperties: LayoutProperties {
        var properties = LayoutProperties()
        properties.stackOrientation = .vertical
        return properties
    }
}
```
