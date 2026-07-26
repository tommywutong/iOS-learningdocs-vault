---
title: 'NSMaxRange(_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmaxrange(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmaxrange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmaxrange%28_%3A%29.json'
content_hash: 'sha256:f6194fcf6d78d552'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMaxRange(_:)

<sub>Function</sub>

Returns the sum of the location and length of the range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSMaxRange(_ range: NSRange) -> Int
```

## Return Value

The sum of the location and length of the range—that is, `range.location` + `range.length`.

## See Also

### Managing ranges

- [NSEqualRanges](<nsequalranges(____).md>) — Returns a Boolean value that indicates whether two given ranges are equal.
- [NSIntersectionRange](<nsintersectionrange(____).md>) — Returns the intersection of the specified ranges.
- [NSLocationInRange](<nslocationinrange(____).md>) — Returns a Boolean value that indicates whether a specified position is in a given range.
- [NSMakeRange](<nsmakerange(____).md>) — Creates a new NSRange from the specified values.
- [NSRangeFromString](<nsrangefromstring(__).md>) — Returns a range from a textual representation.
- [NSStringFromRange](<nsstringfromrange(__).md>) — Returns a string representation of a range.
- [NSUnionRange](<nsunionrange(____).md>) — Returns the union of the specified ranges.
