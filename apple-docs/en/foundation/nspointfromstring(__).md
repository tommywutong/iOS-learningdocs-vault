---
title: 'NSPointFromString(_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nspointfromstring(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nspointfromstring(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspointfromstring%28_%3A%29.json'
content_hash: 'sha256:9449fe0e46a0474f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSPointFromString(_:)

<sub>Function</sub>

Returns a point from a text-based representation.

<sub>Mac Catalyst, macOS</sub>

```swift
func NSPointFromString(_ aString: String) -> NSPoint
```

## Parameters

- `aString` — A string of the form “{x, y}”.

## Return Value

If `aString` is of the form “{x, y}” an `NSPoint` structure that uses x and y as the x and y coordinates, in that order.

## Discussion

If `aString` only contains a single number, it is used as the x coordinate. If `aString` does not contain any numbers, returns an `NSPoint` object whose x and y coordinates are both 0.

## See Also

### Managing Points

- [NSEqualPoints](<nsequalpoints(____).md>) — Returns a Boolean value that indicates whether two points are equal.
- [NSMakePoint](<nsmakepoint(____).md>) — Creates a new `NSPoint` from the specified values.
- [NSStringFromPoint](<nsstringfrompoint(__).md>) — Returns a string representation of a point.
- [NSPointFromCGPoint](<nspointfromcgpoint(__).md>) — Returns an `NSPoint` typecast from a `CGPoint`.
- [NSPointToCGPoint](<nspointtocgpoint(__).md>) — Returns a `CGPoint` typecast from an `NSPoint`.
