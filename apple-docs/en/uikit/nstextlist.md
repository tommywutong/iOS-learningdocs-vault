---
title: NSTextList
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlist
source_url: 'https://developer.apple.com/documentation/uikit/nstextlist'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlist.json'
content_hash: 'sha256:d88dbb7137c995c7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextList

<sub>Class</sub>

A section of text that forms a single list.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class NSTextList
```

## Overview

The visible elements of the list, including list markers, appear in the text as they do for lists created by hand. The list object, however, allows the list to be recognized as such by the text system. This enables automatic creation of markers and spacing. Text lists are used in HTML import and export.

Text lists appear as attributes on paragraphs, as part of the paragraph style. An [NSParagraphStyle](nsparagraphstyle.md) may have an array of text lists, representing the nested lists containing the paragraph, in order from outermost to innermost. For example, if list1 contains four paragraphs, the middle two of which are also in the inner list2, then the text lists array for the first and fourth paragraphs is (list1), while the text lists array for the second and third paragraphs is (list1, list2).

The methods implementing this are [textLists](nsparagraphstyle/textlists.md) on [NSParagraphStyle](nsparagraphstyle.md), and [textLists](nsmutableparagraphstyle/textlists.md) on [NSMutableParagraphStyle](nsmutableparagraphstyle.md).

In addition, [NSAttributedString](../foundation/nsattributedstring.md) has convenience methods for lists, such as [range(of:at:)](<../foundation/nsattributedstring/range(of_at_)-6um0x.md>), which determines the range covered by a list, and [itemNumber(in:at:)](<../foundation/nsattributedstring/itemnumber(in_at_).md>), which determines the ordinal position within a list of a particular item.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Creating a text list

- [- initWithCoder:](<nstextlist/init(coder_).md>) — Initializes and returns a newly allocated text list item.
- [- initWithMarkerFormat:options:](<nstextlist/init(markerformat_options_).md>) — Returns an initialized text list.
- [- initWithMarkerFormat:options:startingItemNumber:](<nstextlist/init(markerformat_options_startingitemnumber_).md>) — Returns a new text list with the format, options, and starting item number you provide.

### Working with markers

- [markerFormat](nstextlist/markerformat-swift.property.md) — Returns the marker format string used by the receiver.
- [MarkerFormat](nstextlist/markerformat-swift.struct.md) — Constants that describe marker symbols you can apply to list elements in text lists.
- [- markerForItemNumber:](<nstextlist/marker(foritemnumber_).md>) — Returns the computed value for a specific ordinal position in the list.

### Getting list options

- [ordered](nstextlist/isordered.md) — A Boolean value that indicates whether the list is ordered.
- [listOptions](nstextlist/listoptions.md) — Returns the list options mask value of the receiver.
- [Options](nstextlist/options.md) — Values that available options for text list items.

### Managing item numbering

- [startingItemNumber](nstextlist/startingitemnumber.md) — Sets the starting item number for the text list.

### Constants

- [NSTextListPrependEnclosingMarker](nstextlist/options/prependenclosingmarker.md) — Specifies that a nested list should include the marker for its enclosing superlist before its own marker.

### Type Properties

- [includesTextListMarkers](nstextlist/includestextlistmarkers.md) — A Boolean value that indicates whether TextKit includes text list markers in the contents.

## See Also

### Formatting and attributes

- [NSParagraphStyle](nsparagraphstyle.md) — The paragraph or ruler attributes for an attributed string.
- [NSMutableParagraphStyle](nsmutableparagraphstyle.md) — An object for changing the values of the subattributes in a paragraph style attribute.
- [NSTextTab](nstexttab.md) — A tab in a paragraph.
- [Adding tables to attributed strings in UIKit](adding-tables-to-attributed-strings.md) — Create and configure tables in attributed strings and display them in a text view.
