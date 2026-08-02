---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/AssetsLibrary.html
archived_at: '2026-07-18T02:56:40.439871Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# AssetsLibrary Changes for Swift

### AssetsLibrary

Modified [ALAsset](https://developer.apple.com/documentation/assetslibrary/alasset)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAsset.aspectRatioThumbnail() -> Unmanaged<CGImage>!](https://developer.apple.com/documentation/assetslibrary/alasset/1615872-aspectratiothumbnail)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAsset.defaultRepresentation() -> ALAssetRepresentation!](https://developer.apple.com/documentation/assetslibrary/alasset/1615864-defaultrepresentation)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAsset.editable](https://developer.apple.com/documentation/assetslibrary/alasset/1615867-iseditable)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAsset.originalAsset](https://developer.apple.com/documentation/assetslibrary/alasset/1615857-originalasset)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAsset.representationForUTI(_: String!) -> ALAssetRepresentation!](https://developer.apple.com/documentation/assetslibrary/alasset/1615859-representation)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAsset.setImageData(_: NSData!, metadata: [NSObject : AnyObject]!, completionBlock: ALAssetsLibraryWriteImageCompletionBlock!)](https://developer.apple.com/documentation/assetslibrary/alasset/1615874-setimagedata)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAsset.setVideoAtPath(_: NSURL!, completionBlock: ALAssetsLibraryWriteVideoCompletionBlock!)](https://developer.apple.com/documentation/assetslibrary/alasset/1615880-setvideoatpath)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAsset.thumbnail() -> Unmanaged<CGImage>!](https://developer.apple.com/documentation/assetslibrary/alasset/1615879-thumbnail)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAsset.valueForProperty(_: String!) -> AnyObject!](https://developer.apple.com/documentation/assetslibrary/alasset/1615862-valueforproperty)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAsset.writeModifiedImageDataToSavedPhotosAlbum(_: NSData!, metadata: [NSObject : AnyObject]!, completionBlock: ALAssetsLibraryWriteImageCompletionBlock!)](https://developer.apple.com/documentation/assetslibrary/alasset/1615863-writemodifiedimagedatatosavedpho)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAsset.writeModifiedVideoAtPathToSavedPhotosAlbum(_: NSURL!, completionBlock: ALAssetsLibraryWriteVideoCompletionBlock!)](https://developer.apple.com/documentation/assetslibrary/alasset/1615878-writemodifiedvideoatpathtosavedp)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetOrientation [enum]](https://developer.apple.com/documentation/assetslibrary/alassetorientation)

|  | Introduction | Deprecation | Raw Value Type |
| --- | --- | --- | --- |
| From | iOS 8.1 | -- | -- |
| To | iOS 4.0 | iOS 9.0 | Int |

Modified [ALAssetOrientation.Down](https://developer.apple.com/documentation/assetslibrary/alassetorientation/down)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetOrientation.DownMirrored](https://developer.apple.com/documentation/assetslibrary/alassetorientation/alassetorientationdownmirrored)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetOrientation.Left](https://developer.apple.com/documentation/assetslibrary/alassetorientation/left)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetOrientation.LeftMirrored](https://developer.apple.com/documentation/assetslibrary/alassetorientation/leftmirrored)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetOrientation.Right](https://developer.apple.com/documentation/assetslibrary/alassetorientation/alassetorientationright)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetOrientation.RightMirrored](https://developer.apple.com/documentation/assetslibrary/alassetorientation/rightmirrored)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetOrientation.Up](https://developer.apple.com/documentation/assetslibrary/alassetorientation/up)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetOrientation.UpMirrored](https://developer.apple.com/documentation/assetslibrary/alassetorientation/alassetorientationupmirrored)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetRepresentation](https://developer.apple.com/documentation/assetslibrary/alassetrepresentation)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetRepresentation.CGImageWithOptions(_: [NSObject : AnyObject]!) -> Unmanaged<CGImage>!](https://developer.apple.com/documentation/assetslibrary/alassetrepresentation/1617855-cgimage)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetRepresentation.dimensions() -> CGSize](https://developer.apple.com/documentation/assetslibrary/alassetrepresentation/1617856-dimensions)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetRepresentation.filename() -> String!](https://developer.apple.com/documentation/assetslibrary/alassetrepresentation/1617857-filename)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetRepresentation.fullResolutionImage() -> Unmanaged<CGImage>!](https://developer.apple.com/documentation/assetslibrary/alassetrepresentation/1617864-fullresolutionimage)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetRepresentation.fullScreenImage() -> Unmanaged<CGImage>!](https://developer.apple.com/documentation/assetslibrary/alassetrepresentation/1617858-fullscreenimage)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetRepresentation.getBytes(_: UnsafeMutablePointer<UInt8>, fromOffset: Int64, length: Int, error: NSErrorPointer) -> Int](https://developer.apple.com/documentation/assetslibrary/alassetrepresentation/1617860-getbytes)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetRepresentation.metadata() -> [NSObject : AnyObject]!](https://developer.apple.com/documentation/assetslibrary/alassetrepresentation/1617859-metadata)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetRepresentation.orientation() -> ALAssetOrientation](https://developer.apple.com/documentation/assetslibrary/alassetrepresentation/1617863-orientation)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetRepresentation.scale() -> Float](https://developer.apple.com/documentation/assetslibrary/alassetrepresentation/1617862-scale)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetRepresentation.size() -> Int64](https://developer.apple.com/documentation/assetslibrary/alassetrepresentation/1617854-size)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetRepresentation.url() -> NSURL!](https://developer.apple.com/documentation/assetslibrary/alassetrepresentation/1617853-url)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetRepresentation.UTI() -> String!](https://developer.apple.com/documentation/assetslibrary/alassetrepresentation/1617865-uti)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetsFilter](https://developer.apple.com/documentation/assetslibrary/alassetsfilter)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetsFilter.allAssets() -> ALAssetsFilter! [class]](https://developer.apple.com/documentation/assetslibrary/alassetsfilter/1619377-allassets)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetsFilter.allPhotos() -> ALAssetsFilter! [class]](https://developer.apple.com/documentation/assetslibrary/alassetsfilter/1619376-allphotos)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetsFilter.allVideos() -> ALAssetsFilter! [class]](https://developer.apple.com/documentation/assetslibrary/alassetsfilter/1619375-allvideos)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetsGroup](https://developer.apple.com/documentation/assetslibrary/alassetsgroup)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetsGroup.addAsset(_: ALAsset!) -> Bool](https://developer.apple.com/documentation/assetslibrary/alassetsgroup/1621964-addasset)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetsGroup.editable](https://developer.apple.com/documentation/assetslibrary/alassetsgroup/1621969-iseditable)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetsGroup.enumerateAssetsAtIndexes(_: NSIndexSet!, options: NSEnumerationOptions, usingBlock: ALAssetsGroupEnumerationResultsBlock!)](https://developer.apple.com/documentation/assetslibrary/alassetsgroup/1621966-enumerateassetsatindexes)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetsGroup.enumerateAssetsUsingBlock(_: ALAssetsGroupEnumerationResultsBlock!)](https://developer.apple.com/documentation/assetslibrary/alassetsgroup/1621968-enumerateassets)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetsGroup.enumerateAssetsWithOptions(_: NSEnumerationOptions, usingBlock: ALAssetsGroupEnumerationResultsBlock!)](https://developer.apple.com/documentation/assetslibrary/alassetsgroup/1621960-enumerateassetswithoptions)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetsGroup.numberOfAssets() -> Int](https://developer.apple.com/documentation/assetslibrary/alassetsgroup/1621963-numberofassets)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetsGroup.posterImage() -> Unmanaged<CGImage>!](https://developer.apple.com/documentation/assetslibrary/alassetsgroup/1621961-posterimage)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetsGroup.setAssetsFilter(_: ALAssetsFilter!)](https://developer.apple.com/documentation/assetslibrary/alassetsgroup/1621967-setassetsfilter)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetsGroup.valueForProperty(_: String!) -> AnyObject!](https://developer.apple.com/documentation/assetslibrary/alassetsgroup/1621971-value)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetsLibrary](https://developer.apple.com/documentation/assetslibrary/alassetslibrary)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` class ALAssetsLibrary : NSObject {     func enumerateGroupsWithTypes(_ types: ALAssetsGroupType, usingBlock enumerationBlock: ALAssetsLibraryGroupsEnumerationResultsBlock!, failureBlock failureBlock: ALAssetsLibraryAccessFailureBlock!)     func assetForURL(_ assetURL: NSURL!, resultBlock resultBlock: ALAssetsLibraryAssetForURLResultBlock!, failureBlock failureBlock: ALAssetsLibraryAccessFailureBlock!)     func groupForURL(_ groupURL: NSURL!, resultBlock resultBlock: ALAssetsLibraryGroupResultBlock!, failureBlock failureBlock: ALAssetsLibraryAccessFailureBlock!)     func addAssetsGroupAlbumWithName(_ name: String!, resultBlock resultBlock: ALAssetsLibraryGroupResultBlock!, failureBlock failureBlock: ALAssetsLibraryAccessFailureBlock!)     func writeImageToSavedPhotosAlbum(_ imageRef: CGImage!, orientation orientation: ALAssetOrientation, completionBlock completionBlock: ALAssetsLibraryWriteImageCompletionBlock!)     func writeImageToSavedPhotosAlbum(_ imageRef: CGImage!, metadata metadata: [NSObject : AnyObject]!, completionBlock completionBlock: ALAssetsLibraryWriteImageCompletionBlock!)     func writeImageDataToSavedPhotosAlbum(_ imageData: NSData!, metadata metadata: [NSObject : AnyObject]!, completionBlock completionBlock: ALAssetsLibraryWriteImageCompletionBlock!)     func writeVideoAtPathToSavedPhotosAlbum(_ videoPathURL: NSURL!, completionBlock completionBlock: ALAssetsLibraryWriteVideoCompletionBlock!)     func videoAtPathIsCompatibleWithSavedPhotosAlbum(_ videoPathURL: NSURL!) -> Bool     class func authorizationStatus() -> ALAuthorizationStatus     class func disableSharedPhotoStreamsSupport() } extension ALAssetsLibrary {     func enumerateGroupsWithTypes(_ types: UInt32, usingBlock enumerationBlock: ALAssetsLibraryGroupsEnumerationResultsBlock!, failureBlock failureBlock: ALAssetsLibraryAccessFailureBlock!) } extension ALAssetsLibrary {     func enumerateGroupsWithTypes(_ types: UInt32, usingBlock enumerationBlock: ALAssetsLibraryGroupsEnumerationResultsBlock!, failureBlock failureBlock: ALAssetsLibraryAccessFailureBlock!) } ``` | -- |
| To | ``` class ALAssetsLibrary : NSObject {     func enumerateGroupsWithTypes(_ types: ALAssetsGroupType, usingBlock enumerationBlock: ALAssetsLibraryGroupsEnumerationResultsBlock!, failureBlock failureBlock: ALAssetsLibraryAccessFailureBlock!)     func assetForURL(_ assetURL: NSURL!, resultBlock resultBlock: ALAssetsLibraryAssetForURLResultBlock!, failureBlock failureBlock: ALAssetsLibraryAccessFailureBlock!)     func groupForURL(_ groupURL: NSURL!, resultBlock resultBlock: ALAssetsLibraryGroupResultBlock!, failureBlock failureBlock: ALAssetsLibraryAccessFailureBlock!)     func addAssetsGroupAlbumWithName(_ name: String!, resultBlock resultBlock: ALAssetsLibraryGroupResultBlock!, failureBlock failureBlock: ALAssetsLibraryAccessFailureBlock!)     func writeImageToSavedPhotosAlbum(_ imageRef: CGImage!, orientation orientation: ALAssetOrientation, completionBlock completionBlock: ALAssetsLibraryWriteImageCompletionBlock!)     func writeImageToSavedPhotosAlbum(_ imageRef: CGImage!, metadata metadata: [NSObject : AnyObject]!, completionBlock completionBlock: ALAssetsLibraryWriteImageCompletionBlock!)     func writeImageDataToSavedPhotosAlbum(_ imageData: NSData!, metadata metadata: [NSObject : AnyObject]!, completionBlock completionBlock: ALAssetsLibraryWriteImageCompletionBlock!)     func writeVideoAtPathToSavedPhotosAlbum(_ videoPathURL: NSURL!, completionBlock completionBlock: ALAssetsLibraryWriteVideoCompletionBlock!)     func videoAtPathIsCompatibleWithSavedPhotosAlbum(_ videoPathURL: NSURL!) -> Bool     class func authorizationStatus() -> ALAuthorizationStatus     class func disableSharedPhotoStreamsSupport() } extension ALAssetsLibrary {     @nonobjc func enumerateGroupsWithTypes(_ types: UInt32, usingBlock enumerationBlock: ALAssetsLibraryGroupsEnumerationResultsBlock!, failureBlock failureBlock: ALAssetsLibraryAccessFailureBlock!) } extension ALAssetsLibrary {     @nonobjc func enumerateGroupsWithTypes(_ types: UInt32, usingBlock enumerationBlock: ALAssetsLibraryGroupsEnumerationResultsBlock!, failureBlock failureBlock: ALAssetsLibraryAccessFailureBlock!) } ``` | iOS 9.0 |

Modified [ALAssetsLibrary.addAssetsGroupAlbumWithName(_: String!, resultBlock: ALAssetsLibraryGroupResultBlock!, failureBlock: ALAssetsLibraryAccessFailureBlock!)](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/1617872-addassetsgroupalbumwithname)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetsLibrary.assetForURL(_: NSURL!, resultBlock: ALAssetsLibraryAssetForURLResultBlock!, failureBlock: ALAssetsLibraryAccessFailureBlock!)](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/1617909-assetforurl)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetsLibrary.authorizationStatus() -> ALAuthorizationStatus [class]](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/1617901-authorizationstatus)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetsLibrary.disableSharedPhotoStreamsSupport() [class]](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/1617905-disablesharedphotostreamssupport)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified ALAssetsLibrary.enumerateGroupsWithTypes(_: UInt32, usingBlock: ALAssetsLibraryGroupsEnumerationResultsBlock!, failureBlock: ALAssetsLibraryAccessFailureBlock!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func enumerateGroupsWithTypes(_ types: UInt32, usingBlock enumerationBlock: ALAssetsLibraryGroupsEnumerationResultsBlock!, failureBlock failureBlock: ALAssetsLibraryAccessFailureBlock!) ``` | iOS 8.1 |
| To | ``` @nonobjc func enumerateGroupsWithTypes(_ types: UInt32, usingBlock enumerationBlock: ALAssetsLibraryGroupsEnumerationResultsBlock!, failureBlock failureBlock: ALAssetsLibraryAccessFailureBlock!) ``` | iOS 9.0 |

Modified [ALAssetsLibrary.enumerateGroupsWithTypes(_: ALAssetsGroupType, usingBlock: ALAssetsLibraryGroupsEnumerationResultsBlock!, failureBlock: ALAssetsLibraryAccessFailureBlock!)](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/1617900-enumerategroupswithtypes)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetsLibrary.groupForURL(_: NSURL!, resultBlock: ALAssetsLibraryGroupResultBlock!, failureBlock: ALAssetsLibraryAccessFailureBlock!)](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/1617907-groupforurl)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetsLibrary.videoAtPathIsCompatibleWithSavedPhotosAlbum(_: NSURL!) -> Bool](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/1617920-videoatpathiscompatiblewithsaved)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 5.0 | iOS 9.0 |

Modified [ALAssetsLibrary.writeImageDataToSavedPhotosAlbum(_: NSData!, metadata: [NSObject : AnyObject]!, completionBlock: ALAssetsLibraryWriteImageCompletionBlock!)](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/1617926-writeimagedata)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetsLibrary.writeImageToSavedPhotosAlbum(_: CGImage!, metadata: [NSObject : AnyObject]!, completionBlock: ALAssetsLibraryWriteImageCompletionBlock!)](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/1617898-writeimagetosavedphotosalbum)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetsLibrary.writeImageToSavedPhotosAlbum(_: CGImage!, orientation: ALAssetOrientation, completionBlock: ALAssetsLibraryWriteImageCompletionBlock!)](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/1617913-writeimagetosavedphotosalbum)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetsLibrary.writeVideoAtPathToSavedPhotosAlbum(_: NSURL!, completionBlock: ALAssetsLibraryWriteVideoCompletionBlock!)](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/1617921-writevideoatpathtosavedphotosalb)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAuthorizationStatus [enum]](https://developer.apple.com/documentation/assetslibrary/alauthorizationstatus)

|  | Deprecation | Raw Value Type |
| --- | --- | --- |
| From | -- | -- |
| To | iOS 9.0 | Int |

Modified [ALAuthorizationStatus.Authorized](https://developer.apple.com/documentation/assetslibrary/alauthorizationstatus/authorized)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 6.0 | iOS 9.0 |

Modified [ALAuthorizationStatus.Denied](https://developer.apple.com/documentation/assetslibrary/alauthorizationstatus/alauthorizationstatusdenied)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 6.0 | iOS 9.0 |

Modified [ALAuthorizationStatus.NotDetermined](https://developer.apple.com/documentation/assetslibrary/alauthorizationstatus/notdetermined)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 6.0 | iOS 9.0 |

Modified [ALAuthorizationStatus.Restricted](https://developer.apple.com/documentation/assetslibrary/alauthorizationstatus/alauthorizationstatusrestricted)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 6.0 | iOS 9.0 |

Modified [ALAssetLibraryDeletedAssetGroupsKey](https://developer.apple.com/documentation/assetslibrary/alassetlibrarydeletedassetgroupskey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetLibraryInsertedAssetGroupsKey](https://developer.apple.com/documentation/assetslibrary/alassetlibraryinsertedassetgroupskey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetLibraryUpdatedAssetGroupsKey](https://developer.apple.com/documentation/assetslibrary/alassetlibraryupdatedassetgroupskey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetLibraryUpdatedAssetsKey](https://developer.apple.com/documentation/assetslibrary/alassetlibraryupdatedassetskey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetPropertyAssetURL](https://developer.apple.com/documentation/assetslibrary/alassetpropertyasseturl)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 6.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetPropertyDate](https://developer.apple.com/documentation/assetslibrary/alassetpropertydate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetPropertyDuration](https://developer.apple.com/documentation/assetslibrary/alassetpropertyduration)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetPropertyLocation](https://developer.apple.com/documentation/assetslibrary/alassetpropertylocation)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetPropertyOrientation](https://developer.apple.com/documentation/assetslibrary/alassetpropertyorientation)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetPropertyRepresentations](https://developer.apple.com/documentation/assetslibrary/alassetpropertyrepresentations)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetPropertyType](https://developer.apple.com/documentation/assetslibrary/alassetpropertytype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetPropertyURLs](https://developer.apple.com/documentation/assetslibrary/alassetpropertyurls)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetsGroupAlbum](https://developer.apple.com/documentation/assetslibrary/1617883-types_of_asset/alassetsgroupalbum)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetsGroupAll](https://developer.apple.com/documentation/assetslibrary/alassetsgroupall)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetsGroupEnumerationResultsBlock](https://developer.apple.com/documentation/assetslibrary/alassetsgroupenumerationresultsblock)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetsGroupEvent](https://developer.apple.com/documentation/assetslibrary/alassetsgroupevent)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetsGroupFaces](https://developer.apple.com/documentation/assetslibrary/alassetsgroupfaces)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetsGroupLibrary](https://developer.apple.com/documentation/assetslibrary/alassetsgrouplibrary)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetsGroupPhotoStream](https://developer.apple.com/documentation/assetslibrary/1617883-types_of_asset/alassetsgroupphotostream)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 5.0 | iOS 9.0 |

Modified [ALAssetsGroupPropertyName](https://developer.apple.com/documentation/assetslibrary/alassetsgrouppropertyname)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetsGroupPropertyPersistentID](https://developer.apple.com/documentation/assetslibrary/alassetsgrouppropertypersistentid)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetsGroupPropertyType](https://developer.apple.com/documentation/assetslibrary/alassetsgrouppropertytype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetsGroupPropertyURL](https://developer.apple.com/documentation/assetslibrary/alassetsgrouppropertyurl)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetsGroupSavedPhotos](https://developer.apple.com/documentation/assetslibrary/1617883-types_of_asset/alassetsgroupsavedphotos)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetsGroupType](https://developer.apple.com/documentation/assetslibrary/alassetsgrouptype)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetsLibraryAccessFailureBlock](https://developer.apple.com/documentation/assetslibrary/alassetslibraryaccessfailureblock)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetsLibraryAssetForURLResultBlock](https://developer.apple.com/documentation/assetslibrary/alassetslibraryassetforurlresultblock)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetsLibraryChangedNotification](https://developer.apple.com/documentation/assetslibrary/alassetslibrarychangednotification)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetsLibraryErrorDomain](https://developer.apple.com/documentation/assetslibrary/alassetslibraryerrordomain)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetsLibraryGroupResultBlock](https://developer.apple.com/documentation/assetslibrary/alassetslibrarygroupresultblock)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetsLibraryGroupsEnumerationResultsBlock](https://developer.apple.com/documentation/assetslibrary/alassetslibrarygroupsenumerationresultsblock)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetsLibraryWriteImageCompletionBlock](https://developer.apple.com/documentation/assetslibrary/alassetslibrarywriteimagecompletionblock)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetsLibraryWriteVideoCompletionBlock](https://developer.apple.com/documentation/assetslibrary/alassetslibrarywritevideocompletionblock)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.0 | iOS 9.0 |

Modified [ALAssetTypePhoto](https://developer.apple.com/documentation/assetslibrary/alassettypephoto)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetTypeUnknown](https://developer.apple.com/documentation/assetslibrary/alassettypeunknown)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALAssetTypeVideo](https://developer.apple.com/documentation/assetslibrary/alassettypevideo)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [ALErrorInvalidProperty](https://developer.apple.com/documentation/assetslibrary/alerrorinvalidproperty)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

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
