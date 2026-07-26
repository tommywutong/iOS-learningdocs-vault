---
title: PHAssetCollectionSubtype
framework: Photos
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetcollectionsubtype
source_url: 'https://developer.apple.com/documentation/photos/phassetcollectionsubtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetcollectionsubtype.json'
content_hash: 'sha256:cd0042d6c7b62185'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHAssetCollectionSubtype

<sub>Enumeration</sub>

Minor distinctions between kinds of asset collections, used by the [assetCollectionSubtype](phassetcollection/assetcollectionsubtype.md) property and the [+ fetchAssetCollectionsWithType:subtype:options:](<phassetcollection/fetchassetcollections(with_subtype_options_).md>) method.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum PHAssetCollectionSubtype
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### User Album Types

- [PHAssetCollectionSubtypeAlbumRegular](phassetcollectionsubtype/albumregular.md) — An album created in the Photos app.
- [PHAssetCollectionSubtypeAlbumSyncedEvent](phassetcollectionsubtype/albumsyncedevent.md) — An Event synced to the device from iPhoto.
- [PHAssetCollectionSubtypeAlbumSyncedFaces](phassetcollectionsubtype/albumsyncedfaces.md) — A Faces group synced to the device from iPhoto.
- [PHAssetCollectionSubtypeAlbumSyncedAlbum](phassetcollectionsubtype/albumsyncedalbum.md) — An album synced to the device from iPhoto.
- [PHAssetCollectionSubtypeAlbumImported](phassetcollectionsubtype/albumimported.md) — An album imported from a camera or external storage.

### Cloud Album Types

- [PHAssetCollectionSubtypeAlbumMyPhotoStream](phassetcollectionsubtype/albummyphotostream.md) — The user’s personal iCloud Photo Stream.
- [PHAssetCollectionSubtypeAlbumCloudShared](phassetcollectionsubtype/albumcloudshared.md) — An iCloud Shared Photo Stream.

### Smart Album Types

- [PHAssetCollectionSubtypeSmartAlbumAllHidden](phassetcollectionsubtype/smartalbumallhidden.md) — A Smart Album that groups all assets hidden from the Moments view in the Photos app.
- [PHAssetCollectionSubtypeSmartAlbumAnimated](phassetcollectionsubtype/smartalbumanimated.md) — A Smart Album that groups all image animation assets.
- [PHAssetCollectionSubtypeSmartAlbumBursts](phassetcollectionsubtype/smartalbumbursts.md) — A Smart Album that groups all burst photo sequences in the photo library.
- [PHAssetCollectionSubtypeSmartAlbumCinematic](phassetcollectionsubtype/smartalbumcinematic.md) — A Smart Album that groups all cinematic photo assets.
- [PHAssetCollectionSubtypeSmartAlbumDepthEffect](phassetcollectionsubtype/smartalbumdeptheffect.md) — A Smart Album that groups all images captured using the Depth Effect camera mode on compatible devices.
- [PHAssetCollectionSubtypeSmartAlbumFavorites](phassetcollectionsubtype/smartalbumfavorites.md) — A Smart Album that groups all assets that the user marks as favorites.
- [PHAssetCollectionSubtypeSmartAlbumGeneric](phassetcollectionsubtype/smartalbumgeneric.md) — A Smart Album without a more-specific subtype.
- [PHAssetCollectionSubtypeSmartAlbumLivePhotos](phassetcollectionsubtype/smartalbumlivephotos.md) — A Smart Album that groups all Live Photos assets.
- [PHAssetCollectionSubtypeSmartAlbumLongExposures](phassetcollectionsubtype/smartalbumlongexposures.md) — A Smart Album that groups all Live Photos assets where the Long Exposure variation is in an enabled state.
- [PHAssetCollectionSubtypeSmartAlbumPanoramas](phassetcollectionsubtype/smartalbumpanoramas.md) — A Smart Album that groups all panorama photos in the photo library.
- [PHAssetCollectionSubtypeSmartAlbumRAW](phassetcollectionsubtype/smartalbumraw.md) — A Smart Album that groups all RAW assets in the photo library.
- [PHAssetCollectionSubtypeSmartAlbumRecentlyAdded](phassetcollectionsubtype/smartalbumrecentlyadded.md) — A Smart Album that groups all recently added assets in the photo library.
- [PHAssetCollectionSubtypeSmartAlbumScreenshots](phassetcollectionsubtype/smartalbumscreenshots.md) — A Smart Album that groups all images captured using the device’s screenshot function.
- [PHAssetCollectionSubtypeSmartAlbumSelfPortraits](phassetcollectionsubtype/smartalbumselfportraits.md) — A Smart Album that groups all photos and videos captured using the device’s front-facing camera.
- [PHAssetCollectionSubtypeSmartAlbumSlomoVideos](phassetcollectionsubtype/smartalbumslomovideos.md) — A Smart Album that groups all Slow-Mo videos in the photo library.
- [PHAssetCollectionSubtypeSmartAlbumScreenRecordings](phassetcollectionsubtype/smartalbumscreenrecordings.md)
- [PHAssetCollectionSubtypeSmartAlbumSpatial](phassetcollectionsubtype/smartalbumspatial.md)
- [PHAssetCollectionSubtypeSmartAlbumTimelapses](phassetcollectionsubtype/smartalbumtimelapses.md) — A Smart Album that groups all time-lapse videos in the photo library.
- [PHAssetCollectionSubtypeSmartAlbumUnableToUpload](phassetcollectionsubtype/smartalbumunabletoupload.md) — A Smart Album that groups all assets that the system can’t upload to iCloud.
- [PHAssetCollectionSubtypeSmartAlbumUserLibrary](phassetcollectionsubtype/smartalbumuserlibrary.md) — A Smart Album that groups all assets that originate in the user’s own library (as opposed to assets from iCloud Shared Albums).
- [PHAssetCollectionSubtypeSmartAlbumVideos](phassetcollectionsubtype/smartalbumvideos.md) — A Smart Album that groups all video assets in the photo library.

### Wildcard Search

- [PHAssetCollectionSubtypeAny](phassetcollectionsubtype/any.md) — A bit mask representing all possible subtypes.

### Initializers

- [init(rawValue:)](<phassetcollectionsubtype/init(rawvalue_).md>)

## See Also

### Reading Asset Collection Metadata

- [assetCollectionType](phassetcollection/assetcollectiontype.md) — The type of the asset collection, such as an album or a moment.
- [PHAssetCollectionType](phassetcollectiontype.md) — Major distinctions between kinds of asset collections, used by the [assetCollectionType](phassetcollection/assetcollectiontype.md) property and the [+ fetchAssetCollectionsContainingAsset:withType:options:](<phassetcollection/fetchassetcollectionscontaining(__with_options_).md>) and [+ fetchAssetCollectionsWithType:subtype:options:](<phassetcollection/fetchassetcollections(with_subtype_options_).md>) methods.
- [assetCollectionSubtype](phassetcollection/assetcollectionsubtype.md) — The subtype of the asset collection.
- [estimatedAssetCount](phassetcollection/estimatedassetcount.md) — The estimated number of assets in the asset collection.
- [startDate](phassetcollection/startdate.md) — The earliest creation date among all assets in the asset collection.
- [endDate](phassetcollection/enddate.md) — The latest creation date among all assets in the asset collection.
- [approximateLocation](phassetcollection/approximatelocation.md) — A location representing those of all assets in the collection.
- [localizedLocationNames](phassetcollection/localizedlocationnames.md) — The names of locations grouped by the collection (an array of `NSString` objects).
