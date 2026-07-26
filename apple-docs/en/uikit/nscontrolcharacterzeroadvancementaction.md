---
title: NSControlCharacterZeroAdvancementAction
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+（9.0 起废弃）, iPadOS 7.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/nscontrolcharacterzeroadvancementaction
source_url: 'https://developer.apple.com/documentation/uikit/nscontrolcharacterzeroadvancementaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nscontrolcharacterzeroadvancementaction.json'
content_hash: 'sha256:8c4f234446660b16'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSControlCharacterZeroAdvancementAction

<sub>Global Variable</sub>

An action that removes the glyph from layout.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var NSControlCharacterZeroAdvancementAction: Int { get }
```

## Discussion

Glyphs with this action are filtered out from layout ([- notShownAttributeForGlyphAtIndex:](<nslayoutmanager/notshownattribute(forglyphat_).md>) `== YES` for the glyph).

## See Also

### Constants

- [NSControlCharacterContainerBreakAction](nscontrolcharactercontainerbreakaction.md) — A character that causes a break in layout. _(deprecated)_
- [NSControlCharacterHorizontalTabAction](nscontrolcharacterhorizontaltabaction.md) — An action that inserts a horizontal tab. _(deprecated)_
- [NSControlCharacterLineBreakAction](nscontrolcharacterlinebreakaction.md) — An action that causes a line break. _(deprecated)_
- [NSControlCharacterParagraphBreakAction](nscontrolcharacterparagraphbreakaction.md) — An action that causes a paragraph break. _(deprecated)_
- [NSControlCharacterWhitespaceAction](nscontrolcharacterwhitespaceaction.md) — An action that programmatically changes the white space around the glyph. _(deprecated)_
