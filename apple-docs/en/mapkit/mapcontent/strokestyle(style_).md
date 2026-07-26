---
title: 'strokeStyle(style:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapcontent/strokestyle(style:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapcontent/strokestyle(style:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcontent/strokestyle%28style%3A%29.json'
content_hash: 'sha256:92eb577d304dfd47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapContent](../mapcontent.md)

# strokeStyle(style:)

<sub>Instance Method</sub>

Applies the given stroke style to drawn map overlays.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func strokeStyle(style: StrokeStyle) -> some MapContent

```

## Parameters

- `style` — The stroke style to apply.

## Return Value

Returns [MapContent](../mapcontent.md) with overlays drawn with the [StrokeStyle](../../swiftui/strokestyle.md) you specified.

## See Also

### Setting stroke properties

- [stroke(_:lineWidth:)](<stroke(__linewidth_).md>) — Applies the given shape style to drawn map overlays using the line width you specify.
- [stroke(_:style:)](<stroke(__style_).md>) — Applies the given shape style to drawn map overlays using the stroke style you specify.
- [stroke(lineWidth:)](<stroke(linewidth_).md>) — Applies the given stoke drawn map overlays using the line width you specify.
