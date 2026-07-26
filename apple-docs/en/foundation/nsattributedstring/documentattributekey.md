---
title: NSAttributedString.DocumentAttributeKey
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/documentattributekey
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/documentattributekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/documentattributekey.json'
content_hash: 'sha256:5befc8ddfc5283bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# NSAttributedString.DocumentAttributeKey

<sub>Structure</sub>

The attributes you apply to an entire document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DocumentAttributeKey
```

## Overview

The [DocumentAttributeKey](documentattributekey.md) type defines attributes that apply to an entire attributed string, and not to specific ranges of characters. You specify these attributes when writing an attributed string to disk, or reading text from a file on disk. Use these attributes to specify metadata about the overall document, including its author or title, page margin details, font-scaling options for cross-platform interchange, and more.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting document type keys

- [documentType](documentattributekey/documenttype.md) — The document type.
- [fileType](documentattributekey/filetype.md) — The document type for interpreting the document.
- [textEncodingName](documentattributekey/textencodingname.md) — The name of the text encoding to use.

### Getting document metadata keys

- [author](documentattributekey/author.md) — The author of the document.
- [category](documentattributekey/category.md) — The document’s category.
- [characterEncoding](documentattributekey/characterencoding.md) — The string encoding for the document.
- [cocoaVersionDocumentAttribute](documentattributekey/cocoaversiondocumentattribute.md) — The version of Cocoa that created the file.
- [comment](documentattributekey/comment.md) — The document comments.
- [company](documentattributekey/company.md) — The company or organization name associated with the document.
- [converted](documentattributekey/converted.md) — A value that indicates whether a filter service converted the file.
- [copyright](documentattributekey/copyright.md) — The document’s copyright information.
- [creationTime](documentattributekey/creationtime.md) — The creation date of the document.
- [editor](documentattributekey/editor.md) — The name of person who last edited the document.
- [keywords](documentattributekey/keywords.md) — The document keywords.
- [manager](documentattributekey/manager.md) — The name of the author’s manager.
- [modificationTime](documentattributekey/modificationtime.md) — The modification date of the document.
- [readOnly](documentattributekey/readonly.md) — An indication of whether the document is read-only.
- [subject](documentattributekey/subject.md) — The subject of the document.
- [title](documentattributekey/title.md) — The document title.

### Getting document appearance keys

- [appearance](documentattributekey/appearance.md) — The appearance of the document.
- [backgroundColor](documentattributekey/backgroundcolor.md) — The background color of the document.
- [bottomMargin](documentattributekey/bottommargin.md) — The bottom margin of the document.
- [defaultFontExcluded](documentattributekey/defaultfontexcluded.md)
- [defaultTabInterval](documentattributekey/defaulttabinterval.md) — The default tab stop interval for the document.
- [excludedElements](documentattributekey/excludedelements.md) — The HTML elements to exclude in generated HTML.
- [hyphenationFactor](documentattributekey/hyphenationfactor.md) — The hyphenation factor of the document.
- [leftMargin](documentattributekey/leftmargin.md) — The left margin of the document.
- [paperMargin](documentattributekey/papermargin.md) — The paper margin of the document.
- [paperSize](documentattributekey/papersize.md) — The paper size for the document.
- [prefixSpaces](documentattributekey/prefixspaces.md) — The number of spaces for indenting nested HTML elements.
- [rightMargin](documentattributekey/rightmargin.md) — The right margin of the document.
- [textLayoutSections](documentattributekey/textlayoutsections.md) — The layout orientations for each section.
- [topMargin](documentattributekey/topmargin.md) — The top margin of the document.
- [viewMode](documentattributekey/viewmode.md) — The view mode.
- [viewSize](documentattributekey/viewsize.md) — The view size.
- [viewZoom](documentattributekey/viewzoom.md) — The view zoom.

### Getting the font-scaling options

- [sourceTextScaling](documentattributekey/sourcetextscaling.md) — The text-scaling mode you used when creating the text.
- [textScaling](documentattributekey/textscaling.md) — The text-scaling mode to use when displaying the text.

### Getting the default attributes

- [defaultAttributes](documentattributekey/defaultattributes.md) — The default document attributes.

### Initializers

- [init(_:)](<documentattributekey/init(__).md>) — Creates a document attribute key.
- [init(rawValue:)](<documentattributekey/init(rawvalue_).md>) — Creates a document attribute key with the specified raw value.

## See Also

### Getting document-wide attributes

- [DocumentReadingOptionKey](documentreadingoptionkey.md) — Options for constructing an attributed string from data you read from disk.
- [HTML attributes](../html-attributes.md) — Documentwide attributes that provide control over the form of generated HTML.
- [DocumentType](documenttype.md) — Constants for the document type document attribute key.
- [TextLayoutSectionKey](textlayoutsectionkey.md) — Constants for the text layout sections document attribute key.
- [NSTextScalingType](../../uikit/nstextscalingtype.md) — Constants that specify the text scaling.
