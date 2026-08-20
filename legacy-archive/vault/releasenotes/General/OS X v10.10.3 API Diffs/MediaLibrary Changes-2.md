---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/MediaLibrary.html
archived_at: '2026-07-18T02:52:33.701956Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# MediaLibrary Changes

## MediaLibrary

Removed MLMediaSourceType.valueAdded MLMediaGroup.iconImageAdded MLMediaObject.artworkImageAdded MLMediaSourceType.init(rawValue: UInt)Added MLPhotosAllPhotosAlbumTypeIdentifierAdded MLPhotosBurstGroupTypeIdentifierAdded MLPhotosFacesAlbumTypeIdentifierAdded MLPhotosFolderTypeIdentifierAdded MLPhotosSloMoGroupTypeIdentifierAdded MLPhotosTimelapseGroupTypeIdentifierAdded MLiTunesMusicVideosPlaylistTypeIdentifierAdded MLiTunesVideoPlaylistTypeIdentifierModified MLMediaGroup.URL

|  | Declaration |
| --- | --- |
| From | ``` var URL: NSURL! { get } ``` |
| To | ``` @NSCopying var URL: NSURL! { get } ``` |

Modified MLMediaGroup.mediaLibrary

|  | Declaration |
| --- | --- |
| From | ``` var mediaLibrary: MLMediaLibrary! { get } ``` |
| To | ``` unowned(unsafe) var mediaLibrary: MLMediaLibrary! { get } ``` |

Modified MLMediaGroup.modificationDate

|  | Declaration |
| --- | --- |
| From | ``` var modificationDate: NSDate! { get } ``` |
| To | ``` @NSCopying var modificationDate: NSDate! { get } ``` |

Modified MLMediaGroup.parent

|  | Declaration |
| --- | --- |
| From | ``` var parent: MLMediaGroup! { get } ``` |
| To | ``` unowned(unsafe) var parent: MLMediaGroup! { get } ``` |

Modified MLMediaLibrary.init(options: [NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(options options: [NSObject : AnyObject]!) ``` |
| To | ``` init!(options options: [NSObject : AnyObject]!) ``` |

Modified MLMediaObject.URL

|  | Declaration |
| --- | --- |
| From | ``` var URL: NSURL! { get } ``` |
| To | ``` @NSCopying var URL: NSURL! { get } ``` |

Modified MLMediaObject.mediaLibrary

|  | Declaration |
| --- | --- |
| From | ``` var mediaLibrary: MLMediaLibrary! { get } ``` |
| To | ``` unowned(unsafe) var mediaLibrary: MLMediaLibrary! { get } ``` |

Modified MLMediaObject.modificationDate

|  | Declaration |
| --- | --- |
| From | ``` var modificationDate: NSDate! { get } ``` |
| To | ``` @NSCopying var modificationDate: NSDate! { get } ``` |

Modified MLMediaObject.originalURL

|  | Declaration |
| --- | --- |
| From | ``` var originalURL: NSURL! { get } ``` |
| To | ``` @NSCopying var originalURL: NSURL! { get } ``` |

Modified MLMediaObject.thumbnailURL

|  | Declaration |
| --- | --- |
| From | ``` var thumbnailURL: NSURL! { get } ``` |
| To | ``` @NSCopying var thumbnailURL: NSURL! { get } ``` |

Modified MLMediaSource.mediaLibrary

|  | Declaration |
| --- | --- |
| From | ``` var mediaLibrary: MLMediaLibrary! { get } ``` |
| To | ``` unowned(unsafe) var mediaLibrary: MLMediaLibrary! { get } ``` |

Modified MLMediaSourceType [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct MLMediaSourceType : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var Audio: MLMediaSourceType { get }     static var Image: MLMediaSourceType { get }     static var Movie: MLMediaSourceType { get } } ``` | RawOptionSet |
| To | ``` struct MLMediaSourceType : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Audio: MLMediaSourceType { get }     static var Image: MLMediaSourceType { get }     static var Movie: MLMediaSourceType { get } } ``` | RawOptionSetType |

Modified MLMediaSourceType.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified MLApertureAllPhotosTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLApertureAllPhotosTypeIdentifier: NSString! ``` |
| To | ``` let MLApertureAllPhotosTypeIdentifier: String ``` |

Modified MLApertureAllProjectsTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLApertureAllProjectsTypeIdentifier: NSString! ``` |
| To | ``` let MLApertureAllProjectsTypeIdentifier: String ``` |

Modified MLApertureFacebookAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLApertureFacebookAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLApertureFacebookAlbumTypeIdentifier: String ``` |

Modified MLApertureFacebookGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLApertureFacebookGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLApertureFacebookGroupTypeIdentifier: String ``` |

Modified MLApertureFacesAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLApertureFacesAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLApertureFacesAlbumTypeIdentifier: String ``` |

Modified MLApertureFlaggedTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLApertureFlaggedTypeIdentifier: NSString! ``` |
| To | ``` let MLApertureFlaggedTypeIdentifier: String ``` |

Modified MLApertureFlickrAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLApertureFlickrAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLApertureFlickrAlbumTypeIdentifier: String ``` |

Modified MLApertureFlickrGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLApertureFlickrGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLApertureFlickrGroupTypeIdentifier: String ``` |

Modified MLApertureFolderAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLApertureFolderAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLApertureFolderAlbumTypeIdentifier: String ``` |

Modified MLApertureLastImportAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLApertureLastImportAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLApertureLastImportAlbumTypeIdentifier: String ``` |

Modified MLApertureLastNMonthsAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLApertureLastNMonthsAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLApertureLastNMonthsAlbumTypeIdentifier: String ``` |

Modified MLApertureLastViewedEventAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLApertureLastViewedEventAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLApertureLastViewedEventAlbumTypeIdentifier: String ``` |

Modified MLApertureLightTableTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLApertureLightTableTypeIdentifier: NSString! ``` |
| To | ``` let MLApertureLightTableTypeIdentifier: String ``` |

Modified MLAperturePhotoStreamAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLAperturePhotoStreamAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLAperturePhotoStreamAlbumTypeIdentifier: String ``` |

Modified MLAperturePlacesAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLAperturePlacesAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLAperturePlacesAlbumTypeIdentifier: String ``` |

Modified MLAperturePlacesCityAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLAperturePlacesCityAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLAperturePlacesCityAlbumTypeIdentifier: String ``` |

Modified MLAperturePlacesCountryAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLAperturePlacesCountryAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLAperturePlacesCountryAlbumTypeIdentifier: String ``` |

Modified MLAperturePlacesPointOfInterestAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLAperturePlacesPointOfInterestAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLAperturePlacesPointOfInterestAlbumTypeIdentifier: String ``` |

Modified MLAperturePlacesProvinceAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLAperturePlacesProvinceAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLAperturePlacesProvinceAlbumTypeIdentifier: String ``` |

Modified MLApertureProjectAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLApertureProjectAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLApertureProjectAlbumTypeIdentifier: String ``` |

Modified MLApertureProjectFolderAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLApertureProjectFolderAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLApertureProjectFolderAlbumTypeIdentifier: String ``` |

Modified MLApertureRootGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLApertureRootGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLApertureRootGroupTypeIdentifier: String ``` |

Modified MLApertureSlideShowTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLApertureSlideShowTypeIdentifier: NSString! ``` |
| To | ``` let MLApertureSlideShowTypeIdentifier: String ``` |

Modified MLApertureSmugMugAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLApertureSmugMugAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLApertureSmugMugAlbumTypeIdentifier: String ``` |

Modified MLApertureSmugMugGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLApertureSmugMugGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLApertureSmugMugGroupTypeIdentifier: String ``` |

Modified MLApertureUserAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLApertureUserAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLApertureUserAlbumTypeIdentifier: String ``` |

Modified MLApertureUserSmartAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLApertureUserSmartAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLApertureUserSmartAlbumTypeIdentifier: String ``` |

Modified MLFinalCutEventCalendarGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLFinalCutEventCalendarGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLFinalCutEventCalendarGroupTypeIdentifier: String ``` |

Modified MLFinalCutEventGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLFinalCutEventGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLFinalCutEventGroupTypeIdentifier: String ``` |

Modified MLFinalCutEventLibraryGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLFinalCutEventLibraryGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLFinalCutEventLibraryGroupTypeIdentifier: String ``` |

Modified MLFinalCutFolderGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLFinalCutFolderGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLFinalCutFolderGroupTypeIdentifier: String ``` |

Modified MLFinalCutProjectGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLFinalCutProjectGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLFinalCutProjectGroupTypeIdentifier: String ``` |

Modified MLFinalCutRootGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLFinalCutRootGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLFinalCutRootGroupTypeIdentifier: String ``` |

Modified MLFolderGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLFolderGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLFolderGroupTypeIdentifier: String ``` |

Modified MLFolderRootGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLFolderRootGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLFolderRootGroupTypeIdentifier: String ``` |

Modified MLGarageBandFolderGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLGarageBandFolderGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLGarageBandFolderGroupTypeIdentifier: String ``` |

Modified MLGarageBandRootGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLGarageBandRootGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLGarageBandRootGroupTypeIdentifier: String ``` |

Modified MLLogicBouncesGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLLogicBouncesGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLLogicBouncesGroupTypeIdentifier: String ``` |

Modified MLLogicProjectTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLLogicProjectTypeIdentifier: NSString! ``` |
| To | ``` let MLLogicProjectTypeIdentifier: String ``` |

Modified MLLogicProjectsGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLLogicProjectsGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLLogicProjectsGroupTypeIdentifier: String ``` |

Modified MLLogicRootGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLLogicRootGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLLogicRootGroupTypeIdentifier: String ``` |

Modified MLMediaLoadAppFoldersKey

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaLoadAppFoldersKey: NSString! ``` |
| To | ``` let MLMediaLoadAppFoldersKey: String ``` |

Modified MLMediaLoadAppleLoops

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaLoadAppleLoops: NSString! ``` |
| To | ``` let MLMediaLoadAppleLoops: String ``` |

Modified MLMediaLoadExcludeSourcesKey

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaLoadExcludeSourcesKey: NSString! ``` |
| To | ``` let MLMediaLoadExcludeSourcesKey: String ``` |

Modified MLMediaLoadFoldersKey

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaLoadFoldersKey: NSString! ``` |
| To | ``` let MLMediaLoadFoldersKey: String ``` |

Modified MLMediaLoadIncludeSourcesKey

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaLoadIncludeSourcesKey: NSString! ``` |
| To | ``` let MLMediaLoadIncludeSourcesKey: String ``` |

Modified MLMediaLoadMoviesFolder

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaLoadMoviesFolder: NSString! ``` |
| To | ``` let MLMediaLoadMoviesFolder: String ``` |

Modified MLMediaLoadSourceTypesKey

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaLoadSourceTypesKey: NSString! ``` |
| To | ``` let MLMediaLoadSourceTypesKey: String ``` |

Modified MLMediaObjectAlbumKey

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaObjectAlbumKey: NSString! ``` |
| To | ``` let MLMediaObjectAlbumKey: String ``` |

Modified MLMediaObjectArtistKey

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaObjectArtistKey: NSString! ``` |
| To | ``` let MLMediaObjectArtistKey: String ``` |

Modified MLMediaObjectBitRateKey

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaObjectBitRateKey: NSString! ``` |
| To | ``` let MLMediaObjectBitRateKey: String ``` |

Modified MLMediaObjectChannelCountKey

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaObjectChannelCountKey: NSString! ``` |
| To | ``` let MLMediaObjectChannelCountKey: String ``` |

Modified MLMediaObjectCommentsKey

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaObjectCommentsKey: NSString! ``` |
| To | ``` let MLMediaObjectCommentsKey: String ``` |

Modified MLMediaObjectDurationKey

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaObjectDurationKey: NSString! ``` |
| To | ``` let MLMediaObjectDurationKey: String ``` |

Modified MLMediaObjectGenreKey

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaObjectGenreKey: NSString! ``` |
| To | ``` let MLMediaObjectGenreKey: String ``` |

Modified MLMediaObjectKeywordsKey

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaObjectKeywordsKey: NSString! ``` |
| To | ``` let MLMediaObjectKeywordsKey: String ``` |

Modified MLMediaObjectKindKey

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaObjectKindKey: NSString! ``` |
| To | ``` let MLMediaObjectKindKey: String ``` |

Modified MLMediaObjectProtectedKey

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaObjectProtectedKey: NSString! ``` |
| To | ``` let MLMediaObjectProtectedKey: String ``` |

Modified MLMediaObjectResolutionStringKey

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaObjectResolutionStringKey: NSString! ``` |
| To | ``` let MLMediaObjectResolutionStringKey: String ``` |

Modified MLMediaObjectSampleRateKey

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaObjectSampleRateKey: NSString! ``` |
| To | ``` let MLMediaObjectSampleRateKey: String ``` |

Modified MLMediaObjectTrackNumberKey

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaObjectTrackNumberKey: NSString! ``` |
| To | ``` let MLMediaObjectTrackNumberKey: String ``` |

Modified MLMediaSourceApertureIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaSourceApertureIdentifier: NSString! ``` |
| To | ``` let MLMediaSourceApertureIdentifier: String ``` |

Modified MLMediaSourceAppDefinedFoldersIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaSourceAppDefinedFoldersIdentifier: NSString! ``` |
| To | ``` let MLMediaSourceAppDefinedFoldersIdentifier: String ``` |

Modified MLMediaSourceCustomFoldersIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaSourceCustomFoldersIdentifier: NSString! ``` |
| To | ``` let MLMediaSourceCustomFoldersIdentifier: String ``` |

Modified MLMediaSourceFinalCutIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaSourceFinalCutIdentifier: NSString! ``` |
| To | ``` let MLMediaSourceFinalCutIdentifier: String ``` |

Modified MLMediaSourceGarageBandIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaSourceGarageBandIdentifier: NSString! ``` |
| To | ``` let MLMediaSourceGarageBandIdentifier: String ``` |

Modified MLMediaSourceLogicIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaSourceLogicIdentifier: NSString! ``` |
| To | ``` let MLMediaSourceLogicIdentifier: String ``` |

Modified MLMediaSourceMoviesFolderIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaSourceMoviesFolderIdentifier: NSString! ``` |
| To | ``` let MLMediaSourceMoviesFolderIdentifier: String ``` |

Modified MLMediaSourcePhotoBoothIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaSourcePhotoBoothIdentifier: NSString! ``` |
| To | ``` let MLMediaSourcePhotoBoothIdentifier: String ``` |

Modified MLMediaSourcePhotosIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaSourcePhotosIdentifier: NSString! ``` |
| To | ``` let MLMediaSourcePhotosIdentifier: String ``` |

Modified MLMediaSourceiMovieIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaSourceiMovieIdentifier: NSString! ``` |
| To | ``` let MLMediaSourceiMovieIdentifier: String ``` |

Modified MLMediaSourceiPhotoIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaSourceiPhotoIdentifier: NSString! ``` |
| To | ``` let MLMediaSourceiPhotoIdentifier: String ``` |

Modified MLMediaSourceiTunesIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLMediaSourceiTunesIdentifier: NSString! ``` |
| To | ``` let MLMediaSourceiTunesIdentifier: String ``` |

Modified MLPhotosAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLPhotosAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLPhotosAlbumTypeIdentifier: String ``` |

Modified MLPhotosAlbumsGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLPhotosAlbumsGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLPhotosAlbumsGroupTypeIdentifier: String ``` |

Modified MLPhotosAllCollectionsGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLPhotosAllCollectionsGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLPhotosAllCollectionsGroupTypeIdentifier: String ``` |

Modified MLPhotosAllMomentsGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLPhotosAllMomentsGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLPhotosAllMomentsGroupTypeIdentifier: String ``` |

Modified MLPhotosAllYearsGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLPhotosAllYearsGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLPhotosAllYearsGroupTypeIdentifier: String ``` |

Modified MLPhotosCollectionGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLPhotosCollectionGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLPhotosCollectionGroupTypeIdentifier: String ``` |

Modified MLPhotosFavoritesGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLPhotosFavoritesGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLPhotosFavoritesGroupTypeIdentifier: String ``` |

Modified MLPhotosLastImportGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLPhotosLastImportGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLPhotosLastImportGroupTypeIdentifier: String ``` |

Modified MLPhotosMomentGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLPhotosMomentGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLPhotosMomentGroupTypeIdentifier: String ``` |

Modified MLPhotosMyPhotoStreamTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLPhotosMyPhotoStreamTypeIdentifier: NSString! ``` |
| To | ``` let MLPhotosMyPhotoStreamTypeIdentifier: String ``` |

Modified MLPhotosPanoramasGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLPhotosPanoramasGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLPhotosPanoramasGroupTypeIdentifier: String ``` |

Modified MLPhotosPublishedAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLPhotosPublishedAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLPhotosPublishedAlbumTypeIdentifier: String ``` |

Modified MLPhotosRootGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLPhotosRootGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLPhotosRootGroupTypeIdentifier: String ``` |

Modified MLPhotosSharedGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLPhotosSharedGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLPhotosSharedGroupTypeIdentifier: String ``` |

Modified MLPhotosSharedPhotoStreamTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLPhotosSharedPhotoStreamTypeIdentifier: NSString! ``` |
| To | ``` let MLPhotosSharedPhotoStreamTypeIdentifier: String ``` |

Modified MLPhotosSmartAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLPhotosSmartAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLPhotosSmartAlbumTypeIdentifier: String ``` |

Modified MLPhotosVideosGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLPhotosVideosGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLPhotosVideosGroupTypeIdentifier: String ``` |

Modified MLPhotosYearGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLPhotosYearGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLPhotosYearGroupTypeIdentifier: String ``` |

Modified MLiMovieEventCalendarGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiMovieEventCalendarGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLiMovieEventCalendarGroupTypeIdentifier: String ``` |

Modified MLiMovieEventGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiMovieEventGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLiMovieEventGroupTypeIdentifier: String ``` |

Modified MLiMovieEventLibraryGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiMovieEventLibraryGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLiMovieEventLibraryGroupTypeIdentifier: String ``` |

Modified MLiMovieFolderGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiMovieFolderGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLiMovieFolderGroupTypeIdentifier: String ``` |

Modified MLiMovieProjectGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiMovieProjectGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLiMovieProjectGroupTypeIdentifier: String ``` |

Modified MLiMovieRootGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiMovieRootGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLiMovieRootGroupTypeIdentifier: String ``` |

Modified MLiPhotoAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiPhotoAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLiPhotoAlbumTypeIdentifier: String ``` |

Modified MLiPhotoEventAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiPhotoEventAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLiPhotoEventAlbumTypeIdentifier: String ``` |

Modified MLiPhotoEventsFolderTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiPhotoEventsFolderTypeIdentifier: NSString! ``` |
| To | ``` let MLiPhotoEventsFolderTypeIdentifier: String ``` |

Modified MLiPhotoFacebookAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiPhotoFacebookAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLiPhotoFacebookAlbumTypeIdentifier: String ``` |

Modified MLiPhotoFacebookGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiPhotoFacebookGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLiPhotoFacebookGroupTypeIdentifier: String ``` |

Modified MLiPhotoFacesAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiPhotoFacesAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLiPhotoFacesAlbumTypeIdentifier: String ``` |

Modified MLiPhotoFlaggedAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiPhotoFlaggedAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLiPhotoFlaggedAlbumTypeIdentifier: String ``` |

Modified MLiPhotoFlickrAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiPhotoFlickrAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLiPhotoFlickrAlbumTypeIdentifier: String ``` |

Modified MLiPhotoFlickrGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiPhotoFlickrGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLiPhotoFlickrGroupTypeIdentifier: String ``` |

Modified MLiPhotoFolderAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiPhotoFolderAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLiPhotoFolderAlbumTypeIdentifier: String ``` |

Modified MLiPhotoLastImportAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiPhotoLastImportAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLiPhotoLastImportAlbumTypeIdentifier: String ``` |

Modified MLiPhotoLastNMonthsAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiPhotoLastNMonthsAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLiPhotoLastNMonthsAlbumTypeIdentifier: String ``` |

Modified MLiPhotoLastViewedEventAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiPhotoLastViewedEventAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLiPhotoLastViewedEventAlbumTypeIdentifier: String ``` |

Modified MLiPhotoLibraryAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiPhotoLibraryAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLiPhotoLibraryAlbumTypeIdentifier: String ``` |

Modified MLiPhotoPhotoStreamAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiPhotoPhotoStreamAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLiPhotoPhotoStreamAlbumTypeIdentifier: String ``` |

Modified MLiPhotoPlacesAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiPhotoPlacesAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLiPhotoPlacesAlbumTypeIdentifier: String ``` |

Modified MLiPhotoPlacesCityAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiPhotoPlacesCityAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLiPhotoPlacesCityAlbumTypeIdentifier: String ``` |

Modified MLiPhotoPlacesCountryAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiPhotoPlacesCountryAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLiPhotoPlacesCountryAlbumTypeIdentifier: String ``` |

Modified MLiPhotoPlacesPointOfInterestAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiPhotoPlacesPointOfInterestAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLiPhotoPlacesPointOfInterestAlbumTypeIdentifier: String ``` |

Modified MLiPhotoPlacesProvinceAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiPhotoPlacesProvinceAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLiPhotoPlacesProvinceAlbumTypeIdentifier: String ``` |

Modified MLiPhotoRootGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiPhotoRootGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLiPhotoRootGroupTypeIdentifier: String ``` |

Modified MLiPhotoSlideShowAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiPhotoSlideShowAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLiPhotoSlideShowAlbumTypeIdentifier: String ``` |

Modified MLiPhotoSmartAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiPhotoSmartAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLiPhotoSmartAlbumTypeIdentifier: String ``` |

Modified MLiPhotoSubscribedAlbumTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiPhotoSubscribedAlbumTypeIdentifier: NSString! ``` |
| To | ``` let MLiPhotoSubscribedAlbumTypeIdentifier: String ``` |

Modified MLiTunesAudioBooksPlaylistTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiTunesAudioBooksPlaylistTypeIdentifier: NSString! ``` |
| To | ``` let MLiTunesAudioBooksPlaylistTypeIdentifier: String ``` |

Modified MLiTunesFolderPlaylistTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiTunesFolderPlaylistTypeIdentifier: NSString! ``` |
| To | ``` let MLiTunesFolderPlaylistTypeIdentifier: String ``` |

Modified MLiTunesGeniusPlaylistTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiTunesGeniusPlaylistTypeIdentifier: NSString! ``` |
| To | ``` let MLiTunesGeniusPlaylistTypeIdentifier: String ``` |

Modified MLiTunesMoviesPlaylistTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiTunesMoviesPlaylistTypeIdentifier: NSString! ``` |
| To | ``` let MLiTunesMoviesPlaylistTypeIdentifier: String ``` |

Modified MLiTunesMusicPlaylistTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiTunesMusicPlaylistTypeIdentifier: NSString! ``` |
| To | ``` let MLiTunesMusicPlaylistTypeIdentifier: String ``` |

Modified MLiTunesPlaylistTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiTunesPlaylistTypeIdentifier: NSString! ``` |
| To | ``` let MLiTunesPlaylistTypeIdentifier: String ``` |

Modified MLiTunesPodcastPlaylistTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiTunesPodcastPlaylistTypeIdentifier: NSString! ``` |
| To | ``` let MLiTunesPodcastPlaylistTypeIdentifier: String ``` |

Modified MLiTunesPurchasedPlaylistTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiTunesPurchasedPlaylistTypeIdentifier: NSString! ``` |
| To | ``` let MLiTunesPurchasedPlaylistTypeIdentifier: String ``` |

Modified MLiTunesRootGroupTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiTunesRootGroupTypeIdentifier: NSString! ``` |
| To | ``` let MLiTunesRootGroupTypeIdentifier: String ``` |

Modified MLiTunesSavedGeniusPlaylistTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiTunesSavedGeniusPlaylistTypeIdentifier: NSString! ``` |
| To | ``` let MLiTunesSavedGeniusPlaylistTypeIdentifier: String ``` |

Modified MLiTunesSmartPlaylistTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiTunesSmartPlaylistTypeIdentifier: NSString! ``` |
| To | ``` let MLiTunesSmartPlaylistTypeIdentifier: String ``` |

Modified MLiTunesTVShowsPlaylistTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiTunesTVShowsPlaylistTypeIdentifier: NSString! ``` |
| To | ``` let MLiTunesTVShowsPlaylistTypeIdentifier: String ``` |

Modified MLiTunesiTunesUPlaylistTypeIdentifier

|  | Declaration |
| --- | --- |
| From | ``` let MLiTunesiTunesUPlaylistTypeIdentifier: NSString! ``` |
| To | ``` let MLiTunesiTunesUPlaylistTypeIdentifier: String ``` |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
