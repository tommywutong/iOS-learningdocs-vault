---
title: renderMetadataSource
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassettrack/associationtype/rendermetadatasource
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack/associationtype/rendermetadatasource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack/associationtype/rendermetadatasource.json'
content_hash: 'sha256:7f6f5b9d65e3cc3f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetTrack](../../avassettrack.md) · [AssociationType](../associationtype.md)

# renderMetadataSource

<sub>Type Property</sub>

Indicates an association between a metadata track and another track where the metadata provides additional information for rendering of that track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let renderMetadataSource: AVAssetTrack.AssociationType
```

## Discussion

This track association is not symmetric; when used with -[AVAssetWriterInput addTrackAssociationWithTrackOfInput:type:], the receiver should be an instance of AVAssetWriterInput with mediaType, AVMediaTypeMetadata, while the input parameter should be an instance of AVAssetWriterInput for the target track that would be rendered (for example, a video track).

## See Also

### Track association types

- [AVTrackAssociationTypeAudioFallback](audiofallback.md) — The track contains the same content as another track, but in a more widely supported format.
- [AVTrackAssociationTypeChapterList](chapterlist.md) — The associated track contains chapter information for the base track.
- [AVTrackAssociationTypeForcedSubtitlesOnly](forcedsubtitlesonly.md) — An association between a subtitle track containing forced and nonforced subtitles and one with a subtitle track containing only forced subtitles.
- [AVTrackAssociationTypeMetadataReferent](metadatareferent.md) — An association between a metadata track and the track that it describes or annotates.
- [AVTrackAssociationTypeSelectionFollower](selectionfollower.md) — An association between two tracks that specifies when a user selects the main track, the system should follow that selection by automatically selecting the associated track.
- [AVTrackAssociationTypeTimecode](timecode.md) — An association between a timecode track providing timing information for the main track.
