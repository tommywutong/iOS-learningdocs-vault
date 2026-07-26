---
title: AVSampleCursorChunkInfo
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplecursorchunkinfo
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplecursorchunkinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplecursorchunkinfo.json'
content_hash: 'sha256:43a9889870ba0ec2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVSampleCursorChunkInfo

<sub>Structure</sub>

A value that provides information about a chunk of media samples.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AVSampleCursorChunkInfo
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Chunk information

- [chunkSampleCount](avsamplecursorchunkinfo/chunksamplecount.md) — The count of media samples in the chunk.
- [chunkHasUniformSampleSizes](avsamplecursorchunkinfo/chunkhasuniformsamplesizes.md) — The samples in the chunk occupy the same number of bytes in storage.
- [chunkHasUniformSampleDurations](avsamplecursorchunkinfo/chunkhasuniformsampledurations.md) — The samples in the chunk have the same duration.
- [chunkHasUniformFormatDescriptions](avsamplecursorchunkinfo/chunkhasuniformformatdescriptions.md) — The samples in the chunk have the same format description.

### Initializers

- [init()](<avsamplecursorchunkinfo/init().md>) — Creates a chunk information structure.
- [init(chunkSampleCount:chunkHasUniformSampleSizes:chunkHasUniformSampleDurations:chunkHasUniformFormatDescriptions:)](<avsamplecursorchunkinfo/init(chunksamplecount_chunkhasuniformsamplesizes_chunkhasuniformsampledurations_chunkhasuniformformatdescriptions_).md>) — Creates a chunk information structure with the specified values.

## See Also

### Sample cursors

- [AVSampleCursor](avsamplecursor.md) — An object that provides information about the media sample at the cursor’s current position.
- [AVSampleCursorSyncInfo](avsamplecursorsyncinfo.md) — A structure that describes the attributes of media samples to consider when resynchronizing a decoder.
- [AVSampleCursorDependencyInfo](avsamplecursordependencyinfo.md) — A value for describing dependencies between a media sample and other media samples in the same sample sequence.
- [AVSampleCursorAudioDependencyInfo](avsamplecursoraudiodependencyinfo.md) — A structure that describes the independent decodability of audio samples.
- [AVSampleCursorStorageRange](avsamplecursorstoragerange.md) — A structure that indicates the offset and length of storage for a media sample or its chunk.
