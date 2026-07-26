---
title: forcedSubtitlesOnly
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassettrack/associationtype/forcedsubtitlesonly
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack/associationtype/forcedsubtitlesonly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack/associationtype/forcedsubtitlesonly.json'
content_hash: 'sha256:7a335561088a91ac'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetTrack](../../avassettrack.md) · [AssociationType](../associationtype.md)

# forcedSubtitlesOnly

<sub>Type Property</sub>

An association between a subtitle track containing forced and nonforced subtitles and one with a subtitle track containing only forced subtitles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let forcedSubtitlesOnly: AVAssetTrack.AssociationType
```

## Discussion

Nonforced subtitles typically transcribe dialogue in a media asset and are typically not presented by default. Forced subtitles are those that are essential for presentation even if the user disables playback of normal subtitles (for example, when a character speaks in a language foreign to that of the audio track).

Subtitle tracks must present forced subtitles with the same content and the same language, but may have different timing.

## See Also

### Track association types

- [AVTrackAssociationTypeAudioFallback](audiofallback.md) — The track contains the same content as another track, but in a more widely supported format.
- [AVTrackAssociationTypeChapterList](chapterlist.md) — The associated track contains chapter information for the base track.
- [AVTrackAssociationTypeMetadataReferent](metadatareferent.md) — An association between a metadata track and the track that it describes or annotates.
- [AVTrackAssociationTypeSelectionFollower](selectionfollower.md) — An association between two tracks that specifies when a user selects the main track, the system should follow that selection by automatically selecting the associated track.
- [AVTrackAssociationTypeTimecode](timecode.md) — An association between a timecode track providing timing information for the main track.
- [AVTrackAssociationTypeRenderMetadataSource](rendermetadatasource.md) — Indicates an association between a metadata track and another track where the metadata provides additional information for rendering of that track.
