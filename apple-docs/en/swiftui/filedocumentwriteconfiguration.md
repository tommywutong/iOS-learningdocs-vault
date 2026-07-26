---
title: FileDocumentWriteConfiguration
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/filedocumentwriteconfiguration
source_url: 'https://developer.apple.com/documentation/swiftui/filedocumentwriteconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/filedocumentwriteconfiguration.json'
content_hash: 'sha256:fe115b78402e4428'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# FileDocumentWriteConfiguration

<sub>Structure</sub>

The configuration for serializing file contents.

> [!warning] Deprecated
> Use the Document protocol and URLDocumentConfiguration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct FileDocumentWriteConfiguration
```

## Topics

### Writing the content

- [contentType](filedocumentwriteconfiguration/contenttype.md) — The expected uniform type of the file contents. _(deprecated)_
- [existingFile](filedocumentwriteconfiguration/existingfile.md) — The file wrapper containing the current document content. `nil` if the document is unsaved. _(deprecated)_

## See Also

### Deprecated

- [FileDocument](filedocument.md) — A type that you use to serialize documents to and from file. _(deprecated)_
- [FileDocumentConfiguration](filedocumentconfiguration.md) — The properties of an open file document. _(deprecated)_
- [FileDocumentReadConfiguration](filedocumentreadconfiguration.md) — The configuration for reading file contents. _(deprecated)_
- [NewDocumentAction](newdocumentaction.md) — An action that presents a new document. _(deprecated)_
- [ReferenceFileDocument](referencefiledocument.md) — A type that you use to serialize reference type documents to and from file. _(deprecated)_
- [ReferenceFileDocumentConfiguration](referencefiledocumentconfiguration.md) — The properties of an open reference file document. _(deprecated)_
