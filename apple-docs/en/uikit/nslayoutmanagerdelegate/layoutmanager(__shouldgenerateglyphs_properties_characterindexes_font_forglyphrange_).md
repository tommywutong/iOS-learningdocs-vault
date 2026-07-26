---
title: 'layoutManager(_:shouldGenerateGlyphs:properties:characterIndexes:font:forGlyphRange:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanagerdelegate/layoutmanager(_:shouldgenerateglyphs:properties:characterindexes:font:forglyphrange:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate/layoutmanager(_:shouldgenerateglyphs:properties:characterindexes:font:forglyphrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanagerdelegate/layoutmanager%28_%3Ashouldgenerateglyphs%3Aproperties%3Acharacterindexes%3Afont%3Aforglyphrange%3A%29.json'
content_hash: 'sha256:a1908469b633b6bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManagerDelegate](../nslayoutmanagerdelegate.md)

# layoutManager(_:shouldGenerateGlyphs:properties:characterIndexes:font:forGlyphRange:)

<sub>Instance Method</sub>

Enables customization of the initial glyph generation process.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func layoutManager(_ layoutManager: NSLayoutManager, shouldGenerateGlyphs glyphs: UnsafePointer<CGGlyph>, properties props: UnsafePointer<NSLayoutManager.GlyphProperty>, characterIndexes charIndexes: UnsafePointer<Int>, font aFont: UIFont, forGlyphRange glyphRange: NSRange) -> Int
```

## Parameters

- `layoutManager` — The layout manager doing the layout.

- `glyphs` — A pointer to the layout manager’s glyph cache.

- `props` — A pointer to a buffer containing glyph properties for the glyphs in the cache.

- `charIndexes` — A pointer to the starting index for the characters in the text storage for which glyphs are generated.

- `aFont` — A font to override the font attributes in the text storage for the specified character range.

- `glyphRange` — The range of glyphs in the glyph cache to set.

## Return Value

The actual glyph range stored in this method. By returning `0`, it can indicate for the layout manager to do the default processing.

## Discussion

This message is sent whenever the layout manager is about to store the initial glyph information via [- setGlyphs:properties:characterIndexes:font:forGlyphRange:](<../nslayoutmanager/setglyphs(__properties_characterindexes_font_forglyphrange_).md>). To customize the initial glyph generation process, this method can invoke [- setGlyphs:properties:characterIndexes:font:forGlyphRange:](<../nslayoutmanager/setglyphs(__properties_characterindexes_font_forglyphrange_).md>) with modified glyph information.

> [!note] Note
> Querying glyph information surrounding `glyphRange` could lead to recursion since the data might not be available yet.

## See Also

### Invalidating glyphs and layout

- [- layoutManagerDidInvalidateLayout:](<layoutmanagerdidinvalidatelayout(__).md>) — Informs the delegate when the specified layout manager invalidates layout information (not glyph information).
- [- layoutManager:shouldUseAction:forControlCharacterAtIndex:](<layoutmanager(__shoulduse_forcontrolcharacterat_).md>) — Returns the control character action for the control character at the specified character index.
- [ControlCharacterAction](../nslayoutmanager/controlcharacteraction.md) — Constants that describe actions for control characters.
