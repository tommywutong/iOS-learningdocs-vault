---
title: 'NSEqualSizes(_:_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsequalsizes(_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsequalsizes(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsequalsizes%28_%3A_%3A%29.json'
content_hash: 'sha256:b6eec247515e6ac3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSEqualSizes(_:_:)

<sub>Function</sub>

Returns a Boolean that indicates whether two size values are equal.

<sub>Mac Catalyst, macOS</sub>

```swift
func NSEqualSizes(_ aSize: NSSize, _ bSize: NSSize) -> Bool
```

## Return Value

[true](../swift/true.md) if `aSize` and `bSize` are identical, otherwise [false](../swift/false.md).

## See Also

### Managing Sizes

- [NSMakeSize](<nsmakesize(____).md>) — Returns a new `NSSize` from the specified values.
- [NSSizeFromString](<nssizefromstring(__).md>) — Returns an `NSSize` from a text-based representation.
- [NSStringFromSize](<nsstringfromsize(__).md>) — Returns a string representation of a size.
- [NSSizeFromCGSize](<nssizefromcgsize(__).md>) — Returns an `NSSize` typecast from a `CGSize`.
- [NSSizeToCGSize](<nssizetocgsize(__).md>) — Returns a `CGSize` typecast from an `NSSize`.
