---
title: iOS 9.3 API Diffs
apple_id: TP40016662
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-03-01'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS93APIDiffs/Objective-C/MediaPlayer.html
archived_at: '2026-07-18T02:57:14.139034Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.3 API Diffs](iOS%209.2%20to%20iOS%209.3%20API%20Differences.md)


# MediaPlayer Changes for Objective-C

### MediaPlayer

#### MPError.h (Added)

Added [MPErrorCloudServiceCapabilityMissing](https://developer.apple.com/documentation/mediaplayer/mperrorcode/mperrorcloudservicecapabilitymissing)Added [MPErrorCode](https://developer.apple.com/documentation/mediaplayer/mperror/code)Added [MPErrorDomain](https://developer.apple.com/documentation/mediaplayer/mperrordomain)Added [MPErrorNetworkConnectionFailed](https://developer.apple.com/documentation/mediaplayer/mperrorcode/mperrornetworkconnectionfailed)Added [MPErrorNotFound](https://developer.apple.com/documentation/mediaplayer/mperror/code/notfound)Added [MPErrorNotSupported](https://developer.apple.com/documentation/mediaplayer/mperrorcode/mperrornotsupported)Added [MPErrorPermissionDenied](https://developer.apple.com/documentation/mediaplayer/mperrorcode/mperrorpermissiondenied)Added [MPErrorUnknown](https://developer.apple.com/documentation/mediaplayer/mperrorcode/mperrorunknown)

#### MPMediaLibrary.h

Added [-[MPMediaLibrary addItemWithProductID:completionHandler:]](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary/1621278-additemwithproductid)Added [+[MPMediaLibrary authorizationStatus]](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary/1621282-authorizationstatus)Added [-[MPMediaLibrary getPlaylistWithUUID:creationMetadata:completionHandler:]](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary/1621273-getplaylistwithuuid)Added [+[MPMediaLibrary requestAuthorization:]](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary/1621276-requestauthorization)Added [MPMediaLibraryAuthorizationStatus](https://developer.apple.com/documentation/mediaplayer/mpmedialibraryauthorizationstatus)Added [MPMediaLibraryAuthorizationStatusAuthorized](https://developer.apple.com/documentation/mediaplayer/mpmedialibraryauthorizationstatus/mpmedialibraryauthorizationstatusauthorized)Added [MPMediaLibraryAuthorizationStatusDenied](https://developer.apple.com/documentation/mediaplayer/mpmedialibraryauthorizationstatus/denied)Added [MPMediaLibraryAuthorizationStatusNotDetermined](https://developer.apple.com/documentation/mediaplayer/mpmedialibraryauthorizationstatus/notdetermined)Added [MPMediaLibraryAuthorizationStatusRestricted](https://developer.apple.com/documentation/mediaplayer/mpmedialibraryauthorizationstatus/restricted)

#### MPMediaPlaylist.h

Added [-[MPMediaPlaylist addItemWithProductID:completionHandler:]](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist/1618706-additemwithproductid)Added [-[MPMediaPlaylist addMediaItems:completionHandler:]](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist/1618710-addmediaitems)Added [MPMediaPlaylist.authorDisplayName](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist/1618702-authordisplayname)Added [MPMediaPlaylist.descriptionText](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist/1618715-descriptiontext)Added [MPMediaPlaylistCreationMetadata](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylistcreationmetadata)Added [MPMediaPlaylistCreationMetadata.authorDisplayName](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylistcreationmetadata/1618699-authordisplayname)Added [MPMediaPlaylistCreationMetadata.descriptionText](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylistcreationmetadata/1618713-descriptiontext)Added [-[MPMediaPlaylistCreationMetadata initWithName:]](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylistcreationmetadata/1618723-initwithname)Added [MPMediaPlaylistCreationMetadata.name](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylistcreationmetadata/1618703-name)Added [MPMediaPlaylistPropertyAuthorDisplayName](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylistpropertyauthordisplayname)Added [MPMediaPlaylistPropertyDescriptionText](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylistpropertydescriptiontext)

#### MPMusicPlayerController.h

Added [-[MPMusicPlayerController setQueueWithStoreIDs:]](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/1624253-setqueue)

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
