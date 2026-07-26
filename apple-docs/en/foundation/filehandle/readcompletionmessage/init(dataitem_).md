---
title: 'init(dataItem:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filehandle/readcompletionmessage/init(dataitem:)'
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/readcompletionmessage/init(dataitem:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/readcompletionmessage/init%28dataitem%3A%29.json'
content_hash: 'sha256:6afdb32882095a26'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [FileHandle](../../filehandle.md) · [ReadCompletionMessage](../readcompletionmessage.md)

# init(dataItem:)

<sub>Initializer</sub>

Creates a message that indicates a file handle read data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(dataItem: Result<Data, POSIXError>)
```

## Parameters

- `dataItem` — A result instance that contains either the data read or an error.
