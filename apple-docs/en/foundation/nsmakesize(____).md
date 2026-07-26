---
title: 'NSMakeSize(_:_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmakesize(_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmakesize(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmakesize%28_%3A_%3A%29.json'
content_hash: 'sha256:0c3a5864971398a0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMakeSize(_:_:)

<sub>Function</sub>

Returns a new `NSSize` from the specified values.

<sub>Mac Catalyst, macOS</sub>

```swift
func NSMakeSize(_ w: Double, _ h: Double) -> NSSize
```

## Return Value

An `NSSize` having the specified `width` and `height`.

## See Also

### Managing Sizes

- [NSEqualSizes](<nsequalsizes(____).md>) — Returns a Boolean that indicates whether two size values are equal.
- [NSSizeFromString](<nssizefromstring(__).md>) — Returns an `NSSize` from a text-based representation.
- [NSStringFromSize](<nsstringfromsize(__).md>) — Returns a string representation of a size.
- [NSSizeFromCGSize](<nssizefromcgsize(__).md>) — Returns an `NSSize` typecast from a `CGSize`.
- [NSSizeToCGSize](<nssizetocgsize(__).md>) — Returns a `CGSize` typecast from an `NSSize`.
