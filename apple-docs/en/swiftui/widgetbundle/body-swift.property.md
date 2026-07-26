---
title: body
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/widgetbundle/body-swift.property
source_url: 'https://developer.apple.com/documentation/swiftui/widgetbundle/body-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/widgetbundle/body-swift.property.json'
content_hash: 'sha256:759b13f1827d92e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WidgetBundle](../widgetbundle.md)

# body

<sub>Instance Property</sub>

Declares the group of widgets that an app supports.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@WidgetBundleBuilder @MainActor @preconcurrency var body: Self.Body { get }
```

## Discussion

The order that the widgets appear in this property determines the order they are shown to the user when adding a widget. The following example shows how to use a widget bundle builder to define a body showing a game status widget first and a character detail widget second:

```swift
@main
struct GameWidgets: WidgetBundle {
   var body: some Widget {
       GameStatusWidget()
       CharacterDetailWidget()
   }
}
```

## See Also

### Implementing a widget bundle

- [Body](body-swift.associatedtype.md) — The type of widget that represents the content of the bundle.
- [WidgetBundleBuilder](../widgetbundlebuilder.md) — A custom attribute that constructs a widget bundle’s body.
