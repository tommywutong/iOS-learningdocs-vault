---
title: 'init(offset:length:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avsamplecursorstoragerange/init(offset:length:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplecursorstoragerange/init(offset:length:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplecursorstoragerange/init%28offset%3Alength%3A%29.json'
content_hash: 'sha256:1fec0b0160d783f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleCursorStorageRange](../avsamplecursorstoragerange.md)

# init(offset:length:)

<sub>Initializer</sub>

Creates a storage range structure with offset and length values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(offset: Int64, length: Int64)
```

## Parameters

- `offset` — The offset of the first byte of storage that a media sample or its chunk occupies.

- `length` — The number of storage bytes that a media sample or its chunk occupies.
