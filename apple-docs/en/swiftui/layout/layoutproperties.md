---
title: layoutProperties
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/layout/layoutproperties
source_url: 'https://developer.apple.com/documentation/swiftui/layout/layoutproperties'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/layout/layoutproperties.json'
content_hash: 'sha256:df83a0c16eb54854'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Layout](../layout.md)

# layoutProperties

<sub>Type Property</sub>

Properties of a layout container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var layoutProperties: LayoutProperties { get }
```

## Discussion

Implement this property in a type that conforms to the [Layout](../layout.md) protocol to characterize your custom layout container. For example, you can indicate that your layout has a vertical [stackOrientation](../layoutproperties/stackorientation.md):

```swift
extension BasicVStack {
    static var layoutProperties: LayoutProperties {
        var properties = LayoutProperties()
        properties.stackOrientation = .vertical
        return properties
    }
}
```

If you don’t implement this property in your custom layout, the protocol provides a default implementation, namely [layoutProperties](layoutproperties-6h7w0.md), that returns a [LayoutProperties](../layoutproperties.md) instance with default values.

## Default Implementations

### Layout Implementations

- [layoutProperties](layoutproperties-6h7w0.md) — The default property values for a layout.

## See Also

### Reporting layout container characteristics

- [explicitAlignment(of:in:proposal:subviews:cache:)](<explicitalignment(of_in_proposal_subviews_cache_).md>) — Returns the position of the specified horizontal alignment guide along the x axis.
- [spacing(subviews:cache:)](<spacing(subviews_cache_).md>) — Returns the preferred spacing values of the composite view.
