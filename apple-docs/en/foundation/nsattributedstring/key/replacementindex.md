---
title: replacementIndex
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/key/replacementindex
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/key/replacementindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/key/replacementindex.json'
content_hash: 'sha256:780efad9c14f3534'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [Key](../key.md)

# replacementIndex

<sub>Type Property</sub>

The replacement position associated with a format string specifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let replacementIndex: NSAttributedString.Key
```

## Discussion

When creating an attributed string from a format string and one or more replacement values, this attribute indicates the ordinal index of each replacement. You must specify the [NSAttributedStringFormattingApplyReplacementIndexAttribute](../../nsattributedstringformattingoptions/nsattributedstringformattingapplyreplacementindexattribute.md) option at creation time to add this attribute to the substituted text. The value of this key is an `NSNumber` with the replacement position of the substitute text.

## See Also

### Getting text attribute keys

- [cursor](cursor.md) — The cursor object.
- [link](link.md) — The link for the text.
- [markedClauseSegment](markedclausesegment.md) — The index of the marked clause segment.
- [shadow](shadow.md) — The shadow of the text.
- [spellingState](spellingstate.md) — The spelling state of the text.
- [suggestionHighlight](suggestionhighlight.md) — A highlight associated with a Spotlight suggestion.
- [textAlternatives](textalternatives.md) — The alternatives for the text.
- [textEffect](texteffect.md) — An attribute that applies a text effect to the text.
- [textHighlightColorScheme](texthighlightcolorscheme.md) — The custom highlight color to apply to the text.
- [textHighlightStyle](texthighlightstyle.md) — An attribute that adds a highlight color to the text to emphasize it.
- [textItemTag](textitemtag.md) — The name of a custom tag associated with a text item.
- [toolTip](tooltip.md) — The tooltip text.
