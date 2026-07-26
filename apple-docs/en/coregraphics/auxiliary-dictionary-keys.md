---
title: Auxiliary Dictionary Keys
framework: Core Graphics
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/auxiliary-dictionary-keys
source_url: 'https://developer.apple.com/documentation/coregraphics/auxiliary-dictionary-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/auxiliary-dictionary-keys.json'
content_hash: 'sha256:b48dcb31dad9a3e1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md) · [CGContext](cgcontext.md)

# Auxiliary Dictionary Keys

<sub>API Collection</sub>

Keys for the auxiliary info dictionary you specify when creating a PDF context.

## Overview

For more information about using these keys in a PDF context, see [CGPDFContextCreate](<cgcontext/init(consumer_mediabox___).md>) and [CGPDFContextCreateWithURL](<cgcontext/init(__mediabox___).md>).

## Topics

### Metadata Keys

- [kCGPDFContextAuthor](kcgpdfcontextauthor.md) — The corresponding value is a string that represents the name of the person who created the document. This key is optional.
- [kCGPDFContextCreator](kcgpdfcontextcreator.md) — The corresponding value is a string that represents the name of the application used to produce the document. This key is optional.
- [kCGPDFContextTitle](kcgpdfcontexttitle.md) — The corresponding value is a string that represents the title of the document. This key is optional.
- [kCGPDFContextOwnerPassword](kcgpdfcontextownerpassword.md)
- [kCGPDFContextUserPassword](kcgpdfcontextuserpassword.md)
- [kCGPDFContextAllowsPrinting](kcgpdfcontextallowsprinting.md) — Whether the document allows printing when unlocked with the user password.
- [kCGPDFContextAllowsCopying](kcgpdfcontextallowscopying.md) — Whether the document allows copying when unlocked with the user password.
- [kCGPDFContextOutputIntent](kcgpdfcontextoutputintent.md)
- [kCGPDFContextOutputIntents](kcgpdfcontextoutputintents.md)
- [kCGPDFContextSubject](kcgpdfcontextsubject.md)
- [kCGPDFContextKeywords](kcgpdfcontextkeywords.md)
- [kCGPDFContextEncryptionKeyLength](kcgpdfcontextencryptionkeylength.md)

### Box Keys

- [kCGPDFContextMediaBox](kcgpdfcontextmediabox.md) — The media box for the document or for a given page.
- [kCGPDFContextCropBox](kcgpdfcontextcropbox.md) — The crop box for the document or for a given page.
- [kCGPDFContextBleedBox](kcgpdfcontextbleedbox.md) — The bleed box for the document or for a given page.
- [kCGPDFContextTrimBox](kcgpdfcontexttrimbox.md) — The trim box for the document or for a given page.
- [kCGPDFContextArtBox](kcgpdfcontextartbox.md) — The art box for the document or for a given page.

### Output Intent Keys

- [kCGPDFXOutputIntentSubtype](kcgpdfxoutputintentsubtype.md) — The output intent subtype. This key is required.
- [kCGPDFXOutputConditionIdentifier](kcgpdfxoutputconditionidentifier.md)
- [kCGPDFXOutputCondition](kcgpdfxoutputcondition.md) — A text string identifying the intended output device or production condition in a human-readable form.
- [kCGPDFXRegistryName](kcgpdfxregistryname.md)
- [kCGPDFXInfo](kcgpdfxinfo.md)
- [kCGPDFXDestinationOutputProfile](kcgpdfxdestinationoutputprofile.md)

## See Also

### Creating PDF Graphics Contexts

- [CGPDFContextCreateWithURL](<cgcontext/init(__mediabox___).md>) — Creates a URL-based PDF graphics context.
- [CGPDFContextCreate](<cgcontext/init(consumer_mediabox___).md>) — Creates a PDF graphics context.
