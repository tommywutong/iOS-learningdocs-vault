---
title: link
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/key/link
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/key/link'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/key/link.json'
content_hash: 'sha256:7ecdcd8b003eaf96'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [Key](../key.md)

# link

<sub>Type Property</sub>

The link for the text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let link: NSAttributedString.Key
```

## Discussion

The value of this attribute is an [NSURL](../../nsurl.md) object (preferred) or an [NSString](../../nsstring.md) object. The default value of this property is `nil`, indicating no link.

## See Also

### Getting text attribute keys

- [cursor](cursor.md) — The cursor object.
- [markedClauseSegment](markedclausesegment.md) — The index of the marked clause segment.
- [NSReplacementIndexAttributeName](replacementindex.md) — The replacement position associated with a format string specifier.
- [shadow](shadow.md) — The shadow of the text.
- [spellingState](spellingstate.md) — The spelling state of the text.
- [suggestionHighlight](suggestionhighlight.md) — A highlight associated with a Spotlight suggestion.
- [textAlternatives](textalternatives.md) — The alternatives for the text.
- [textEffect](texteffect.md) — An attribute that applies a text effect to the text.
- [textHighlightColorScheme](texthighlightcolorscheme.md) — The custom highlight color to apply to the text.
- [textHighlightStyle](texthighlightstyle.md) — An attribute that adds a highlight color to the text to emphasize it.
- [textItemTag](textitemtag.md) — The name of a custom tag associated with a text item.
- [toolTip](tooltip.md) — The tooltip text.
