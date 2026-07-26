---
title: 'layoutManager(_:shouldSetLineFragmentRect:lineFragmentUsedRect:baselineOffset:in:forGlyphRange:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanagerdelegate/layoutmanager(_:shouldsetlinefragmentrect:linefragmentusedrect:baselineoffset:in:forglyphrange:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate/layoutmanager(_:shouldsetlinefragmentrect:linefragmentusedrect:baselineoffset:in:forglyphrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanagerdelegate/layoutmanager%28_%3Ashouldsetlinefragmentrect%3Alinefragmentusedrect%3Abaselineoffset%3Ain%3Aforglyphrange%3A%29.json'
content_hash: 'sha256:7be4d053caa422d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManagerDelegate](../nslayoutmanagerdelegate.md)

# layoutManager(_:shouldSetLineFragmentRect:lineFragmentUsedRect:baselineOffset:in:forGlyphRange:)

<sub>Instance Method</sub>

Customizes the line fragment geometry before committing it to the layout cache.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func layoutManager(_ layoutManager: NSLayoutManager, shouldSetLineFragmentRect lineFragmentRect: UnsafeMutablePointer<CGRect>, lineFragmentUsedRect: UnsafeMutablePointer<CGRect>, baselineOffset: UnsafeMutablePointer<CGFloat>, in textContainer: NSTextContainer, forGlyphRange glyphRange: NSRange) -> Bool
```

## Parameters

- `layoutManager` — The layout manager doing the work.

- `lineFragmentRect` — The proposed rectangle that contains the glyphs. You may modify this rectangle as needed.

- `lineFragmentUsedRect` — The portion of `lineFragmentRect` that actually contains glyphs or other rendered marks, including the text container’s line fragment padding. This rectangle must be equal to `lineFragmentRect` or wholly contained by it. You may modify this rectangle as needed.

- `baselineOffset` — The vertical distance (in pixels) from the line fragment origin to the baseline on which the glyphs align.

- `textContainer` — The text container for the line fragments.

- `glyphRange` — The range of glyphs being laid out.

## Return Value

[true](../../swift/true.md) if you modified the layout information and want your modifications to be used or [false](../../swift/false.md) if the original layout information should be used.

## Discussion

Use this method to modify the line fragment rectangles associated with the text container. It is your responsibility to ensure that the modified rectangles remain valid and still lie within the text container.

## See Also

### Handling line fragments

- [- layoutManager:shouldBreakLineByHyphenatingBeforeCharacterAtIndex:](<layoutmanager(__shouldbreaklinebyhyphenatingbeforecharacterat_).md>) — Asks the delegate whether to break the line at the specified character.
- [- layoutManager:shouldBreakLineByWordBeforeCharacterAtIndex:](<layoutmanager(__shouldbreaklinebywordbeforecharacterat_).md>) — Asks the delegate whether to break the line at the specified word.
- [- layoutManager:lineSpacingAfterGlyphAtIndex:withProposedLineFragmentRect:](<layoutmanager(__linespacingafterglyphat_withproposedlinefragmentrect_).md>) — Returns the amount of space to add to the end of a line.
- [- layoutManager:paragraphSpacingAfterGlyphAtIndex:withProposedLineFragmentRect:](<layoutmanager(__paragraphspacingafterglyphat_withproposedlinefragmentrect_).md>) — Returns the amount of space to add at the end of a paragraph.
- [- layoutManager:paragraphSpacingBeforeGlyphAtIndex:withProposedLineFragmentRect:](<layoutmanager(__paragraphspacingbeforeglyphat_withproposedlinefragmentrect_).md>) — Returns the amount of space to add at the beginning of a paragraph.
- [- layoutManager:boundingBoxForControlGlyphAtIndex:forTextContainer:proposedLineFragment:glyphPosition:characterIndex:](<layoutmanager(__boundingboxforcontrolglyphat_for_proposedlinefragment_glyphposition_characterindex_).md>) — Returns the bounding rectangle for the specified control glyph with the specified parameters.
