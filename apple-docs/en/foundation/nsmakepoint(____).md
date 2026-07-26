---
title: 'NSMakePoint(_:_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmakepoint(_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmakepoint(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmakepoint%28_%3A_%3A%29.json'
content_hash: 'sha256:30599bf65c7a2ea8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMakePoint(_:_:)

<sub>Function</sub>

Creates a new `NSPoint` from the specified values.

<sub>Mac Catalyst, macOS</sub>

```swift
func NSMakePoint(_ x: Double, _ y: Double) -> NSPoint
```

## Return Value

An `NSPoint` having the coordinates `x` and `y`.

## See Also

### Managing Points

- [NSEqualPoints](<nsequalpoints(____).md>) — Returns a Boolean value that indicates whether two points are equal.
- [NSPointFromString](<nspointfromstring(__).md>) — Returns a point from a text-based representation.
- [NSStringFromPoint](<nsstringfrompoint(__).md>) — Returns a string representation of a point.
- [NSPointFromCGPoint](<nspointfromcgpoint(__).md>) — Returns an `NSPoint` typecast from a `CGPoint`.
- [NSPointToCGPoint](<nspointtocgpoint(__).md>) — Returns a `CGPoint` typecast from an `NSPoint`.
