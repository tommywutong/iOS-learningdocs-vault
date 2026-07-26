---
title: nonBaseCharacter
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nslayoutmanager/glyphproperty/nonbasecharacter
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/glyphproperty/nonbasecharacter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/glyphproperty/nonbasecharacter.json'
content_hash: 'sha256:ec83fb3bfd652434'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [NSLayoutManager](../../nslayoutmanager.md) · [GlyphProperty](../glyphproperty.md)

# nonBaseCharacter

<sub>Type Property</sub>

A glyph that combines several properties.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var nonBaseCharacter: NSLayoutManager.GlyphProperty { get }
```

## Discussion

A glyph of this type typically represents characters in the Unicode Mn class.

## See Also

### Glyph properties

- [NSGlyphPropertyNull](null.md) — The null glyph, which the layout manager ignores.
- [NSGlyphPropertyControlCharacter](controlcharacter.md) — A glyph representing a control character.
- [NSGlyphPropertyElastic](elastic.md) — A glyph with a changeable width, such as a white space character.
