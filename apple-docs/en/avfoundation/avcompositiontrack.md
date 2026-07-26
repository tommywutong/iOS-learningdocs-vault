---
title: AVCompositionTrack
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcompositiontrack
source_url: 'https://developer.apple.com/documentation/avfoundation/avcompositiontrack'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcompositiontrack.json'
content_hash: 'sha256:6e30473c7e25f5e9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCompositionTrack

<sub>Class</sub>

A track in a composition that presents media of a uniform type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVCompositionTrack
```

## Overview

This object provides an immutable composition track. The framework also provides a mutable subclass, [AVMutableCompositionTrack](avmutablecompositiontrack.md).

## Relationships

- **Inherits From**: [AVAssetTrack](avassettrack.md)

- **Inherited By**: [AVMutableCompositionTrack](avmutablecompositiontrack.md)

- **Conforms To**: [AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accessing track information

- [isPlayable](avcompositiontrack/isplayable.md) — A Boolean value that indicates whether the track is playable in the current environment.
- [isDecodable](avcompositiontrack/isdecodable.md) — A Boolean value that indicates whether the track is decodable in the current environment.
- [isEnabled](avcompositiontrack/isenabled.md) — A Boolean value that indicates whether the track’s container enables it.
- [isSelfContained](avcompositiontrack/isselfcontained.md) — A Boolean value that indicates whether this track references sample data only within its container file.
- [totalSampleDataLength](avcompositiontrack/totalsampledatalength.md) — The total number of bytes of sample data the track requires.
- [- hasMediaCharacteristic:](<avcompositiontrack/hasmediacharacteristic(__).md>) — Returns a Boolean value that indicates whether the track references media with the specified media characteristic.

### Accessing temporal information

- [timeRange](avcompositiontrack/timerange.md) — The time range of the track within the overall timeline of the asset.
- [naturalTimeScale](avcompositiontrack/naturaltimescale.md) — The natural time scale of the media that a track references.
- [estimatedDataRate](avcompositiontrack/estimateddatarate.md) — The estimated data rate, in bits per second, of the media that the track references.
- [- samplePresentationTimeForTrackTime:](<avcompositiontrack/samplepresentationtime(fortracktime_).md>) — Maps the specified track time through the appropriate time mapping and returns the resulting sample presentation time.

### Accessing language support

- [languageCode](avcompositiontrack/languagecode.md) — The language code of the track.
- [extendedLanguageTag](avcompositiontrack/extendedlanguagetag.md) — The language tag of the track.

### Managing format descriptions

- [formatDescriptions](avcompositiontrack/formatdescriptions.md) — The format descriptions of the media samples that a track references.
- [formatDescriptionReplacements](avcompositiontrack/formatdescriptionreplacements.md) — The replacement format descriptions.
- [AVCompositionTrackFormatDescriptionReplacement](avcompositiontrackformatdescriptionreplacement.md) — An object that represents a format description and its replacement.

### Accessing visual characteristics

- [naturalSize](avcompositiontrack/naturalsize.md) — The natural dimensions of the media data that the track references.
- [preferredTransform](avcompositiontrack/preferredtransform.md) — The track’s transform preference to apply to its visual content during presentation or processing.

### Accessing audible characteristics

- [preferredVolume](avcompositiontrack/preferredvolume.md) — The track’s volume preference for playing its audible media.
- [hasAudioSampleDependencies](avcompositiontrack/hasaudiosampledependencies.md) — A Boolean value that indicates whether the track has sample dependencies.

### Accessing frame-based characteristics

- [nominalFrameRate](avcompositiontrack/nominalframerate.md) — The frame rate of the track, in frames per second.
- [minFrameDuration](avcompositiontrack/minframeduration.md) — The minimum duration of the track’s frames.
- [requiresFrameReordering](avcompositiontrack/requiresframereordering.md) — A Boolean value that indicates whether samples in the track may have different presentation and decode timestamps.

### Accessing metadata

- [metadata](avcompositiontrack/metadata.md) — An array of metadata items for all metadata identifiers that have a value.
- [commonMetadata](avcompositiontrack/commonmetadata.md) — An array of metadata items for all common metadata keys that have a value.
- [availableMetadataFormats](avcompositiontrack/availablemetadataformats.md) — An array of metadata formats available for the track.
- [- metadataForFormat:](<avcompositiontrack/metadata(forformat_).md>) — Returns metadata items that a track contains for the specified format.

### Accessing track segments

- [segments](avcompositiontrack/segments.md) — The time mappings from the track’s media samples to its timeline.
- [- segmentForTrackTime:](<avcompositiontrack/segment(fortracktime_).md>) — Returns a segment whose target time range contains, or is closest to, the specified track time.

### Accessing track associations

- [availableTrackAssociationTypes](avcompositiontrack/availabletrackassociationtypes.md) — An array of association types that the track uses to associate with other tracks.
- [- associatedTracksOfType:](<avcompositiontrack/associatedtracks(oftype_).md>) — Returns an array of associated tracks that have the specified association type.

### Determining sample cursor support

- [canProvideSampleCursors](avcompositiontrack/canprovidesamplecursors.md) — A Boolean value that indicates whether the track can provide instances of sample cursors to traverse its media samples and discover information.

## See Also

### Compositions

- [AVComposition](avcomposition.md) — An object that combines and arranges media from multiple assets into a single composite asset that you can play or process.
- [AVCompositionTrackSegment](avcompositiontracksegment.md) — A track segment that maps a time from the source media track to the composition track.
