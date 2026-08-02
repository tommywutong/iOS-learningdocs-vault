---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Objective-C/Photos.html
archived_at: '2026-07-18T02:50:41.632434Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# Photos Changes for Objective-C

### Photos

#### PHContentEditingInput.h

Added [PHContentEditingInput.livePhoto](https://developer.apple.com/documentation/photokit/phcontenteditinginput/1638106-livephoto)

#### PHLivePhoto.h (Added)

Added [PHLivePhoto](https://developer.apple.com/documentation/photokit/phlivephoto)Added [PHLivePhoto.size](https://developer.apple.com/documentation/photokit/phlivephoto/1616430-size)

#### PHLivePhotoEditingContext.h (Added)

Added [PHLivePhotoEditingContext](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext)Added [PHLivePhotoEditingContext.audioVolume](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext/1642113-audiovolume)Added [-[PHLivePhotoEditingContext cancel]](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext/1642083-cancel)Added [PHLivePhotoEditingContext.duration](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext/1642109-duration)Added [PHLivePhotoEditingContext.frameProcessor](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext/1642132-frameprocessor)Added [PHLivePhotoEditingContext.fullSizeImage](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext/1642106-fullsizeimage)Added [-[PHLivePhotoEditingContext initWithLivePhotoEditingInput:]](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext/1642121-initwithlivephotoeditinginput)Added [PHLivePhotoEditingContext.orientation](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext/1642093-orientation)Added [PHLivePhotoEditingContext.photoTime](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext/1642131-phototime)Added [-[PHLivePhotoEditingContext prepareLivePhotoForPlaybackWithTargetSize:options:completionHandler:]](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext/1642101-preparelivephotoforplayback)Added [-[PHLivePhotoEditingContext saveLivePhotoToOutput:options:completionHandler:]](https://developer.apple.com/documentation/photokit/phlivephotoeditingcontext/1642082-savelivephototooutput)Added [PHLivePhotoFrame](https://developer.apple.com/documentation/photokit/phlivephotoframe)Added [PHLivePhotoFrame.image](https://developer.apple.com/documentation/photokit/phlivephotoframe/1642114-image)Added [PHLivePhotoFrame.renderScale](https://developer.apple.com/documentation/photokit/phlivephotoframe/1642123-renderscale)Added [PHLivePhotoFrame.time](https://developer.apple.com/documentation/photokit/phlivephotoframe/1642126-time)Added [PHLivePhotoFrame.type](https://developer.apple.com/documentation/photokit/phlivephotoframe/1642087-type)Added [PHLivePhotoEditingErrorCode](https://developer.apple.com/documentation/photokit/phlivephotoeditingerrorcode)Added [PHLivePhotoEditingErrorCodeAborted](https://developer.apple.com/documentation/photokit/phlivephotoeditingerrorcode/aborted)Added [PHLivePhotoEditingErrorCodeUnknown](https://developer.apple.com/documentation/photokit/phlivephotoeditingerrorcode/unknown)Added [PHLivePhotoEditingErrorDomain](https://developer.apple.com/documentation/photokit/phlivephotoeditingerrordomain)Added [PHLivePhotoEditingOption](https://developer.apple.com/documentation/photokit/phlivephotoeditingoption)Added [PHLivePhotoFrameProcessingBlock](https://developer.apple.com/documentation/photokit/phlivephotoframeprocessingblock)Added [PHLivePhotoFrameType](https://developer.apple.com/documentation/photokit/phlivephotoframetype)Added [PHLivePhotoFrameTypePhoto](https://developer.apple.com/documentation/photokit/phlivephotoframetype/photo)Added [PHLivePhotoFrameTypeVideo](https://developer.apple.com/documentation/photokit/phlivephotoframetype/phlivephotoframetypevideo)Added [PHLivePhotoShouldRenderAtPlaybackTime](https://developer.apple.com/documentation/photokit/phlivephotoeditingoption/1642124-shouldrenderatplaybacktime)

#### PhotosTypes.h

Added [PHAssetBurstSelectionType](https://developer.apple.com/documentation/photokit/phassetburstselectiontype)Added [PHAssetBurstSelectionTypeAutoPick](https://developer.apple.com/documentation/photokit/phassetburstselectiontype/phassetburstselectiontypeautopick)Added [PHAssetBurstSelectionTypeNone](https://developer.apple.com/documentation/photokit/phassetburstselectiontype/phassetburstselectiontypenone)Added [PHAssetBurstSelectionTypeUserPick](https://developer.apple.com/documentation/photokit/phassetburstselectiontype/phassetburstselectiontypeuserpick)Added [PHAssetCollectionSubtype](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype)Added [PHAssetCollectionSubtypeAlbumCloudShared](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/phassetcollectionsubtypealbumcloudshared)Added [PHAssetCollectionSubtypeAlbumImported](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/phassetcollectionsubtypealbumimported)Added [PHAssetCollectionSubtypeAlbumMyPhotoStream](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/albummyphotostream)Added [PHAssetCollectionSubtypeAlbumRegular](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/phassetcollectionsubtypealbumregular)Added [PHAssetCollectionSubtypeAlbumSyncedAlbum](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/albumsyncedalbum)Added [PHAssetCollectionSubtypeAlbumSyncedEvent](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/phassetcollectionsubtypealbumsyncedevent)Added [PHAssetCollectionSubtypeAlbumSyncedFaces](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/albumsyncedfaces)Added [PHAssetCollectionSubtypeAny](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/any)Added [PHAssetCollectionSubtypeSmartAlbumAllHidden](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/smartalbumallhidden)Added [PHAssetCollectionSubtypeSmartAlbumBursts](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/phassetcollectionsubtypesmartalbumbursts)Added [PHAssetCollectionSubtypeSmartAlbumFavorites](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/phassetcollectionsubtypesmartalbumfavorites)Added [PHAssetCollectionSubtypeSmartAlbumGeneric](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/smartalbumgeneric)Added [PHAssetCollectionSubtypeSmartAlbumPanoramas](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/smartalbumpanoramas)Added [PHAssetCollectionSubtypeSmartAlbumRecentlyAdded](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/phassetcollectionsubtypesmartalbumrecentlyadded)Added [PHAssetCollectionSubtypeSmartAlbumScreenshots](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/smartalbumscreenshots)Added [PHAssetCollectionSubtypeSmartAlbumSelfPortraits](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/smartalbumselfportraits)Added [PHAssetCollectionSubtypeSmartAlbumSlomoVideos](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/smartalbumslomovideos)Added [PHAssetCollectionSubtypeSmartAlbumTimelapses](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/phassetcollectionsubtypesmartalbumtimelapses)Added [PHAssetCollectionSubtypeSmartAlbumUserLibrary](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/smartalbumuserlibrary)Added [PHAssetCollectionSubtypeSmartAlbumVideos](https://developer.apple.com/documentation/photokit/phassetcollectionsubtype/phassetcollectionsubtypesmartalbumvideos)Added [PHAssetCollectionType](https://developer.apple.com/documentation/photokit/phassetcollectiontype)Added [PHAssetCollectionTypeAlbum](https://developer.apple.com/documentation/photokit/phassetcollectiontype/album)Added [PHAssetCollectionTypeMoment](https://developer.apple.com/documentation/photokit/phassetcollectiontype/moment)Added [PHAssetCollectionTypeSmartAlbum](https://developer.apple.com/documentation/photokit/phassetcollectiontype/phassetcollectiontypesmartalbum)Added [PHAssetEditOperation](https://developer.apple.com/documentation/photokit/phasseteditoperation)Added [PHAssetEditOperationContent](https://developer.apple.com/documentation/photokit/phasseteditoperation/content)Added [PHAssetEditOperationDelete](https://developer.apple.com/documentation/photokit/phasseteditoperation/delete)Added [PHAssetEditOperationProperties](https://developer.apple.com/documentation/photokit/phasseteditoperation/phasseteditoperationproperties)Added [PHAssetMediaSubtypePhotoLive](https://developer.apple.com/documentation/photokit/phassetmediasubtype/phassetmediasubtypephotolive)Added [PHAssetResourceType](https://developer.apple.com/documentation/photokit/phassetresourcetype)Added [PHAssetResourceTypeAdjustmentBasePhoto](https://developer.apple.com/documentation/photokit/phassetresourcetype/adjustmentbasephoto)Added [PHAssetResourceTypeAdjustmentData](https://developer.apple.com/documentation/photokit/phassetresourcetype/phassetresourcetypeadjustmentdata)Added [PHAssetResourceTypeAlternatePhoto](https://developer.apple.com/documentation/photokit/phassetresourcetype/alternatephoto)Added [PHAssetResourceTypeAudio](https://developer.apple.com/documentation/photokit/phassetresourcetype/phassetresourcetypeaudio)Added [PHAssetResourceTypeFullSizePhoto](https://developer.apple.com/documentation/photokit/phassetresourcetype/fullsizephoto)Added [PHAssetResourceTypeFullSizeVideo](https://developer.apple.com/documentation/photokit/phassetresourcetype/phassetresourcetypefullsizevideo)Added [PHAssetResourceTypePairedVideo](https://developer.apple.com/documentation/photokit/phassetresourcetype/pairedvideo)Added [PHAssetResourceTypePhoto](https://developer.apple.com/documentation/photokit/phassetresourcetype/phassetresourcetypephoto)Added [PHAssetResourceTypeVideo](https://developer.apple.com/documentation/photokit/phassetresourcetype/phassetresourcetypevideo)Added [PHAssetSourceType](https://developer.apple.com/documentation/photokit/phassetsourcetype)Added [PHAssetSourceTypeCloudShared](https://developer.apple.com/documentation/photokit/phassetsourcetype/phassetsourcetypecloudshared)Added [PHAssetSourceTypeiTunesSynced](https://developer.apple.com/documentation/photokit/phassetsourcetype/phassetsourcetypeitunessynced)Added [PHAssetSourceTypeNone](https://developer.apple.com/documentation/photokit/phassetsourcetype/phassetsourcetypenone)Added [PHAssetSourceTypeUserLibrary](https://developer.apple.com/documentation/photokit/phassetsourcetype/phassetsourcetypeuserlibrary)Added [PHCollectionEditOperation](https://developer.apple.com/documentation/photokit/phcollectioneditoperation)Added [PHCollectionEditOperationAddContent](https://developer.apple.com/documentation/photokit/phcollectioneditoperation/addcontent)Added [PHCollectionEditOperationCreateContent](https://developer.apple.com/documentation/photokit/phcollectioneditoperation/createcontent)Added [PHCollectionEditOperationDelete](https://developer.apple.com/documentation/photokit/phcollectioneditoperation/delete)Added [PHCollectionEditOperationDeleteContent](https://developer.apple.com/documentation/photokit/phcollectioneditoperation/deletecontent)Added [PHCollectionEditOperationRearrangeContent](https://developer.apple.com/documentation/photokit/phcollectioneditoperation/phcollectioneditoperationrearrangecontent)Added [PHCollectionEditOperationRemoveContent](https://developer.apple.com/documentation/photokit/phcollectioneditoperation/phcollectioneditoperationremovecontent)Added [PHCollectionEditOperationRename](https://developer.apple.com/documentation/photokit/phcollectioneditoperation/rename)Added [PHCollectionListSubtype](https://developer.apple.com/documentation/photokit/phcollectionlistsubtype)Added [PHCollectionListSubtypeAny](https://developer.apple.com/documentation/photokit/phcollectionlistsubtype/phcollectionlistsubtypeany)Added [PHCollectionListSubtypeMomentListCluster](https://developer.apple.com/documentation/photokit/phcollectionlistsubtype/momentlistcluster)Added [PHCollectionListSubtypeMomentListYear](https://developer.apple.com/documentation/photokit/phcollectionlistsubtype/phcollectionlistsubtypemomentlistyear)Added [PHCollectionListSubtypeRegularFolder](https://developer.apple.com/documentation/photokit/phcollectionlistsubtype/regularfolder)Added [PHCollectionListSubtypeSmartFolderEvents](https://developer.apple.com/documentation/photokit/phcollectionlistsubtype/smartfolderevents)Added [PHCollectionListSubtypeSmartFolderFaces](https://developer.apple.com/documentation/photokit/phcollectionlistsubtype/smartfolderfaces)Added [PHCollectionListType](https://developer.apple.com/documentation/photokit/phcollectionlisttype)Added [PHCollectionListTypeFolder](https://developer.apple.com/documentation/photokit/phcollectionlisttype/folder)Added [PHCollectionListTypeMomentList](https://developer.apple.com/documentation/photokit/phcollectionlisttype/phcollectionlisttypemomentlist)Added [PHCollectionListTypeSmartFolder](https://developer.apple.com/documentation/photokit/phcollectionlisttype/smartfolder)Added [PHImageContentMode](https://developer.apple.com/documentation/photokit/phimagecontentmode)Added [PHImageContentModeAspectFill](https://developer.apple.com/documentation/photokit/phimagecontentmode/phimagecontentmodeaspectfill)Added [PHImageContentModeAspectFit](https://developer.apple.com/documentation/photokit/phimagecontentmode/aspectfit)Added [PHImageContentModeDefault](https://developer.apple.com/documentation/photokit/phimagecontentmode/phimagecontentmodedefault)

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
