---
title: AVAssetTrack
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassettrack-async-properties
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack-async-properties'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack-async-properties.json'
content_hash: 'sha256:e07ae082b067741f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Media assets](media-assets.md) · [AVPartialAsyncProperty](avpartialasyncproperty.md)

# AVAssetTrack

<sub>API Collection</sub>

Asynchronous properties for asset tracks.

## Topics

### Loading track information

- [totalSampleDataLength](avpartialasyncproperty/totalsampledatalength.md) — The total number of bytes of sample data the track requires.
- [formatDescriptions](avpartialasyncproperty/formatdescriptions.md) — The format descriptions of the media samples that a track references.
- [isDecodable](avpartialasyncproperty/isdecodable.md) — A Boolean value that indicates whether the track is decodable in the current environment.
- [isEnabled](avpartialasyncproperty/isenabled.md) — A Boolean value that indicates whether the track is in an enabled state.
- [isPlayable](avpartialasyncproperty/isplayable-6txa5.md) — A Boolean value that indicates whether the track is playable in the current environment.
- [mediaCharacteristics](avpartialasyncproperty/mediacharacteristics.md) — The media characteristics for the track.
- [isSelfContained](avpartialasyncproperty/isselfcontained.md) — A Boolean value that indicates whether the track references sample data only within its container file.

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
- [availableMetadataFormats](avpartialasyncproperty/availablemetadataformats-5p9xg.md) — An array of metadata formats available for the track.
- [commonMetadata](avpartialasyncproperty/commonmetadata-73m58.md) — An array of metadata items for all common metadata keys that have a value.

### Loading track segments

- [segments](avpartialasyncproperty/segments.md) — The time mappings from the track’s media samples to its timeline.

### Loading track associations

- [availableTrackAssociationTypes](avpartialasyncproperty/availabletrackassociationtypes.md) — An array of association types that the track uses to associate with other tracks.

### Creating sample cursors

- [canProvideSampleCursors](avpartialasyncproperty/canprovidesamplecursors.md) — A Boolean value that indicates whether the track can provide instances of sample cursors to traverse its media samples and discover information.

## See Also

### Loading properties

- [AVAsset](avasset-async-properties.md) — Asynchronous properties for assets.
- [AVURLAsset](avurlasset-async-properties.md) — Asynchronous properties for URL assets.
- [AVFragmentedAsset](avfragmentedasset-async-properties.md) — Asynchronous properties for fragmented assets.
- [AVMetadataItem](avmetadataitem-async-properties.md) — Asynchronous properties for metadata items.
- [AVComposition](avcomposition-async-properties.md) — Asynchronous properties for compositions.
- [AVMutableComposition](avmutablecomposition-async-properties.md) — Asynchronous properties for mutable compositions.
- [AVMovie](avmovie-async-properties.md) — Asynchronous properties for movies.
- [AVMutableMovie](avmutablemovie-async-properties.md) — Asynchronous properties for mutable movies.
- [AVFragmentedMovie](avfragmentedmovie-async-properties.md) — Asynchronous properties for fragmented movies.
