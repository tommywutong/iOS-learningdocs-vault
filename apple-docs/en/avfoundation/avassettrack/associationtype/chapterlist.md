---
title: chapterList
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassettrack/associationtype/chapterlist
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack/associationtype/chapterlist'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack/associationtype/chapterlist.json'
content_hash: 'sha256:1d3613589264988e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetTrack](../../avassettrack.md) · [AssociationType](../associationtype.md)

# chapterList

<sub>Type Property</sub>

The associated track contains chapter information for the base track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let chapterList: AVAssetTrack.AssociationType
```

## Discussion

The track containing the chapter information can be a text track, a video track, or a timed metadata track.

## See Also

### Track association types

- [AVTrackAssociationTypeAudioFallback](audiofallback.md) — The track contains the same content as another track, but in a more widely supported format.
- [AVTrackAssociationTypeForcedSubtitlesOnly](forcedsubtitlesonly.md) — An association between a subtitle track containing forced and nonforced subtitles and one with a subtitle track containing only forced subtitles.
- [AVTrackAssociationTypeMetadataReferent](metadatareferent.md) — An association between a metadata track and the track that it describes or annotates.
- [AVTrackAssociationTypeSelectionFollower](selectionfollower.md) — An association between two tracks that specifies when a user selects the main track, the system should follow that selection by automatically selecting the associated track.
- [AVTrackAssociationTypeTimecode](timecode.md) — An association between a timecode track providing timing information for the main track.
- [AVTrackAssociationTypeRenderMetadataSource](rendermetadatasource.md) — Indicates an association between a metadata track and another track where the metadata provides additional information for rendering of that track.
