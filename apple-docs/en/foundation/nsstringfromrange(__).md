---
title: 'NSStringFromRange(_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstringfromrange(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstringfromrange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstringfromrange%28_%3A%29.json'
content_hash: 'sha256:55dcba6a2925dc7e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSStringFromRange(_:)

<sub>Function</sub>

Returns a string representation of a range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSStringFromRange(_ range: NSRange) -> String
```

## Return Value

A string of the form “{a, b}”, where a and b are non-negative integers representing `aRange`.

## See Also

### Managing ranges

- [NSEqualRanges](<nsequalranges(____).md>) — Returns a Boolean value that indicates whether two given ranges are equal.
- [NSIntersectionRange](<nsintersectionrange(____).md>) — Returns the intersection of the specified ranges.
- [NSLocationInRange](<nslocationinrange(____).md>) — Returns a Boolean value that indicates whether a specified position is in a given range.
- [NSMakeRange](<nsmakerange(____).md>) — Creates a new NSRange from the specified values.
- [NSMaxRange](<nsmaxrange(__).md>) — Returns the sum of the location and length of the range.
- [NSRangeFromString](<nsrangefromstring(__).md>) — Returns a range from a textual representation.
- [NSUnionRange](<nsunionrange(____).md>) — Returns the union of the specified ranges.
