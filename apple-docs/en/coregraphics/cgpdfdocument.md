---
title: CGPDFDocument
framework: Core Graphics
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpdfdocument
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfdocument'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfdocument.json'
content_hash: 'sha256:a6e2565e9075b019'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFDocument

<sub>Class</sub>

A document that contains PDF (Portable Document Format) drawing information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CGPDFDocument
```

## Overview

PDF provides an efficient format for cross-platform exchange of documents with rich content. PDF files can contain multiple pages of images and text. A PDF document object contains all the information relating to a PDF document, including its catalog and contents.

Note that PDF documents may be encrypted, and that some operations may be restricted until a valid password is supplied—see the functions listed in [Working with an Encrypted PDF Document](cgpdfdocument.md#Working-with-an-Encrypted-PDF-Document).  Core Graphics also supports decrypting encrypted documents.

Core Graphics can both display and generate files that are compliant with the PDF standard.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating PDF Documents

- [CGPDFDocumentCreateWithProvider](<cgpdfdocument/init(__)-gbq6.md>) — Creates a Core Graphics PDF document using a data provider.
- [CGPDFDocumentCreateWithURL](<cgpdfdocument/init(__)-2gtsd.md>) — Creates a Core Graphics PDF document using data specified by a URL.

### Examining a PDF Document

- [CGPDFDocumentGetCatalog](cgpdfdocument/catalog.md) — Returns the document catalog of a Core Graphics PDF document.
- [CGPDFDocumentGetID](cgpdfdocument/fileidentifier.md) — Gets the file identifier for a PDF document.
- [CGPDFDocumentGetInfo](cgpdfdocument/info.md) — Gets the information dictionary for a PDF document.
- [CGPDFDocumentGetNumberOfPages](cgpdfdocument/numberofpages.md) — Returns the number of pages in a PDF document.
- [CGPDFDocumentGetVersion](<cgpdfdocument/getversion(majorversion_minorversion_).md>) — Returns the major and minor version numbers of a Core Graphics PDF document.
- [CGPDFDocumentGetPage](<cgpdfdocument/page(at_).md>) — Returns a page from a Core Graphics PDF document.

### Working with an Encrypted PDF Document

- [CGPDFDocumentIsEncrypted](cgpdfdocument/isencrypted.md) — Returns whether the specified PDF file is encrypted.
- [CGPDFDocumentAllowsCopying](cgpdfdocument/allowscopying.md) — Returns whether the specified PDF document allows copying.
- [CGPDFDocumentAllowsPrinting](cgpdfdocument/allowsprinting.md) — Returns whether a PDF document allows printing.
- [CGPDFDocumentIsUnlocked](cgpdfdocument/isunlocked.md) — Returns whether the specified PDF document is currently unlocked.
- [CGPDFDocumentUnlockWithPassword](<cgpdfdocument/unlockwithpassword(__).md>) — Unlocks an encrypted PDF document when a valid password is supplied.

### Working with Core Foundation Types

- [CGPDFDocumentGetTypeID](cgpdfdocument/typeid.md) — Returns the type identifier for Core Graphics PDF documents.

### Abstract Types for PDF Document Content

- [CGPDFPage](cgpdfpage.md) — A type that represents a page in a PDF document.
- [CGPDFArray](cgpdfarray.md) — An array structure within a PDF document.
- [CGPDFObject](cgpdfobject.md) — An object representing content within a PDF document.
- [CGPDFStream](cgpdfstream.md) — A stream or sequence of data bytes in a PDF document.
- [CGPDFString](cgpdfstring.md) — A text string in a PDF document.
- [CGPDFScanner](cgpdfscanner.md) — A parser object for handling content and operators in a PDF content stream.
- [CGPDFDictionary](cgpdfdictionary.md) — A dictionary structure within a PDF document.
- [CGPDFContentStream](cgpdfcontentstream.md) — A representation of one or more content data streams in a PDF page.
- [CGPDFOperatorTable](cgpdfoperatortable.md) — A set of callback functions for operators used when scanning content in a PDF document.

### Instance Properties

- [CGPDFDocumentGetAccessPermissions](cgpdfdocument/accesspermissions.md)
- [CGPDFDocumentGetOutline](cgpdfdocument/outline.md)
