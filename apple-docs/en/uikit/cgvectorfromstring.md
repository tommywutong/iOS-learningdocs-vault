---
title: CGVectorFromString
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/cgvectorfromstring
source_url: 'https://developer.apple.com/documentation/uikit/cgvectorfromstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/cgvectorfromstring.json'
content_hash: 'sha256:b153f347350952be'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# CGVectorFromString

<sub>Function</sub>

Returns a Core Graphics vector corresponding to the data in a given string.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern CGVector CGVectorFromString(NSString *string);
```

## Parameters

- `string` — A string whose contents are of the form “{_dx_, _dy_}”, where _dx_ is the x-coordinate of the vector and _dy_ is the y-coordinate. The _dx_ and _dy_ values can be integer or float values. An example of a valid string is `@"{3.0,2.5}"`. The string is not localized, so items are always separated with a comma.

## Return Value

A Core Graphics structure that represents a two-dimensional vector. If the string is not well-formed, the function returns a vector whose `dx` and `dy` values are `0`.

## Discussion

In general, you should use this function only to convert strings that were previously created using the [NSStringFromCGVector](nsstringfromcgvector.md) function.

## See Also

### Primitive type conversions

- [CGAffineTransformFromString](cgaffinetransformfromstring.md) — Returns a Core Graphics affine transform structure corresponding to the data in a given string.
- [CGPointFromString](cgpointfromstring.md) — Returns a Core Graphics point structure corresponding to the data in a given string.
- [CGRectFromString](cgrectfromstring.md) — Returns a Core Graphics rectangle structure corresponding to the data in a given string.
- [CGSizeFromString](cgsizefromstring.md) — Returns a Core Graphics size structure corresponding to the data in a given string.
- [NSStringFromCGAffineTransform](nsstringfromcgaffinetransform.md) — Returns a string formatted to contain the data from an affine transform.
- [NSStringFromCGPoint](nsstringfromcgpoint.md) — Returns a string formatted to contain the data from a point.
- [NSStringFromCGRect](nsstringfromcgrect.md) — Returns a string formatted to contain the data from a rectangle.
- [NSStringFromCGSize](nsstringfromcgsize.md) — Returns a string formatted to contain the data from a size data structure.
- [NSStringFromCGVector](nsstringfromcgvector.md) — Returns a string formatted to contain the data from a vector data structure.
