---
title: iOS 9.3 API Diffs
apple_id: TP40016662
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-03-01'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS93APIDiffs/Swift/MediaPlayer.html
archived_at: '2026-07-18T02:57:16.138861Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.3 API Diffs](iOS%209.2%20to%20iOS%209.3%20API%20Differences.md)


# MediaPlayer Changes for Swift

### MediaPlayer

Added [MPErrorCode [enum]](https://developer.apple.com/documentation/mediaplayer/mperrorcode)Added [MPErrorCode.CloudServiceCapabilityMissing](https://developer.apple.com/documentation/mediaplayer/mperror/code/cloudservicecapabilitymissing)Added [MPErrorCode.NetworkConnectionFailed](https://developer.apple.com/documentation/mediaplayer/mperrorcode/mperrornetworkconnectionfailed)Added [MPErrorCode.NotFound](https://developer.apple.com/documentation/mediaplayer/mperrorcode/mperrornotfound)Added [MPErrorCode.NotSupported](https://developer.apple.com/documentation/mediaplayer/mperrorcode/mperrornotsupported)Added [MPErrorCode.PermissionDenied](https://developer.apple.com/documentation/mediaplayer/mperror/code/permissiondenied)Added [MPErrorCode.Unknown](https://developer.apple.com/documentation/mediaplayer/mperror/code/unknown)Added [MPMediaLibrary.addItemWithProductID(_: String, completionHandler: (([MPMediaEntity], NSError?) -> Void)?)](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary/1621278-additem)Added [MPMediaLibrary.authorizationStatus() -> MPMediaLibraryAuthorizationStatus [class]](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary/1621282-authorizationstatus)Added [MPMediaLibrary.getPlaylistWithUUID(_: NSUUID, creationMetadata: MPMediaPlaylistCreationMetadata?, completionHandler: (MPMediaPlaylist?, NSError?) -> Void)](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary/1621273-getplaylistwithuuid)Added [MPMediaLibrary.requestAuthorization(_: (MPMediaLibraryAuthorizationStatus) -> Void) [class]](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary/1621276-requestauthorization)Added [MPMediaLibraryAuthorizationStatus [enum]](https://developer.apple.com/documentation/mediaplayer/mpmedialibraryauthorizationstatus)Added [MPMediaLibraryAuthorizationStatus.Authorized](https://developer.apple.com/documentation/mediaplayer/mpmedialibraryauthorizationstatus/mpmedialibraryauthorizationstatusauthorized)Added [MPMediaLibraryAuthorizationStatus.Denied](https://developer.apple.com/documentation/mediaplayer/mpmedialibraryauthorizationstatus/mpmedialibraryauthorizationstatusdenied)Added [MPMediaLibraryAuthorizationStatus.NotDetermined](https://developer.apple.com/documentation/mediaplayer/mpmedialibraryauthorizationstatus/notdetermined)Added [MPMediaLibraryAuthorizationStatus.Restricted](https://developer.apple.com/documentation/mediaplayer/mpmedialibraryauthorizationstatus/mpmedialibraryauthorizationstatusrestricted)Added [MPMediaPlaylist.addItemWithProductID(_: String, completionHandler: ((NSError?) -> Void)?)](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist/1618706-additemwithproductid)Added [MPMediaPlaylist.addMediaItems(_: [MPMediaItem], completionHandler: ((NSError?) -> Void)?)](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist/1618710-addmediaitems)Added [MPMediaPlaylist.authorDisplayName](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist/1618702-authordisplayname)Added [MPMediaPlaylist.descriptionText](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist/1618715-descriptiontext)Added [MPMediaPlaylistCreationMetadata](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylistcreationmetadata)Added [MPMediaPlaylistCreationMetadata.authorDisplayName](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylistcreationmetadata/1618699-authordisplayname)Added [MPMediaPlaylistCreationMetadata.descriptionText](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylistcreationmetadata/1618713-descriptiontext)Added [MPMediaPlaylistCreationMetadata.init(name: String)](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylistcreationmetadata/1618723-init)Added [MPMediaPlaylistCreationMetadata.name](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylistcreationmetadata/1618703-name)Added [MPMusicPlayerController.setQueueWithStoreIDs(_: [String])](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/1624253-setqueuewithstoreids)Added [MPErrorDomain](https://developer.apple.com/documentation/mediaplayer/mperrordomain)Added [MPMediaPlaylistPropertyAuthorDisplayName](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylistpropertyauthordisplayname)Added [MPMediaPlaylistPropertyDescriptionText](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylistpropertydescriptiontext)Modified [MPContentItem](https://developer.apple.com/documentation/mediaplayer/mpcontentitem)

|  | Declaration |
| --- | --- |
| From | ``` class MPContentItem : NSObject {     var identifier: String { get }     var title: String?     var subtitle: String?     var artwork: MPMediaItemArtwork?     var container: Bool     var playable: Bool     var playbackProgress: Float     init(identifier identifier: String) } ``` |
| To | ``` class MPContentItem : NSObject {     init(identifier identifier: String)     var identifier: String { get }     var title: String?     var subtitle: String?     var artwork: MPMediaItemArtwork?     var container: Bool     var playable: Bool     var playbackProgress: Float } ``` |

Modified [MPMediaLibrary](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary)

|  | Declaration |
| --- | --- |
| From | ``` class MPMediaLibrary : NSObject, NSSecureCoding {     class func defaultMediaLibrary() -> MPMediaLibrary     var lastModifiedDate: NSDate { get }     func beginGeneratingLibraryChangeNotifications()     func endGeneratingLibraryChangeNotifications() } ``` |
| To | ``` class MPMediaLibrary : NSObject, NSSecureCoding {     class func defaultMediaLibrary() -> MPMediaLibrary     var lastModifiedDate: NSDate { get }     func beginGeneratingLibraryChangeNotifications()     func endGeneratingLibraryChangeNotifications()     class func authorizationStatus() -> MPMediaLibraryAuthorizationStatus     class func requestAuthorization(_ handler: (MPMediaLibraryAuthorizationStatus) -> Void)     func addItemWithProductID(_ productID: String, completionHandler completionHandler: (([MPMediaEntity], NSError?) -> Void)?)     func getPlaylistWithUUID(_ uuid: NSUUID, creationMetadata creationMetadata: MPMediaPlaylistCreationMetadata?, completionHandler completionHandler: (MPMediaPlaylist?, NSError?) -> Void) } ``` |

Modified [MPMediaPlaylist](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist)

|  | Declaration |
| --- | --- |
| From | ``` class MPMediaPlaylist : MPMediaItemCollection {     var persistentID: MPMediaEntityPersistentID { get }     var name: String? { get }     var playlistAttributes: MPMediaPlaylistAttribute { get }     var seedItems: [MPMediaItem]? { get } } ``` |
| To | ``` class MPMediaPlaylist : MPMediaItemCollection {     var persistentID: MPMediaEntityPersistentID { get }     var name: String? { get }     var playlistAttributes: MPMediaPlaylistAttribute { get }     var seedItems: [MPMediaItem]? { get }     var descriptionText: String? { get }     var authorDisplayName: String? { get }     func addItemWithProductID(_ productID: String, completionHandler completionHandler: ((NSError?) -> Void)?)     func addMediaItems(_ mediaItems: [MPMediaItem], completionHandler completionHandler: ((NSError?) -> Void)?) } ``` |

Modified [MPMusicPlayerController](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller)

|  | Declaration |
| --- | --- |
| From | ``` class MPMusicPlayerController : NSObject, MPMediaPlayback {     class func applicationMusicPlayer() -> MPMusicPlayerController     class func systemMusicPlayer() -> MPMusicPlayerController     class func iPodMusicPlayer() -> MPMusicPlayerController } extension MPMusicPlayerController {     var playbackState: MPMusicPlaybackState { get }     var repeatMode: MPMusicRepeatMode     var shuffleMode: MPMusicShuffleMode     var volume: Float     @NSCopying var nowPlayingItem: MPMediaItem?     var indexOfNowPlayingItem: Int { get }     func setQueueWithQuery(_ query: MPMediaQuery)     func setQueueWithItemCollection(_ itemCollection: MPMediaItemCollection)     func skipToNextItem()     func skipToBeginning()     func skipToPreviousItem()     func beginGeneratingPlaybackNotifications()     func endGeneratingPlaybackNotifications() } ``` |
| To | ``` class MPMusicPlayerController : NSObject, MPMediaPlayback {     class func applicationMusicPlayer() -> MPMusicPlayerController     class func systemMusicPlayer() -> MPMusicPlayerController     class func iPodMusicPlayer() -> MPMusicPlayerController } extension MPMusicPlayerController {     var playbackState: MPMusicPlaybackState { get }     var repeatMode: MPMusicRepeatMode     var shuffleMode: MPMusicShuffleMode     var volume: Float     @NSCopying var nowPlayingItem: MPMediaItem?     var indexOfNowPlayingItem: Int { get }     func setQueueWithQuery(_ query: MPMediaQuery)     func setQueueWithItemCollection(_ itemCollection: MPMediaItemCollection)     func setQueueWithStoreIDs(_ storeIDs: [String])     func skipToNextItem()     func skipToBeginning()     func skipToPreviousItem()     func beginGeneratingPlaybackNotifications()     func endGeneratingPlaybackNotifications() } ``` |

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
