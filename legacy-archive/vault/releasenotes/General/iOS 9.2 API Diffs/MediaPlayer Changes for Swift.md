---
title: iOS 9.2 API Diffs
apple_id: TP40016605
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-12-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS92APIDiffs/Swift/MediaPlayer.html
archived_at: '2026-07-18T02:57:12.677732Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.2 API Diffs](iOS%209.1%20to%20iOS%209.2%20API%20Differences.md)


# MediaPlayer Changes for Swift

### MediaPlayer

Added [MPMediaItem.protectedAsset](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621678-protectedasset)Added [MPMediaPickerController.showsItemsWithProtectedAssets](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontroller/1614665-showsitemswithprotectedassets)Added [MPMediaItemPropertyHasProtectedAsset](https://developer.apple.com/documentation/mediaplayer/mpmediaitempropertyhasprotectedasset)Modified [MPMediaItem](https://developer.apple.com/documentation/mediaplayer/mpmediaitem)

|  | Declaration |
| --- | --- |
| From | ``` class MPMediaItem : MPMediaEntity {     var persistentID: MPMediaEntityPersistentID { get }     var mediaType: MPMediaType { get }     var title: String? { get }     var albumTitle: String? { get }     var albumPersistentID: MPMediaEntityPersistentID { get }     var artist: String? { get }     var artistPersistentID: MPMediaEntityPersistentID { get }     var albumArtist: String? { get }     var albumArtistPersistentID: MPMediaEntityPersistentID { get }     var genre: String? { get }     var genrePersistentID: MPMediaEntityPersistentID { get }     var composer: String? { get }     var composerPersistentID: MPMediaEntityPersistentID { get }     var playbackDuration: NSTimeInterval { get }     var albumTrackNumber: Int { get }     var albumTrackCount: Int { get }     var discNumber: Int { get }     var discCount: Int { get }     var artwork: MPMediaItemArtwork? { get }     var lyrics: String? { get }     var compilation: Bool { get }     var releaseDate: NSDate? { get }     var beatsPerMinute: Int { get }     var comments: String? { get }     var assetURL: NSURL? { get }     var cloudItem: Bool { get }     var podcastTitle: String? { get }     var podcastPersistentID: MPMediaEntityPersistentID { get }     var playCount: Int { get }     var skipCount: Int { get }     var rating: Int { get }     var lastPlayedDate: NSDate? { get }     var userGrouping: String? { get }     var bookmarkTime: NSTimeInterval { get } } extension MPMediaItem {     class func persistentIDPropertyForGroupingType(_ groupingType: MPMediaGrouping) -> String     class func titlePropertyForGroupingType(_ groupingType: MPMediaGrouping) -> String } ``` |
| To | ``` class MPMediaItem : MPMediaEntity {     var persistentID: MPMediaEntityPersistentID { get }     var mediaType: MPMediaType { get }     var title: String? { get }     var albumTitle: String? { get }     var albumPersistentID: MPMediaEntityPersistentID { get }     var artist: String? { get }     var artistPersistentID: MPMediaEntityPersistentID { get }     var albumArtist: String? { get }     var albumArtistPersistentID: MPMediaEntityPersistentID { get }     var genre: String? { get }     var genrePersistentID: MPMediaEntityPersistentID { get }     var composer: String? { get }     var composerPersistentID: MPMediaEntityPersistentID { get }     var playbackDuration: NSTimeInterval { get }     var albumTrackNumber: Int { get }     var albumTrackCount: Int { get }     var discNumber: Int { get }     var discCount: Int { get }     var artwork: MPMediaItemArtwork? { get }     var lyrics: String? { get }     var compilation: Bool { get }     var releaseDate: NSDate? { get }     var beatsPerMinute: Int { get }     var comments: String? { get }     var assetURL: NSURL? { get }     var cloudItem: Bool { get }     var protectedAsset: Bool { get }     var podcastTitle: String? { get }     var podcastPersistentID: MPMediaEntityPersistentID { get }     var playCount: Int { get }     var skipCount: Int { get }     var rating: Int { get }     var lastPlayedDate: NSDate? { get }     var userGrouping: String? { get }     var bookmarkTime: NSTimeInterval { get } } extension MPMediaItem {     class func persistentIDPropertyForGroupingType(_ groupingType: MPMediaGrouping) -> String     class func titlePropertyForGroupingType(_ groupingType: MPMediaGrouping) -> String } ``` |

Modified [MPMediaPickerController](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontroller)

|  | Declaration |
| --- | --- |
| From | ``` class MPMediaPickerController : UIViewController {     init(mediaTypes mediaTypes: MPMediaType)     var mediaTypes: MPMediaType { get }     weak var delegate: MPMediaPickerControllerDelegate?     var allowsPickingMultipleItems: Bool     var showsCloudItems: Bool     var prompt: String? } ``` |
| To | ``` class MPMediaPickerController : UIViewController {     init(mediaTypes mediaTypes: MPMediaType)     var mediaTypes: MPMediaType { get }     weak var delegate: MPMediaPickerControllerDelegate?     var allowsPickingMultipleItems: Bool     var showsCloudItems: Bool     var showsItemsWithProtectedAssets: Bool     var prompt: String? } ``` |

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
