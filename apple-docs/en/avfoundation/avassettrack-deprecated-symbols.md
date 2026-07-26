---
title: Deprecated symbols
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassettrack-deprecated-symbols
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack-deprecated-symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack-deprecated-symbols.json'
content_hash: 'sha256:d4324580c143d85d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Media assets](media-assets.md) · [AVAssetTrack](avassettrack.md)

# Deprecated symbols

<sub>API Collection</sub>

Review unsupported symbols and their replacements.

## Overview

[AVAssetTrack](avassettrack.md) doesn’t support using its synchronous property accessors that can block the calling thread. Instead, use the [load(_:isolation:)](<avasynchronouskeyvalueloading/load(__isolation_).md>) method to load [AVAsyncProperty](avasyncproperty.md) values asynchronously.

## Topics

### Accessing track information

- [formatDescriptions](avassettrack/formatdescriptions.md) — The format descriptions of the media samples that a track references. _(deprecated)_
- [playable](avassettrack/isplayable.md) — A Boolean value that indicates whether the track is playable in the current environment. _(deprecated)_
- [decodable](avassettrack/isdecodable.md) — A Boolean value that indicates whether the track is decodable in the current environment. _(deprecated)_
- [enabled](avassettrack/isenabled.md) — A Boolean value that indicates whether the track’s container enables it. _(deprecated)_
- [selfContained](avassettrack/isselfcontained.md) — A Boolean value that indicates whether this track references sample data only within its container file. _(deprecated)_
- [totalSampleDataLength](avassettrack/totalsampledatalength.md) — The total number of bytes of sample data the track requires. _(deprecated)_
- [- hasMediaCharacteristic:](<avassettrack/hasmediacharacteristic(__).md>) — Returns a Boolean value that indicates whether the track references media with the specified media characteristic. _(deprecated)_

### Accessing temporal information

- [timeRange](avassettrack/timerange.md) — The time range of the track within the overall timeline of the asset. _(deprecated)_
- [naturalTimeScale](avassettrack/naturaltimescale.md) — The natural time scale of the media that a track references. _(deprecated)_
- [estimatedDataRate](avassettrack/estimateddatarate.md) — The estimated data rate, in bits per second, of the media that the track references. _(deprecated)_

### Accessing language support

- [languageCode](avassettrack/languagecode.md) — The language code of the track. _(deprecated)_
- [extendedLanguageTag](avassettrack/extendedlanguagetag.md) — The language tag of the track. _(deprecated)_

### Accessing visual characteristics

- [naturalSize](avassettrack/naturalsize.md) — The natural dimensions of the media data that the track references. _(deprecated)_
- [preferredTransform](avassettrack/preferredtransform.md) — The track’s transform preference to apply to its visual content during presentation or processing. _(deprecated)_

### Accessing audible characteristics

- [preferredVolume](avassettrack/preferredvolume.md) — The track’s volume preference for playing its audible media. _(deprecated)_
- [hasAudioSampleDependencies](avassettrack/hasaudiosampledependencies.md) — A Boolean value that indicates whether the track has sample dependencies. _(deprecated)_

### Accessing frame-based characteristics

- [nominalFrameRate](avassettrack/nominalframerate.md) — The frame rate of the track, in frames per second. _(deprecated)_
- [minFrameDuration](avassettrack/minframeduration.md) — The minimum duration of the track’s frames. _(deprecated)_
- [requiresFrameReordering](avassettrack/requiresframereordering.md) — A Boolean value that indicates whether samples in the track may have different presentation and decode timestamps. _(deprecated)_

### Accessing metadata

- [metadata](avassettrack/metadata.md) — An array of metadata items for all metadata identifiers that have a value. _(deprecated)_
- [commonMetadata](avassettrack/commonmetadata.md) — An array of metadata items for all common metadata keys that have a value. _(deprecated)_
- [availableMetadataFormats](avassettrack/availablemetadataformats.md) — An array of metadata formats available for the track. _(deprecated)_
- [- metadataForFormat:](<avassettrack/metadata(forformat_).md>) — Returns metadata items that a track contains for the specified format. _(deprecated)_

### Accessing track segments

- [segments](avassettrack/segments.md) — The time mappings from the track’s media samples to its timeline. _(deprecated)_
- [- segmentForTrackTime:](<avassettrack/segment(fortracktime_).md>) — Retrieves a segment with a target time range that contains, or is closest to, the specified track time. _(deprecated)_
- [- samplePresentationTimeForTrackTime:](<avassettrack/samplepresentationtime(fortracktime_).md>) — Maps the specified track time through the appropriate time mapping and returns the resulting sample presentation time. _(deprecated)_

### Accessing track associations

- [availableTrackAssociationTypes](avassettrack/availabletrackassociationtypes.md) — An array of association types that the track uses to associate with other tracks. _(deprecated)_
- [- associatedTracksOfType:](<avassettrack/associatedtracks(oftype_).md>) — Returns an array of associated tracks that have the specified association type. _(deprecated)_

### Creating sample cursors

- [canProvideSampleCursors](avassettrack/canprovidesamplecursors.md) — A Boolean value that indicates whether the track can provide instances of sample cursors to traverse its media samples and discover information. _(deprecated)_
