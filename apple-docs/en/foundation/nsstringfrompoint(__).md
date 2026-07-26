---
title: 'NSStringFromPoint(_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstringfrompoint(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstringfrompoint(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstringfrompoint%28_%3A%29.json'
content_hash: 'sha256:84696562d41ebd43'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSStringFromPoint(_:)

<sub>Function</sub>

Returns a string representation of a point.

<sub>Mac Catalyst, macOS</sub>

```swift
func NSStringFromPoint(_ aPoint: NSPoint) -> String
```

## Parameters

- `aPoint` — A point structure.

## Return Value

A string of the form “{a, b}”, where a and b are the x and y coordinates of `aPoint`.

## See Also

### Managing Points

- [NSEqualPoints](<nsequalpoints(____).md>) — Returns a Boolean value that indicates whether two points are equal.
- [NSMakePoint](<nsmakepoint(____).md>) — Creates a new `NSPoint` from the specified values.
- [NSPointFromString](<nspointfromstring(__).md>) — Returns a point from a text-based representation.
- [NSPointFromCGPoint](<nspointfromcgpoint(__).md>) — Returns an `NSPoint` typecast from a `CGPoint`.
- [NSPointToCGPoint](<nspointtocgpoint(__).md>) — Returns a `CGPoint` typecast from an `NSPoint`.
