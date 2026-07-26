---
title: fullColor
framework: WidgetKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/widgetrenderingmode/fullcolor
source_url: 'https://developer.apple.com/documentation/widgetkit/widgetrenderingmode/fullcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/widgetrenderingmode/fullcolor.json'
content_hash: 'sha256:8af1b85c7b86c678'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [WidgetRenderingMode](../widgetrenderingmode.md)

# fullColor

<sub>Type Property</sub>

The system renders the widget in full color.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
static let fullColor: WidgetRenderingMode
```

## Discussion

In this mode, the system doesn’t alter or filter the widget’s colors.

The system displays full-color widget-based complications on some watch faces, such as the Infograph face, on the Home Screen or Today View in iOS or iPadOS, and in Notification Center on macOS.

> [!note] Note
> The Infograph face only uses full-color rendering when the user sets the face to multicolor. If the user selects an accent color, the system uses [accented](accented.md) instead.

## See Also

### Rendering modes

- [accented](accented.md) — The system divides the widget’s view hierarchy into an accent group and a default group, applying a different color to each group.
- [vibrant](vibrant.md) — The system desaturates the widget, making a monochrome version that it uses to create an adaptive, vibrant effect.
