---
title: FileDocumentConfiguration
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/filedocumentconfiguration
source_url: 'https://developer.apple.com/documentation/swiftui/filedocumentconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/filedocumentconfiguration.json'
content_hash: 'sha256:d552d40b00e331d9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# FileDocumentConfiguration

<sub>Structure</sub>

The properties of an open file document.

> [!warning] Deprecated
> Conform your type to Document and use URLDocumentConfiguration instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct FileDocumentConfiguration<Document> where Document : FileDocument
```

## Overview

You receive an instance of this structure when you create a [DocumentGroup](documentgroup.md) with a value file type. Use it to access the document in your viewer or editor.

## Topics

### Getting and setting the document

- [document](filedocumentconfiguration/document.md) — The current document model. _(deprecated)_
- [$document](filedocumentconfiguration/$document.md) _(deprecated)_

### Getting document properties

- [fileURL](filedocumentconfiguration/fileurl.md) — The URL of the open file document. _(deprecated)_
- [isEditable](filedocumentconfiguration/iseditable.md) — A Boolean that indicates whether you can edit the document. _(deprecated)_

### Instance Properties

- [creationSource](filedocumentconfiguration/creationsource.md) — The source associated with the button that created this document. _(deprecated)_

## See Also

### Deprecated

- [FileDocument](filedocument.md) — A type that you use to serialize documents to and from file. _(deprecated)_
- [FileDocumentReadConfiguration](filedocumentreadconfiguration.md) — The configuration for reading file contents. _(deprecated)_
- [FileDocumentWriteConfiguration](filedocumentwriteconfiguration.md) — The configuration for serializing file contents. _(deprecated)_
- [NewDocumentAction](newdocumentaction.md) — An action that presents a new document. _(deprecated)_
- [ReferenceFileDocument](referencefiledocument.md) — A type that you use to serialize reference type documents to and from file. _(deprecated)_
- [ReferenceFileDocumentConfiguration](referencefiledocumentconfiguration.md) — The properties of an open reference file document. _(deprecated)_
