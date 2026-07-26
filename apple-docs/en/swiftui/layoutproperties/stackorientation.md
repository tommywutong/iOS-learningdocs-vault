---
title: stackOrientation
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/layoutproperties/stackorientation
source_url: 'https://developer.apple.com/documentation/swiftui/layoutproperties/stackorientation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/layoutproperties/stackorientation.json'
content_hash: 'sha256:98e3b1a87c40fdae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [LayoutProperties](../layoutproperties.md)

# stackOrientation

<sub>Instance Property</sub>

The orientation of the containing stack-like container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var stackOrientation: Axis?
```

## Discussion

Certain views alter their behavior based on the stack orientation of the container that they appear in. For example, [Spacer](../spacer.md) and [Divider](../divider.md) align their major axis to match that of their container.

Set the orientation for your custom layout container by returning a configured [LayoutProperties](../layoutproperties.md) instance from your [Layout](../layout.md) type’s implementation of the [layoutProperties](../layout/layoutproperties.md) method. For example, you can indicate that your layout has a [Axis.vertical](../axis/vertical.md) major axis:

```swift
extension BasicVStack {
    static var layoutProperties: LayoutProperties {
        var properties = LayoutProperties()
        properties.stackOrientation = .vertical
        return properties
    }
}
```

A value of `nil`, which is the default when you don’t specify a value, indicates an unknown orientation, or that a layout isn’t one-dimensional.
