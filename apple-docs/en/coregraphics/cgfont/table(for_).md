---
title: 'table(for:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgfont/table(for:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfont/table(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfont/table%28for%3A%29.json'
content_hash: 'sha256:13d86c84be406ac5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGFont](../cgfont.md)

# table(for:)

<sub>Instance Method</sub>

Returns the font table that corresponds to the provided tag.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func table(for tag: UInt32) -> CFData?
```

## Parameters

- `tag` — The tag for the table you want to obtain.

## Return Value

The font table that corresponds to the tag, or `nil` if no such table exists.

## See Also

### Working with Font Tables

- [CGFontCopyTableTags](tabletags.md) — Returns an array of tags that correspond to the font tables for a font.
- [Font Table Index Values](../font-table-index-values.md) — Possible values for an index into a font table.
- [Obsolete Font Table Index Values](../obsolete-font-table-index-values.md) — Deprecated values for an index into a font table.
