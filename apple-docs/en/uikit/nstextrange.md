---
title: NSTextRange
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextrange
source_url: 'https://developer.apple.com/documentation/uikit/nstextrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextrange.json'
content_hash: 'sha256:d25395d26b224ea3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextRange

<sub>Class</sub>

A class that represents a contiguous range between two locations inside document contents.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class NSTextRange
```

## Overview

An `NSTextRange` consists of the starting and terminating locations. There the two basic properties: [location](nstextrange/location.md) and [endLocation](nstextrange/endlocation.md), respectively. The terminating [location](nstextrange/location.md), [endLocation](nstextrange/endlocation.md), is directly following the last location in the range. For example, a location contains a range if `(range.location <= location) && (location < range.endLocation)` is `true`.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a text range

- [- initWithLocation:](<nstextrange/init(location_).md>) — Creates a new text range at the location you specify.
- [- initWithLocation:endLocation:](<nstextrange/init(location_end_).md>) — Creates a new text range with the starting and ending locations you specify.

### Characteristics of the text range

- [location](nstextrange/location.md) — The starting location of the text range.
- [endLocation](nstextrange/endlocation.md) — The ending location of the text range.
- [empty](nstextrange/isempty.md) — Returns whether the text range is empty.

### Comparing text ranges

- [- textRangeByIntersectingWithTextRange:](<nstextrange/intersection(__).md>) — Returns the range, if any, where two text ranges intersect.
- [- intersectsWithTextRange:](<nstextrange/intersects(__).md>) — Determines if two ranges intersect.
- [- isEqualToTextRange:](<nstextrange/isequal(to_).md>) — Compares two text ranges.
- [- textRangeByFormingUnionWithTextRange:](<nstextrange/union(__).md>) — Returns a new text range by forming the union with the text range you provide.

### Finding text within the text range

- [- containsLocation:](<nstextrange/contains(__)-7hvi0.md>) — Determines if the text location you specify is in the current text range.
- [- containsRange:](<nstextrange/contains(__)-5j4y2.md>) — Determines if the text range you specify is in the current text range.

### Initializers

- [init(location:endLocation:)](<nstextrange/init(location_endlocation_).md>)

## See Also

### Location and selection

- [NSTextSelection](nstextselection.md) — A class that represents a single logical selection context that corresponds to an insertion point.
- [NSTextSelectionNavigation](nstextselectionnavigation.md) — An interface you use to expose methods for obtaining results from actions performed on text selections.
- [NSTextLocation](nstextlocation.md) — An interface you implement that represents an abstract location inside your document’s content.
