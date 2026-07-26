---
title: textHighlightColorScheme
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/key/texthighlightcolorscheme
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/key/texthighlightcolorscheme'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/key/texthighlightcolorscheme.json'
content_hash: 'sha256:d3dc7fe54813a8e8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [Key](../key.md)

# textHighlightColorScheme

<sub>Type Property</sub>

The custom highlight color to apply to the text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let textHighlightColorScheme: NSAttributedString.Key
```

## Discussion

The value of this attribute is an [TextHighlightColorScheme](../texthighlightcolorscheme.md) structure. The default value of this attribute is `nil`, which applies the default system highlight color to the text when the [textHighlightStyle](texthighlightstyle.md) attribute is present.

A highlight adds a background color behind the text, and applies a contrasting foreground color to the text itself. Set the value of this attribute to [default](../texthighlightcolorscheme/default.md), or don’t specify the attribute at all, to apply a highlight with the default system color. Specify a different value for this attribute to apply that highlight color instead.

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
- [textHighlightStyle](texthighlightstyle.md) — An attribute that adds a highlight color to the text to emphasize it.
- [textItemTag](textitemtag.md) — The name of a custom tag associated with a text item.
- [toolTip](tooltip.md) — The tooltip text.
