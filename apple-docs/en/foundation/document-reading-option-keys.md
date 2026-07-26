---
title: Document reading option keys
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/document-reading-option-keys
source_url: 'https://developer.apple.com/documentation/foundation/document-reading-option-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/document-reading-option-keys.json'
content_hash: 'sha256:88e7b83b5cf4be0d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Strings and Text](strings-and-text.md) · [NSAttributedString](nsattributedstring.md)

# Document reading option keys

<sub>API Collection</sub>

Keys for constructing an attributed string from data on disk.

## Overview

Use these keys when you need to specify a key of type [NSAttributedStringDocumentReadingOptionKey](../uikit/nsattributedstringdocumentreadingoptionkey.md).

## Topics

### Getting the document options

- [baseURL](nsattributedstring/documentreadingoptionkey/baseurl.md) — The base URL for HTML documents.
- [characterEncoding](nsattributedstring/documentreadingoptionkey/characterencoding.md) — The string encoding.
- [defaultAttributes](nsattributedstring/documentreadingoptionkey/defaultattributes.md) — The default attributes to apply to plain files.
- [documentType](nsattributedstring/documentreadingoptionkey/documenttype.md) — The document type.
- [fileType](nsattributedstring/documentreadingoptionkey/filetype.md) — The file type.
- [readAccessURL](nsattributedstring/documentreadingoptionkey/readaccessurl.md) — The local files WebKit can access when loading content.
- [textEncodingName](nsattributedstring/documentreadingoptionkey/textencodingname.md) — The text encoding to use.
- [textSizeMultiplier](nsattributedstring/documentreadingoptionkey/textsizemultiplier.md) — The scale factor for font sizes.
- [timeout](nsattributedstring/documentreadingoptionkey/timeout.md) — The time, in seconds, to wait for a document to finish loading.
- [webPreferences](nsattributedstring/documentreadingoptionkey/webpreferences.md) — A WebPreferences object.
- [webResourceLoadDelegate](nsattributedstring/documentreadingoptionkey/webresourceloaddelegate.md) — An object to serve as the web resource loading delegate.

### Getting the font-scaling options

- [sourceTextScaling](nsattributedstring/documentreadingoptionkey/sourcetextscaling.md) — The text-scaling mode to associate with the document’s content.
- [targetTextScaling](nsattributedstring/documentreadingoptionkey/targettextscaling.md) — The text scaling mode to use after reading the text from disk.

### Getting the key type

- [NSAttributedStringDocumentReadingOptionKey](../uikit/nsattributedstringdocumentreadingoptionkey.md) — Options for constructing an attributed string from data you read from disk.

## See Also

### Getting document-wide attributes

- [NSAttributedStringDocumentAttributeKey](../uikit/nsattributedstringdocumentattributekey.md) — The attributes you apply to an entire document.
- [HTML attributes](html-attributes.md) — Documentwide attributes that provide control over the form of generated HTML.
- [NSAttributedStringDocumentType](../uikit/nsattributedstringdocumenttype.md) — Constants for the document type document attribute key.
- [NSTextLayoutSectionKey](../uikit/nstextlayoutsectionkey.md) — Constants for the text layout sections document attribute key.
- [NSTextScalingType](../uikit/nstextscalingtype.md) — Constants that specify the text scaling.
