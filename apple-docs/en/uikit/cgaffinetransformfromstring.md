---
title: CGAffineTransformFromString
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/cgaffinetransformfromstring
source_url: 'https://developer.apple.com/documentation/uikit/cgaffinetransformfromstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/cgaffinetransformfromstring.json'
content_hash: 'sha256:6b688b611b4c4929'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# CGAffineTransformFromString

<sub>Function</sub>

Returns a Core Graphics affine transform structure corresponding to the data in a given string.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern CGAffineTransform CGAffineTransformFromString(NSString *string);
```

## Parameters

- `string` — A string whose contents are of the form “{_a_, _b_, _c_, _d_, _tx_, _ty_}”, where _a_, _b_, _c_, _d_, _tx_, and _ty_ are the floating-point component values of the [CGAffineTransform](../corefoundation/cgaffinetransform.md) data structure. An example of a valid string is `@"{1,0,0,1,2.5,3.0}"`. The string is not localized, so items are always separated with a comma. For information about the position of each value in the transform array, see [CGAffineTransform](../coregraphics/cgaffinetransform.md).

## Return Value

A Core Graphics affine transform structure. If the string is not well-formed, the function returns the identity transform.

## Discussion

In general, you should use this function only to convert strings that were previously created using the [NSStringFromCGAffineTransform](nsstringfromcgaffinetransform.md) function.

## See Also

### Primitive type conversions

- [CGPointFromString](cgpointfromstring.md) — Returns a Core Graphics point structure corresponding to the data in a given string.
- [CGRectFromString](cgrectfromstring.md) — Returns a Core Graphics rectangle structure corresponding to the data in a given string.
- [CGSizeFromString](cgsizefromstring.md) — Returns a Core Graphics size structure corresponding to the data in a given string.
- [CGVectorFromString](cgvectorfromstring.md) — Returns a Core Graphics vector corresponding to the data in a given string.
- [NSStringFromCGAffineTransform](nsstringfromcgaffinetransform.md) — Returns a string formatted to contain the data from an affine transform.
- [NSStringFromCGPoint](nsstringfromcgpoint.md) — Returns a string formatted to contain the data from a point.
- [NSStringFromCGRect](nsstringfromcgrect.md) — Returns a string formatted to contain the data from a rectangle.
- [NSStringFromCGSize](nsstringfromcgsize.md) — Returns a string formatted to contain the data from a size data structure.
- [NSStringFromCGVector](nsstringfromcgvector.md) — Returns a string formatted to contain the data from a vector data structure.
