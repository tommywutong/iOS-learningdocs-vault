---
title: currentChunkStorageURL
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 10.10+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplecursor/currentchunkstorageurl
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplecursor/currentchunkstorageurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplecursor/currentchunkstorageurl.json'
content_hash: 'sha256:bcc940790b7cbb62'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleCursor](../avsamplecursor.md)

# currentChunkStorageURL

<sub>Instance Property</sub>

The URL of the storage container of the current sample and other samples to load in the same operation as a chunk.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var currentChunkStorageURL: URL? { get }
```

## Discussion

When this property is `nil`, the storage location of the chunk is the URL of the sample cursor’s track’s asset, if it has one.

## See Also

### Getting sample information

- [currentChunkInfo](currentchunkinfo.md) — A value that provides information about the chunk of samples to which the current sample belongs.
- [AVSampleCursorChunkInfo](../avsamplecursorchunkinfo.md) — A value that provides information about a chunk of media samples.
- [currentChunkStorageRange](currentchunkstoragerange.md) — The sample range in the storage container to load together with the current sample as a chunk.
- [AVSampleCursorStorageRange](../avsamplecursorstoragerange.md) — A structure that indicates the offset and length of storage for a media sample or its chunk.
- [currentSampleDependencyInfo](currentsampledependencyinfo.md) — The dependency information that describes relationships between a media sample and other media samples in the same sample sequence.
- [AVSampleCursorDependencyInfo](../avsamplecursordependencyinfo.md) — A value for describing dependencies between a media sample and other media samples in the same sample sequence.
- [currentSampleDuration](currentsampleduration.md) — The decode duration of the sample at the cursor’s current position.
- [currentSampleIndexInChunk](currentsampleindexinchunk.md) — The index of the current sample within the chunk to which it belongs.
- [currentSampleStorageRange](currentsamplestoragerange.md) — The offset and length of the current sample in the current chunk storage URL.
- [currentSampleSyncInfo](currentsamplesyncinfo.md) — The synchronization information for the current sample for consideration when resynchronizing a decoder.
- [AVSampleCursorSyncInfo](../avsamplecursorsyncinfo.md) — A structure that describes the attributes of media samples to consider when resynchronizing a decoder.
- [- copyCurrentSampleFormatDescription](<copycurrentsampleformatdescription().md>) — Returns the format description of the sample at the cursor’s current position.
- [currentSampleAudioDependencyInfo](currentsampleaudiodependencyinfo.md) — The independent decodability information for the audio sample.
- [currentSampleDependencyAttachments](currentsampledependencyattachments.md) — A dictionary of dependency-related sample buffer attachments.
