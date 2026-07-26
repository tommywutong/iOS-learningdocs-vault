---
title: NSStringFromCGAffineTransform
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsstringfromcgaffinetransform
source_url: 'https://developer.apple.com/documentation/uikit/nsstringfromcgaffinetransform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsstringfromcgaffinetransform.json'
content_hash: 'sha256:3b13378a08a153bc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSStringFromCGAffineTransform

<sub>Function</sub>

Returns a string formatted to contain the data from an affine transform.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSString *NSStringFromCGAffineTransform(CGAffineTransform transform);
```

## Parameters

- `transform` — A Core Graphics affine transform structure.

## Return Value

A string that corresponds to `transform`. See [CGAffineTransformFromString](cgaffinetransformfromstring.md) for a discussion of the string format.

## See Also

### Primitive type conversions

- [CGAffineTransformFromString](cgaffinetransformfromstring.md) — Returns a Core Graphics affine transform structure corresponding to the data in a given string.
- [CGPointFromString](cgpointfromstring.md) — Returns a Core Graphics point structure corresponding to the data in a given string.
- [CGRectFromString](cgrectfromstring.md) — Returns a Core Graphics rectangle structure corresponding to the data in a given string.
- [CGSizeFromString](cgsizefromstring.md) — Returns a Core Graphics size structure corresponding to the data in a given string.
- [CGVectorFromString](cgvectorfromstring.md) — Returns a Core Graphics vector corresponding to the data in a given string.
- [NSStringFromCGPoint](nsstringfromcgpoint.md) — Returns a string formatted to contain the data from a point.
- [NSStringFromCGRect](nsstringfromcgrect.md) — Returns a string formatted to contain the data from a rectangle.
- [NSStringFromCGSize](nsstringfromcgsize.md) — Returns a string formatted to contain the data from a size data structure.
- [NSStringFromCGVector](nsstringfromcgvector.md) — Returns a string formatted to contain the data from a vector data structure.
