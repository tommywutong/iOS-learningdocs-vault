---
title: NSControlCharacterWhitespaceAction
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+（9.0 起废弃）, iPadOS 7.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/nscontrolcharacterwhitespaceaction
source_url: 'https://developer.apple.com/documentation/uikit/nscontrolcharacterwhitespaceaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nscontrolcharacterwhitespaceaction.json'
content_hash: 'sha256:115a85fb67a51a0c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSControlCharacterWhitespaceAction

<sub>Global Variable</sub>

An action that programmatically changes the white space around the glyph.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var NSControlCharacterWhitespaceAction: Int { get }
```

## Discussion

The width for a glyph with this action is determined by the delegate method [- layoutManager:boundingBoxForControlGlyphAtIndex:forTextContainer:proposedLineFragment:glyphPosition:characterIndex:](<nslayoutmanagerdelegate/layoutmanager(__boundingboxforcontrolglyphat_for_proposedlinefragment_glyphposition_characterindex_).md>) if the method is implemented; otherwise, it’s the same as `NSControlCharacterZeroAdvancementAction`.

## See Also

### Constants

- [NSControlCharacterContainerBreakAction](nscontrolcharactercontainerbreakaction.md) — A character that causes a break in layout. _(deprecated)_
- [NSControlCharacterHorizontalTabAction](nscontrolcharacterhorizontaltabaction.md) — An action that inserts a horizontal tab. _(deprecated)_
- [NSControlCharacterLineBreakAction](nscontrolcharacterlinebreakaction.md) — An action that causes a line break. _(deprecated)_
- [NSControlCharacterParagraphBreakAction](nscontrolcharacterparagraphbreakaction.md) — An action that causes a paragraph break. _(deprecated)_
- [NSControlCharacterZeroAdvancementAction](nscontrolcharacterzeroadvancementaction.md) — An action that removes the glyph from layout. _(deprecated)_
