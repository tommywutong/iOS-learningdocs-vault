---
title: 'decorationWithImage:color:size:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicalendarviewdecoration/decorationwithimage:color:size:'
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarviewdecoration/decorationwithimage:color:size:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarviewdecoration/decorationwithimage%3Acolor%3Asize%3A.json'
content_hash: 'sha256:11cd615903c5ee2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [Decoration](../uicalendarview/decoration.md)

# decorationWithImage:color:size:

<sub>Type Method</sub>

Creates a new calendar view decoration with the image, color, and size that you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) decorationWithImage:(UIImage *) image color:(UIColor *) color size:(UICalendarViewDecorationSize) size;
```

## Parameters

- `image` — An image to display as the decoration.

- `color` — A color for the decoration.

- `size` — A relative size for the decoration.

## Return Value

A calendar view decoration.

## Discussion

The image defaults to `circlebadge.fill` if you don’t specify it.

The color defaults to [systemFillColor](../uicolor/systemfill.md) if you don’t specify it.

The size defaults to [UICalendarViewDecorationSizeMedium](../uicalendarview/decorationsize/medium.md) if you don’t specify it.

## See Also

### Creating Image Decoration Views

- [initWithImage:color:size:](initwithimage_color_size_.md) — Creates a new calendar view decoration with the image, color, and size that you specify.
- [decorationWithImage:](decorationwithimage_.md) — Creates a new calendar view decoration with the image you specify, using the system fill color and medium relative size.
