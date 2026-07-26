---
title: 'NSIntersectionRange(_:_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsintersectionrange(_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsintersectionrange(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsintersectionrange%28_%3A_%3A%29.json'
content_hash: 'sha256:d96ed81043e00877'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSIntersectionRange(_:_:)

<sub>Function</sub>

Returns the intersection of the specified ranges.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSIntersectionRange(_ range1: NSRange, _ range2: NSRange) -> NSRange
```

## Return Value

A range describing the intersection of `range1` and `range2`—that is, a range containing the indices that exist in both ranges.

## Discussion

If the returned range’s length field is 0, then the two ranges don’t intersect, and the value of the location field is undefined.

## See Also

### Managing ranges

- [NSEqualRanges](<nsequalranges(____).md>) — Returns a Boolean value that indicates whether two given ranges are equal.
- [NSLocationInRange](<nslocationinrange(____).md>) — Returns a Boolean value that indicates whether a specified position is in a given range.
- [NSMakeRange](<nsmakerange(____).md>) — Creates a new NSRange from the specified values.
- [NSMaxRange](<nsmaxrange(__).md>) — Returns the sum of the location and length of the range.
- [NSRangeFromString](<nsrangefromstring(__).md>) — Returns a range from a textual representation.
- [NSStringFromRange](<nsstringfromrange(__).md>) — Returns a string representation of a range.
- [NSUnionRange](<nsunionrange(____).md>) — Returns the union of the specified ranges.
