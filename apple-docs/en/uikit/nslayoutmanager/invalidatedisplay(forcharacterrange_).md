---
title: 'invalidateDisplay(forCharacterRange:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/invalidatedisplay(forcharacterrange:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/invalidatedisplay(forcharacterrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/invalidatedisplay%28forcharacterrange%3A%29.json'
content_hash: 'sha256:b8848aef29f839cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# invalidateDisplay(forCharacterRange:)

<sub>Instance Method</sub>

Invalidates display for the specified character range.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func invalidateDisplay(forCharacterRange charRange: NSRange)
```

## Parameters

- `charRange` — The character range for which display is invalidated.

## Discussion

Parts of the range that are not laid out are remembered and redisplayed later when the layout is available. Does not actually cause layout.

## See Also

### Invalidating glyphs and layout

- [- invalidateDisplayForGlyphRange:](<invalidatedisplay(forglyphrange_).md>) — Invalidates a range of glyphs, requiring new layout information, and updates the appropriate regions of any text views that display those glyphs.
- [- invalidateGlyphsForCharacterRange:changeInLength:actualCharacterRange:](<invalidateglyphs(forcharacterrange_changeinlength_actualcharacterrange_).md>) — Invalidates and adjusts the glyphs in the specified character range.
- [- invalidateLayoutForCharacterRange:actualCharacterRange:](<invalidatelayout(forcharacterrange_actualcharacterrange_).md>) — Invalidates the layout information for the glyphs that map to the specified character range.
- [- processEditingForTextStorage:edited:range:changeInLength:invalidatedRange:](<processediting(for_edited_range_changeinlength_invalidatedrange_).md>) — Notifies the layout manager when an edit action changes the contents of its text storage object.
