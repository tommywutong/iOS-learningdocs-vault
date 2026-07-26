---
title: 'NSSizeToCGSize(_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nssizetocgsize(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nssizetocgsize(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssizetocgsize%28_%3A%29.json'
content_hash: 'sha256:8a21ebee06216c13'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSSizeToCGSize(_:)

<sub>Function</sub>

Returns a `CGSize` typecast from an `NSSize`.

<sub>Mac Catalyst, macOS</sub>

```swift
func NSSizeToCGSize(_ nssize: NSSize) -> CGSize
```

## Return Value

A `CGSize` typecast from an `NSSize`.

## See Also

### Related Documentation

- [NSPointToCGPoint](<nspointtocgpoint(__).md>) — Returns a `CGPoint` typecast from an `NSPoint`.
- [NSRectToCGRect](<nsrecttocgrect(__).md>) — Returns a `CGRect` typecast from an `NSRect`.

### Managing Sizes

- [NSEqualSizes](<nsequalsizes(____).md>) — Returns a Boolean that indicates whether two size values are equal.
- [NSMakeSize](<nsmakesize(____).md>) — Returns a new `NSSize` from the specified values.
- [NSSizeFromString](<nssizefromstring(__).md>) — Returns an `NSSize` from a text-based representation.
- [NSStringFromSize](<nsstringfromsize(__).md>) — Returns a string representation of a size.
- [NSSizeFromCGSize](<nssizefromcgsize(__).md>) — Returns an `NSSize` typecast from a `CGSize`.
