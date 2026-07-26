---
title: textHighlightStyle
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/key/texthighlightstyle
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/key/texthighlightstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/key/texthighlightstyle.json'
content_hash: 'sha256:0861be51d0cdf47c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [Key](../key.md)

# textHighlightStyle

<sub>Type Property</sub>

An attribute that adds a highlight color to the text to emphasize it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let textHighlightStyle: NSAttributedString.Key
```

## Discussion

The value of this attribute is an [TextHighlightStyle](../texthighlightstyle.md) structure. The default value of this attribute is `nil`, which does not add a highlight to the text.

A highlight adds a background color behind the text, and adjusts the color of the text itself to contrast appropriately. The [default](../texthighlightstyle/default.md) highlight style applies the system highlight color to your text. To apply a different color, add the [textHighlightColorScheme](texthighlightcolorscheme.md) attribute to your text in addition to this one. Use the [textHighlightColorScheme](texthighlightcolorscheme.md) key to specify which highlight color you want.

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
- [textEffect](texteffect.md) — An attribute that applies a text effect to the text.
- [textHighlightColorScheme](texthighlightcolorscheme.md) — The custom highlight color to apply to the text.
- [textItemTag](textitemtag.md) — The name of a custom tag associated with a text item.
- [toolTip](tooltip.md) — The tooltip text.
