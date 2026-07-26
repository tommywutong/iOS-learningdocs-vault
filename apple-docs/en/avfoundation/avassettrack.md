---
title: AVAssetTrack
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassettrack
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack.json'
content_hash: 'sha256:d6906a950764d725'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetTrack

<sub>Class</sub>

An object that models a track of media that an asset contains.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVAssetTrack
```

## Overview

An asset contains one or more tracks of media that the framework models using the [AVAssetTrack](avassettrack.md) class. A track object holds the uniformly typed media that an asset provides such as audio, video, or closed captions.

A track, like its containing [AVAsset](avasset.md), doesn’t load all of its media upon creation. Instead, it defers loading its data until you perform an operation that requires it. Because loading the data can take time, an asset track adopts the [AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md) protocol so you can load its property values asynchronously by calling the [load(_:isolation:)](<avasynchronouskeyvalueloading/load(__isolation_).md>) method.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVCompositionTrack](avcompositiontrack.md), [AVFragmentedAssetTrack](avfragmentedassettrack.md), [AVMovieTrack](avmovietrack.md)

- **Conforms To**: [AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Identifying an asset track

- [trackID](avassettrack/trackid.md) — The persistent unique identifier for this track.
- [mediaType](avassettrack/mediatype.md) — The type of media that a track presents.
- [asset](avassettrack/asset.md) — The asset object that contains this track.

### Loading track information

- [formatDescriptions](avpartialasyncproperty/formatdescriptions.md) — The format descriptions of the media samples that a track references.
- [isPlayable](avpartialasyncproperty/isplayable-6txa5.md) — A Boolean value that indicates whether the track is playable in the current environment.
- [isDecodable](avpartialasyncproperty/isdecodable.md) — A Boolean value that indicates whether the track is decodable in the current environment.
- [isEnabled](avpartialasyncproperty/isenabled.md) — A Boolean value that indicates whether the track is in an enabled state.
- [isSelfContained](avpartialasyncproperty/isselfcontained.md) — A Boolean value that indicates whether the track references sample data only within its container file.
- [totalSampleDataLength](avpartialasyncproperty/totalsampledatalength.md) — The total number of bytes of sample data the track requires.
- [mediaCharacteristics](avpartialasyncproperty/mediacharacteristics.md) — The media characteristics for the track.

### Loading temporal information

- [timeRange](avpartialasyncproperty/timerange.md) — The time range of the track within the overall timeline of the asset.
- [naturalTimeScale](avpartialasyncproperty/naturaltimescale.md) — The natural time scale of the media that a track references.
- [estimatedDataRate](avpartialasyncproperty/estimateddatarate.md) — The estimated data rate, in bits per second, of the media that the track references.

### Loading language support

- [languageCode](avpartialasyncproperty/languagecode.md) — The language code of the track.
- [extendedLanguageTag](avpartialasyncproperty/extendedlanguagetag.md) — The language tag of the track.

### Loading visual characteristics

- [naturalSize](avpartialasyncproperty/naturalsize.md) — The natural dimensions of the media data that the track references.
- [preferredTransform](avpartialasyncproperty/preferredtransform-90jdn.md) — The track’s transform preference to apply to its visual content during presentation or processing.

### Loading audible characteristics

- [preferredVolume](avpartialasyncproperty/preferredvolume-8q2yt.md) — The track’s volume preference for playing its audible media.
- [hasAudioSampleDependencies](avpartialasyncproperty/hasaudiosampledependencies.md) — A Boolean value that indicates whether the track has sample dependencies.

### Loading frame-based characteristics

- [nominalFrameRate](avpartialasyncproperty/nominalframerate.md) — The frame rate of the track, in frames per second.
- [minFrameDuration](avpartialasyncproperty/minframeduration.md) — The minimum duration of the track’s frames.
- [requiresFrameReordering](avpartialasyncproperty/requiresframereordering.md) — A Boolean value that indicates whether samples in the track may have different presentation and decode timestamps.

### Loading metadata

- [metadata](avpartialasyncproperty/metadata-6e14c.md) — An array of metadata items for all metadata identifiers that have a value.
- [commonMetadata](avpartialasyncproperty/commonmetadata-73m58.md) — An array of metadata items for all common metadata keys that have a value.
- [availableMetadataFormats](avpartialasyncproperty/availablemetadataformats-5p9xg.md) — An array of metadata formats available for the track.
- [- loadMetadataForFormat:completionHandler:](<avassettrack/loadmetadata(for_completionhandler_).md>) — Loads metadata items that a track contains for the specified format.

### Loading track segments

- [segments](avpartialasyncproperty/segments.md) — The time mappings from the track’s media samples to its timeline.
- [- loadSegmentForTrackTime:completionHandler:](<avassettrack/loadsegment(fortracktime_completionhandler_).md>) — Loads a segment with a target time range that contains, or is closest to, the specified track time.
- [- loadSamplePresentationTimeForTrackTime:completionHandler:](<avassettrack/loadsamplepresentationtime(fortracktime_completionhandler_).md>) — Loads a sample presentation time that maps to the specified track time.
- [AVAssetTrackSegment](avassettracksegment.md) — An object that represents a time range segment of an asset track.

### Loading track associations

- [availableTrackAssociationTypes](avpartialasyncproperty/availabletrackassociationtypes.md) — An array of association types that the track uses to associate with other tracks.
- [- loadAssociatedTracksOfType:completionHandler:](<avassettrack/loadassociatedtracks(oftype_completionhandler_).md>) — Loads associated tracks that have the specified association type.

### Creating sample cursors

- [- makeSampleCursorWithPresentationTimeStamp:](<avassettrack/makesamplecursor(presentationtimestamp_).md>) — Creates a sample cursor and positions it at or near the specified presentation timestamp.
- [- makeSampleCursorAtFirstSampleInDecodeOrder](<avassettrack/makesamplecursoratfirstsampleindecodeorder().md>) — Creates a sample cursor and positions it at the track’s first media sample in decode order.
- [- makeSampleCursorAtLastSampleInDecodeOrder](<avassettrack/makesamplecursoratlastsampleindecodeorder().md>) — Creates a sample cursor and positions it at the track’s last media sample in decode order.

### Deprecated

- [Deprecated symbols](avassettrack-deprecated-symbols.md) — Review unsupported symbols and their replacements.

## See Also

### Assets

- [AVAsset](avasset.md) — An object that models timed audiovisual media.
- [AVURLAsset](avurlasset.md) — An asset that represents media at a local or remote URL.
- [AVAssetTrackSegment](avassettracksegment.md) — An object that represents a time range segment of an asset track.
- [AVAssetTrackGroup](avassettrackgroup.md) — A group of related tracks in an asset.
