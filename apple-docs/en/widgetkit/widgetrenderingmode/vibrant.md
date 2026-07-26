---
title: vibrant
framework: WidgetKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/widgetrenderingmode/vibrant
source_url: 'https://developer.apple.com/documentation/widgetkit/widgetrenderingmode/vibrant'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/widgetrenderingmode/vibrant.json'
content_hash: 'sha256:a6fadeff941790f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [WidgetRenderingMode](../widgetrenderingmode.md)

# vibrant

<sub>Type Property</sub>

The system desaturates the widget, making a monochrome version that it uses to create an adaptive, vibrant effect.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
static let vibrant: WidgetRenderingMode
```

## Discussion

The system displays vibrant widgets on the Lock Screen on iPhone.

## See Also

### Rendering modes

- [fullColor](fullcolor.md) — The system renders the widget in full color.
- [accented](accented.md) — The system divides the widget’s view hierarchy into an accent group and a default group, applying a different color to each group.
