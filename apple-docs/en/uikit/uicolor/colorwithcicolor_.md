---
title: 'colorWithCIColor:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicolor/colorwithcicolor:'
source_url: 'https://developer.apple.com/documentation/uikit/uicolor/colorwithcicolor:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolor/colorwithcicolor%3A.json'
content_hash: 'sha256:1586399e12d8f0fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIColor](../uicolor.md)

# colorWithCIColor:

<sub>Type Method</sub>

Creates a color object that encapsulates a Core Image color.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```objc
+ (UIColor *) colorWithCIColor:(CIColor *) ciColor;
```

## Parameters

- `ciColor` — The Core Image color to convert.

## Return Value

The `UIColor` object corresponding to the specified Core Image color.

## See Also

### Creating a color from another color object

- [- initWithCIColor:](<init(cicolor_)-2z057.md>) — Creates a color object that encapsulates a Core Image color.
- [colorWithCGColor:](colorwithcgcolor_.md) — Creates a color object using the specified Quartz color reference.
- [- initWithCGColor:](<init(cgcolor_)-27r9g.md>) — Creates a color object using the specified Quartz color reference.
- [- colorWithAlphaComponent:](<withalphacomponent(__).md>) — Creates a color object that has the same color space and component values as the receiver, but has the specified alpha component.
