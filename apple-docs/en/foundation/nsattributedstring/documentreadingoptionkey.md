---
title: NSAttributedString.DocumentReadingOptionKey
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/documentreadingoptionkey
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/documentreadingoptionkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/documentreadingoptionkey.json'
content_hash: 'sha256:1911f9836246065f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# NSAttributedString.DocumentReadingOptionKey

<sub>Structure</sub>

Options for constructing an attributed string from data you read from disk.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DocumentReadingOptionKey
```

## Overview

The [DocumentReadingOptionKey](documentreadingoptionkey.md) type defines attributes to use when creating an attributed string from data in a file. Use these strings with methods such as [- initWithData:options:documentAttributes:error:](<init(data_options_documentattributes_).md>), [- initWithHTML:options:documentAttributes:](<init(html_options_documentattributes_).md>), [- initWithURL:options:documentAttributes:error:](<init(url_options_documentattributes_).md>), [- readFromData:options:documentAttributes:error:](<../nsmutableattributedstring/read(from_options_documentattributes_)-5mbcx.md>), and [- readFromURL:options:documentAttributes:error:](<../nsmutableattributedstring/read(from_options_documentattributes_)-54wth.md>) to specify expected details. For example, specify the [documentType](documentreadingoptionkey/documenttype.md) attribute to interpret the file data as a specific file format.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting the document options

- [baseURL](documentreadingoptionkey/baseurl.md) — The base URL for HTML documents.
- [characterEncoding](documentreadingoptionkey/characterencoding.md) — The string encoding.
- [defaultAttributes](documentreadingoptionkey/defaultattributes.md) — The default attributes to apply to plain files.
- [documentType](documentreadingoptionkey/documenttype.md) — The document type.
- [fileType](documentreadingoptionkey/filetype.md) — The file type.
- [readAccessURL](documentreadingoptionkey/readaccessurl.md) — The local files WebKit can access when loading content.
- [textEncodingName](documentreadingoptionkey/textencodingname.md) — The text encoding to use.
- [textSizeMultiplier](documentreadingoptionkey/textsizemultiplier.md) — The scale factor for font sizes.
- [timeout](documentreadingoptionkey/timeout.md) — The time, in seconds, to wait for a document to finish loading.
- [webPreferences](documentreadingoptionkey/webpreferences.md) — A WebPreferences object.
- [webResourceLoadDelegate](documentreadingoptionkey/webresourceloaddelegate.md) — An object to serve as the web resource loading delegate.

### Getting the font-scaling options

- [sourceTextScaling](documentreadingoptionkey/sourcetextscaling.md) — The text-scaling mode to associate with the document’s content.
- [targetTextScaling](documentreadingoptionkey/targettextscaling.md) — The text scaling mode to use after reading the text from disk.

### Initializers

- [init(_:)](<documentreadingoptionkey/init(__).md>) — Creates a document reading option key with the specified raw value.
- [init(rawValue:)](<documentreadingoptionkey/init(rawvalue_).md>) — Creates a document reading option key with the specified raw value.

### Type Properties

- [textKit1ListMarkerFormatDocumentOption](documentreadingoptionkey/textkit1listmarkerformatdocumentoption.md)

## See Also

### Getting document-wide attributes

- [DocumentAttributeKey](documentattributekey.md) — The attributes you apply to an entire document.
- [HTML attributes](../html-attributes.md) — Documentwide attributes that provide control over the form of generated HTML.
- [DocumentType](documenttype.md) — Constants for the document type document attribute key.
- [TextLayoutSectionKey](textlayoutsectionkey.md) — Constants for the text layout sections document attribute key.
- [NSTextScalingType](../../uikit/nstextscalingtype.md) — Constants that specify the text scaling.
