---
title: dataItem
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/filehandle/readcompletionmessage/dataitem
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/readcompletionmessage/dataitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/readcompletionmessage/dataitem.json'
content_hash: 'sha256:0126ed9813e18a58'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [FileHandle](../../filehandle.md) · [ReadCompletionMessage](../readcompletionmessage.md)

# dataItem

<sub>Instance Property</sub>

A result instance containing either the data read from the file or connection, or else an error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var dataItem: Result<Data, POSIXError>
```
