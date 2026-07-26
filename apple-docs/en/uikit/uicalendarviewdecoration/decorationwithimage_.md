---
title: 'decorationWithImage:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicalendarviewdecoration/decorationwithimage:'
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarviewdecoration/decorationwithimage:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarviewdecoration/decorationwithimage%3A.json'
content_hash: 'sha256:357f8ee3723ec5a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [Decoration](../uicalendarview/decoration.md)

# decorationWithImage:

<sub>Type Method</sub>

Creates a new calendar view decoration with the image you specify, using the system fill color and medium relative size.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) decorationWithImage:(UIImage *) image;
```

## Parameters

- `image` — An image to display as the decoration.

## Return Value

A calendar view decoration.

## Discussion

The color defaults to [systemFillColor](../uicolor/systemfill.md) if you don’t specify it.

The size defaults to [UICalendarViewDecorationSizeMedium](../uicalendarview/decorationsize/medium.md) if you don’t specify it.

## See Also

### Creating Image Decoration Views

- [initWithImage:color:size:](initwithimage_color_size_.md) — Creates a new calendar view decoration with the image, color, and size that you specify.
- [decorationWithImage:color:size:](decorationwithimage_color_size_.md) — Creates a new calendar view decoration with the image, color, and size that you specify.
