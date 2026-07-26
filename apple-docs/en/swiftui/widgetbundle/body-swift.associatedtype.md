---
title: Body
framework: SwiftUI
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/widgetbundle/body-swift.associatedtype
source_url: 'https://developer.apple.com/documentation/swiftui/widgetbundle/body-swift.associatedtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/widgetbundle/body-swift.associatedtype.json'
content_hash: 'sha256:47ed86ae43771c74'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WidgetBundle](../widgetbundle.md)

# Body

<sub>Associated Type</sub>

The type of widget that represents the content of the bundle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
associatedtype Body : Widget
```

## Discussion

When you support more than one widget, Swift infers this type from your implementation of the required [body](body-swift.property.md) property.

## See Also

### Implementing a widget bundle

- [body](body-swift.property.md) — Declares the group of widgets that an app supports.
- [WidgetBundleBuilder](../widgetbundlebuilder.md) — A custom attribute that constructs a widget bundle’s body.
