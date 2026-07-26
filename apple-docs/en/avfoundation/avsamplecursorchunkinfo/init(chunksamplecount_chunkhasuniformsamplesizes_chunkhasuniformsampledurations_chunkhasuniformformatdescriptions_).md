---
title: 'init(chunkSampleCount:chunkHasUniformSampleSizes:chunkHasUniformSampleDurations:chunkHasUniformFormatDescriptions:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avsamplecursorchunkinfo/init(chunksamplecount:chunkhasuniformsamplesizes:chunkhasuniformsampledurations:chunkhasuniformformatdescriptions:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplecursorchunkinfo/init(chunksamplecount:chunkhasuniformsamplesizes:chunkhasuniformsampledurations:chunkhasuniformformatdescriptions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplecursorchunkinfo/init%28chunksamplecount%3Achunkhasuniformsamplesizes%3Achunkhasuniformsampledurations%3Achunkhasuniformformatdescriptions%3A%29.json'
content_hash: 'sha256:c353e62f47525314'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleCursorChunkInfo](../avsamplecursorchunkinfo.md)

# init(chunkSampleCount:chunkHasUniformSampleSizes:chunkHasUniformSampleDurations:chunkHasUniformFormatDescriptions:)

<sub>Initializer</sub>

Creates a chunk information structure with the specified values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(chunkSampleCount: Int64, chunkHasUniformSampleSizes: ObjCBool, chunkHasUniformSampleDurations: ObjCBool, chunkHasUniformFormatDescriptions: ObjCBool)
```

## Parameters

- `chunkSampleCount` — The count of media samples in the chunk.

- `chunkHasUniformSampleSizes` — The samples in the chunk occupy the same number of bytes in storage.

- `chunkHasUniformSampleDurations` — The samples in the chunk have the same duration.

- `chunkHasUniformFormatDescriptions` — The samples in the chunk have the same format description.
