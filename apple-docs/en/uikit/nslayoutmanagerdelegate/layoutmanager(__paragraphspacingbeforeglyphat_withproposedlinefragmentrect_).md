---
title: 'layoutManager(_:paragraphSpacingBeforeGlyphAt:withProposedLineFragmentRect:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanagerdelegate/layoutmanager(_:paragraphspacingbeforeglyphat:withproposedlinefragmentrect:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate/layoutmanager(_:paragraphspacingbeforeglyphat:withproposedlinefragmentrect:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanagerdelegate/layoutmanager%28_%3Aparagraphspacingbeforeglyphat%3Awithproposedlinefragmentrect%3A%29.json'
content_hash: 'sha256:4c055f3cb2a1aa64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManagerDelegate](../nslayoutmanagerdelegate.md)

# layoutManager(_:paragraphSpacingBeforeGlyphAt:withProposedLineFragmentRect:)

<sub>Instance Method</sub>

Returns the amount of space to add at the beginning of a paragraph.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func layoutManager(_ layoutManager: NSLayoutManager, paragraphSpacingBeforeGlyphAt glyphIndex: Int, withProposedLineFragmentRect rect: CGRect) -> CGFloat
```

## Parameters

- `layoutManager` — The layout manager doing the layout.

- `glyphIndex` — The index of the glyph at the beginning of the line.

- `rect` — The proposed line fragment rectangle for the current line.

## Return Value

The paragraph spacing before the current line.

## Discussion

This message is sent while each line is laid out to enable the layout manager delegate to customize the shape of line.

## See Also

### Handling line fragments

- [- layoutManager:shouldBreakLineByHyphenatingBeforeCharacterAtIndex:](<layoutmanager(__shouldbreaklinebyhyphenatingbeforecharacterat_).md>) — Asks the delegate whether to break the line at the specified character.
- [- layoutManager:shouldBreakLineByWordBeforeCharacterAtIndex:](<layoutmanager(__shouldbreaklinebywordbeforecharacterat_).md>) — Asks the delegate whether to break the line at the specified word.
- [- layoutManager:lineSpacingAfterGlyphAtIndex:withProposedLineFragmentRect:](<layoutmanager(__linespacingafterglyphat_withproposedlinefragmentrect_).md>) — Returns the amount of space to add to the end of a line.
- [- layoutManager:paragraphSpacingAfterGlyphAtIndex:withProposedLineFragmentRect:](<layoutmanager(__paragraphspacingafterglyphat_withproposedlinefragmentrect_).md>) — Returns the amount of space to add at the end of a paragraph.
- [- layoutManager:boundingBoxForControlGlyphAtIndex:forTextContainer:proposedLineFragment:glyphPosition:characterIndex:](<layoutmanager(__boundingboxforcontrolglyphat_for_proposedlinefragment_glyphposition_characterindex_).md>) — Returns the bounding rectangle for the specified control glyph with the specified parameters.
- [- layoutManager:shouldSetLineFragmentRect:lineFragmentUsedRect:baselineOffset:inTextContainer:forGlyphRange:](<layoutmanager(__shouldsetlinefragmentrect_linefragmentusedrect_baselineoffset_in_forglyphrange_).md>) — Customizes the line fragment geometry before committing it to the layout cache.
