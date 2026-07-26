---
title: WidgetBundleBuilder
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/widgetbundlebuilder
source_url: 'https://developer.apple.com/documentation/swiftui/widgetbundlebuilder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/widgetbundlebuilder.json'
content_hash: 'sha256:d7e1f0d617772d15'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# WidgetBundleBuilder

<sub>Structure</sub>

A custom attribute that constructs a widget bundle’s body.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@resultBuilder struct WidgetBundleBuilder
```

## Overview

Use the `@WidgetBundleBuilder` attribute to group multiple widgets listed in the [body](widgetbundle/body-swift.property.md) property of a widget bundle. For example, the following code defines a widget bundle that consists of two widgets.

```swift
@main
struct GameWidgets: WidgetBundle {
   @WidgetBundleBuilder
   var body: some Widget {
       GameStatusWidget()
       CharacterDetailWidget()
   }
}
```

## Topics

### Bundling widgets

- [buildBlock()](<widgetbundlebuilder/buildblock().md>) — Builds an empty Widget from a block containing no statements, `{ }`.
- [buildBlock(_:)](<widgetbundlebuilder/buildblock(__).md>)
- [buildExpression(_:)](<widgetbundlebuilder/buildexpression(__).md>) — Builds an expression within the builder.
- [buildLimitedAvailability(_:)](<widgetbundlebuilder/buildlimitedavailability(__).md>) — Builds an availability check within the builder
- [buildOptional(_:)](<widgetbundlebuilder/buildoptional(__).md>) — Produces an optional widget for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.

## See Also

### Implementing a widget bundle

- [body](widgetbundle/body-swift.property.md) — Declares the group of widgets that an app supports.
- [Body](widgetbundle/body-swift.associatedtype.md) — The type of widget that represents the content of the bundle.
