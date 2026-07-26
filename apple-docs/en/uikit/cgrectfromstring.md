---
title: CGRectFromString
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/cgrectfromstring
source_url: 'https://developer.apple.com/documentation/uikit/cgrectfromstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/cgrectfromstring.json'
content_hash: 'sha256:f40e6fb7e99baad6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# CGRectFromString

<sub>Function</sub>

Returns a Core Graphics rectangle structure corresponding to the data in a given string.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern CGRect CGRectFromString(NSString *string);
```

## Parameters

- `string` — A string whose contents are of the form “{{_x_,_y_},{_w_, _h_}}”, where _x_ is the x coordinate, _y_ is the y coordinate, _w_ is the width, and _h_ is the height. These components can represent integer or float values. An example of a valid string is `@"{{3,2},{4,5}}"`. The string is not localized, so items are always separated with a comma.

## Return Value

A Core Graphics structure that represents a rectangle. If the string is not well-formed, the function returns [CGRectZero](../coregraphics/cgrectzero.md).

## Discussion

In general, you should use this function only to convert strings that were previously created using the [NSStringFromCGRect](nsstringfromcgrect.md) function.

## See Also

### Primitive type conversions

- [CGAffineTransformFromString](cgaffinetransformfromstring.md) — Returns a Core Graphics affine transform structure corresponding to the data in a given string.
- [CGPointFromString](cgpointfromstring.md) — Returns a Core Graphics point structure corresponding to the data in a given string.
- [CGSizeFromString](cgsizefromstring.md) — Returns a Core Graphics size structure corresponding to the data in a given string.
- [CGVectorFromString](cgvectorfromstring.md) — Returns a Core Graphics vector corresponding to the data in a given string.
- [NSStringFromCGAffineTransform](nsstringfromcgaffinetransform.md) — Returns a string formatted to contain the data from an affine transform.
- [NSStringFromCGPoint](nsstringfromcgpoint.md) — Returns a string formatted to contain the data from a point.
- [NSStringFromCGRect](nsstringfromcgrect.md) — Returns a string formatted to contain the data from a rectangle.
- [NSStringFromCGSize](nsstringfromcgsize.md) — Returns a string formatted to contain the data from a size data structure.
- [NSStringFromCGVector](nsstringfromcgvector.md) — Returns a string formatted to contain the data from a vector data structure.
