---
title: WidgetFamily.accessoryInline
framework: WidgetKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/widgetfamily/accessoryinline
source_url: 'https://developer.apple.com/documentation/widgetkit/widgetfamily/accessoryinline'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/widgetfamily/accessoryinline.json'
content_hash: 'sha256:c15e016a2778cb41'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [WidgetFamily](../widgetfamily.md)

# WidgetFamily.accessoryInline

<sub>Case</sub>

A flat widget that contains a single row of text and an optional image.

<sub>iOS, iPadOS, Mac Catalyst, watchOS</sub>

```swift
case accessoryInline
```

## Discussion

The accessory inline widget can appear as a complication in watchOS, or on the Lock Screen in iOS and iPadOS. On some watch faces, the system renders the complication along a curve.

> [!note] Note
> Widgets on the iPad Lock Screen require iPadOS 17 or later.

## See Also

### Accessing accessory families

- [WidgetFamily.accessoryCircular](accessorycircular.md) — A circular widget.
- [WidgetFamily.accessoryCorner](accessorycorner.md) — A widget-based complication in the corner of a watch face in watchOS.
- [WidgetFamily.accessoryRectangular](accessoryrectangular.md) — A rectangular widget.
