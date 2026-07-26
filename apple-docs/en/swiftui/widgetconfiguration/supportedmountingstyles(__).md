---
title: 'supportedMountingStyles(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/widgetconfiguration/supportedmountingstyles(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/widgetconfiguration/supportedmountingstyles(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/widgetconfiguration/supportedmountingstyles%28_%3A%29.json'
content_hash: 'sha256:60fa8e31450b1c38'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WidgetConfiguration](../widgetconfiguration.md)

# supportedMountingStyles(_:)

<sub>Instance Method</sub>

Specifies the mounting style for this widget.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency func supportedMountingStyles(_ styles: [WidgetMountingStyle]) -> some WidgetConfiguration

```

## Parameters

- `styles` — The set of mounting styles that the widget supports.

## Return Value

A widget configuration that supports the specified mounting styles.

## Discussion

The mounting style view modifier only has an effect to widgets in visionOS, including widgets of compatible widgets of compatible iOS or iPadOS apps.

```swift
struct MySpatialWidget: Widget {
     let kind: String = "MySpatialWidget"

     var body: some WidgetConfiguration {
         AppIntentConfiguration(kind: kind, intent: ConfigurationIntent.self, provider: Provider()) { entry in
             EntryView(entry: entry)
                .containerBackground(.fill.tertiary, for: .widget)
         }
         .supportedFamilies([.systemSmall, .systemLarge])
         .supportedMountingStyles([.recessed])
     }
}
```

The above code defines a widget that only supports the recessed mounting style.

The mounting style view modifier only has an effect to widgets in visionOS, including widgets of compatible widgets of compatible iOS or iPadOS apps.
