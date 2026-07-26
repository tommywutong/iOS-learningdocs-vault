---
title: CGSizeFromString
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/cgsizefromstring
source_url: 'https://developer.apple.com/documentation/uikit/cgsizefromstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/cgsizefromstring.json'
content_hash: 'sha256:9ebc1b2ada49cd59'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# CGSizeFromString

<sub>Function</sub>

Returns a Core Graphics size structure corresponding to the data in a given string.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern CGSize CGSizeFromString(NSString *string);
```

## Parameters

- `string` — A string whose contents are of the form “{_w_, _h_}”, where _w_ is the width and _h_ is the height. The _w_ and _h_ values can be integer or float values. An example of a valid string is `@"{3.0,2.5}"`. The string is not localized, so items are always separated with a comma.

## Return Value

A Core Graphics structure that represents a size. If the string is not well-formed, the function returns [CGSizeZero](../coregraphics/cgsizezero.md).

## Discussion

In general, you should use this function only to convert strings that were previously created using the [NSStringFromCGSize](nsstringfromcgsize.md) function.

## See Also

### Primitive type conversions

- [CGAffineTransformFromString](cgaffinetransformfromstring.md) — Returns a Core Graphics affine transform structure corresponding to the data in a given string.
- [CGPointFromString](cgpointfromstring.md) — Returns a Core Graphics point structure corresponding to the data in a given string.
- [CGRectFromString](cgrectfromstring.md) — Returns a Core Graphics rectangle structure corresponding to the data in a given string.
- [CGVectorFromString](cgvectorfromstring.md) — Returns a Core Graphics vector corresponding to the data in a given string.
- [NSStringFromCGAffineTransform](nsstringfromcgaffinetransform.md) — Returns a string formatted to contain the data from an affine transform.
- [NSStringFromCGPoint](nsstringfromcgpoint.md) — Returns a string formatted to contain the data from a point.
- [NSStringFromCGRect](nsstringfromcgrect.md) — Returns a string formatted to contain the data from a rectangle.
- [NSStringFromCGSize](nsstringfromcgsize.md) — Returns a string formatted to contain the data from a size data structure.
- [NSStringFromCGVector](nsstringfromcgvector.md) — Returns a string formatted to contain the data from a vector data structure.
