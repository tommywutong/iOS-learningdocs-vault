---
title: AVSampleCursorSyncInfo
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplecursorsyncinfo
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplecursorsyncinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplecursorsyncinfo.json'
content_hash: 'sha256:a55129343e8ca06f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVSampleCursorSyncInfo

<sub>Structure</sub>

A structure that describes the attributes of media samples to consider when resynchronizing a decoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AVSampleCursorSyncInfo
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Sync information

- [sampleIsFullSync](avsamplecursorsyncinfo/sampleisfullsync.md) — A Boolean value that indicates whether a sample is a full sync sample.
- [sampleIsPartialSync](avsamplecursorsyncinfo/sampleispartialsync.md) — A Boolean value that indicates whether a sample is a partial sync sample.
- [sampleIsDroppable](avsamplecursorsyncinfo/sampleisdroppable.md) — A Boolean value that indicates whether a sample is droppable.

### Initializers

- [init()](<avsamplecursorsyncinfo/init().md>) — Creates a sample cursor sync information structure.
- [init(sampleIsFullSync:sampleIsPartialSync:sampleIsDroppable:)](<avsamplecursorsyncinfo/init(sampleisfullsync_sampleispartialsync_sampleisdroppable_).md>) — Creates a sample cursor sync information structure with media sample information.

## See Also

### Sample cursors

- [AVSampleCursor](avsamplecursor.md) — An object that provides information about the media sample at the cursor’s current position.
- [AVSampleCursorDependencyInfo](avsamplecursordependencyinfo.md) — A value for describing dependencies between a media sample and other media samples in the same sample sequence.
- [AVSampleCursorAudioDependencyInfo](avsamplecursoraudiodependencyinfo.md) — A structure that describes the independent decodability of audio samples.
- [AVSampleCursorStorageRange](avsamplecursorstoragerange.md) — A structure that indicates the offset and length of storage for a media sample or its chunk.
- [AVSampleCursorChunkInfo](avsamplecursorchunkinfo.md) — A value that provides information about a chunk of media samples.
