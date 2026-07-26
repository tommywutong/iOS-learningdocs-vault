---
title: 'layoutManager(_:shouldBreakLineByWordBeforeCharacterAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanagerdelegate/layoutmanager(_:shouldbreaklinebywordbeforecharacterat:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate/layoutmanager(_:shouldbreaklinebywordbeforecharacterat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanagerdelegate/layoutmanager%28_%3Ashouldbreaklinebywordbeforecharacterat%3A%29.json'
content_hash: 'sha256:b0e044e247ab15cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManagerDelegate](../nslayoutmanagerdelegate.md)

# layoutManager(_:shouldBreakLineByWordBeforeCharacterAt:)

<sub>Instance Method</sub>

Asks the delegate whether to break the line at the specified word.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func layoutManager(_ layoutManager: NSLayoutManager, shouldBreakLineByWordBeforeCharacterAt charIndex: Int) -> Bool
```

## Parameters

- `layoutManager` — The layout manager doing the layout.

- `charIndex` — Index of the character delimiting the break point search.

## Return Value

[true](../../swift/true.md) if the current line break point is acceptable; [false](../../swift/false.md) if the layout manager should find the next break point opportunity before `charIndex`.

## See Also

### Handling line fragments

- [- layoutManager:shouldBreakLineByHyphenatingBeforeCharacterAtIndex:](<layoutmanager(__shouldbreaklinebyhyphenatingbeforecharacterat_).md>) — Asks the delegate whether to break the line at the specified character.
- [- layoutManager:lineSpacingAfterGlyphAtIndex:withProposedLineFragmentRect:](<layoutmanager(__linespacingafterglyphat_withproposedlinefragmentrect_).md>) — Returns the amount of space to add to the end of a line.
- [- layoutManager:paragraphSpacingAfterGlyphAtIndex:withProposedLineFragmentRect:](<layoutmanager(__paragraphspacingafterglyphat_withproposedlinefragmentrect_).md>) — Returns the amount of space to add at the end of a paragraph.
- [- layoutManager:paragraphSpacingBeforeGlyphAtIndex:withProposedLineFragmentRect:](<layoutmanager(__paragraphspacingbeforeglyphat_withproposedlinefragmentrect_).md>) — Returns the amount of space to add at the beginning of a paragraph.
- [- layoutManager:boundingBoxForControlGlyphAtIndex:forTextContainer:proposedLineFragment:glyphPosition:characterIndex:](<layoutmanager(__boundingboxforcontrolglyphat_for_proposedlinefragment_glyphposition_characterindex_).md>) — Returns the bounding rectangle for the specified control glyph with the specified parameters.
- [- layoutManager:shouldSetLineFragmentRect:lineFragmentUsedRect:baselineOffset:inTextContainer:forGlyphRange:](<layoutmanager(__shouldsetlinefragmentrect_linefragmentusedrect_baselineoffset_in_forglyphrange_).md>) — Customizes the line fragment geometry before committing it to the layout cache.
