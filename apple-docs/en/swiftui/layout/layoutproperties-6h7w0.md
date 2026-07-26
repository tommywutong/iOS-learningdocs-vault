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
doc_path: /documentation/swiftui/layout/layoutproperties-6h7w0
source_url: 'https://developer.apple.com/documentation/swiftui/layout/layoutproperties-6h7w0'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/layout/layoutproperties-6h7w0.json'
content_hash: 'sha256:65f0f7c606fb3718'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Layout](../layout.md)

# layoutProperties

<sub>Type Property</sub>

The default property values for a layout.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var layoutProperties: LayoutProperties { get }
```

## Discussion

If you don’t implement the [layoutProperties](layoutproperties.md) method in your custom layout, the protocol uses this default implementation instead, which returns a [LayoutProperties](../layoutproperties.md) instance with default values. The properties instance contains information about the layout container, like a [stackOrientation](../layoutproperties/stackorientation.md) property that indicates the container’s major axis.
