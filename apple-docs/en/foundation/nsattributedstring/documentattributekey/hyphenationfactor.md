---
title: hyphenationFactor
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/documentattributekey/hyphenationfactor
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/documentattributekey/hyphenationfactor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/documentattributekey/hyphenationfactor.json'
content_hash: 'sha256:ab654f6885fbafe4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [DocumentAttributeKey](../documentattributekey.md)

# hyphenationFactor

<sub>Type Property</sub>

The hyphenation factor of the document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let hyphenationFactor: NSAttributedString.DocumentAttributeKey
```

## Discussion

The value of this attribute is an [NSNumber](../../nsnumber.md) object containing a float. A value of 0 indicates that hyphenation is off, and a value of 1 indicates full hyphenation.

The string constant in macOS 10.3 and earlier is `@"HyphenationFactor"`.

## See Also

### Getting document appearance keys

- [appearance](appearance.md) — The appearance of the document.
- [backgroundColor](backgroundcolor.md) — The background color of the document.
- [bottomMargin](bottommargin.md) — The bottom margin of the document.
- [defaultFontExcluded](defaultfontexcluded.md)
- [defaultTabInterval](defaulttabinterval.md) — The default tab stop interval for the document.
- [excludedElements](excludedelements.md) — The HTML elements to exclude in generated HTML.
- [leftMargin](leftmargin.md) — The left margin of the document.
- [paperMargin](papermargin.md) — The paper margin of the document.
- [paperSize](papersize.md) — The paper size for the document.
- [prefixSpaces](prefixspaces.md) — The number of spaces for indenting nested HTML elements.
- [rightMargin](rightmargin.md) — The right margin of the document.
- [textLayoutSections](textlayoutsections.md) — The layout orientations for each section.
- [topMargin](topmargin.md) — The top margin of the document.
- [viewMode](viewmode.md) — The view mode.
- [viewSize](viewsize.md) — The view size.
