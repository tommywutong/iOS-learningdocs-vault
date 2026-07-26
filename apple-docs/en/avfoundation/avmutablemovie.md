---
title: AVMutableMovie
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.11+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablemovie
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovie'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovie.json'
content_hash: 'sha256:3a804b730c87fb1a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMutableMovie

<sub>Class</sub>

A mutable object that represents an audiovisual container that conforms to the QuickTime movie file format or a related format like MPEG-4.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
class AVMutableMovie
```

## Overview

This class is a mutable subclass of [AVMovie](avmovie.md) that provides methods that support movie editing. For example, you can use a mutable movie to copy media data from one track and paste it into another. You can also use this object to create track references from one track to another (for example, to set one track as a chapter track of another track). To perform editing operations on individual tracks, use the associated classes [AVMovieTrack](avmovietrack.md) and [AVMutableMovieTrack](avmutablemovietrack.md).

You use movie objects only when operating on format-specific features of a QuickTime or ISO base media file. You typically don’t use these classes to open and play QuickTime movie files or ISO base media files. Instead, you use [AVURLAsset](avurlasset.md) and [AVPlayerItem](avplayeritem.md).

When performing media insertions, a movie interleaves media data from tracks in the source asset to optimize the movie file for playback. However, performing a series of media insertions may result in a movie file that’s not optimally interleaved. You can optimize a movie file for playback by exporting it with an [AVAssetExportSession](avassetexportsession.md) object using the export preset [AVAssetExportPresetPassthrough](avassetexportpresetpassthrough.md), and setting the [shouldOptimizeForNetworkUse](avassetexportsession/shouldoptimizefornetworkuse.md) property value to [true](../swift/true.md).

## Relationships

- **Inherits From**: [AVMovie](avmovie.md)

- **Conforms To**: [AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a movie

- [- initWithURL:options:error:](<avmutablemovie/init(url_options_error_)-8rnnj.md>) — Creates a mutable movie object from a movie header stored in a QuickTime movie file of ISO base media file.
- [- initWithData:options:error:](<avmutablemovie/init(data_options_error_).md>) — Creates a mutable movie object from a movie stored in a data object.
- [- initWithSettingsFromMovie:options:error:](<avmutablemovie/init(settingsfrom_options_).md>) — Creates a mutable movie object without tracks.

### Configuring a movie

- [modified](avmutablemovie/ismodified.md) — A Boolean value that indicates whether the movie is in a modified state.
- [timescale](avmutablemovie/timescale.md) — The time scale of the movie.
- [interleavingPeriod](avmutablemovie/interleavingperiod.md) — A time period indicating the duration for interleaving runs of samples for each track.
- [defaultMediaDataStorage](avmutablemovie/defaultmediadatastorage.md) — The default storage container for media data that you add to a movie.

### Loading tracks

- [tracks](avpartialasyncproperty/tracks-2lj40.md) — The tracks that a movie contains.
- [- loadTrackWithTrackID:completionHandler:](<avmutablemovie/loadtrack(withtrackid_completionhandler_).md>) — Loads a track that contains the specified identifier.
- [- loadTracksWithMediaType:completionHandler:](<avmutablemovie/loadtracks(withmediatype_completionhandler_).md>) — Loads tracks that contain media of a specified type.
- [- loadTracksWithMediaCharacteristic:completionHandler:](<avmutablemovie/loadtracks(withmediacharacteristic_completionhandler_).md>) — Loads tracks that contain media of a specified characteristic.

### Accessing tracks

- [tracks](avmutablemovie/tracks.md) — The tracks that a movie contains.
- [- trackWithTrackID:](<avmutablemovie/track(withtrackid_).md>) — Retrieves a track in the movie that contains the specified identifier.
- [- tracksWithMediaType:](<avmutablemovie/tracks(withmediatype_).md>) — Retrieves tracks in the movie that present media of the specified type.
- [- tracksWithMediaCharacteristic:](<avmutablemovie/tracks(withmediacharacteristic_).md>) — Retrieve tracks in the movie that present media of the specified characteristic.
- [- unusedTrackID](<avmutablemovie/unusedtrackid().md>) — Returns an identifier that no other tracks in the asset use.

### Accessing track groups

- [trackGroups](avmutablemovie/trackgroups.md) — The track groups an asset contains.

### Managing tracks

- [- mutableTrackCompatibleWithTrack:](<avmutablemovie/mutabletrack(compatiblewith_).md>) — Provides a reference to a track from a mutable movie into which you can insert any time range.
- [- addMutableTrackWithMediaType:copySettingsFromTrack:options:](<avmutablemovie/addmutabletrack(withmediatype_copysettingsfrom_options_).md>) — Adds an empty track to the target movie.
- [- addMutableTracksCopyingSettingsFromTracks:options:](<avmutablemovie/addmutabletrackscopyingsettings(from_options_).md>) — Adds one or more empty tracks to the target movie and copies the track settings from the source tracks.
- [- removeTrack:](<avmutablemovie/removetrack(__).md>) — Removes the specified track from the target movie.

### Managing time ranges

- [- insertEmptyTimeRange:](<avmutablemovie/insertemptytimerange(__).md>) — Adds an empty time range to a movie.
- [- insertTimeRange:ofAsset:atTime:copySampleData:error:](<avmutablemovie/inserttimerange(__of_at_copysampledata_).md>) — Inserts all of the tracks in a specified time range of an asset into a movie.
- [- scaleTimeRange:toDuration:](<avmutablemovie/scale(__toduration_).md>) — Changes the duration of a time range in a movie.
- [- removeTimeRange:](<avmutablemovie/removetimerange(__).md>) — Removes the specified time range from a movie.

### Accessing duration and timing

- [duration](avmutablemovie/duration.md) — A time value that indicates the asset’s duration.
- [providesPreciseDurationAndTiming](avmutablemovie/providesprecisedurationandtiming.md) — A Boolean value that indicates whether the asset provides precise duration and timing.
- [minimumTimeOffsetFromLive](avmutablemovie/minimumtimeoffsetfromlive.md) — A time value that indicates how closely playback follows the latest live stream content.

### Accessing metadata

- [metadata](avmutablemovie/metadata.md) — An array of metadata items for all metadata identifiers for which a value is available.
- [commonMetadata](avmutablemovie/commonmetadata.md) — The metadata items an asset contains for common metadata identifiers that provide a value.
- [availableMetadataFormats](avmutablemovie/availablemetadataformats.md) — The metadata formats this asset contains.
- [- metadataForFormat:](<avmutablemovie/metadata(forformat_).md>) — Returns an array of metadata items from the container with the specified format.
- [creationDate](avmutablemovie/creationdate.md) — A metadata item that indicates the asset’s creation date.
- [lyrics](avmutablemovie/lyrics.md) — The lyrics of the asset in a language suitable for the current locale.

### Determining suitability

- [isPlayable](avmutablemovie/isplayable.md) — A Boolean value that indicates whether the asset has playable content.
- [isReadable](avmutablemovie/isreadable.md) — A Boolean value that indicates whether you can extract the asset’s media data using an asset reader.
- [isExportable](avmutablemovie/isexportable.md) — A Boolean value that indicates whether you can export this asset using an export session.
- [isComposable](avmutablemovie/iscomposable.md) — A Boolean value that indicates whether you can use the asset as a segment of a composition track.
- [isCompatibleWithAirPlayVideo](avmutablemovie/iscompatiblewithairplayvideo.md) — A Boolean value that indicates whether the asset is compatible with AirPlay Video.
- [isCompatibleWithSavedPhotosAlbum](avmutablemovie/iscompatiblewithsavedphotosalbum.md) — A Boolean value that indicates whether you can write the composition to the Saved Photos album.

### Inspecting preferences

- [preferredRate](avmutablemovie/preferredrate.md) — The asset’s rate preference for playing its media.
- [preferredVolume](avmutablemovie/preferredvolume.md) — The asset’s volume preference for playing its audible media.
- [preferredTransform](avmutablemovie/preferredtransform.md) — The asset’s transform preference to apply to its visual content during presentation or processing.
- [preferredMediaSelection](avmutablemovie/preferredmediaselection.md) — The default media selections for this asset’s media selection groups.

### Accessing media selections

- [allMediaSelections](avmutablemovie/allmediaselections.md) — The array of available media selections for this asset.
- [availableMediaCharacteristicsWithMediaSelectionOptions](avmutablemovie/availablemediacharacteristicswithmediaselectionoptions.md) — An array of media characteristics for which a media selection option is available.
- [- mediaSelectionGroupForMediaCharacteristic:](<avmutablemovie/mediaselectiongroup(formediacharacteristic_).md>) — Returns a media selection group that contains one or more options with the specified media characteristic.

### Accessing chapter metadata

- [availableChapterLocales](avmutablemovie/availablechapterlocales.md) — The locales of the asset’s chapter metadata.
- [- chapterMetadataGroupsBestMatchingPreferredLanguages:](<avmutablemovie/chaptermetadatagroups(bestmatchingpreferredlanguages_).md>) — Returns an array of chapters with a locale that best matches the list of preferred languages.
- [- chapterMetadataGroupsWithTitleLocale:containingItemsWithCommonKeys:](<avmutablemovie/chaptermetadatagroups(withtitlelocale_containingitemswithcommonkeys_).md>) — Returns an array of chapters that contain the specified title locale and common keys.

### Determining content protections

- [hasProtectedContent](avmutablemovie/hasprotectedcontent.md) — A Boolean value that indicates whether the asset contains protected content.

### Determining fragment support

- [canContainFragments](avmutablemovie/cancontainfragments.md) — A Boolean value that indicates whether you can extend the asset by fragments.
- [containsFragments](avmutablemovie/containsfragments.md) — A Boolean value that indicates whether at least one movie fragment extends the asset.
- [overallDurationHint](avmutablemovie/overalldurationhint.md) — The total duration of fragments that currently exist, or may exist in the future.

### Initializers

- [init(URL:options:error:)](<avmutablemovie/init(url_options_error_)-1scrb.md>)
- [init(URL:options:error:)](<avmutablemovie/init(url_options_error_)-9is91.md>)
- [init(data:options:)](<avmutablemovie/init(data_options_).md>)
- [init(settingsFromMovie:options:)](<avmutablemovie/init(settingsfrommovie_options_)-1soot.md>)
- [init(settingsFromMovie:options:)](<avmutablemovie/init(settingsfrommovie_options_)-6p8zv.md>)

## See Also

### Mutable movies

- [AVMutableMovieTrack](avmutablemovietrack.md) — A mutable track that conforms to the QuickTime or ISO base media file format.
