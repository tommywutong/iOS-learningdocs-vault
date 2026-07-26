---
title: 'NSEqualPoints(_:_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsequalpoints(_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsequalpoints(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsequalpoints%28_%3A_%3A%29.json'
content_hash: 'sha256:909d52b3e41b2db5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSEqualPoints(_:_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether two points are equal.

<sub>Mac Catalyst, macOS</sub>

```swift
func NSEqualPoints(_ aPoint: NSPoint, _ bPoint: NSPoint) -> Bool
```

## Return Value

[true](../swift/true.md) if the two points `aPoint` and `bPoint` are identical, otherwise [false](../swift/false.md).

## See Also

### Managing Points

- [NSMakePoint](<nsmakepoint(____).md>) — Creates a new `NSPoint` from the specified values.
- [NSPointFromString](<nspointfromstring(__).md>) — Returns a point from a text-based representation.
- [NSStringFromPoint](<nsstringfrompoint(__).md>) — Returns a string representation of a point.
- [NSPointFromCGPoint](<nspointfromcgpoint(__).md>) — Returns an `NSPoint` typecast from a `CGPoint`.
- [NSPointToCGPoint](<nspointtocgpoint(__).md>) — Returns a `CGPoint` typecast from an `NSPoint`.
