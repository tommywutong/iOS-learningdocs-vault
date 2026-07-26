---
title: 'colorWithPatternImage:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicolor/colorwithpatternimage:'
source_url: 'https://developer.apple.com/documentation/uikit/uicolor/colorwithpatternimage:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolor/colorwithpatternimage%3A.json'
content_hash: 'sha256:75fd31caae5bd92a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIColor](../uicolor.md)

# colorWithPatternImage:

<sub>Type Method</sub>

Creates a color object using the specified image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (UIColor *) colorWithPatternImage:(UIImage *) image;
```

## Parameters

- `image` — The image to use when creating the pattern color.

## Return Value

The pattern color.

## Discussion

You can use pattern colors to set the fill or stroke color just as you’d a solid color. During drawing, the image in the pattern color is tiled as necessary to cover the given area.

By default, the phase of the returned color is 0, which causes the top-left corner of the image to be aligned with the drawing origin. To change the phase, make the color the current color and then use the [setPatternPhase(_:)](<../../coregraphics/cgcontext/setpatternphase(__).md>) function to change the phase.

## See Also

### Creating a pattern-based color

- [- initWithPatternImage:](<init(patternimage_).md>) — Creates a color object using the specified image object.
