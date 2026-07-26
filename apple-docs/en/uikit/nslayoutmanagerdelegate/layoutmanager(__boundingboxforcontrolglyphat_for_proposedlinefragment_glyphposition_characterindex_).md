---
title: 'layoutManager(_:boundingBoxForControlGlyphAt:for:proposedLineFragment:glyphPosition:characterIndex:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanagerdelegate/layoutmanager(_:boundingboxforcontrolglyphat:for:proposedlinefragment:glyphposition:characterindex:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate/layoutmanager(_:boundingboxforcontrolglyphat:for:proposedlinefragment:glyphposition:characterindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanagerdelegate/layoutmanager%28_%3Aboundingboxforcontrolglyphat%3Afor%3Aproposedlinefragment%3Aglyphposition%3Acharacterindex%3A%29.json'
content_hash: 'sha256:21f707d3a8af301a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManagerDelegate](../nslayoutmanagerdelegate.md)

# layoutManager(_:boundingBoxForControlGlyphAt:for:proposedLineFragment:glyphPosition:characterIndex:)

<sub>Instance Method</sub>

Returns the bounding rectangle for the specified control glyph with the specified parameters.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func layoutManager(_ layoutManager: NSLayoutManager, boundingBoxForControlGlyphAt glyphIndex: Int, for textContainer: NSTextContainer, proposedLineFragment proposedRect: CGRect, glyphPosition: CGPoint, characterIndex charIndex: Int) -> CGRect
```

## Parameters

- `layoutManager` — The layout manager doing the layout.

- `glyphIndex` — The index of the control glyph in question.

- `textContainer` — The text container to use to calculate the position.

- `proposedRect` — The proposed line fragment rectangle.

- `glyphPosition` — The position of the glyph in `textContainer`.

- `charIndex` — The character index in `textContainer`.

## Return Value

The bounding rectangle for the specified control glyph with the specified parameters.

## Discussion

Sent for resolving the glyph metrics for [NSControlCharacterWhitespaceAction](../nscontrolcharacterwhitespaceaction.md) control character.

## See Also

### Handling line fragments

- [- layoutManager:shouldBreakLineByHyphenatingBeforeCharacterAtIndex:](<layoutmanager(__shouldbreaklinebyhyphenatingbeforecharacterat_).md>) — Asks the delegate whether to break the line at the specified character.
- [- layoutManager:shouldBreakLineByWordBeforeCharacterAtIndex:](<layoutmanager(__shouldbreaklinebywordbeforecharacterat_).md>) — Asks the delegate whether to break the line at the specified word.
- [- layoutManager:lineSpacingAfterGlyphAtIndex:withProposedLineFragmentRect:](<layoutmanager(__linespacingafterglyphat_withproposedlinefragmentrect_).md>) — Returns the amount of space to add to the end of a line.
- [- layoutManager:paragraphSpacingAfterGlyphAtIndex:withProposedLineFragmentRect:](<layoutmanager(__paragraphspacingafterglyphat_withproposedlinefragmentrect_).md>) — Returns the amount of space to add at the end of a paragraph.
- [- layoutManager:paragraphSpacingBeforeGlyphAtIndex:withProposedLineFragmentRect:](<layoutmanager(__paragraphspacingbeforeglyphat_withproposedlinefragmentrect_).md>) — Returns the amount of space to add at the beginning of a paragraph.
- [- layoutManager:shouldSetLineFragmentRect:lineFragmentUsedRect:baselineOffset:inTextContainer:forGlyphRange:](<layoutmanager(__shouldsetlinefragmentrect_linefragmentusedrect_baselineoffset_in_forglyphrange_).md>) — Customizes the line fragment geometry before committing it to the layout cache.
