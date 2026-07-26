---
title: 'layoutManager(_:shouldBreakLineByHyphenatingBeforeCharacterAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanagerdelegate/layoutmanager(_:shouldbreaklinebyhyphenatingbeforecharacterat:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate/layoutmanager(_:shouldbreaklinebyhyphenatingbeforecharacterat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanagerdelegate/layoutmanager%28_%3Ashouldbreaklinebyhyphenatingbeforecharacterat%3A%29.json'
content_hash: 'sha256:ffac02b0a7deb50e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManagerDelegate](../nslayoutmanagerdelegate.md)

# layoutManager(_:shouldBreakLineByHyphenatingBeforeCharacterAt:)

<sub>Instance Method</sub>

Asks the delegate whether to break the line at the specified character.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func layoutManager(_ layoutManager: NSLayoutManager, shouldBreakLineByHyphenatingBeforeCharacterAt charIndex: Int) -> Bool
```

## Parameters

- `layoutManager` — The layout manager doing the layout.

- `charIndex` — Index of the character delimiting the hyphenation point search.

## Return Value

[true](../../swift/true.md) if the current hyphenation point is acceptable; [false](../../swift/false.md) if the layout manager should find the next hyphenation opportunity before `charIndex`.

## See Also

### Handling line fragments

- [- layoutManager:shouldBreakLineByWordBeforeCharacterAtIndex:](<layoutmanager(__shouldbreaklinebywordbeforecharacterat_).md>) — Asks the delegate whether to break the line at the specified word.
- [- layoutManager:lineSpacingAfterGlyphAtIndex:withProposedLineFragmentRect:](<layoutmanager(__linespacingafterglyphat_withproposedlinefragmentrect_).md>) — Returns the amount of space to add to the end of a line.
- [- layoutManager:paragraphSpacingAfterGlyphAtIndex:withProposedLineFragmentRect:](<layoutmanager(__paragraphspacingafterglyphat_withproposedlinefragmentrect_).md>) — Returns the amount of space to add at the end of a paragraph.
- [- layoutManager:paragraphSpacingBeforeGlyphAtIndex:withProposedLineFragmentRect:](<layoutmanager(__paragraphspacingbeforeglyphat_withproposedlinefragmentrect_).md>) — Returns the amount of space to add at the beginning of a paragraph.
- [- layoutManager:boundingBoxForControlGlyphAtIndex:forTextContainer:proposedLineFragment:glyphPosition:characterIndex:](<layoutmanager(__boundingboxforcontrolglyphat_for_proposedlinefragment_glyphposition_characterindex_).md>) — Returns the bounding rectangle for the specified control glyph with the specified parameters.
- [- layoutManager:shouldSetLineFragmentRect:lineFragmentUsedRect:baselineOffset:inTextContainer:forGlyphRange:](<layoutmanager(__shouldsetlinefragmentrect_linefragmentusedrect_baselineoffset_in_forglyphrange_).md>) — Customizes the line fragment geometry before committing it to the layout cache.
