---
title: documentTidyHTML
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlnode/options/documenttidyhtml
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/options/documenttidyhtml'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/options/documenttidyhtml.json'
content_hash: 'sha256:13930bc3417da2aa'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [XMLNode](../../xmlnode.md) · [Options](../options.md)

# documentTidyHTML

<sub>Type Property</sub>

Formats HTML into valid XHTML during processing of the document.

<sub>Mac Catalyst, macOS</sub>

```swift
static var documentTidyHTML: XMLNode.Options { get }
```

## Discussion

When tidying, `NSXMLDocument` adds a line break before the close tag of a block-level element (`<p>`, `<div>`, `<h1>`, and so on); it also makes the string value of `<br>` or `<hr>` a line break. These operations make the string value of the HTML `<body>` more readable. After using this option, avoid outputting the document as anything other than the default kind, `NSXMLDocumentXHTMLKind`.

(Input)

## See Also

### Constants

- [NSXMLDocumentTidyXML](documenttidyxml.md) — Changes malformed XML into valid XML during processing of the document.
- [NSXMLDocumentValidate](documentvalidate.md) — Validates this document against its DTD (internal or external) or XML Schema.
- [NSXMLDocumentXInclude](documentxinclude.md) — Replaces all XInclude nodes in the document with the nodes referred to.
- [NSXMLDocumentIncludeContentTypeDeclaration](documentincludecontenttypedeclaration.md) — Includes a content type declaration for HTML or XHTML in the output of the document.
