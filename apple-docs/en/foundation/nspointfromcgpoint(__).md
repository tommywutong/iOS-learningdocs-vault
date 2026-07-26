---
title: 'NSPointFromCGPoint(_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nspointfromcgpoint(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nspointfromcgpoint(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspointfromcgpoint%28_%3A%29.json'
content_hash: 'sha256:d79b1c9726e40654'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSPointFromCGPoint(_:)

<sub>Function</sub>

Returns an `NSPoint` typecast from a `CGPoint`.

<sub>Mac Catalyst, macOS</sub>

```swift
func NSPointFromCGPoint(_ cgpoint: CGPoint) -> NSPoint
```

## Return Value

An `NSPoint` typecast from a `CGPoint`.

## See Also

### Related Documentation

- [NSRectFromCGRect](<nsrectfromcgrect(__).md>) — Returns an `NSRect` typecast from a `CGRect`.
- [NSSizeFromCGSize](<nssizefromcgsize(__).md>) — Returns an `NSSize` typecast from a `CGSize`.

### Managing Points

- [NSEqualPoints](<nsequalpoints(____).md>) — Returns a Boolean value that indicates whether two points are equal.
- [NSMakePoint](<nsmakepoint(____).md>) — Creates a new `NSPoint` from the specified values.
- [NSPointFromString](<nspointfromstring(__).md>) — Returns a point from a text-based representation.
- [NSStringFromPoint](<nsstringfrompoint(__).md>) — Returns a string representation of a point.
- [NSPointToCGPoint](<nspointtocgpoint(__).md>) — Returns a `CGPoint` typecast from an `NSPoint`.
