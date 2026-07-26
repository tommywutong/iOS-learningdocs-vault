---
title: NSTextList.MarkerFormat
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlist/markerformat-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/nstextlist/markerformat-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlist/markerformat-swift.struct.json'
content_hash: 'sha256:dd951ea0b2ef7125'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextList](../nstextlist.md)

# NSTextList.MarkerFormat

<sub>Structure</sub>

Constants that describe marker symbols you can apply to list elements in text lists.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
struct MarkerFormat
```

## Overview

Select a marker symbol to apply to your list elements in your text list, then set it in [markerFormat](markerformat-swift.property.md). Or, specify a marker symbol when you create a text list with [- initWithMarkerFormat:options:](<init(markerformat_options_).md>) or [- initWithMarkerFormat:options:startingItemNumber:](<init(markerformat_options_startingitemnumber_).md>).

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Selecting a marker format

- [NSTextListMarkerBox](markerformat-swift.struct/box.md) — The value that represents a square-shaped marker that you can apply to a text list item.
- [NSTextListMarkerCheck](markerformat-swift.struct/check.md) — The value that represents a checkmark-shaped marker that you can apply to a text list item.
- [NSTextListMarkerCircle](markerformat-swift.struct/circle.md) — The value that represents a circle-shaped marker that you can apply to a text list item.
- [NSTextListMarkerDecimal](markerformat-swift.struct/decimal.md) — The value that represents a decimal annotation marker that you can apply to a text list item.
- [NSTextListMarkerDiamond](markerformat-swift.struct/diamond.md) — The value that represents a diamond-shaped marker that you can apply to a text list item.
- [NSTextListMarkerDisc](markerformat-swift.struct/disc.md) — The value that represents a disc-shaped marker that you can apply to a text list item.
- [NSTextListMarkerHyphen](markerformat-swift.struct/hyphen.md) — The value that represents a hyphen-shaped marker that you can apply to a text list item.
- [NSTextListMarkerLowercaseAlpha](markerformat-swift.struct/lowercasealpha.md) — The value that represents a lowercase localized alphabetical marker you that can apply to a text list item.
- [NSTextListMarkerLowercaseHexadecimal](markerformat-swift.struct/lowercasehexadecimal.md) — The value that represents a lowercase hexadecimal (base 16) numerical marker that you can apply to a text list item.
- [NSTextListMarkerLowercaseLatin](markerformat-swift.struct/lowercaselatin.md) — The value that represents a lowercase Latin alphabetical marker that you can apply to a text list item.
- [NSTextListMarkerLowercaseRoman](markerformat-swift.struct/lowercaseroman.md) — The value that represents a lowercase Roman numeral marker that you can apply to a text list item.
- [NSTextListMarkerOctal](markerformat-swift.struct/octal.md) — The value that represents an octal (base 8) numerical marker that you can apply to a text list item.
- [NSTextListMarkerSquare](markerformat-swift.struct/square.md) — The value that represents a square-shaped marker that you can apply to a text list item.
- [NSTextListMarkerUppercaseAlpha](markerformat-swift.struct/uppercasealpha.md) — The value that represents an uppercase localized alphabetical marker that you can apply to a text list item.
- [NSTextListMarkerUppercaseHexadecimal](markerformat-swift.struct/uppercasehexadecimal.md) — The value that represents an uppercase hexadecimal (base 16) numerical marker that you can apply to a text list item.
- [NSTextListMarkerUppercaseLatin](markerformat-swift.struct/uppercaselatin.md) — The value that represents an uppercase Latin alphabetical marker that you can apply to a text list item.
- [NSTextListMarkerUppercaseRoman](markerformat-swift.struct/uppercaseroman.md) — The value that represents an uppercase Roman numeral marker that you can apply to a text list item.

### Initializing a marker format

- [init(_:)](<markerformat-swift.struct/init(__).md>) — Creates a new marker that you can apply to an item in a text list with the raw value you provide.
- [init(rawValue:)](<markerformat-swift.struct/init(rawvalue_).md>) — Creates a new marker that you can apply to an item in a text list using the string you provide.

## See Also

### Working with markers

- [markerFormat](markerformat-swift.property.md) — Returns the marker format string used by the receiver.
- [- markerForItemNumber:](<marker(foritemnumber_).md>) — Returns the computed value for a specific ordinal position in the list.
