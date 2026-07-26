---
title: fileHandleItem
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/filehandle/connectionacceptedmessage/filehandleitem
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/connectionacceptedmessage/filehandleitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/connectionacceptedmessage/filehandleitem.json'
content_hash: 'sha256:2561a6a3f4eff318'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [FileHandle](../../filehandle.md) · [ConnectionAcceptedMessage](../connectionacceptedmessage.md)

# fileHandleItem

<sub>Instance Property</sub>

A result instance that contains either the file handle representing the “near” end of a socket connection, or an error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var fileHandleItem: Result<FileHandle, POSIXError>
```
