---
title: AVSampleCursorDependencyInfo
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplecursordependencyinfo
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplecursordependencyinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplecursordependencyinfo.json'
content_hash: 'sha256:571b4a86ef112976'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVSampleCursorDependencyInfo

<sub>Structure</sub>

A value for describing dependencies between a media sample and other media samples in the same sample sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AVSampleCursorDependencyInfo
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Dependency information

- [sampleIndicatesWhetherItHasDependentSamples](avsamplecursordependencyinfo/sampleindicateswhetherithasdependentsamples.md) — A Boolean value that determines whether the sample indicates if other samples depend on it.
- [sampleHasDependentSamples](avsamplecursordependencyinfo/samplehasdependentsamples.md) — A Boolean value that determines whether the sample has dependent samples.
- [sampleIndicatesWhetherItDependsOnOthers](avsamplecursordependencyinfo/sampleindicateswhetheritdependsonothers.md) — A Boolean value that determines whether the sample indicates that it depends on other samples.
- [sampleDependsOnOthers](avsamplecursordependencyinfo/sampledependsonothers.md) — A Boolean value that determines whether the sample depends on other samples.
- [sampleIndicatesWhetherItHasRedundantCoding](avsamplecursordependencyinfo/sampleindicateswhetherithasredundantcoding.md) — A Boolean value that determines whether the sample indicates that it has redundant coding.
- [sampleHasRedundantCoding](avsamplecursordependencyinfo/samplehasredundantcoding.md) — A Boolean value that determines whether the sample has redundant coding.

### Initializers

- [init()](<avsamplecursordependencyinfo/init().md>) — Creates a sample cursor dependency information structure.
- [init(sampleIndicatesWhetherItHasDependentSamples:sampleHasDependentSamples:sampleIndicatesWhetherItDependsOnOthers:sampleDependsOnOthers:sampleIndicatesWhetherItHasRedundantCoding:sampleHasRedundantCoding:)](<avsamplecursordependencyinfo/init(sampleindicateswhetherithasdependentsamples_samplehasdependentsamples_sampleindicateswhetheritdependsonothers_sampledependsonothers_sampleindicateswhetheri-a5be0090e2.md>) — Creates a sample cursor dependency information structure with sample information.

## See Also

### Sample cursors

- [AVSampleCursor](avsamplecursor.md) — An object that provides information about the media sample at the cursor’s current position.
- [AVSampleCursorSyncInfo](avsamplecursorsyncinfo.md) — A structure that describes the attributes of media samples to consider when resynchronizing a decoder.
- [AVSampleCursorAudioDependencyInfo](avsamplecursoraudiodependencyinfo.md) — A structure that describes the independent decodability of audio samples.
- [AVSampleCursorStorageRange](avsamplecursorstoragerange.md) — A structure that indicates the offset and length of storage for a media sample or its chunk.
- [AVSampleCursorChunkInfo](avsamplecursorchunkinfo.md) — A value that provides information about a chunk of media samples.
