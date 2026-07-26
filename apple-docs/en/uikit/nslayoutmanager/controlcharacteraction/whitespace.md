---
title: whitespace
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslayoutmanager/controlcharacteraction/whitespace
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/controlcharacteraction/whitespace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/controlcharacteraction/whitespace.json'
content_hash: 'sha256:6f83e70d0753ce27'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [NSLayoutManager](../../nslayoutmanager.md) · [ControlCharacterAction](../controlcharacteraction.md)

# whitespace

<sub>Type Property</sub>

An action that adds whitespace.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var whitespace: NSLayoutManager.ControlCharacterAction { get }
```

## Discussion

The width for a glyph with this action is determined by the delegate method [- layoutManager:boundingBoxForControlGlyphAtIndex:forTextContainer:proposedLineFragment:glyphPosition:characterIndex:](<../../nslayoutmanagerdelegate/layoutmanager(__boundingboxforcontrolglyphat_for_proposedlinefragment_glyphposition_characterindex_).md>) if the method is implemented; otherwise, same as `NSControlCharacterZeroAdvancementAction`.

## See Also

### Actions

- [NSControlCharacterActionContainerBreak](containerbreak.md) — An action that triggers a break in layout for the current container.
- [NSControlCharacterActionHorizontalTab](horizontaltab.md) — An action that inserts a horizontal tab.
- [NSControlCharacterActionLineBreak](linebreak.md) — An action that causes a line break.
- [NSControlCharacterActionParagraphBreak](paragraphbreak.md) — An action that causes a paragraph break.
- [NSControlCharacterActionZeroAdvancement](zeroadvancement.md) — An action that removes the glyph from layout.
