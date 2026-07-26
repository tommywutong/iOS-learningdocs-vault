---
title: 'stroke(_:style:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapcontent/stroke(_:style:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapcontent/stroke(_:style:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcontent/stroke%28_%3Astyle%3A%29.json'
content_hash: 'sha256:b54c46bef398589a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapContent](../mapcontent.md)

# stroke(_:style:)

<sub>Instance Method</sub>

Applies the given shape style to drawn map overlays using the stroke style you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func stroke(_ content: some ShapeStyle, style: StrokeStyle) -> some MapContent

```

## Parameters

- `content` — The shape style to apply.

- `style` — The stroke style to apply.

## See Also

### Setting stroke properties

- [stroke(_:lineWidth:)](<stroke(__linewidth_).md>) — Applies the given shape style to drawn map overlays using the line width you specify.
- [stroke(lineWidth:)](<stroke(linewidth_).md>) — Applies the given stoke drawn map overlays using the line width you specify.
- [strokeStyle(style:)](<strokestyle(style_).md>) — Applies the given stroke style to drawn map overlays.
