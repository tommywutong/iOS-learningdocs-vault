---
title: XMLDocument.ContentKind.xhtml
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmldocument/contentkind/xhtml
source_url: 'https://developer.apple.com/documentation/foundation/xmldocument/contentkind/xhtml'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldocument/contentkind/xhtml.json'
content_hash: 'sha256:0e964dfc37808f8e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [XMLDocument](../../xmldocument.md) · [ContentKind](../contentkind.md)

# XMLDocument.ContentKind.xhtml

<sub>Case</sub>

The document output is XHTML.

<sub>Mac Catalyst, macOS</sub>

```swift
case xhtml
```

## Discussion

This is set automatically if the `NSXMLDocumentTidyHTML` option is set and NSXML detects HTML.

## See Also

### Enumeration Cases

- [NSXMLDocumentHTMLKind](html.md) — Outputs empty tags in HTML without a close tag, such as `<br>`.
- [NSXMLDocumentTextKind](text.md) — Outputs the string value of the document by extracting the string values from all text nodes.
- [NSXMLDocumentXMLKind](xml.md) — The default type of document content type, which is XML.
