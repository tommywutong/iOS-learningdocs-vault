---
title: NSStringFromCGRect
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsstringfromcgrect
source_url: 'https://developer.apple.com/documentation/uikit/nsstringfromcgrect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsstringfromcgrect.json'
content_hash: 'sha256:a7ba3608e183be1c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSStringFromCGRect

<sub>Function</sub>

Returns a string formatted to contain the data from a rectangle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSString *NSStringFromCGRect(CGRect rect);
```

## Parameters

- `rect` — A Core Graphics structure representing a rectangle.

## Return Value

A string that corresponds to `rect`. See [CGRectFromString](cgrectfromstring.md) for a discussion of the string format.

## See Also

### Primitive type conversions

- [CGAffineTransformFromString](cgaffinetransformfromstring.md) — Returns a Core Graphics affine transform structure corresponding to the data in a given string.
- [CGPointFromString](cgpointfromstring.md) — Returns a Core Graphics point structure corresponding to the data in a given string.
- [CGRectFromString](cgrectfromstring.md) — Returns a Core Graphics rectangle structure corresponding to the data in a given string.
- [CGSizeFromString](cgsizefromstring.md) — Returns a Core Graphics size structure corresponding to the data in a given string.
- [CGVectorFromString](cgvectorfromstring.md) — Returns a Core Graphics vector corresponding to the data in a given string.
- [NSStringFromCGAffineTransform](nsstringfromcgaffinetransform.md) — Returns a string formatted to contain the data from an affine transform.
- [NSStringFromCGPoint](nsstringfromcgpoint.md) — Returns a string formatted to contain the data from a point.
- [NSStringFromCGSize](nsstringfromcgsize.md) — Returns a string formatted to contain the data from a size data structure.
- [NSStringFromCGVector](nsstringfromcgvector.md) — Returns a string formatted to contain the data from a vector data structure.
