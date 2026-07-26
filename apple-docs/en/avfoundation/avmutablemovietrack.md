---
title: AVMutableMovieTrack
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovietrack
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovietrack'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovietrack.json'
content_hash: 'sha256:0f3051a58d4767aa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMutableMovieTrack

<sub>Class</sub>

A mutable track that conforms to the QuickTime or ISO base media file format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
class AVMutableMovieTrack
```

## Relationships

- **Inherits From**: [AVMovieTrack](avmovietrack.md)

- **Conforms To**: [AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Managing time ranges

- [- insertTimeRange:ofTrack:atTime:copySampleData:error:](<avmutablemovietrack/inserttimerange(__of_at_copysampledata_).md>) — Inserts a portion of an asset track into the target movie.
- [- insertEmptyTimeRange:](<avmutablemovietrack/insertemptytimerange(__).md>) — Adds an empty time range to a track.
- [- removeTimeRange:](<avmutablemovietrack/removetimerange(__).md>) — Removes the specified time range from a track.
- [- scaleTimeRange:toDuration:](<avmutablemovietrack/scaletimerange(__toduration_).md>) — Changes the duration of a time range in a track.

### Appending sample data

- [append(_:)](<avmutablemovietrack/append(__).md>) — Appends sample data to a media file and adds sample references for the added data to a track’s media sample tables.
- [- appendSampleBuffer:decodeTime:presentationTime:error:](<avmutablemovietrack/append(__decodetime_presentationtime_).md>) — Appends sample data to a media file and adds sample references for the added data to a track’s media sample tables. _(deprecated)_
- [- insertMediaTimeRange:intoTimeRange:](<avmutablemovietrack/insertmediatimerange(__into_).md>) — Inserts a reference to a media time range into a track.

### Accessing media chunks

- [preferredMediaChunkAlignment](avmutablemovietrack/preferredmediachunkalignment.md) — The boundary for media chunk alignment for file types that support media chunk alignment.
- [preferredMediaChunkDuration](avmutablemovietrack/preferredmediachunkduration.md) — The maximum duration to use for each chunk of sample data written to the file for file types that support media chunk duration.
- [preferredMediaChunkSize](avmutablemovietrack/preferredmediachunksize.md) — The maximum size to use for each chunk of sample data written to the file for file types that support media chunk duration.

### Changing format descriptions

- [formatDescriptions](avmutablemovietrack/formatdescriptions.md) — The format descriptions of the media samples that a track references.
- [- replaceFormatDescription:withFormatDescription:](<avmutablemovietrack/replaceformatdescription(__with_).md>) — Replaces the track’s format description with a new format description.

### Configuring track information

- [modified](avmutablemovietrack/ismodified.md) — A Boolean value that indicates whether a track is in a modified state.
- [alternateGroupID](avmutablemovietrack/alternategroupid.md) — A number that identifies the track as a member of a particular alternate group.
- [mediaDataStorage](avmutablemovietrack/mediadatastorage.md) — A storage container for the media data to be added to a track.
- [sampleReferenceBaseURL](avmutablemovietrack/samplereferencebaseurl.md) — The base URL for sample references.

### Accessing track information

- [isPlayable](avmutablemovietrack/isplayable.md) — A Boolean value that indicates whether the track is playable in the current environment.
- [isDecodable](avmutablemovietrack/isdecodable.md) — A Boolean value that indicates whether the track is decodable in the current environment.
- [enabled](avmutablemovietrack/isenabled.md) — A Boolean value that indicates whether the track’s container enables it.
- [isSelfContained](avmutablemovietrack/isselfcontained.md) — A Boolean value that indicates whether this track references sample data only within its container file.
- [hasProtectedContent](avmutablemovietrack/hasprotectedcontent.md) — A Boolean value that indicates whether a track contains protected content.
- [totalSampleDataLength](avmutablemovietrack/totalsampledatalength.md) — The total number of bytes of sample data the track requires.
- [- hasMediaCharacteristic:](<avmutablemovietrack/hasmediacharacteristic(__).md>) — Returns a Boolean value that indicates whether the track references media with the specified media characteristic.

### Accessing temporal information

- [timeRange](avmutablemovietrack/timerange.md) — The time range of the track within the overall timeline of the asset.
- [timescale](avmutablemovietrack/timescale.md) — The time scale for tracks that contain the `moov` atom.
- [naturalTimeScale](avmutablemovietrack/naturaltimescale.md) — The natural time scale of the media that a track references.
- [estimatedDataRate](avmutablemovietrack/estimateddatarate.md) — The estimated data rate, in bits per second, of the media that the track references.
- [- samplePresentationTimeForTrackTime:](<avmutablemovietrack/samplepresentationtime(fortracktime_).md>) — Maps the specified track time through the appropriate time mapping and returns the resulting sample presentation time.

### Accessing language support

- [languageCode](avmutablemovietrack/languagecode.md) — The language code of the track.
- [extendedLanguageTag](avmutablemovietrack/extendedlanguagetag.md) — The language tag of the track.

### Accessing visual characteristics

- [naturalSize](avmutablemovietrack/naturalsize.md) — The dimensions used to display the visual media data for the track.
- [preferredTransform](avmutablemovietrack/preferredtransform.md) — The transform performed on the visual media data of the track for display purposes.
- [layer](avmutablemovietrack/layer.md) — The layer level for the visual media of the track.
- [cleanApertureDimensions](avmutablemovietrack/cleanaperturedimensions.md) — The clean aperture dimension of the track.
- [productionApertureDimensions](avmutablemovietrack/productionaperturedimensions.md) — The production aperture dimensions of the track.
- [encodedPixelsDimensions](avmutablemovietrack/encodedpixelsdimensions.md) — The encoded pixels dimensions of the track.

### Accessing audible characteristics

- [preferredVolume](avmutablemovietrack/preferredvolume.md) — The preferred volume for the audible medata data of the track.
- [hasAudioSampleDependencies](avmutablemovietrack/hasaudiosampledependencies.md) — A Boolean value that indicates whether the track has sample dependencies.

### Accessing frame-based characteristics

- [nominalFrameRate](avmutablemovietrack/nominalframerate.md) — The frame rate of the track, in frames per second.
- [minFrameDuration](avmutablemovietrack/minframeduration.md) — The minimum duration of the track’s frames.
- [requiresFrameReordering](avmutablemovietrack/requiresframereordering.md) — A Boolean value that indicates whether samples in the track may have different presentation and decode timestamps.

### Accessing metadata

- [metadata](avmutablemovietrack/metadata.md) — An array of metadata stored by the track.
- [commonMetadata](avmutablemovietrack/commonmetadata.md) — An array of metadata items for all common metadata keys that have a value.
- [availableMetadataFormats](avmutablemovietrack/availablemetadataformats.md) — An array of metadata formats available for the track.
- [- metadataForFormat:](<avmutablemovietrack/metadata(forformat_).md>) — Returns metadata items that a track contains for the specified format.

### Accessing track segments

- [segments](avmutablemovietrack/segments.md) — The time mappings from the track’s media samples to its timeline.
- [- segmentForTrackTime:](<avmutablemovietrack/segment(fortracktime_).md>) — Returns a segment whose target time range contains, or is closest to, the specified track time.

### Managing track associations

- [availableTrackAssociationTypes](avmutablemovietrack/availabletrackassociationtypes.md) — An array of association types that the track uses to associate with other tracks.
- [- associatedTracksOfType:](<avmutablemovietrack/associatedtracks(oftype_).md>) — Returns an array of associated tracks that have the specified association type.
- [- addTrackAssociationToTrack:type:](<avmutablemovietrack/addtrackassociation(to_type_).md>) — Creates a specific type of track association between two tracks.
- [- removeTrackAssociationToTrack:type:](<avmutablemovietrack/removetrackassociation(to_type_).md>) — Removes a specific type of track association between two tracks.

### Determining sample cursor support

- [canProvideSampleCursors](avmutablemovietrack/canprovidesamplecursors.md) — A Boolean value that indicates whether the track can provide instances of sample cursors to traverse its media samples and discover information.

## See Also

### Mutable movies

- [AVMutableMovie](avmutablemovie.md) — A mutable object that represents an audiovisual container that conforms to the QuickTime movie file format or a related format like MPEG-4.
