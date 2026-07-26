---
title: CGPointFromString
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/cgpointfromstring
source_url: 'https://developer.apple.com/documentation/uikit/cgpointfromstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/cgpointfromstring.json'
content_hash: 'sha256:d7e0432ce515ae82'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# CGPointFromString

<sub>Function</sub>

Returns a Core Graphics point structure corresponding to the data in a given string.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern CGPoint CGPointFromString(NSString *string);
```

## Parameters

- `string` — A string whose contents are of the form “{_x_,_y_}”, where _x_ is the x coordinate and _y_ is the y coordinate. The _x_ and _y_ values can represent integer or float values. An example of a valid string is `@"{3.0,2.5}"`. The string is not localized, so items are always separated with a comma.

## Return Value

A Core Graphics structure that represents a point. If the string is not well-formed, the function returns [CGPointZero](../coregraphics/cgpointzero.md).

## Discussion

In general, you should use this function only to convert strings that were previously created using the [NSStringFromCGPoint](nsstringfromcgpoint.md) function.

## See Also

### Primitive type conversions

- [CGAffineTransformFromString](cgaffinetransformfromstring.md) — Returns a Core Graphics affine transform structure corresponding to the data in a given string.
- [CGRectFromString](cgrectfromstring.md) — Returns a Core Graphics rectangle structure corresponding to the data in a given string.
- [CGSizeFromString](cgsizefromstring.md) — Returns a Core Graphics size structure corresponding to the data in a given string.
- [CGVectorFromString](cgvectorfromstring.md) — Returns a Core Graphics vector corresponding to the data in a given string.
- [NSStringFromCGAffineTransform](nsstringfromcgaffinetransform.md) — Returns a string formatted to contain the data from an affine transform.
- [NSStringFromCGPoint](nsstringfromcgpoint.md) — Returns a string formatted to contain the data from a point.
- [NSStringFromCGRect](nsstringfromcgrect.md) — Returns a string formatted to contain the data from a rectangle.
- [NSStringFromCGSize](nsstringfromcgsize.md) — Returns a string formatted to contain the data from a size data structure.
- [NSStringFromCGVector](nsstringfromcgvector.md) — Returns a string formatted to contain the data from a vector data structure.
