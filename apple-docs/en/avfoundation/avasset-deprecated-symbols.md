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
doc_path: /documentation/avfoundation/avasset-deprecated-symbols
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset-deprecated-symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset-deprecated-symbols.json'
content_hash: 'sha256:7b3c08d57bed415a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Media assets](media-assets.md) · [AVAsset](avasset.md)

# Deprecated symbols

<sub>API Collection</sub>

Review unsupported symbols and their replacements.

## Overview

[AVAsset](avasset.md) doesn’t support using its synchronous property accessors that can block the calling thread. Instead, use the [load(_:isolation:)](<avasynchronouskeyvalueloading/load(__isolation_).md>) method to load [AVAsyncProperty](avasyncproperty.md) values asynchronously.

## Topics

### Accessing duration and timing

- [duration](avasset/duration.md) — A time value that indicates the asset’s duration. _(deprecated)_
- [providesPreciseDurationAndTiming](avasset/providesprecisedurationandtiming.md) — A Boolean value that indicates whether the asset provides precise duration and timing. _(deprecated)_
- [minimumTimeOffsetFromLive](avasset/minimumtimeoffsetfromlive.md) — A time value that indicates how closely playback follows the latest live stream content. _(deprecated)_

### Accessing tracks

- [tracks](avasset/tracks.md) — The tracks an asset contains. _(deprecated)_
- [- trackWithTrackID:](<avasset/track(withtrackid_).md>) — Returns a track that contains the specified identifier. _(deprecated)_
- [- tracksWithMediaType:](<avasset/tracks(withmediatype_).md>) — Returns tracks that contain media of a specified type. _(deprecated)_
- [- tracksWithMediaCharacteristic:](<avasset/tracks(withmediacharacteristic_).md>) — Returns an array of asset tracks matching the specified media characteristic. _(deprecated)_
- [- unusedTrackID](<avasset/unusedtrackid().md>) — Returns an identifier that no other tracks in the asset use. _(deprecated)_

### Accessing track groups

- [trackGroups](avasset/trackgroups.md) — The track groups an asset contains. _(deprecated)_

### Accessing metadata

- [metadata](avasset/metadata.md) — An array of metadata items for all metadata identifiers for which a value is available. _(deprecated)_
- [commonMetadata](avasset/commonmetadata.md) — The metadata items an asset contains for common metadata identifiers that provide a value. _(deprecated)_
- [availableMetadataFormats](avasset/availablemetadataformats.md) — The metadata formats this asset contains. _(deprecated)_
- [- metadataForFormat:](<avasset/metadata(forformat_).md>) — Returns an array of metadata items from the container with the specified format. _(deprecated)_
- [creationDate](avasset/creationdate.md) — A metadata item that indicates the asset’s creation date. _(deprecated)_
- [lyrics](avasset/lyrics.md) — The lyrics of the asset in a language suitable for the current locale. _(deprecated)_

### Accessing suitability

- [playable](avasset/isplayable.md) — A Boolean value that indicates whether the asset has playable content. _(deprecated)_
- [exportable](avasset/isexportable.md) — A Boolean value that indicates whether you can export this asset using an export session. _(deprecated)_
- [readable](avasset/isreadable.md) — A Boolean value that indicates whether you can extract the asset’s media data using an asset reader. _(deprecated)_
- [composable](avasset/iscomposable.md) — A Boolean value that indicates whether you can use the asset as a segment of a composition track. _(deprecated)_
- [compatibleWithAirPlayVideo](avasset/iscompatiblewithairplayvideo.md) — A Boolean value that indicates whether the asset is compatible with AirPlay Video. _(deprecated)_
- [compatibleWithSavedPhotosAlbum](avasset/iscompatiblewithsavedphotosalbum.md) — A Boolean value that indicates whether you can write the asset to the Saved Photos album. _(deprecated)_

### Accessing asset preferences

- [preferredRate](avasset/preferredrate.md) — The asset’s rate preference for playing its media. _(deprecated)_
- [preferredVolume](avasset/preferredvolume.md) — The asset’s volume preference for playing its audible media. _(deprecated)_
- [preferredTransform](avasset/preferredtransform.md) — The asset’s transform preference to apply to its visual content during presentation or processing. _(deprecated)_
- [preferredDisplayCriteria](avasset/preferreddisplaycriteria.md) — The asset’s display mode preference for optimal playback of its content. _(deprecated)_
- [preferredMediaSelection](avasset/preferredmediaselection.md) — The default media selections for this asset’s media selection groups. _(deprecated)_

### Accessing media selections

- [allMediaSelections](avasset/allmediaselections.md) — The array of available media selections for this asset. _(deprecated)_
- [availableMediaCharacteristicsWithMediaSelectionOptions](avasset/availablemediacharacteristicswithmediaselectionoptions.md) — An array of media characteristics for which a media selection option is available. _(deprecated)_
- [- mediaSelectionGroupForMediaCharacteristic:](<avasset/mediaselectiongroup(formediacharacteristic_).md>) — Returns a media selection group that contains one or more options with the specified media characteristic. _(deprecated)_

### Accessing chapter metadata

- [availableChapterLocales](avasset/availablechapterlocales.md) — The locales of the asset’s chapter metadata. _(deprecated)_
- [- chapterMetadataGroupsWithTitleLocale:containingItemsWithCommonKeys:](<avasset/chaptermetadatagroups(withtitlelocale_containingitemswithcommonkeys_).md>) — Returns an array of chapters that contain the specified title locale and common keys. _(deprecated)_
- [- chapterMetadataGroupsBestMatchingPreferredLanguages:](<avasset/chaptermetadatagroups(bestmatchingpreferredlanguages_).md>) — Returns an array of chapters with a locale that best matches the list of preferred languages. _(deprecated)_

### Accessing content protections

- [hasProtectedContent](avasset/hasprotectedcontent.md) — A Boolean value that indicates whether the asset contains protected content. _(deprecated)_

### Accessing fragment support

- [canContainFragments](avasset/cancontainfragments.md) — A Boolean value that indicates whether you can extend the asset by fragments. _(deprecated)_
- [containsFragments](avasset/containsfragments.md) — A Boolean value that indicates whether at least one movie fragment extends the asset. _(deprecated)_
- [overallDurationHint](avasset/overalldurationhint.md) — The total duration of fragments that currently exist, or may exist in the future. _(deprecated)_

### Inspecting visual attributes

- [naturalSize](avasset/naturalsize.md) — The encoded or authored size of the visual portion of the asset. _(deprecated)_
