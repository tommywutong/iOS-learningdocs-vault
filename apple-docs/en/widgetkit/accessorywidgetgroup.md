---
title: AccessoryWidgetGroup
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/accessorywidgetgroup
source_url: 'https://developer.apple.com/documentation/widgetkit/accessorywidgetgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/accessorywidgetgroup.json'
content_hash: 'sha256:8b041c2850c72f27'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# AccessoryWidgetGroup

<sub>Structure</sub>

A view type that has a label at the top and three content views masked with a circle or rounded square.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency struct AccessoryWidgetGroup<Label, Content> where Label : View, Content : View
```

## Overview

You can use this view on `.accessoryRectangular` family widgets on watchOS to lay out three content views horizontally inside of a rectangular widget.

Example usage:

```swift
struct WeatherGroupView: View {
   var entry: Provider.Entry

   var body: some View {
       AccessoryWidgetGroup("Weather", systemImage: "cloud.sun.fill") {
           TemperatureWidgetView(entry.temperature)
           ConditionsWidgetView(entry.conditions)
           UVIndexWidgetView(entry.UVIndex)
       }
       .accessoryWidgetGroupStyle(.circular)
   }
}
```

The above example creates an `.accessoryRectangular` widget that has a `SwiftUI.Label` as its label and has three content views: temperature, conditions, and UVIndex; all of which are circular. If fewer than three views are provided, the content views are centered within the available space.

You can change the shape with which the content views are masked using the `.accessoryWidgetGroupStyle(_:)` view modifier.

## Relationships

- **Conforms To**: [View](../swiftui/view.md)

## Topics

### Initializers

- [init(_:content:)](<accessorywidgetgroup/init(__content_)-3ij0e.md>) — Creates an `AccessoryWidgetGroup` that generates its label from a string.
- [init(_:content:)](<accessorywidgetgroup/init(__content_)-75rkg.md>) — Creates an `AccessoryWidgetGroup` that generates its label from a localized string resource.
- [init(_:content:)](<accessorywidgetgroup/init(__content_)-nb0.md>) — Creates an `AccessoryWidgetGroup` that generates its label from a localized string key.
- [init(_:image:content:)](<accessorywidgetgroup/init(__image_content_)-385rt.md>) — Creates an `AccessoryWidgetGroup` that generates its label from a localized string resource and image resource.
- [init(_:image:content:)](<accessorywidgetgroup/init(__image_content_)-50iyk.md>) — Creates an `AccessoryWidgetGroup` that generates its label from a localized string key and image resource.
- [init(_:image:content:)](<accessorywidgetgroup/init(__image_content_)-66iys.md>) — Creates an `AccessoryWidgetGroup` that generates its label from a string and image resource.
- [init(_:systemImage:content:)](<accessorywidgetgroup/init(__systemimage_content_)-3mynu.md>) — Creates an `AccessoryWidgetGroup` that generates its label from a localized string resource and a system image name.
- [init(_:systemImage:content:)](<accessorywidgetgroup/init(__systemimage_content_)-54h9w.md>) — Creates an `AccessoryWidgetGroup` that generates its label from a localized string key and a system image name.
- [init(_:systemImage:content:)](<accessorywidgetgroup/init(__systemimage_content_)-7rnqc.md>) — Creates an `AccessoryWidgetGroup` that generates its label from a string and system image name.
- [init(label:content:)](<accessorywidgetgroup/init(label_content_).md>) — Creates an AccessoryWidgetGroup composed of a label and three circular or rounded square contents with equal spacing and vertical alignment.

## See Also

### Accessory and watchOS widgets

- [Creating accessory widgets and watch complications](creating-accessory-widgets-and-watch-complications.md) — Support accessory widgets that appear on the Lock Screen and as complications on Apple Watch.
- [AccessoryWidgetGroupStyle](accessorywidgetgroupstyle.md) — The style for an [AccessoryWidgetGroup](accessorywidgetgroup.md) view.
- [Migrating ClockKit complications to WidgetKit](converting-a-clockkit-app.md) — Leverage WidgetKit’s API to create watchOS complications using SwiftUI.
