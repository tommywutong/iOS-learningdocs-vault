---
title: CTFontFormat
framework: Core Text
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctfontformat
source_url: 'https://developer.apple.com/documentation/coretext/ctfontformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontformat.json'
content_hash: 'sha256:85f21f03edc6abdf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontFormat

<sub>Enumeration</sub>

The recognized format of the font.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CTFontFormat
```

## Overview

Use the values of this enumeration for [kCTFontFormatAttribute](kctfontformatattribute.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Font Formats

- [kCTFontFormatUnrecognized](ctfontformat/unrecognized.md) — The font is not a recognized format.
- [kCTFontFormatOpenTypePostScript](ctfontformat/opentypepostscript.md) — The font is an OpenType format containing PostScript data.
- [kCTFontFormatOpenTypeTrueType](ctfontformat/opentypetruetype.md) — The font is an OpenType format containing TrueType data.
- [kCTFontFormatTrueType](ctfontformat/truetype.md) — The font is a recognized TrueType format.
- [kCTFontFormatPostScript](ctfontformat/postscript.md) — The font is a recognized PostScript format.
- [kCTFontFormatBitmap](ctfontformat/bitmap.md) — The font is a bitmap-only format.

### Initializers

- [init(rawValue:)](<ctfontformat/init(rawvalue_).md>)

## See Also

### Related Documentation

- [kCTFontFormatAttribute](kctfontformatattribute.md) — The recognized format of the font.

### Accessing Font Attributes

- [Font Attributes](font-attributes.md) — The keys for accessing font attributes from a font descriptor.
- [CTFontOrientation](ctfontorientation.md) — The intended rendering orientation of the font for obtaining glyph metrics.
- [CTFontPriority](ctfontpriority.md) — The priority of font descriptors when resolving duplicates and sorting match results.
