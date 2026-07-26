---
title: AVAssetTrack.AssociationType
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassettrack/associationtype
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack/associationtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack/associationtype.json'
content_hash: 'sha256:428ab6dff7dab928'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrack](../avassettrack.md)

# AVAssetTrack.AssociationType

<sub>Structure</sub>

Constants that define track association types.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AssociationType
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Track association types

- [AVTrackAssociationTypeAudioFallback](associationtype/audiofallback.md) — The track contains the same content as another track, but in a more widely supported format.
- [AVTrackAssociationTypeChapterList](associationtype/chapterlist.md) — The associated track contains chapter information for the base track.
- [AVTrackAssociationTypeForcedSubtitlesOnly](associationtype/forcedsubtitlesonly.md) — An association between a subtitle track containing forced and nonforced subtitles and one with a subtitle track containing only forced subtitles.
- [AVTrackAssociationTypeMetadataReferent](associationtype/metadatareferent.md) — An association between a metadata track and the track that it describes or annotates.
- [AVTrackAssociationTypeSelectionFollower](associationtype/selectionfollower.md) — An association between two tracks that specifies when a user selects the main track, the system should follow that selection by automatically selecting the associated track.
- [AVTrackAssociationTypeTimecode](associationtype/timecode.md) — An association between a timecode track providing timing information for the main track.
- [AVTrackAssociationTypeRenderMetadataSource](associationtype/rendermetadatasource.md) — Indicates an association between a metadata track and another track where the metadata provides additional information for rendering of that track.

### Initializers

- [init(rawValue:)](<associationtype/init(rawvalue_).md>) — Creates an association type with a string value.
