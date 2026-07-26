---
title: 'nsDirectionalEdgeInsets(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/nsdirectionaledgeinsets(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/nsdirectionaledgeinsets(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/nsdirectionaledgeinsets%28for%3A%29.json'
content_hash: 'sha256:b1087d9bf99b1b75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# nsDirectionalEdgeInsets(for:)

<sub>Type Method</sub>

Returns a directional edge insets structure based on data in the specified string.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class func nsDirectionalEdgeInsets(for string: String) -> NSDirectionalEdgeInsets
```

## Parameters

- `string` — A string whose contents are of the form “{top, leading, bottom, trailing}”, where top, leading, bottom, trailing are the floating-point component values of the [NSDirectionalEdgeInsets](../../appkit/nsdirectionaledgeinsets.md) structure. An example of a valid string is “`{3.0,8.0,3.0,5.0}`”. The string is not localized, so items are always separated with a comma.

## Return Value

A directional edge insets data structure. If the string is not well-formed, the function returns [NSDirectionalEdgeInsetsZero](../../appkit/nsdirectionaledgeinsetszero.md).

## See Also

### Representing Geometric Types as Strings

- [cgAffineTransform(for:)](<cgaffinetransform(for_).md>) — Returns a Core Graphics affine transform structure corresponding to the data in a given string.
- [cgPoint(for:)](<cgpoint(for_).md>) — Returns a Core Graphics point structure corresponding to the data in a given string.
- [cgRect(for:)](<cgrect(for_).md>) — Returns a Core Graphics rectangle structure corresponding to the data in a given string.
- [cgSize(for:)](<cgsize(for_).md>) — Returns a Core Graphics size structure corresponding to the data in a given string.
- [cgVector(for:)](<cgvector(for_).md>) — Returns a Core Graphics vector corresponding to the data in a given string.
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
