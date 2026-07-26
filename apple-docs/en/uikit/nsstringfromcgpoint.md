---
title: NSStringFromCGPoint
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsstringfromcgpoint
source_url: 'https://developer.apple.com/documentation/uikit/nsstringfromcgpoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsstringfromcgpoint.json'
content_hash: 'sha256:6a2e468f3e5e6222'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSStringFromCGPoint

<sub>Function</sub>

Returns a string formatted to contain the data from a point.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSString *NSStringFromCGPoint(CGPoint point);
```

## Parameters

- `point` — A Core Graphics structure representing a point.

## Return Value

A string that corresponds to `point`. See [CGPointFromString](cgpointfromstring.md) for a discussion of the string format.

## See Also

### Primitive type conversions

- [CGAffineTransformFromString](cgaffinetransformfromstring.md) — Returns a Core Graphics affine transform structure corresponding to the data in a given string.
- [CGPointFromString](cgpointfromstring.md) — Returns a Core Graphics point structure corresponding to the data in a given string.
- [CGRectFromString](cgrectfromstring.md) — Returns a Core Graphics rectangle structure corresponding to the data in a given string.
- [CGSizeFromString](cgsizefromstring.md) — Returns a Core Graphics size structure corresponding to the data in a given string.
- [CGVectorFromString](cgvectorfromstring.md) — Returns a Core Graphics vector corresponding to the data in a given string.
- [NSStringFromCGAffineTransform](nsstringfromcgaffinetransform.md) — Returns a string formatted to contain the data from an affine transform.
- [NSStringFromCGRect](nsstringfromcgrect.md) — Returns a string formatted to contain the data from a rectangle.
- [NSStringFromCGSize](nsstringfromcgsize.md) — Returns a string formatted to contain the data from a size data structure.
- [NSStringFromCGVector](nsstringfromcgvector.md) — Returns a string formatted to contain the data from a vector data structure.
