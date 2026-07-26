---
title: NSRange
framework: Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsrange-swift.typealias
source_url: 'https://developer.apple.com/documentation/foundation/nsrange-swift.typealias'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsrange-swift.typealias.json'
content_hash: 'sha256:009e6811abca10ec'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSRange

<sub>Type Alias</sub>

A structure used to describe a portion of a series, such as characters in a string or objects in an array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias NSRange = _NSRange
```

## Discussion

Foundation functions that operate on ranges include the following:

- [NSEqualRanges](<nsequalranges(____).md>)
- [NSIntersectionRange](<nsintersectionrange(____).md>)
- [NSLocationInRange](<nslocationinrange(____).md>)
- [NSMakeRange](<nsmakerange(____).md>)
- [NSMaxRange](<nsmaxrange(__).md>)
- [NSRangeFromString](<nsrangefromstring(__).md>)
- [NSStringFromRange](<nsstringfromrange(__).md>)
- [NSUnionRange](<nsunionrange(____).md>)

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a range

- [init()](<nsrange-swift.typealias/init().md>) — Creates an empty range.
- [init(location:length:)](<nsrange-swift.typealias/init(location_length_).md>) — Creates a range with the given location and length.

### Accessing range properties

- [location](nsrange-swift.typealias/location.md) — The index of the first member of the range.
- [length](nsrange-swift.typealias/length.md) — The number of items in the range.

### Managing ranges

- [NSEqualRanges](<nsequalranges(____).md>) — Returns a Boolean value that indicates whether two given ranges are equal.
- [NSIntersectionRange](<nsintersectionrange(____).md>) — Returns the intersection of the specified ranges.
- [NSLocationInRange](<nslocationinrange(____).md>) — Returns a Boolean value that indicates whether a specified position is in a given range.
- [NSMakeRange](<nsmakerange(____).md>) — Creates a new NSRange from the specified values.
- [NSMaxRange](<nsmaxrange(__).md>) — Returns the sum of the location and length of the range.
- [NSRangeFromString](<nsrangefromstring(__).md>) — Returns a range from a textual representation.
- [NSStringFromRange](<nsstringfromrange(__).md>) — Returns a string representation of a range.
- [NSUnionRange](<nsunionrange(____).md>) — Returns the union of the specified ranges.

### Related types

- [NSRangePointer](nsrangepointer.md) — Type indicating a parameter is a pointer to an `NSRange` structure.
- [NSNotFound](nsnotfound-4qp9h.md) — A value indicating that a requested item couldn’t be found or doesn’t exist.
