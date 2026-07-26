---
title: ReferenceFileDocumentConfiguration
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/referencefiledocumentconfiguration
source_url: 'https://developer.apple.com/documentation/swiftui/referencefiledocumentconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/referencefiledocumentconfiguration.json'
content_hash: 'sha256:060bb18020650f59'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ReferenceFileDocumentConfiguration

<sub>Structure</sub>

The properties of an open reference file document.

> [!warning] Deprecated
> Use Document protocol and URLDocumentConfiguration instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency struct ReferenceFileDocumentConfiguration<Document> where Document : ReferenceFileDocument
```

## Overview

You receive an instance of this structure when you create a [DocumentGroup](documentgroup.md) with a reference file type. Use it to access the document in your viewer or editor.

## Topics

### Getting and setting the document

- [document](referencefiledocumentconfiguration/document.md) — The current document model. _(deprecated)_
- [$document](referencefiledocumentconfiguration/$document.md) _(deprecated)_

### Getting document properties

- [fileURL](referencefiledocumentconfiguration/fileurl.md) — The URL of the open file document. _(deprecated)_
- [isEditable](referencefiledocumentconfiguration/iseditable.md) — A Boolean that indicates whether you can edit the document. _(deprecated)_

## See Also

### Deprecated

- [FileDocument](filedocument.md) — A type that you use to serialize documents to and from file. _(deprecated)_
- [FileDocumentConfiguration](filedocumentconfiguration.md) — The properties of an open file document. _(deprecated)_
- [FileDocumentReadConfiguration](filedocumentreadconfiguration.md) — The configuration for reading file contents. _(deprecated)_
- [FileDocumentWriteConfiguration](filedocumentwriteconfiguration.md) — The configuration for serializing file contents. _(deprecated)_
- [NewDocumentAction](newdocumentaction.md) — An action that presents a new document. _(deprecated)_
- [ReferenceFileDocument](referencefiledocument.md) — A type that you use to serialize reference type documents to and from file. _(deprecated)_
