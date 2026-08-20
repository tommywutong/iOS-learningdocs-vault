---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/MediaLibrary.html
archived_at: '2026-07-15T07:34:46.831072Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# MediaLibrary Changes

## MediaLibrary

MLMediaLibrary.hAdded [MLMediaSourcePhotosIdentifier](https://developer.apple.com/documentation/medialibrary/mlmediasourcephotosidentifier)Modified [-[MLMediaLibrary initWithOptions:]](https://developer.apple.com/documentation/medialibrary/mlmedialibrary/1418988-initwithoptions)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithOptions:(NSDictionary *)options ``` | -- |
| To | ``` - (instancetype)initWithOptions:(NSDictionary *)options ``` | yes |

MLMediaTypes.hAdded [MLPhotosAlbumTypeIdentifier](https://developer.apple.com/documentation/medialibrary/mlphotosalbumtypeidentifier)Added [MLPhotosAlbumsGroupTypeIdentifier](https://developer.apple.com/documentation/medialibrary/mlphotosalbumsgrouptypeidentifier)Added [MLPhotosAllCollectionsGroupTypeIdentifier](https://developer.apple.com/documentation/medialibrary/mlphotosallcollectionsgrouptypeidentifier)Added [MLPhotosAllMomentsGroupTypeIdentifier](https://developer.apple.com/documentation/medialibrary/mlphotosallmomentsgrouptypeidentifier)Added [MLPhotosAllYearsGroupTypeIdentifier](https://developer.apple.com/documentation/medialibrary/mlphotosallyearsgrouptypeidentifier)Added [MLPhotosCollectionGroupTypeIdentifier](https://developer.apple.com/documentation/medialibrary/mlphotoscollectiongrouptypeidentifier)Added [MLPhotosFavoritesGroupTypeIdentifier](https://developer.apple.com/documentation/medialibrary/mlphotosfavoritesgrouptypeidentifier)Added [MLPhotosFolderTypeIdentifier](https://developer.apple.com/documentation/medialibrary/mlphotosfoldertypeidentifier)Added [MLPhotosLastImportGroupTypeIdentifier](https://developer.apple.com/documentation/medialibrary/mlphotoslastimportgrouptypeidentifier)Added [MLPhotosMomentGroupTypeIdentifier](https://developer.apple.com/documentation/medialibrary/mlphotosmomentgrouptypeidentifier)Added [MLPhotosMyPhotoStreamTypeIdentifier](https://developer.apple.com/documentation/medialibrary/mlphotosmyphotostreamtypeidentifier)Added [MLPhotosPanoramasGroupTypeIdentifier](https://developer.apple.com/documentation/medialibrary/mlphotospanoramasgrouptypeidentifier)Added [MLPhotosPublishedAlbumTypeIdentifier](https://developer.apple.com/documentation/medialibrary/mlphotospublishedalbumtypeidentifier)Added [MLPhotosRootGroupTypeIdentifier](https://developer.apple.com/documentation/medialibrary/mlphotosrootgrouptypeidentifier)Added [MLPhotosSharedGroupTypeIdentifier](https://developer.apple.com/documentation/medialibrary/mlphotossharedgrouptypeidentifier)Added [MLPhotosSharedPhotoStreamTypeIdentifier](https://developer.apple.com/documentation/medialibrary/mlphotossharedphotostreamtypeidentifier)Added [MLPhotosSmartAlbumTypeIdentifier](https://developer.apple.com/documentation/medialibrary/mlphotossmartalbumtypeidentifier)Added [MLPhotosVideosGroupTypeIdentifier](https://developer.apple.com/documentation/medialibrary/mlphotosvideosgrouptypeidentifier)Added [MLPhotosYearGroupTypeIdentifier](https://developer.apple.com/documentation/medialibrary/mlphotosyeargrouptypeidentifier)Added [MLiTunesMusicVideosPlaylistTypeIdentifier](https://developer.apple.com/documentation/medialibrary/mlitunesmusicvideosplaylisttypeidentifier)Added [MLiTunesVideoPlaylistTypeIdentifier](https://developer.apple.com/documentation/medialibrary/mlitunesvideoplaylisttypeidentifier)

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
