---
title: AVSampleCursorStorageRange
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplecursorstoragerange
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplecursorstoragerange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplecursorstoragerange.json'
content_hash: 'sha256:c611c45354aa5ee1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVSampleCursorStorageRange

<sub>Structure</sub>

A structure that indicates the offset and length of storage for a media sample or its chunk.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AVSampleCursorStorageRange
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Storage range

- [offset](avsamplecursorstoragerange/offset.md) — The offset of the first byte of storage that a media sample or its chunk occupies.
- [length](avsamplecursorstoragerange/length.md) — The count of bytes of storage that a media sample or its chunk occupies.

### Initializers

- [init()](<avsamplecursorstoragerange/init().md>) — Creates a storage range structure.
- [init(offset:length:)](<avsamplecursorstoragerange/init(offset_length_).md>) — Creates a storage range structure with offset and length values.

## See Also

### Sample cursors

- [AVSampleCursor](avsamplecursor.md) — An object that provides information about the media sample at the cursor’s current position.
- [AVSampleCursorSyncInfo](avsamplecursorsyncinfo.md) — A structure that describes the attributes of media samples to consider when resynchronizing a decoder.
- [AVSampleCursorDependencyInfo](avsamplecursordependencyinfo.md) — A value for describing dependencies between a media sample and other media samples in the same sample sequence.
- [AVSampleCursorAudioDependencyInfo](avsamplecursoraudiodependencyinfo.md) — A structure that describes the independent decodability of audio samples.
- [AVSampleCursorChunkInfo](avsamplecursorchunkinfo.md) — A value that provides information about a chunk of media samples.
