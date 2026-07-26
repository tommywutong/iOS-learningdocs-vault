---
title: 'processEditing(for:edited:range:changeInLength:invalidatedRange:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/processediting(for:edited:range:changeinlength:invalidatedrange:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/processediting(for:edited:range:changeinlength:invalidatedrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/processediting%28for%3Aedited%3Arange%3Achangeinlength%3Ainvalidatedrange%3A%29.json'
content_hash: 'sha256:a2a59f5716bc249e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# processEditing(for:edited:range:changeInLength:invalidatedRange:)

<sub>Instance Method</sub>

Notifies the layout manager when an edit action changes the contents of its text storage object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func processEditing(for textStorage: NSTextStorage, edited editMask: NSTextStorage.EditActions, range newCharRange: NSRange, changeInLength delta: Int, invalidatedRange invalidatedCharRange: NSRange)
```

## Parameters

- `textStorage` — The text storage object processing edits.

- `editMask` — The types of edits done: `NSTextStorageEditedAttributes`, `NSTextStorageEditedCharacters`, or both.

- `newCharRange` — The range in the final string that was explicitly edited.

- `delta` — The length delta for the editing changes.

- `invalidatedCharRange` — The range of characters that changed as a result of attribute fixing. This invalidated range is either equal to `newCharRange` or larger.

## Discussion

The [- processEditing](<../nstextstorage/processediting().md>) method of [NSTextStorage](../nstextstorage.md) calls this method to notify the layout manager of an edit action. Layout managers must not change the contents of the text storage during the execution of this message.

## See Also

### Invalidating glyphs and layout

- [- invalidateDisplayForCharacterRange:](<invalidatedisplay(forcharacterrange_).md>) — Invalidates display for the specified character range.
- [- invalidateDisplayForGlyphRange:](<invalidatedisplay(forglyphrange_).md>) — Invalidates a range of glyphs, requiring new layout information, and updates the appropriate regions of any text views that display those glyphs.
- [- invalidateGlyphsForCharacterRange:changeInLength:actualCharacterRange:](<invalidateglyphs(forcharacterrange_changeinlength_actualcharacterrange_).md>) — Invalidates and adjusts the glyphs in the specified character range.
- [- invalidateLayoutForCharacterRange:actualCharacterRange:](<invalidatelayout(forcharacterrange_actualcharacterrange_).md>) — Invalidates the layout information for the glyphs that map to the specified character range.
