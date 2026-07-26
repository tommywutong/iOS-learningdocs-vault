---
title: textEffect
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/key/texteffect
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/key/texteffect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/key/texteffect.json'
content_hash: 'sha256:2973ba41c9537914'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [Key](../key.md)

# textEffect

<sub>Type Property</sub>

An attribute that applies a text effect to the text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let textEffect: NSAttributedString.Key
```

## Discussion

The value of this attribute is an [NSString](../../nsstring.md) object. Use this attribute to specify a text effect, such as [letterpressStyle](../texteffectstyle/letterpressstyle.md). The default value of this property is `nil`, indicating no text effect.

## See Also

### Getting text attribute keys

- [cursor](cursor.md) — The cursor object.
- [link](link.md) — The link for the text.
- [markedClauseSegment](markedclausesegment.md) — The index of the marked clause segment.
- [NSReplacementIndexAttributeName](replacementindex.md) — The replacement position associated with a format string specifier.
- [shadow](shadow.md) — The shadow of the text.
- [spellingState](spellingstate.md) — The spelling state of the text.
- [suggestionHighlight](suggestionhighlight.md) — A highlight associated with a Spotlight suggestion.
- [textAlternatives](textalternatives.md) — The alternatives for the text.
- [textHighlightColorScheme](texthighlightcolorscheme.md) — The custom highlight color to apply to the text.
- [textHighlightStyle](texthighlightstyle.md) — An attribute that adds a highlight color to the text to emphasize it.
- [textItemTag](textitemtag.md) — The name of a custom tag associated with a text item.
- [toolTip](tooltip.md) — The tooltip text.
