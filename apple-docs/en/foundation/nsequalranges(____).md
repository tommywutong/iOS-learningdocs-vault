---
title: 'NSEqualRanges(_:_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsequalranges(_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsequalranges(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsequalranges%28_%3A_%3A%29.json'
content_hash: 'sha256:88890da4b8f3a0be'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSEqualRanges(_:_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether two given ranges are equal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSEqualRanges(_ range1: NSRange, _ range2: NSRange) -> Bool
```

## Return Value

[true](../swift/true.md) if `range1` and `range2` have the same locations and lengths.

## See Also

### Managing ranges

- [NSIntersectionRange](<nsintersectionrange(____).md>) — Returns the intersection of the specified ranges.
- [NSLocationInRange](<nslocationinrange(____).md>) — Returns a Boolean value that indicates whether a specified position is in a given range.
- [NSMakeRange](<nsmakerange(____).md>) — Creates a new NSRange from the specified values.
- [NSMaxRange](<nsmaxrange(__).md>) — Returns the sum of the location and length of the range.
- [NSRangeFromString](<nsrangefromstring(__).md>) — Returns a range from a textual representation.
- [NSStringFromRange](<nsstringfromrange(__).md>) — Returns a string representation of a range.
- [NSUnionRange](<nsunionrange(____).md>) — Returns the union of the specified ranges.
