---
title: Media assets
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/media-assets
source_url: 'https://developer.apple.com/documentation/avfoundation/media-assets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/media-assets.json'
content_hash: 'sha256:6f88d0064b2fb40b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# Media assets

<sub>API Collection</sub>

Load media assets from files and streams to inspect their attributes, tracks, and embedded metadata.

## Topics

### Essentials

- [Loading media data asynchronously](loading-media-data-asynchronously.md) — Build responsive apps by using language-level concurrency features to efficiently load media data.

### Assets

- [AVAsset](avasset.md) — An object that models timed audiovisual media.
- [AVURLAsset](avurlasset.md) — An asset that represents media at a local or remote URL.
- [AVAssetTrack](avassettrack.md) — An object that models a track of media that an asset contains.
- [AVAssetTrackSegment](avassettracksegment.md) — An object that represents a time range segment of an asset track.
- [AVAssetTrackGroup](avassettrackgroup.md) — A group of related tracks in an asset.

### Metadata

- [Retrieving media metadata](retrieving-media-metadata.md) — Load descriptive metadata for media assets and their tracks.
- [AVMetadataItem](avmetadataitem.md) — A metadata item for an audiovisual asset or one of its tracks.
- [AVMutableMetadataItem](avmutablemetadataitem.md) — A mutable metadata item for an audiovisual asset or for one of its tracks.
- [AVMetadataIdentifier](avmetadataidentifier.md) — A structure that defines identifiers for metadata formats.
- [AVMetadataKey](avmetadatakey.md) — A structure that defines a metadata key.
- [AVMetadataKeySpace](avmetadatakeyspace.md) — A structure that defines a metadata key space.
- [AVMetadataExtraAttributeKey](avmetadataextraattributekey.md) — A structure that defines keys for extra metadata attributes.
- [AVMetadataFormat](avmetadataformat.md) — A structure that defines metadata formats.
- [AVMetadataItemFilter](avmetadataitemfilter.md) — An object that filters selected information from a metadata item.

### Property loading

- [AVAsynchronousKeyValueLoading](avasynchronouskeyvalueloading.md) — A protocol that defines the interface to load media data asynchronously.
- [AVAsyncProperty](avasyncproperty.md) — An asynchronous property that constrains its type and value.
- [AVPartialAsyncProperty](avpartialasyncproperty.md) — An asynchronous property that constrains its type.
- [AVAnyAsyncProperty](avanyasyncproperty.md) — A base class for asynchronous properties.

### Fragmented assets

- [AVFragmentedAsset](avfragmentedasset.md) — An asset with a duration that the system can extend without modifying its existing media data.
- [AVFragmentedAssetTrack](avfragmentedassettrack.md) — An object that provides the track-level interface to inspect a fragmented asset’s media tracks.
- [AVFragmentedAssetMinder](avfragmentedassetminder.md) — An object that periodically checks whether the system adds new fragments to a fragmented asset.
- [AVFragmentMinding](avfragmentminding.md) — A protocol that defines whether an asset supports fragment minding.

## See Also

### Common

- [Media reading and writing](media-reading-and-writing.md) — Read images from video, export to alternative formats, and perform sample-level reading and writing of media data.
- [Media types and utilities](media-types-and-utilities.md) — Identify the types of content and file formats that AVFoundation supports.
- [Video settings](video-settings.md) — Configure video processing settings using standard key and value constants.
- [Audio settings](audio-settings.md) — Configure audio processing settings using standard key and value constants.
