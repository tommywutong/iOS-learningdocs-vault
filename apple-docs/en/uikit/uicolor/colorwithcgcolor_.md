---
title: 'colorWithCGColor:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicolor/colorwithcgcolor:'
source_url: 'https://developer.apple.com/documentation/uikit/uicolor/colorwithcgcolor:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolor/colorwithcgcolor%3A.json'
content_hash: 'sha256:8763a7e0a27ea834'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIColor](../uicolor.md)

# colorWithCGColor:

<sub>Type Method</sub>

Creates a color object using the specified Quartz color reference.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (UIColor *) colorWithCGColor:(CGColorRef) cgColor;
```

## Parameters

- `cgColor` — A reference to a Quartz color.

## Return Value

The color object. The color information represented by this object is in the native colorspace of the specified Quartz color.

## See Also

### Creating a color from another color object

- [colorWithCIColor:](colorwithcicolor_.md) — Creates a color object that encapsulates a Core Image color.
- [- initWithCIColor:](<init(cicolor_)-2z057.md>) — Creates a color object that encapsulates a Core Image color.
- [- initWithCGColor:](<init(cgcolor_)-27r9g.md>) — Creates a color object using the specified Quartz color reference.
- [- colorWithAlphaComponent:](<withalphacomponent(__).md>) — Creates a color object that has the same color space and component values as the receiver, but has the specified alpha component.
