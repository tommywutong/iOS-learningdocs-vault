---
title: 'image(_:color:size:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicalendarview/decoration/image(_:color:size:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarview/decoration/image(_:color:size:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarview/decoration/image%28_%3Acolor%3Asize%3A%29.json'
content_hash: 'sha256:ba3efa857e9d1750'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UICalendarView](../../uicalendarview.md) · [Decoration](../decoration.md)

# image(_:color:size:)

<sub>Type Method</sub>

Creates a new calendar view decoration with the image, color, and size that you specify.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency static func image(_ image: UIImage?, color: UIColor? = nil, size: UICalendarView.DecorationSize = .medium) -> UICalendarView.Decoration
```

## Parameters

- `image` — An image to display as the decoration.

- `color` — A color for the decoration.

- `size` — A relative size for the decoration.

## Return Value

A calendar view decoration.

## Discussion

The image defaults to `circlebadge.fill` if you don’t specify it.

The color defaults to [systemFillColor](../../uicolor/systemfill.md) if you don’t specify it.

The size defaults to [UICalendarViewDecorationSizeMedium](../decorationsize/medium.md) if nil.
