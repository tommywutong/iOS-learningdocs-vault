---
title: NSTextTab
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstexttab
source_url: 'https://developer.apple.com/documentation/uikit/nstexttab'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstexttab.json'
content_hash: 'sha256:674de4d28378c336'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextTab

<sub>Class</sub>

A tab in a paragraph.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class NSTextTab
```

## Overview

A text tab represents a tab in an [NSParagraphStyle](nsparagraphstyle.md) object, storing an alignment type and location. [NSTextTab](nstexttab.md) objects are most frequently used with the TextKit system and with [NSRulerView](../appkit/nsrulerview.md) and [NSRulerMarker](../appkit/nsrulermarker.md) objects.

The text system supports four alignment types: left, center, right, and decimal (based on the decimal separator character of the locale in effect). These alignment types are absolute, not based on the line sweep direction of text. For example, tabbed text is always positioned to the left of a right-aligned tab, whether the line sweep direction is left to right or right to left. A tab’s location, on the other hand, is relative to the back margin. A tab set at 1.5”, for example, is at 1.5” from the right in right to left text.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Creating a text tab

- [- initWithTextAlignment:location:options:](<nstexttab/init(textalignment_location_options_).md>) — Initializes a text tab with the specified text alignment, location, and options.

### Getting tab stop information

- [location](nstexttab/location.md) — The text tab’s ruler location relative to the back margin.

### Getting text tab information

- [alignment](nstexttab/alignment.md) — The text alignment of the text tab.
- [options](nstexttab/options.md) — The dictionary of attributes for the text tab.
- [+ columnTerminatorsForLocale:](<nstexttab/columnterminators(for_).md>) — Returns the column terminators for the specified locale.

### Constants

- [NSParagraphStyle.TextTabType](../appkit/nsparagraphstyle/texttabtype.md) — Constants that specify the type of tab stop. _(deprecated)_
- [OptionKey](nstexttab/optionkey.md) — The terminating character for a tab column.

### Deprecated

- [init(type:location:)](<../appkit/nstexttab/init(type_location_).md>) — Initializes a newly allocated text tab with the specified alignment and location. _(deprecated)_
- [tabStopType](../appkit/nstexttab/tabstoptype.md) — The text tab’s type of tab stop. _(deprecated)_

### Initializers

- [init(coder:)](<nstexttab/init(coder_).md>)

## See Also

### Formatting and attributes

- [NSParagraphStyle](nsparagraphstyle.md) — The paragraph or ruler attributes for an attributed string.
- [NSMutableParagraphStyle](nsmutableparagraphstyle.md) — An object for changing the values of the subattributes in a paragraph style attribute.
- [NSTextList](nstextlist.md) — A section of text that forms a single list.
- [Adding tables to attributed strings in UIKit](adding-tables-to-attributed-strings.md) — Create and configure tables in attributed strings and display them in a text view.
