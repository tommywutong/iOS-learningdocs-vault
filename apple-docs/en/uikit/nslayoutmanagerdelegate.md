---
title: NSLayoutManagerDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslayoutmanagerdelegate
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanagerdelegate.json'
content_hash: 'sha256:d4edf2676bf834c0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSLayoutManagerDelegate

<sub>Protocol</sub>

A set of optional methods that delegates of layout manager objects implement.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
protocol NSLayoutManagerDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Invalidating glyphs and layout

- [- layoutManagerDidInvalidateLayout:](<nslayoutmanagerdelegate/layoutmanagerdidinvalidatelayout(__).md>) — Informs the delegate when the specified layout manager invalidates layout information (not glyph information).
- [- layoutManager:shouldGenerateGlyphs:properties:characterIndexes:font:forGlyphRange:](<nslayoutmanagerdelegate/layoutmanager(__shouldgenerateglyphs_properties_characterindexes_font_forglyphrange_).md>) — Enables customization of the initial glyph generation process.
- [- layoutManager:shouldUseAction:forControlCharacterAtIndex:](<nslayoutmanagerdelegate/layoutmanager(__shoulduse_forcontrolcharacterat_).md>) — Returns the control character action for the control character at the specified character index.
- [ControlCharacterAction](nslayoutmanager/controlcharacteraction.md) — Constants that describe actions for control characters.

### Responding to text container layout

- [- layoutManager:didCompleteLayoutForTextContainer:atEnd:](<nslayoutmanagerdelegate/layoutmanager(__didcompletelayoutfor_atend_).md>) — Informs the delegate when the layout manager finishes laying out text in the specified text container.
- [- layoutManager:textContainer:didChangeGeometryFromSize:](<nslayoutmanagerdelegate/layoutmanager(__textcontainer_didchangegeometryfrom_).md>) — Informs the delegate when the layout manager invalidates layout due to a change in the geometry of the specified text container.

### Handling line fragments

- [- layoutManager:shouldBreakLineByHyphenatingBeforeCharacterAtIndex:](<nslayoutmanagerdelegate/layoutmanager(__shouldbreaklinebyhyphenatingbeforecharacterat_).md>) — Asks the delegate whether to break the line at the specified character.
- [- layoutManager:shouldBreakLineByWordBeforeCharacterAtIndex:](<nslayoutmanagerdelegate/layoutmanager(__shouldbreaklinebywordbeforecharacterat_).md>) — Asks the delegate whether to break the line at the specified word.
- [- layoutManager:lineSpacingAfterGlyphAtIndex:withProposedLineFragmentRect:](<nslayoutmanagerdelegate/layoutmanager(__linespacingafterglyphat_withproposedlinefragmentrect_).md>) — Returns the amount of space to add to the end of a line.
- [- layoutManager:paragraphSpacingAfterGlyphAtIndex:withProposedLineFragmentRect:](<nslayoutmanagerdelegate/layoutmanager(__paragraphspacingafterglyphat_withproposedlinefragmentrect_).md>) — Returns the amount of space to add at the end of a paragraph.
- [- layoutManager:paragraphSpacingBeforeGlyphAtIndex:withProposedLineFragmentRect:](<nslayoutmanagerdelegate/layoutmanager(__paragraphspacingbeforeglyphat_withproposedlinefragmentrect_).md>) — Returns the amount of space to add at the beginning of a paragraph.
- [- layoutManager:boundingBoxForControlGlyphAtIndex:forTextContainer:proposedLineFragment:glyphPosition:characterIndex:](<nslayoutmanagerdelegate/layoutmanager(__boundingboxforcontrolglyphat_for_proposedlinefragment_glyphposition_characterindex_).md>) — Returns the bounding rectangle for the specified control glyph with the specified parameters.
- [- layoutManager:shouldSetLineFragmentRect:lineFragmentUsedRect:baselineOffset:inTextContainer:forGlyphRange:](<nslayoutmanagerdelegate/layoutmanager(__shouldsetlinefragmentrect_linefragmentusedrect_baselineoffset_in_forglyphrange_).md>) — Customizes the line fragment geometry before committing it to the layout cache.

### Managing temporary attribute support

- [layoutManager(_:shouldUseTemporaryAttributes:forDrawingToScreen:atCharacterIndex:effectiveRange:)](<../appkit/nslayoutmanagerdelegate/layoutmanager(__shouldusetemporaryattributes_fordrawingtoscreen_atcharacterindex_effectiverange_).md>) — Asks the delegate whether to use temporary attributes when drawing the text.

### Deprecated

- [Control Characters](1619233-control-characters.md) — Constants that describe actions for control characters.

## See Also

### Managing the layout process

- [delegate](nslayoutmanager/delegate.md) — The layout manager’s delegate.
