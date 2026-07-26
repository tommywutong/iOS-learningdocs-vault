---
title: existingFile
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/filedocumentwriteconfiguration/existingfile
source_url: 'https://developer.apple.com/documentation/swiftui/filedocumentwriteconfiguration/existingfile'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/filedocumentwriteconfiguration/existingfile.json'
content_hash: 'sha256:d0d69a4c4068a5c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FileDocumentWriteConfiguration](../filedocumentwriteconfiguration.md)

# existingFile

<sub>Instance Property</sub>

The file wrapper containing the current document content. `nil` if the document is unsaved.

> [!warning] Deprecated
> Use the Document protocol and URLDocumentConfiguration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
let existingFile: FileWrapper?
```

## See Also

### Writing the content

- [contentType](contenttype.md) — The expected uniform type of the file contents. _(deprecated)_
