---
title: tableTags
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgfont/tabletags
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfont/tabletags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfont/tabletags.json'
content_hash: 'sha256:523df21e4925b8d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGFont](../cgfont.md)

# tableTags

<sub>Instance Property</sub>

Returns an array of tags that correspond to the font tables for a font.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var tableTags: CFArray? { get }
```

## Discussion

Each entry in the returned array is a four-byte value that represents a single TrueType or OpenType font table tag. To obtain a tag at index `k` in a manner that is appropriate for 32-bit and 64-bit architectures, you need to use code similar to the following:

```objc
tag = (uint32_t)(uintptr_t)CFArrayGetValue(table, k);
```

## See Also

### Working with Font Tables

- [CGFontCopyTableForTag](<table(for_).md>) — Returns the font table that corresponds to the provided tag.
- [Font Table Index Values](../font-table-index-values.md) — Possible values for an index into a font table.
- [Obsolete Font Table Index Values](../obsolete-font-table-index-values.md) — Deprecated values for an index into a font table.
