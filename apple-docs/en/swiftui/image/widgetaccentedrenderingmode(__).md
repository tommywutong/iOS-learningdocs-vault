---
title: 'widgetAccentedRenderingMode(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 26.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/image/widgetaccentedrenderingmode(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/image/widgetaccentedrenderingmode(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/image/widgetaccentedrenderingmode%28_%3A%29.json'
content_hash: 'sha256:83fbc7bdb21515cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Image](../image.md)

# widgetAccentedRenderingMode(_:)

<sub>Instance Method</sub>

Specifies the how to render an `Image` when using the `WidgetKit/WidgetRenderingMode/accented` mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func widgetAccentedRenderingMode(_ renderingMode: WidgetAccentedRenderingMode?) -> some View

```

## Parameters

- `renderingMode` — A constant describing how the `Image` should be rendered.

## Discussion

```swift
var body: some View {
    VStack {
        Image("cat_full")
            .resizable()
            .widgetAccentedRenderingMode(.fullColor)
    }
}
```

> [!important] Important
> If the `Image` is a subview for a group that has `widgetAccentable(true)` applied, this modifier may conflict.
