---
title: Enriching your text in text views
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta, Xcode 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/uikit/enriching-your-text-in-text-views
source_url: 'https://developer.apple.com/documentation/uikit/enriching-your-text-in-text-views'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/enriching-your-text-in-text-views.json'
content_hash: 'sha256:f981de691897230f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [TextKit](textkit.md)

# Enriching your text in text views

<sub>Sample Code</sub>

Support line numbering, section collapsing, inline attachment caching, exclusion paths, text attachments, and text lists in a text view.

## Overview

> [!note] Note
> This sample code project is associated with the following WWDC sessions:
>
> - WWDC26 session [370: Elevate your app’s text experience with TextKit](https://developer.apple.com/wwdc26/370/).
> - WWDC22 session [10090: What’s new in TextKit and text views](https://developer.apple.com/wwdc22/10090/).

## See Also

### Content elements

- [NSTextParagraph](nstextparagraph.md) — A class that represents a single paragraph backed by an attributed string as the contents.
- [NSTextListElement](nstextlistelement.md) — A class that represents a text list node.
- [NSTextElement](nstextelement.md) — An abstract base class that represents the smallest units of text layout such as paragraphs or attachments.
- [NSTextElementProvider](nstextelementprovider.md) — A protocol the text content manager and its concrete subclasses conform to, which defines the interface for interacting with custom content types of a text document.

## Download

- [EnrichingYourTextInTextViews.zip](https://docs-assets.developer.apple.com/published/44b0d825b47c/EnrichingYourTextInTextViews.zip)
