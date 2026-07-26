---
title: 'stroke(lineWidth:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapcontent/stroke(linewidth:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapcontent/stroke(linewidth:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcontent/stroke%28linewidth%3A%29.json'
content_hash: 'sha256:8ea3e38b38f40512'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapContent](../mapcontent.md)

# stroke(lineWidth:)

<sub>Instance Method</sub>

Applies the given stoke drawn map overlays using the line width you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func stroke(lineWidth: CGFloat = 1) -> some MapContent

```

## Parameters

- `lineWidth` — The line width to draw the stroke with.

## Return Value

Returns [MapContent](../mapcontent.md) with overlays drawn with `lineWidth` you specified.

## See Also

### Setting stroke properties

- [stroke(_:lineWidth:)](<stroke(__linewidth_).md>) — Applies the given shape style to drawn map overlays using the line width you specify.
- [stroke(_:style:)](<stroke(__style_).md>) — Applies the given shape style to drawn map overlays using the stroke style you specify.
- [strokeStyle(style:)](<strokestyle(style_).md>) — Applies the given stroke style to drawn map overlays.
