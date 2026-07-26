---
title: 'decorationWithColor:size:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicalendarviewdecoration/decorationwithcolor:size:'
source_url: 'https://developer.apple.com/documentation/uikit/uicalendarviewdecoration/decorationwithcolor:size:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicalendarviewdecoration/decorationwithcolor%3Asize%3A.json'
content_hash: 'sha256:82fbdc7e5c829ad7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [Decoration](../uicalendarview/decoration.md)

# decorationWithColor:size:

<sub>Type Method</sub>

Creates a new calendar view decoration with a filled circle image, using the color and size that you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) decorationWithColor:(UIColor *) color size:(UICalendarViewDecorationSize) size;
```

## Parameters

- `color` — A color for the decoration.

- `size` — A relative size for the decoration.

## Return Value

A calendar view decoration.

## Discussion

The color defaults to [systemFillColor](../uicolor/systemfill.md) if you don’t specify it.

The size defaults to .[UICalendarViewDecorationSizeMedium](../uicalendarview/decorationsize/medium.md) if you don’t specify it.

## See Also

### Creating a Default Decoration View

- [- init](<../uicalendarview/decoration/init().md>) — Creates a default calendar view decoration with a filled circle image, using the system fill color and medium size.
