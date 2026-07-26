---
title: AVMutableCompositionTrack
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablecompositiontrack
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablecompositiontrack'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablecompositiontrack.json'
content_hash: 'sha256:6f496711aac7bffd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMutableCompositionTrack

<sub>Class</sub>

A mutable track in a composition that you use to insert, remove, and scale track segments without affecting their low-level representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVMutableCompositionTrack
```

## Overview

Use this object to define constraints for the temporal arrangement of the track segments. If you set the composition’s track segments, you can test whether they meet the constraints by calling the [- validateTrackSegments:error:](<avmutablecompositiontrack/validatesegments(__).md>) method.

## Relationships

- **Inherits From**: [AVCompositionTrack](avcompositiontrack.md)

- **Conforms To**: [AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring track properties

- [enabled](avmutablecompositiontrack/isenabled.md) — A Boolean value that indicates whether the tracks is in an enabled state.
- [naturalTimeScale](avmutablecompositiontrack/naturaltimescale.md) — The time scale in which you can perform time-based operations without extra numerical conversion.
- [languageCode](avmutablecompositiontrack/languagecode.md) — The language associated with the track, as an ISO 639-2/T language code.
- [extendedLanguageTag](avmutablecompositiontrack/extendedlanguagetag.md) — The language tag associated with the track, as an RFC 4646 language tag.
- [preferredTransform](avmutablecompositiontrack/preferredtransform.md) — The preferred transformation of the visual media data for display purposes.
- [preferredVolume](avmutablecompositiontrack/preferredvolume.md) — The volume the track prefers for its audible media data.

### Managing time ranges

- [segments](avmutablecompositiontrack/segments.md) — The track segments that a composition track contains.
- [- insertEmptyTimeRange:](<avmutablecompositiontrack/insertemptytimerange(__).md>) — Adds or extends an empty time range within the track.
- [- insertTimeRange:ofTrack:atTime:error:](<avmutablecompositiontrack/inserttimerange(__of_at_).md>) — Inserts a time range of media from a source track into a composition track.
- [- insertTimeRanges:ofTracks:atTime:error:](<avmutablecompositiontrack/inserttimeranges(__of_at_).md>) — Inserts the time ranges of multiple source tracks into a track of a composition.
- [- removeTimeRange:](<avmutablecompositiontrack/removetimerange(__).md>) — Removes a time range of media from a composition track.
- [- scaleTimeRange:toDuration:](<avmutablecompositiontrack/scaletimerange(__toduration_).md>) — Changes the duration of a time range of the track.

### Associating tracks

- [- addTrackAssociationToTrack:type:](<avmutablecompositiontrack/addtrackassociation(to_type_).md>) — Establishes a track association of a specific type between two tracks.
- [- removeTrackAssociationToTrack:type:](<avmutablecompositiontrack/removetrackassociation(to_type_).md>) — Removes an association from a composition track.

### Replacing format descriptions

- [- replaceFormatDescription:withFormatDescription:](<avmutablecompositiontrack/replaceformatdescription(__with_).md>) — Replaces a format description with another or cancels a previous replacement.

### Validating segments

- [- validateTrackSegments:error:](<avmutablecompositiontrack/validatesegments(__).md>) — Returns a Boolean value that indicates whether a given array of track segments conform to the timing rules for a composition track.

## See Also

### Mutable compositions

- [AVMutableComposition](avmutablecomposition.md) — An object that you use to create a new composition from existing assets.
