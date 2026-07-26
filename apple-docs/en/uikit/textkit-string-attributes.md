---
title: TextKit string attributes
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/textkit-string-attributes
source_url: 'https://developer.apple.com/documentation/uikit/textkit-string-attributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/textkit-string-attributes.json'
content_hash: 'sha256:724df6c752357e37'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [TextKit](textkit.md)

# TextKit string attributes

<sub>API Collection</sub>

UIKit-specific keys and values for displaying text and managing documents.

## Overview

UIKit defines these attributes and attribute keys you use to specify attribute values in [NSAttributedString](../foundation/nsattributedstring.md) and [NSMutableAttributedString](../foundation/nsmutableattributedstring.md).

## Topics

### Getting text content attributes

- [TextKit string attribute keys](textkit-string-attribute-keys.md) — UIKit-specific keys you use to apply attributes to ranges of characters in an attributed string.
- [NSTextHighlightStyle](nstexthighlightstyle.md) — Constants that specify the type of highlight to apply to text.
- [NSTextHighlightColorScheme](nstexthighlightcolorscheme.md) — Constants that specify the highlight color to use with the text.
- [NSTextEffectStyle](nstexteffectstyle.md) — Constants for the type of effect to apply to the text.
- [NSUnderlineStyle](nsunderlinestyle.md) — Constants for the underline style and strikethrough style attribute keys.
- [NSWritingDirectionFormatType](nswritingdirectionformattype.md) — Constants for the writing direction attribute key.

### Getting document-wide attributes

- [NSAttributedStringDocumentAttributeKey](nsattributedstringdocumentattributekey.md) — The attributes you apply to an entire document.
- [Document reading option keys](document-reading-option-keys.md) — Keys for constructing an attributed string from data on disk.
- [NSAttributedStringDocumentType](nsattributedstringdocumenttype.md) — Constants for the document type document attribute key.
- [NSTextLayoutSectionKey](nstextlayoutsectionkey.md) — Constants for the text layout sections document attribute key.
- [NSTextScalingType](nstextscalingtype.md) — Constants that specify the text scaling.

### Deprecated constants

- [NSTextWritingDirection](nstextwritingdirection.md) — Options for specifying text-writing direction. _(deprecated)_

## See Also

### Text management

- [NSTextContentStorage](nstextcontentstorage.md) — A concrete object for managing your view’s text content and generating the text elements necessary for layout.
- [NSTextContentManager](nstextcontentmanager.md) — An abstract class that defines the interface and a default implementation for managing the text document contents.
- [NSAttributedString](../foundation/nsattributedstring.md) — A string of text that manages data, layout, and stylistic information for ranges of characters to support rendering.
- [NSMutableAttributedString](../foundation/nsmutableattributedstring.md) — A mutable string with associated attributes (such as visual style, hyperlinks, or accessibility data) for portions of its text.
