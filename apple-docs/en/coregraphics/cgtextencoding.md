---
title: CGTextEncoding
framework: Core Graphics
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+（7.0 起废弃）, iPadOS 2.0+（7.0 起废弃）, tvOS, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/coregraphics/cgtextencoding
source_url: 'https://developer.apple.com/documentation/coregraphics/cgtextencoding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgtextencoding.json'
content_hash: 'sha256:2340b4e80c6651ae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGTextEncoding

<sub>Enumeration</sub>

Text encodings for fonts.

<sub>tvOS, visionOS, watchOS</sub>

```swift
enum CGTextEncoding
```

## Overview

For more information on setting the font in a graphics context, see [CGContextSelectFont](<cgcontext/selectfont(name_size_textencoding_).md>).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCGEncodingFontSpecific](cgtextencoding/encodingfontspecific.md) — The built-in encoding of the font.
- [kCGEncodingMacRoman](cgtextencoding/encodingmacroman.md) — The MacRoman encoding. MacRoman is an ASCII variant originally created for use in the Mac OS, in which characters 127 and lower are ASCII, and characters 128 and higher are non-English characters and symbols.

### Initializers

- [init(rawValue:)](<cgtextencoding/init(rawvalue_).md>)

## See Also

### Constants

- [CGPathFillRule](cgpathfillrule.md) — Rules for determining which regions are interior to a path, used by the [fillPath(using:)](<cgcontext/fillpath(using_).md>) and [clip(using:)](<cgcontext/clip(using_).md>) methods.
