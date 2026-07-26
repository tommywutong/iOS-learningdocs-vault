---
title: PHAssetCollectionSubtype.smartAlbumAllHidden
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetcollectionsubtype/smartalbumallhidden
source_url: 'https://developer.apple.com/documentation/photos/phassetcollectionsubtype/smartalbumallhidden'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetcollectionsubtype/smartalbumallhidden.json'
content_hash: 'sha256:8f9f7d1a45b98ff4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetCollectionSubtype](../phassetcollectionsubtype.md)

# PHAssetCollectionSubtype.smartAlbumAllHidden

<sub>Case</sub>

A Smart Album that groups all assets hidden from the Moments view in the Photos app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case smartAlbumAllHidden
```

## Discussion

Hidden assets have an [hidden](../phasset/ishidden.md) value of `true` and the system doesn’t return them through a fetch request, by default. Hide or show an asset by setting the [hidden](../phassetchangerequest/ishidden.md) property of a [PHAssetChangeRequest](../phassetchangerequest.md) object.

Beginning with iOS 16, users can require authentication to view the hidden Smart Album, and the user setting is `true` by default. When `true`, the system returns an empty Smart Album.

## See Also

### Smart Album Types

- [PHAssetCollectionSubtypeSmartAlbumAnimated](smartalbumanimated.md) — A Smart Album that groups all image animation assets.
- [PHAssetCollectionSubtypeSmartAlbumBursts](smartalbumbursts.md) — A Smart Album that groups all burst photo sequences in the photo library.
- [PHAssetCollectionSubtypeSmartAlbumCinematic](smartalbumcinematic.md) — A Smart Album that groups all cinematic photo assets.
- [PHAssetCollectionSubtypeSmartAlbumDepthEffect](smartalbumdeptheffect.md) — A Smart Album that groups all images captured using the Depth Effect camera mode on compatible devices.
- [PHAssetCollectionSubtypeSmartAlbumFavorites](smartalbumfavorites.md) — A Smart Album that groups all assets that the user marks as favorites.
- [PHAssetCollectionSubtypeSmartAlbumGeneric](smartalbumgeneric.md) — A Smart Album without a more-specific subtype.
- [PHAssetCollectionSubtypeSmartAlbumLivePhotos](smartalbumlivephotos.md) — A Smart Album that groups all Live Photos assets.
- [PHAssetCollectionSubtypeSmartAlbumLongExposures](smartalbumlongexposures.md) — A Smart Album that groups all Live Photos assets where the Long Exposure variation is in an enabled state.
- [PHAssetCollectionSubtypeSmartAlbumPanoramas](smartalbumpanoramas.md) — A Smart Album that groups all panorama photos in the photo library.
- [PHAssetCollectionSubtypeSmartAlbumRAW](smartalbumraw.md) — A Smart Album that groups all RAW assets in the photo library.
- [PHAssetCollectionSubtypeSmartAlbumRecentlyAdded](smartalbumrecentlyadded.md) — A Smart Album that groups all recently added assets in the photo library.
- [PHAssetCollectionSubtypeSmartAlbumScreenshots](smartalbumscreenshots.md) — A Smart Album that groups all images captured using the device’s screenshot function.
- [PHAssetCollectionSubtypeSmartAlbumSelfPortraits](smartalbumselfportraits.md) — A Smart Album that groups all photos and videos captured using the device’s front-facing camera.
- [PHAssetCollectionSubtypeSmartAlbumSlomoVideos](smartalbumslomovideos.md) — A Smart Album that groups all Slow-Mo videos in the photo library.
- [PHAssetCollectionSubtypeSmartAlbumScreenRecordings](smartalbumscreenrecordings.md)
