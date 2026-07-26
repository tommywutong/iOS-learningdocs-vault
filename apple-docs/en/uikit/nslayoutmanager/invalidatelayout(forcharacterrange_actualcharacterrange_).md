---
title: 'invalidateLayout(forCharacterRange:actualCharacterRange:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/invalidatelayout(forcharacterrange:actualcharacterrange:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/invalidatelayout(forcharacterrange:actualcharacterrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/invalidatelayout%28forcharacterrange%3Aactualcharacterrange%3A%29.json'
content_hash: 'sha256:0cbf92b74366f713'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# invalidateLayout(forCharacterRange:actualCharacterRange:)

<sub>Instance Method</sub>

Invalidates the layout information for the glyphs that map to the specified character range.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func invalidateLayout(forCharacterRange charRange: NSRange, actualCharacterRange actualCharRange: NSRangePointer?)
```

## Parameters

- `charRange` — The range of characters to invalidate.

- `actualCharRange` — If not `NULL`, on output, the actual range invalidated after any necessary expansion.

## Discussion

This method has the same effect as [invalidateLayout(forCharacterRange:isSoft:actualCharacterRange:)](<../../appkit/nslayoutmanager/invalidatelayout(forcharacterrange_issoft_actualcharacterrange_).md>) with `flag` set to [false](../../swift/false.md).

This method only invalidates information; it performs no glyph generation or layout. You should rarely need to invoke this method.

## See Also

### Invalidating glyphs and layout

- [- invalidateDisplayForCharacterRange:](<invalidatedisplay(forcharacterrange_).md>) — Invalidates display for the specified character range.
- [- invalidateDisplayForGlyphRange:](<invalidatedisplay(forglyphrange_).md>) — Invalidates a range of glyphs, requiring new layout information, and updates the appropriate regions of any text views that display those glyphs.
- [- invalidateGlyphsForCharacterRange:changeInLength:actualCharacterRange:](<invalidateglyphs(forcharacterrange_changeinlength_actualcharacterrange_).md>) — Invalidates and adjusts the glyphs in the specified character range.
- [- processEditingForTextStorage:edited:range:changeInLength:invalidatedRange:](<processediting(for_edited_range_changeinlength_invalidatedrange_).md>) — Notifies the layout manager when an edit action changes the contents of its text storage object.
