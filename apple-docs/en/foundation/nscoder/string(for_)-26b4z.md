---
title: 'string(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscoder/string(for:)-26b4z'
source_url: 'https://developer.apple.com/documentation/foundation/nscoder/string(for:)-26b4z'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscoder/string%28for%3A%29-26b4z.json'
content_hash: 'sha256:19a6788a169ce35a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCoder](../nscoder.md)

# string(for:)

<sub>Type Method</sub>

Returns a string formatted to contain the data from an edge insets structure.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class func string(for insets: UIEdgeInsets) -> String
```

## Parameters

- `insets` — A UIKit edge insets data structure.

## Return Value

A string that corresponds to `insets`. See [uiEdgeInsets(for:)](<uiedgeinsets(for_).md>) for a discussion of the string format.

## See Also

### Representing Geometric Types as Strings

- [cgAffineTransform(for:)](<cgaffinetransform(for_).md>) — Returns a Core Graphics affine transform structure corresponding to the data in a given string.
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
- [string(for:)](<string(for_)-454dj.md>) — Returns a string formatted to contain the data from an offset structure.
