---
title: zeroAdvancement
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslayoutmanager/controlcharacteraction/zeroadvancement
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/controlcharacteraction/zeroadvancement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/controlcharacteraction/zeroadvancement.json'
content_hash: 'sha256:6034ce33e28b2ff1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [NSLayoutManager](../../nslayoutmanager.md) · [ControlCharacterAction](../controlcharacteraction.md)

# zeroAdvancement

<sub>Type Property</sub>

An action that removes the glyph from layout.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var zeroAdvancement: NSLayoutManager.ControlCharacterAction { get }
```

## Discussion

Glyphs with this action are filtered out from layout ([- notShownAttributeForGlyphAtIndex:](<../notshownattribute(forglyphat_).md>) `== YES` for the glyph).

## See Also

### Actions

- [NSControlCharacterActionContainerBreak](containerbreak.md) — An action that triggers a break in layout for the current container.
- [NSControlCharacterActionHorizontalTab](horizontaltab.md) — An action that inserts a horizontal tab.
- [NSControlCharacterActionLineBreak](linebreak.md) — An action that causes a line break.
- [NSControlCharacterActionParagraphBreak](paragraphbreak.md) — An action that causes a paragraph break.
- [NSControlCharacterActionWhitespace](whitespace.md) — An action that adds whitespace.
