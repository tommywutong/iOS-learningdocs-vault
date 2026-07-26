---
title: 'invalidateGlyphs(forCharacterRange:changeInLength:actualCharacterRange:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/invalidateglyphs(forcharacterrange:changeinlength:actualcharacterrange:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/invalidateglyphs(forcharacterrange:changeinlength:actualcharacterrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/invalidateglyphs%28forcharacterrange%3Achangeinlength%3Aactualcharacterrange%3A%29.json'
content_hash: 'sha256:8b7897618367ebd2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# invalidateGlyphs(forCharacterRange:changeInLength:actualCharacterRange:)

<sub>Instance Method</sub>

Invalidates and adjusts the glyphs in the specified character range.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func invalidateGlyphs(forCharacterRange charRange: NSRange, changeInLength delta: Int, actualCharacterRange actualCharRange: NSRangePointer?)
```

## Parameters

- `charRange` — The range of characters for which to invalidate glyphs.

- `delta` — The number of characters added or removed.

- `actualCharRange` — If not `NULL`, on output, the actual range invalidated after any necessary expansion. This range can be larger than the range of characters given due to the effect of context on glyphs and layout.

## Discussion

This method invalidates the cached glyphs for the characters in the given character range, adjusts the character indices of all the subsequent glyphs by the change in length, and invalidates the new character range. This method invalidates only glyph information and performs no glyph generation or layout. Because invalidating glyphs also invalidates layout, after invoking this method you should also invoke [- invalidateLayoutForCharacterRange:actualCharacterRange:](<invalidatelayout(forcharacterrange_actualcharacterrange_).md>), passing `charRange` as the first argument.

This method is used by the layout mechanism and should be invoked only during typesetting, in almost all cases only by the typesetter. For example, a custom typesetter might invoke it.

## See Also

### Invalidating glyphs and layout

- [- invalidateDisplayForCharacterRange:](<invalidatedisplay(forcharacterrange_).md>) — Invalidates display for the specified character range.
- [- invalidateDisplayForGlyphRange:](<invalidatedisplay(forglyphrange_).md>) — Invalidates a range of glyphs, requiring new layout information, and updates the appropriate regions of any text views that display those glyphs.
- [- invalidateLayoutForCharacterRange:actualCharacterRange:](<invalidatelayout(forcharacterrange_actualcharacterrange_).md>) — Invalidates the layout information for the glyphs that map to the specified character range.
- [- processEditingForTextStorage:edited:range:changeInLength:invalidatedRange:](<processediting(for_edited_range_changeinlength_invalidatedrange_).md>) — Notifies the layout manager when an edit action changes the contents of its text storage object.
