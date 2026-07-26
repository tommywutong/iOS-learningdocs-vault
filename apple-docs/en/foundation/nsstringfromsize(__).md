---
title: 'NSStringFromSize(_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstringfromsize(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstringfromsize(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstringfromsize%28_%3A%29.json'
content_hash: 'sha256:5b0aee7882942dae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSStringFromSize(_:)

<sub>Function</sub>

Returns a string representation of a size.

<sub>Mac Catalyst, macOS</sub>

```swift
func NSStringFromSize(_ aSize: NSSize) -> String
```

## Return Value

A string of the form “{a, b}”, where a and b are the width and height, respectively, of `aSize`.

## See Also

### Managing Sizes

- [NSEqualSizes](<nsequalsizes(____).md>) — Returns a Boolean that indicates whether two size values are equal.
- [NSMakeSize](<nsmakesize(____).md>) — Returns a new `NSSize` from the specified values.
- [NSSizeFromString](<nssizefromstring(__).md>) — Returns an `NSSize` from a text-based representation.
- [NSSizeFromCGSize](<nssizefromcgsize(__).md>) — Returns an `NSSize` typecast from a `CGSize`.
- [NSSizeToCGSize](<nssizetocgsize(__).md>) — Returns a `CGSize` typecast from an `NSSize`.
