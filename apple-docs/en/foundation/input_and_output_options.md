---
title: Input and Output Options
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/input_and_output_options
source_url: 'https://developer.apple.com/documentation/foundation/input_and_output_options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/input_and_output_options.json'
content_hash: 'sha256:1b496b7c1c887acc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Archives and Serialization](archives-and-serialization.md) · [XML Processing and Modeling](xml-processing-and-modeling.md) · [XMLDocument](xmldocument.md)

# Input and Output Options

<sub>API Collection</sub>

Input and output options specifically intended for `NSXMLDocument` objects.

## Overview

Because `NSXMLDocument` is a subclass of [XMLNode](xmlnode.md), you can also use the relevant input and output options described in Constants in the `NSXMLNode` class reference. You can specify input options in the `NSXMLDocument` methods [- initWithContentsOfURL:options:error:](<xmldocument/init(contentsof_options_).md>), [- initWithData:options:error:](<xmldocument/init(data_options_).md>), [- initWithXMLString:options:error:](<xmldocument/init(xmlstring_options_)-65m2r.md>). The [- XMLDataWithOptions:](<xmldocument/xmldata(options_).md>) method takes output options.

## Topics

### Constants

- [NSXMLDocumentTidyHTML](xmlnode/options/documenttidyhtml.md) — Formats HTML into valid XHTML during processing of the document.
- [NSXMLDocumentTidyXML](xmlnode/options/documenttidyxml.md) — Changes malformed XML into valid XML during processing of the document.
- [NSXMLDocumentValidate](xmlnode/options/documentvalidate.md) — Validates this document against its DTD (internal or external) or XML Schema.
- [NSXMLDocumentXInclude](xmlnode/options/documentxinclude.md) — Replaces all XInclude nodes in the document with the nodes referred to.
- [NSXMLDocumentIncludeContentTypeDeclaration](xmlnode/options/documentincludecontenttypedeclaration.md) — Includes a content type declaration for HTML or XHTML in the output of the document.

## See Also

### Constants

- [ContentKind](xmldocument/contentkind.md) — Type used to define the kind of document content.
- [Document Content Types](document-content-types.md) — Define document types.
