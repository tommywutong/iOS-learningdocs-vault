---
title: 'cgAffineTransform(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/cgaffinetransform(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/cgaffinetransform(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/cgaffinetransform%28for%3A%29.json'
content_hash: 'sha256:34a64d81730ff5dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# cgAffineTransform(for:)

<sub>Type Method</sub>

Returns a Core Graphics affine transform structure corresponding to the data in a given string.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class func cgAffineTransform(for string: String) -> CGAffineTransform
```

## Parameters

- `string` — A string whose contents are of the form “{_a_, _b_, _c_, _d_, _tx_, _ty_}”, where _a_, _b_, _c_, _d_, _tx_, and _ty_ are the floating-point component values of the [CGAffineTransform](../../coregraphics/cgaffinetransform.md) data structure. An example of a valid string is @”{1,0,0,1,2.5,3.0}”. The string is not localized, so items are always separated with a comma. For information about the position of each value in the transform array, see [CGAffineTransform](../../coregraphics/cgaffinetransform.md).

## Return Value

A Core Graphics affine transform structure. If the string is not well-formed, the function returns the identity transform.

## Discussion

In general, you should use this function only to convert strings that were previously created using the [string(for:)](<string(for_)-6yx6n.md>) function.

## See Also

### Representing Geometric Types as Strings

- [cgPoint(for:)](<cgpoint(for_).md>) — Returns a Core Graphics point structure corresponding to the data in a given string.
- [cgRect(for:)](<cgrect(for_).md>) — Returns a Core Graphics rectangle structure corresponding to the data in a given string.
- [cgSize(for:)](<cgsize(for_).md>) — Returns a Core Graphics size structure corresponding to the data in a given string.
- [cgVector(for:)](<cgvector(for_).md>) — Returns a Core Graphics vector corresponding to the data in a given string.
- [nsDirectionalEdgeInsets(for:)](<nsdirectionaledgeinsets(for_).md>) — Returns a directional edge insets structure based on data in the specified string.
- [uiEdgeInsets(for:)](<uiedgeinsets(for_).md>) — Returns a UIKit edge insets structure based on the data in the specified string.
- [uiOffset(for:)](<uioffset(for_).md>) — Returns a UIKit offset structure corresponding to the data in a given string.
- [string(for:)](<string(for_)-4qz0a.md>) — Returns a string formatted to contain the data from a rectangle.
- [string(for:)](<string(for_)-4omzv.md>) — Returns a string formatted to contain the data from a vector data structure.
- [string(for:)](<string(for_)-6yx6n.md>) — Returns a string formatted to contain the data from an affine transform.
- [string(for:)](<string(for_)-6ix86.md>) — Returns a string formatted to contain the data from a point.
- [string(for:)](<string(for_)-2f1xb.md>) — Returns a string formatted to contain the data from a size data structure.
- [string(for:)](<string(for_)-hp8b.md>) — Returns a string formatted to contain the data from a directional edge insets structure.
- [string(for:)](<string(for_)-26b4z.md>) — Returns a string formatted to contain the data from an edge insets structure.
- [string(for:)](<string(for_)-454dj.md>) — Returns a string formatted to contain the data from an offset structure.
