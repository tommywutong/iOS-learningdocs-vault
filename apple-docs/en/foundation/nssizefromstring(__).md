---
title: 'NSSizeFromString(_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nssizefromstring(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nssizefromstring(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssizefromstring%28_%3A%29.json'
content_hash: 'sha256:ca48589d87005d0c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSSizeFromString(_:)

<sub>Function</sub>

Returns an `NSSize` from a text-based representation.

<sub>Mac Catalyst, macOS</sub>

```swift
func NSSizeFromString(_ aString: String) -> NSSize
```

## Discussion

Scans `aString` for two numbers which are used as the width and height, in that order, to create an `NSSize` struct. If `aString` only contains a single number, it is used as the width. The `aString` argument should be formatted like the output of [NSStringFromSize](<nsstringfromsize(__).md>), for example, `@"{10,20}"`. If `aString` does not contain any numbers, this function returns an `NSSize` struct whose width and height are both `0`.

## See Also

### Managing Sizes

- [NSEqualSizes](<nsequalsizes(____).md>) — Returns a Boolean that indicates whether two size values are equal.
- [NSMakeSize](<nsmakesize(____).md>) — Returns a new `NSSize` from the specified values.
- [NSStringFromSize](<nsstringfromsize(__).md>) — Returns a string representation of a size.
- [NSSizeFromCGSize](<nssizefromcgsize(__).md>) — Returns an `NSSize` typecast from a `CGSize`.
- [NSSizeToCGSize](<nssizetocgsize(__).md>) — Returns a `CGSize` typecast from an `NSSize`.
