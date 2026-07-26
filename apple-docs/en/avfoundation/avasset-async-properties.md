---
title: AVAsset
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avasset-async-properties
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset-async-properties'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset-async-properties.json'
content_hash: 'sha256:bfa7354340e584f0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Media assets](media-assets.md) · [AVPartialAsyncProperty](avpartialasyncproperty.md)

# AVAsset

<sub>API Collection</sub>

Asynchronous properties for assets.

## Topics

### Loading duration and timing

- [duration](avpartialasyncproperty/duration.md) — A time value that represents the duration of the asset.
- [providesPreciseDurationAndTiming](avpartialasyncproperty/providesprecisedurationandtiming.md) — A Boolean value that indicates whether the asset provides precise duration and timing.
- [minimumTimeOffsetFromLive](avpartialasyncproperty/minimumtimeoffsetfromlive.md) — A time value that indicates how closely playback follows the latest live stream content.

### Loading tracks

- [tracks](avpartialasyncproperty/tracks-48zyw.md) — The tracks of media that an asset contains.

### Loading track groups

- [trackGroups](avpartialasyncproperty/trackgroups.md) — The track groups an asset contains.

### Loading metadata

- [metadata](avpartialasyncproperty/metadata-16qej.md) — The metadata items that an asset contains for all metadata identifiers.
- [commonMetadata](avpartialasyncproperty/commonmetadata-3j3n4.md) — The metadata items that an asset contains for common metadata identifiers.
- [availableMetadataFormats](avpartialasyncproperty/availablemetadataformats-4yiq8.md) — The formats of metadata that an asset contains.
- [creationDate](avpartialasyncproperty/creationdate.md) — A metadata item that indicates the creation date of an asset.
- [lyrics](avpartialasyncproperty/lyrics.md) — The lyrics of the asset in a language suitable for the current locale.

### Loading suitability

- [isPlayable](avpartialasyncproperty/isplayable-45h5v.md) — A Boolean value that indicates whether an asset contains playable content.
- [isExportable](avpartialasyncproperty/isexportable.md) — A Boolean value that indicates whether you can export an asset using an export session.
- [isReadable](avpartialasyncproperty/isreadable.md) — A Boolean value that indicates whether you can extract the asset’s media data using an asset reader.
- [isComposable](avpartialasyncproperty/iscomposable.md) — A Boolean value that indicates whether you can use the asset in a media composition.
- [isCompatibleWithSavedPhotosAlbum](avpartialasyncproperty/iscompatiblewithsavedphotosalbum.md) — A Boolean value that indicates whether you can write the asset to the Saved Photos album.
- [isCompatibleWithAirPlayVideo](avpartialasyncproperty/iscompatiblewithairplayvideo.md) — A Boolean value that indicates whether the asset is compatible with AirPlay Video.

### Loading asset preferences

- [preferredRate](avpartialasyncproperty/preferredrate.md) — The asset’s rate preference for playing its media.
- [preferredTransform](avpartialasyncproperty/preferredtransform-80d13.md) — The asset’s transform preference to apply to its visual content during presentation or processing.
- [preferredVolume](avpartialasyncproperty/preferredvolume-20mb3.md) — The asset’s volume preference for playing its audible media.
- [preferredDisplayCriteria](avpartialasyncproperty/preferreddisplaycriteria.md) — The asset’s display mode preference for optimal playback of its content.

### Loading media selections

- [allMediaSelections](avpartialasyncproperty/allmediaselections.md) — The available media selections for an asset.
- [preferredMediaSelection](avpartialasyncproperty/preferredmediaselection.md) — The default media selections for the media selection groups of an asset.
- [availableMediaCharacteristicsWithMediaSelectionOptions](avpartialasyncproperty/availablemediacharacteristicswithmediaselectionoptions.md) — The media characteristics that provide media selection options.

### Loading chapter metadata

- [availableChapterLocales](avpartialasyncproperty/availablechapterlocales.md) — The locales of an asset’s chapter metadata.

### Loading content protections

- [hasProtectedContent](avpartialasyncproperty/hasprotectedcontent.md) — A Boolean value that indicates whether the asset contains protected content.

### Loading fragment support

- [canContainFragments](avpartialasyncproperty/cancontainfragments.md) — A Boolean value that indicates whether you can extend the asset by fragments.
- [containsFragments](avpartialasyncproperty/containsfragments.md) — A Boolean value that indicates whether at least one movie fragment extends the asset.
- [overallDurationHint](avpartialasyncproperty/overalldurationhint.md) — A hint to the total duration of fragments that currently exist or may exist in the future.

## See Also

### Loading properties

- [AVAssetTrack](avassettrack-async-properties.md) — Asynchronous properties for asset tracks.
- [AVURLAsset](avurlasset-async-properties.md) — Asynchronous properties for URL assets.
- [AVFragmentedAsset](avfragmentedasset-async-properties.md) — Asynchronous properties for fragmented assets.
- [AVMetadataItem](avmetadataitem-async-properties.md) — Asynchronous properties for metadata items.
- [AVComposition](avcomposition-async-properties.md) — Asynchronous properties for compositions.
- [AVMutableComposition](avmutablecomposition-async-properties.md) — Asynchronous properties for mutable compositions.
- [AVMovie](avmovie-async-properties.md) — Asynchronous properties for movies.
- [AVMutableMovie](avmutablemovie-async-properties.md) — Asynchronous properties for mutable movies.
- [AVFragmentedMovie](avfragmentedmovie-async-properties.md) — Asynchronous properties for fragmented movies.
