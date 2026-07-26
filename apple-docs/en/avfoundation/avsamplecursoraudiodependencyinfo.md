---
title: AVSampleCursorAudioDependencyInfo
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplecursoraudiodependencyinfo
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplecursoraudiodependencyinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplecursoraudiodependencyinfo.json'
content_hash: 'sha256:acf181cf7c732d0c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVSampleCursorAudioDependencyInfo

<sub>Structure</sub>

A structure that describes the independent decodability of audio samples.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AVSampleCursorAudioDependencyInfo
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Querying independent decodability

- [audioSampleIsIndependentlyDecodable](avsamplecursoraudiodependencyinfo/audiosampleisindependentlydecodable.md) — A Boolean value indicating whether the sample is independently decodable.
- [audioSamplePacketRefreshCount](avsamplecursoraudiodependencyinfo/audiosamplepacketrefreshcount.md) — The number of samples, starting at the current sample, that must be fed to the decoder to achieve full decoder refresh.

### Initializers

- [init()](<avsamplecursoraudiodependencyinfo/init().md>) — Creates an audio sample decodability information structure.
- [init(audioSampleIsIndependentlyDecodable:audioSamplePacketRefreshCount:)](<avsamplecursoraudiodependencyinfo/init(audiosampleisindependentlydecodable_audiosamplepacketrefreshcount_).md>) — Creates an audio sample decodability information structure with the specified values.

## See Also

### Sample cursors

- [AVSampleCursor](avsamplecursor.md) — An object that provides information about the media sample at the cursor’s current position.
- [AVSampleCursorSyncInfo](avsamplecursorsyncinfo.md) — A structure that describes the attributes of media samples to consider when resynchronizing a decoder.
- [AVSampleCursorDependencyInfo](avsamplecursordependencyinfo.md) — A value for describing dependencies between a media sample and other media samples in the same sample sequence.
- [AVSampleCursorStorageRange](avsamplecursorstoragerange.md) — A structure that indicates the offset and length of storage for a media sample or its chunk.
- [AVSampleCursorChunkInfo](avsamplecursorchunkinfo.md) — A value that provides information about a chunk of media samples.
