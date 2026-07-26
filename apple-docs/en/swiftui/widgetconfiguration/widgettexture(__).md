---
title: 'widgetTexture(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/widgetconfiguration/widgettexture(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/widgetconfiguration/widgettexture(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/widgetconfiguration/widgettexture%28_%3A%29.json'
content_hash: 'sha256:a900da0dfd4fb9de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WidgetConfiguration](../widgetconfiguration.md)

# widgetTexture(_:)

<sub>Instance Method</sub>

Specifies the widget texture for this widget.

<sub>visionOS</sub>

```swift
@MainActor @preconcurrency func widgetTexture(_ material: WidgetTexture) -> some WidgetConfiguration

```

## Return Value

A widget configuration using the specified widget texture.

## Discussion

Widgets in visionOS use a have a material treatment applied. By default, all widgets use the `glass` widget texture. Use this modifier to explicitly set the widget texture for a widget.

The following displays a widget whose texture is paper:

```swift
AppIntentConfiguration(
    kind: kind, intent: LatestPostConfiguration.self, provider: Provider()
) { entry in
    LatestPostsView(entry: entry)
}
.widgetTexture(.paper)
```
