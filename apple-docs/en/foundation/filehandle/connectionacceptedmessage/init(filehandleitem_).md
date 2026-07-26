---
title: 'init(fileHandleItem:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filehandle/connectionacceptedmessage/init(filehandleitem:)'
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/connectionacceptedmessage/init(filehandleitem:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/connectionacceptedmessage/init%28filehandleitem%3A%29.json'
content_hash: 'sha256:f39a76734377b941'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [FileHandle](../../filehandle.md) · [ConnectionAcceptedMessage](../connectionacceptedmessage.md)

# init(fileHandleItem:)

<sub>Initializer</sub>

Creates a message for a file handle connection acceptance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(fileHandleItem: Result<FileHandle, POSIXError>)
```

## Parameters

- `fileHandleItem` — A result instance containing either the file handle representing the “near” end of a socket connection, or an error.
